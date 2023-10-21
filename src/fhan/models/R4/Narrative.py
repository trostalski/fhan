"""
Generated class for Narrative. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel


class Narrative(BaseModel):
    """Base StructureDefinition for Narrative Type: A human-readable summary of the resource conveying the essential clinical and business information for the resource.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str status: generated | extensions | additional | empty
    :param str div: Limited xhtml content
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
        status: "str" = None,
        div: "str" = None,
    ):
        self.resourceType = resourceType or "Narrative"
        self.id = id
        self.extension = extension or []
        self.status = status
        self.div = div

    @classmethod
    def from_dict(cls, data: dict) -> "Narrative":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Narrative":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
