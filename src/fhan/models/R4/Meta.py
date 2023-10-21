"""
Generated class for Meta. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Coding import *
from fhan.models.generator_models import BaseModel


class Meta(BaseModel):
    """Base StructureDefinition for Meta Type: The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str versionId: Version specific identifier
    :param str lastUpdated: When the resource version last changed
    :param str source: Identifies where the resource comes from
    :param str profile: Profiles this resource claims to conform to
    :param Coding security: Security Labels applied to this resource
    :param Coding tag: Tags applied to this resource
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "security": {"class_name": "Coding", "is_contained": False},
        "tag": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        versionId: "str" = None,
        lastUpdated: "str" = None,
        source: "str" = None,
        profile: list["str"] = None,
        security: list["Coding"] = None,
        tag: list["Coding"] = None,
    ):
        self.resourceType = resourceType or "Meta"
        self.id = id
        self.extension = extension or []
        self.versionId = versionId
        self.lastUpdated = lastUpdated
        self.source = source
        self.profile = profile or []
        self.security = security or []
        self.tag = tag or []

    @classmethod
    def from_dict(cls, data: dict) -> "Meta":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Meta":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
