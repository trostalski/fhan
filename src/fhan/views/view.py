from fhirpathpy import compile

example_view_definition = {
    "name": "patient_demographics",
    "resource": "Patient",
    "description": "A view of simple patient demographics",
    "select": [
        {"path": "getResourceKey()", "alias": "id"},
        {"path": "gender"},
        {
            # Select nested fields from the first official name.
            "forEach": "name.where(use = 'official').first()",
            "select": [
                {"path": "given.join(' ')", "alias": "given_name"},
                {"path": "family", "alias": "family_name"},
            ],
        },
    ],
}


class View:
    def __init__(self, view_definition: dict, fhir_intput: dict = None):
        _validate_view_definition_structure(view_definition)
        self._fhir_input = fhir_intput
        self._view_definition = view_definition

    def _execute(self):
        """
        Execute the view.
        """
        constraint_fns = self._get_constraint_fns()

    def _parse_view_definition(self):
        """
        Parse the view definition.
        """

    def _get_constraint_fns(self):
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


def _validate_view_definition_structure(view_definition: dict):
    """
    Validate the view definition.
    """
    errors = []
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
