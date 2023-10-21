"""
Generated class for Expression. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel


class Expression(BaseModel):
    """Base StructureDefinition for Expression Type: A expression that is evaluated in a specified context and returns a value. The context of use of the expression must specify the context in which the expression is evaluated, and how the result of the expression is used.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str description: Natural language description of the condition
    :param str name: Short name assigned to expression for reuse
    :param str language: text/cql | text/fhirpath | application/x-fhir-query | etc.
    :param str expression: Expression in specified language
    :param str reference: Where the expression is found
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        description: "str" = None,
        name: "str" = None,
        language: "str" = None,
        expression: "str" = None,
        reference: "str" = None,
    ):
        self.resourceType = resourceType or "Expression"
        self.id = id
        self.extension = extension or []
        self.description = description
        self.name = name
        self.language = language
        self.expression = expression
        self.reference = reference

    @classmethod
    def from_dict(cls, data: dict) -> "Expression":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Expression":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
