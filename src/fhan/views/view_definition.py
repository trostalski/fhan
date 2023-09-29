import dataclasses
from typing import Any, Literal

from fhirpathpy import compile


@dataclasses.dataclass
class ViewDefinitionConstant:
    """Constant that can be used in FHIRPath expressions.

    Args:
        name (str): Name of constant (referred to in FHIRPath as %[name]).
        value (Any, optional): Value of constant.
    """

    name: str
    value: Any = None


@dataclasses.dataclass
class ViewDefinitionSelect:
    """Defines the content of a column within the view.

    Args:
        path (str): FHIRPath expression that creates a column and defines its content.
        alias (str, optional): Column alias produced in the output.
        forEach (str, optional): Creates a row for each of the elements in the given expression.
        forEachOrNull (str, optional): Same as forEach, but will produce a row with null values if the collection is empty.
    """

    path: str
    alias: str = None
    forEach: str = None
    forEachOrNull: str = None
    # spec also defines union

    def is_valid(self):
        """
        Validate the fhirpath of the where path.
        """
        try:
            validate_fhir_path(self.path)
            return True
        except:
            return False

    def validate(self):
        """
        Validate the fhirpath of the select path.
        """
        validate_fhir_path(self.path)


@dataclasses.dataclass
class ViewDefinitionWhere:
    """Zero or more FHIRPath constraints to filter resourses for the view.

    Args:
        path (str):	A FHIRPath expression defining a filter condition.
        description (str, optional): A human-readable description of the above where constraint.
    """

    path: str
    description: str = None

    def is_valid(self):
        """
        Validate the fhirpath of the where path.
        """
        try:
            validate_fhir_path(self.path)
            return True
        except:
            return False

    def validate(self):
        """
        Validate the fhirpath of the where path.
        """
        validate_fhir_path(self.path)


@dataclasses.dataclass
class ViewDefinition:
    """View definitions represent a tabular projection of a FHIR resource, where the columns and inclusion criteria are defined by FHIRPath expressions."""

    resource: str = None
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
    constant: list[ViewDefinitionConstant] = None
    select: list[ViewDefinitionSelect] = None
    where: list[ViewDefinitionWhere] = None

    def validate(self):
        """
        Validate the view definition.
        """
        validate_view_definition(self)

    def is_valid(self):
        """
        Validate the view definition.
        """
        try:
            validate_view_definition(self)
            return True
        except:
            return False

    def as_dict(self):
        return dataclasses.asdict(self)


def validate_view_definition(view_definition: ViewDefinition):
    """
    Validate the view definition.
    """
    errors = []
    if not view_definition.resource:
        errors.append("View definition must have a resource.")
    if not view_definition.select:
        errors.append("View definition must have a select.")
    if view_definition.where:
        for constraint in view_definition.where:
            if not constraint.path:
                errors.append(
                    f"All where clauses must contain `path` fields. Got {constraint}."
                )
            if not isinstance(constraint.path, str):
                errors.append(
                    "The `path` field in a where clause must be strings."
                    f" Got {constraint.path}."
                )
    if errors:
        raise Exception("\n".join(errors))


def validate_fhir_path(fhirpath: str):
    compile(fhirpath)
