from typing import Any, Literal
import logging
import dataclasses

from fhirpathpy import compile
from pandas import DataFrame

from fhan.views.resource_collection import ResourceCollection

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class ViewMetadata:
    uri: str = None
    identifier: str = None
    name: str = None
    version: str = None
    title: str = None
    status: Literal["draft", "active", "retired", "unknown"] = None
    experimental: bool = None
    publisher: str = None
    description: str = None
    copyright: str = None
    resourceVersion: str = None


class ViewResult:
    def __init__(self, table: dict):
        """_summary_

        Args:
            table (dict): Result from the view execution. The keys are the aliases
                from the view definition and the values are lists of values.
        """
        self._table_dict = table

    def _validate_table(self):
        """
        Validate the table. The table must have the same length for all keys.
        """

    def to_dataframe(self):
        """
        Return the view result as a pandas dataframe.
        """
        return DataFrame(self._table_dict, columns=self._table_dict.keys())


class View:
    def __init__(self, view_definition: dict, fhir_input: dict = None):
        """
        Main class for sql on fhir views.
        """
        _validate_view_definition_structure(view_definition)
        self._fhir_input = fhir_input
        self._view_definition = view_definition
        self._resource = view_definition.get("resource")
        self._metadata = self._get_metadata()

        self._select_fns = self._get_select_fns()
        self._constraint_fns = self._get_constraint_fns()
        self._select_aliases = self._get_select_aliases()

        self._view_result = None

        if fhir_input:
            self._get_collection_from_input(fhir_input)

    @property
    def result(self):
        return self._view_result

    def __call__(self, fhir_input: dict) -> ViewResult:
        """
        Executes the view definition on fhir input.
        """
        self._resource_collection = self._get_collection_from_input(fhir_input)
        view_result = self._execute()
        return view_result

    def _get_metadata(self) -> ViewMetadata:
        """
        Get the metadata of the view.
        """
        metadata = ViewMetadata(
            uri=self._view_definition.get("uri"),
            identifier=self._view_definition.get("identifier"),
            name=self._view_definition.get("name"),
            version=self._view_definition.get("version"),
            title=self._view_definition.get("title"),
            status=self._view_definition.get("status"),
            experimental=self._view_definition.get("experimental"),
            publisher=self._view_definition.get("publisher"),
            description=self._view_definition.get("description"),
        )
        return metadata

    def _get_collection_from_input(self, fhir_input: dict):
        """
        Get the resource collection from the input.
        """
        resource_collection = None
        if isinstance(fhir_input, ResourceCollection):
            resource_collection = fhir_input
        elif isinstance(fhir_input, list):
            resource_collection = ResourceCollection(fhir_input)
        elif isinstance(fhir_input, dict):
            if fhir_input["resourceType"] == "Bundle":
                resource_collection = ResourceCollection.from_bundle(fhir_input)
        else:
            raise ValueError(
                "Input must be a list of resources, a bundle or a ResourceCollection."
            )
        resource_collection.filter_resources(
            lambda x: x["resourceType"] == self._resource
        )
        return resource_collection

    def _execute(self) -> ViewResult:
        """
        Execute the view.
        """
        self._apply_constraints()  # filters the _resource_collection
        select_result = self._apply_selects()  # returns a list of dicts

        execution_result = {
            alias: select_result[i] for i, alias in enumerate(self._select_aliases)
        }  # returns a dict with the aliases as keys and lists of values as values
        print(execution_result)
        view_result = ViewResult(execution_result)
        self._view_result = view_result
        return view_result

    def _apply_constraints(self) -> None:
        """
        Filter resources from the input based on the constraints. The constraints
        should evaluate to a boolean, however, everything that is not `False` or
        `None` or [] is considered `True` for now.
        """
        for constraint_fn in self._constraint_fns:
            self._resource_collection.filter_resources(constraint_fn)

    def _apply_selects(self) -> list[list[list]]:
        """
        Apply the select functions to the resource collection. Returns a list of lists of lists
        with the shape (path_nums, resource_nums, fp_result). This means the first list is the same
        length as the number of aliases and they can be merged.
        """
        select_results = []
        for select_fn in self._select_fns:
            fn_results = []
            for resource in self._resource_collection:
                fn_result = select_fn(resource)  # fp always returns a list
                fn_result = self._unnest_fn_result(fn_result)
                fn_results.append(fn_result)
            select_results.append(fn_results)
        return select_results

    def _unnest_fn_result(self, fn_result: list) -> Any:
        """
        Unnest the result from the select function. If the result is a list of length 0,
        it is considered `None`. If the result is a list of length 1, the first element
        is returned. If the result is a list of length > 1, a warning is logged and the
        list is returned.
        """
        if len(fn_result) == 0:
            fn_result = None
        elif len(fn_result) == 1:
            fn_result = fn_result[0]
        elif len(fn_result) > 1:
            logger.warning(
                f"Select function returned more than one result: {fn_result}. "
                "Keeping list."
            )
        return fn_result

    def _get_constraint_fns(self) -> list:
        """
        Get the constraints from the view definition.
        """
        constraint_fns = []
        if not "where" in self._view_definition:
            return constraint_fns
        for constraint in self._view_definition["where"]:
            path = constraint["path"]
            fn = compile(path)
            constraint_fns.append(fn)
        return constraint_fns

    def _get_select_fns(self) -> list:
        """
        Get the select functions from the view definition.
        """
        select_fns = []
        for select in self._view_definition["select"]:
            path = select["path"]
            fn = compile(path)
            select_fns.append(fn)
        return select_fns

    def _get_select_aliases(self) -> list:
        """
        Get the select aliases from the view definition.
        """
        select_aliases = []
        for select in self._view_definition["select"]:
            alias = select.get("alias") or select["path"]
            select_aliases.append(alias)
        return select_aliases


def _validate_view_definition_structure(view_definition: dict):
    """
    Validate the view definition.
    """
    errors = []
    if "resource" not in view_definition:
        errors.append("View definition must have a resource.")
    if "select" not in view_definition:
        errors.append("View definition must have a select.")
    if "where" in view_definition:
        for constraint in view_definition["where"]:
            if "path" not in constraint:
                errors.append(
                    f"All where clauses must contain `path` fields. Got {constraint}."
                )
            if not isinstance(constraint["path"], str):
                errors.append(
                    "The `path` field in a where clause must be strings."
                    f' Got {constraint["path"]}.'
                )
    if errors:
        raise ValueError("\n".join(errors))
