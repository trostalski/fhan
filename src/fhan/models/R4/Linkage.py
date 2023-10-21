"""
Generated class for Linkage. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Item(BaseModel):
    """Identifies which record considered as the reference to the same real-world occurrence as well as how the items should be evaluated within the collection of linked items.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: source | alternate | historical
    :param Reference resource: Resource being linked
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "resource": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "str" = None,
        resource: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.resource = resource

    @classmethod
    def from_dict(cls, data: dict) -> "Linkage":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Linkage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Linkage(DomainResource):
    """Identifies two or more records (resource instances) that refer to the same real-world "occurrence".
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param bool active: Whether this linkage assertion is active or not
    :param Reference author: Who is responsible for linkages
    :param Item item: Item to be linked
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "item": {"class_name": "Item", "is_contained": True},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        active: "bool" = None,
        author: "Reference" = None,
        item: list["Item"] = None,
    ):
        self.resourceType = resourceType or "Linkage"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.active = active
        self.author = author
        self.item = item or []

    @classmethod
    def from_dict(cls, data: dict) -> "Linkage":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Linkage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
