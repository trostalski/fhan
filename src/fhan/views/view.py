from typing import Any
import logging
import dataclasses

from fhirpathpy import compile
from pandas import DataFrame
from dacite import from_dict

from fhan.views.resource_collection import ResourceCollection
from fhan.views.view_definition import ViewDefinition, validate_view_definition

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class ViewResult:
    """Result from a view execution.

    Args:
        table_dict (dict): Result from the view execution. The keys are the aliases
            from the view definition and the values are lists of values.
    """

    table_dict: dict

    def to_dataframe(self):
        """
        Returns the view result as a pandas dataframe.
        """
        return DataFrame(self.table_dict, columns=self.table_dict.keys())


class View:
    def __init__(self, view_definition: ViewDefinition | dict, fhir_input: dict = None):
        """
        Main class for sql on FHIR views.
        """
        if isinstance(view_definition, dict):
            view_definition = from_dict(data_class=ViewDefinition, data=view_definition)
        validate_view_definition(view_definition)
        self._fhir_input = fhir_input
        self._view_definition = view_definition
        self._resource = view_definition.resource

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
        view_result = ViewResult(table_dict=execution_result)
        self._view_result = view_result
        return view_result

    def _apply_constraints(self) -> None:
        """
        Filter resources from the input based on the constraints. The constraints
        should evaluate to a boolean, however, everything that is not `False` or
        `None` or [] is considered `True` for now.
        """
        for constraint_fn in self._constraint_fns:
            self._resource_collection.filter_resources(
                lambda x: _unnest_fp_result(constraint_fn(x))
            )

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
                fn_result = _unnest_fp_result(fn_result)
                fn_results.append(fn_result)
            select_results.append(fn_results)
        return select_results

    def _get_constraint_fns(self) -> list:
        """
        Get the constraints from the view definition.
        """
        constraint_fns = []
        if not self._view_definition.where:
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
        for select in self._view_definition.select:
            path = select.path
            fn = compile(path)
            select_fns.append(fn)
        return select_fns

    def _get_select_aliases(self) -> list:
        """
        Get the select aliases from the view definition.
        """
        select_aliases = []
        for select in self._view_definition.select:
            alias = select.alias or select.path
            select_aliases.append(alias)
        return select_aliases


def _unnest_fp_result(fp_result: list) -> Any:
    """
    Unnest the result from the select function. If the result is a list of length 0,
    it is considered `None`. If the result is a list of length 1, the first element
    is returned. If the result is a list of length > 1, a warning is logged and the
    list is returned.
    """
    if len(fp_result) == 0:
        fp_result = None
    elif len(fp_result) == 1:
        fp_result = fp_result[0]
    elif len(fp_result) > 1:
        logger.warning(
            f"Select function returned more than one result: {fp_result}. "
            "Keeping list."
        )
    return fp_result
