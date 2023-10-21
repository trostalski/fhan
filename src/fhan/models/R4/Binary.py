"""
Generated class for Binary. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Binary(DomainResource):
    """A resource that represents the data of a single raw artifact as digital content accessible in its native format.  A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param str contentType: MimeType of the binary content
    :param Reference securityContext: Identifies another resource to use as proxy when enforcing access control
    :param str data: The actual content
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "securityContext": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        contentType: "str" = None,
        securityContext: "Reference" = None,
        data: "str" = None,
    ):
        self.resourceType = resourceType or "Binary"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.contentType = contentType
        self.securityContext = securityContext
        self.data = data

    @classmethod
    def from_dict(cls, data: dict) -> "Binary":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Binary":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
