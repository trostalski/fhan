"""
Generated class for Annotation. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import BaseModel


class Annotation(BaseModel):
    """Base StructureDefinition for Annotation Type: A  text note which also  contains information about who made the statement and when.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Reference authorReference: Individual responsible for the annotation
    :param str authorString: Individual responsible for the annotation
    :param str time: When the annotation was made
    :param str text: The annotation  - text content (as markdown)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "authorReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        authorReference: "Reference" = None,
        authorString: "str" = None,
        time: "str" = None,
        text: "str" = None,
    ):
        self.resourceType = resourceType or "Annotation"
        self.id = id
        self.extension = extension or []
        self.authorReference = authorReference
        self.authorString = authorString
        self.time = time
        self.text = text

    @classmethod
    def from_dict(cls, data: dict) -> "Annotation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Annotation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
