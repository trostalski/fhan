from typing import Any, Union

from fhirpathpy import compile
from pandas import DataFrame

from fhan.views.resource_collection import ResourceCollection
from fhan.views.view_definition import ViewDefinition


class ViewResult:
    """Result from a view execution.

    Args:
        table_dict (dict): Result from the view execution. The keys are the aliases
            from the view definition and the values are lists of values.
    """

    def __init__(self, view_definition: ViewDefinition, table: dict[str, list[str]]):
        self.view_definition = view_definition
        self.table = table

    @property
    def columns(self):
        """
        Returns the columns of the view result.
        """
        return list(self.table.keys())

    def to_dataframe(self):
        """
        Returns the view result as a pandas dataframe.
        """
        return DataFrame(self.table, columns=self.table.keys())

    def to_row_lists(self):
        """
        Returns the view result as a list of lists of rows.
        """
        return [dict(zip(self.table, t)) for t in zip(*self.table.values())]

    def __getitem__(self, key):
        """
        Returns the column from the view result.
        """
        return self.table[key]


class View:
    def __init__(
        self, view_definition: Union[ViewDefinition, dict], fhir_input: dict = None
    ):
        """
        Main class for sql on FHIR views.
        """
        if isinstance(view_definition, dict):
            view_definition = ViewDefinition.from_dict(view_definition)
        view_definition.validate()

        self._view_definition = view_definition
        self._fhir_input = fhir_input
        self._resource = view_definition.resource

        self._select_fns, self._select_names = self._get_select_fns_and_names()
        self._constraint_fns = self._get_constraint_fns()

        if fhir_input:
            self._resource_collection = self._get_collection_from_input(fhir_input)

    def execute(self, fhir_input: dict = None) -> ViewResult:
        """
        Execute the view.
        """
        if fhir_input:
            self._resource_collection = self._get_collection_from_input(fhir_input)
        if not self._resource_collection:
            raise ValueError("No fhir data provided.")
        self._apply_constraints()  # filters the _resource_collection
        select_result = self._apply_selects()  # returns a list of dicts
        execution_result = {
            alias: select_result[i] for i, alias in enumerate(self._select_names)
        }  # returns a dict with the aliases as keys and lists of values as values
        view_result = ViewResult(
            view_definition=self._view_definition, table=execution_result
        )
        return view_result

    def __call__(self, fhir_input: dict) -> ViewResult:
        """
        Executes the view definition on fhir input.
        """
        self._resource_collection = self._get_collection_from_input(fhir_input)
        view_result = self.execute()
        return view_result

    def _get_collection_from_input(self, fhir_input: dict | ResourceCollection | list):
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
                resource_collection = ResourceCollection([fhir_input])
        else:
            raise ValueError(
                "Input must be a list of resources, a bundle or a ResourceCollection."
            )
        resource_collection.filter_resources(
            lambda x: x["resourceType"] == self._resource
        )
        return resource_collection

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

    def _apply_selects(self) -> list[list]:
        """
        Apply the select functions to the resource collection. Returns a list of lists
        with the shape (path_nums, fp_result). This means the first list is the same
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
        for constraint in self._view_definition.where:
            path = constraint.path
            fn = compile(path)
            constraint_fns.append(fn)
        return constraint_fns

    def _get_select_fns_and_names(self) -> tuple[list, list]:
        """
        Get the select functions from the view definition.
        """
        select_fns = []
        select_names = []
        for select in self._view_definition.select:
            for col in select.column:
                path = col.path
                name = col.name
                fn = compile(path)
                select_fns.append(fn)
                select_names.append(name)
        return select_fns, select_names


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
        # TODO: how to handle lists
        pass
    return fp_result
