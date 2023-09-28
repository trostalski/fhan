"""
Generated class for Reference. 
Time: 2023-09-27 19:27:05
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Identifier import *
from fhan.models.generator_models import BaseModel


class Reference(BaseModel):
    """Base StructureDefinition for Reference Type: A reference from one resource to another.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str reference: Literal reference, Relative, internal or absolute URL
    :param str type: Type the reference refers to (e.g. "Patient")
    :param Identifier identifier: Logical reference, when literal reference is not known
    :param str display: Text alternative for the resource
    """

    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        reference: "str" = None,
        type: "str" = None,
        identifier: "Identifier" = None,
        display: "str" = None,
    ):
        self.resourceType = resourceType or "Reference"
        self.id = id
        self.extension = extension or []
        self.reference = reference
        self.type = type
        self.identifier = identifier
        self.display = display

    @classmethod
    def from_dict(cls, data: dict) -> "Reference":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Reference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
