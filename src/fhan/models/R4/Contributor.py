"""
Generated class for Contributor. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel


class Contributor(BaseModel):
    """Base StructureDefinition for Contributor Type: A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: author | editor | reviewer | endorser
    :param str name: Who contributed the content
    :param ContactDetail contact: Contact details of the contributor
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        type: "str" = None,
        name: "str" = None,
        contact: list["ContactDetail"] = None,
    ):
        self.resourceType = resourceType or "Contributor"
        self.id = id
        self.extension = extension or []
        self.type = type
        self.name = name
        self.contact = contact or []

    @classmethod
    def from_dict(cls, data: dict) -> "Contributor":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contributor":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
