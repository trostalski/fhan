"""
Generated class for Resource. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Meta import *
from fhan.models.generator_models import BaseModel


class Resource(BaseModel):
    """This is the base resource type for everything.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
    ):
        self.resourceType = resourceType or "Resource"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language

    @classmethod
    def from_dict(cls, data: dict) -> "Resource":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Resource":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
