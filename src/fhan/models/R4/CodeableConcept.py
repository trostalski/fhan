"""
Generated class for CodeableConcept. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Coding import *
from fhan.models.generator_models import BaseModel


class CodeableConcept(BaseModel):
    """Base StructureDefinition for CodeableConcept Type: A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding coding: Code defined by a terminology system
    :param str text: Plain text representation of the concept
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "coding": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        coding: list["Coding"] = None,
        text: "str" = None,
    ):
        self.resourceType = resourceType or "CodeableConcept"
        self.id = id
        self.extension = extension or []
        self.coding = coding or []
        self.text = text

    @classmethod
    def from_dict(cls, data: dict) -> "CodeableConcept":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CodeableConcept":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
