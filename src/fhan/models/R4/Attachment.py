"""
Generated class for Attachment. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel


class Attachment(BaseModel):
    """Base StructureDefinition for Attachment Type: For referring to data content defined in other formats.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str contentType: Mime type of the content, with charset etc.
    :param str language: Human language of the content (BCP-47)
    :param str data: Data inline, base64ed
    :param str url: Uri where the data can be found
    :param int size: Number of bytes of content (if url provided)
    :param str hash: Hash of the data (sha-1, base64ed)
    :param str title: Label to display in place of the data
    :param str creation: Date attachment was first created
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
        contentType: "str" = None,
        language: "str" = None,
        data: "str" = None,
        url: "str" = None,
        size: "int" = None,
        hash: "str" = None,
        title: "str" = None,
        creation: "str" = None,
    ):
        self.resourceType = resourceType or "Attachment"
        self.id = id
        self.extension = extension or []
        self.contentType = contentType
        self.language = language
        self.data = data
        self.url = url
        self.size = size
        self.hash = hash
        self.title = title
        self.creation = creation

    @classmethod
    def from_dict(cls, data: dict) -> "Attachment":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Attachment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
