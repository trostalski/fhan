import dataclasses
from typing import Any, Literal, Optional
from dacite import from_dict
from fhirpathpy import compile

from fhan.core.exceptions import InvalidFhirPathException


@dataclasses.dataclass
class Constant:
    """Constant that can be used in FHIRPath expressions.

    Args:
        name (str): Name of constant (referred to in FHIRPath as %[name]).
        value (Any, optional): Value of constant.
    """

    name: str
    value: Any = None


@dataclasses.dataclass
class Tag:
    name: str
    value: str


@dataclasses.dataclass
class Column:
    path: str
    name: str
    description: Optional[str] = None
    collection: Optional[bool] = None
    type: Optional[str] = None
    tag: Optional[Tag] = None

    def __post_init__(self):
        # Assign the path to name if name is not provided
        if not self.name:
            self.name = self.path

    def is_valid(self):
        """
        Validate the fhirpath of the select path.
        """
        if not self.path or not self.name:
            return False
        try:
            validate_fhir_path(self.path)
            return True
        except:
            return False

    def validate(self):
        """
        Validate the fhirpath of the select path.
        """
        if not self.path:
            raise Exception("Column must have a path.")
        if not self.name:
            raise Exception("Column must have a name.")
        validate_fhir_path(self.path)


@dataclasses.dataclass
class Select:
    """Defines the content of a column within the view.

    Args:
        column (list[Column]): A column to be produced in the resulting table.
    """

    column: list[Column]

    def validate(self):
        """
        Validate the fhirpath of the select path.
        """
        for column in self.column:
            column.validate()

    # TODO: These are not implemented yet.
    # forEach: Optional[str] = None
    # forEachOrNull: Optional[str] = None
    # unionAll: Optional["Select"] = None


@dataclasses.dataclass
class Where:
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
        if not self.path:
            return False
        try:
            validate_fhir_path(self.path)
            return True
        except:
            return False

    def validate(self):
        """
        Validate the fhirpath of the where path.
        """
        if not self.path:
            raise Exception("Where clause must have a path.")
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
    constant: list[Constant] = None
    select: list[Select] = None
    where: list[Where] = None

    @classmethod
    def from_dict(cls, data: dict):
        vd = from_dict(data_class=cls, data=data)
        vd.validate()
        return vd

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
    names = []
    for select in view_definition.select:
        for column in select.column:
            names.append(column.name)
            if not column.path:
                errors.append(
                    f"All select clauses must contain `path` fields. Got {column}."
                )
            if not isinstance(column.path, str):
                errors.append(
                    "The `path` field in a select clause must be strings."
                    f" Got {column.path}."
                )
            if not column.name:
                errors.append(
                    f"All select clauses must contain `name` fields. Got {column}."
                )
            if not isinstance(column.name, str):
                errors.append(
                    "The `name` field in a select clause must be strings."
                    f" Got {column.name}."
                )
            if not column.is_valid():
                errors.append(
                    f"The `path` field in a select clause must be valid FHIRPath."
                    f" Got {column.path}."
                )
    if len(names) != len(set(names)):
        # TODO: This should be a warning, not an error.
        errors.append("All select clauses must have unique names.")
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
    try:
        compile(fhirpath)
    except Exception as e:
        raise InvalidFhirPathException(
            f"Invalid FHIRPath expression: {fhirpath}. Error: {e}"
        )
