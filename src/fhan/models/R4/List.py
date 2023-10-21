"""
Generated class for List. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Entry(BaseModel):
    """Entries in this list.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept flag: Status/Workflow information about this item
    :param bool deleted: If this item is actually marked as deleted
    :param str date: When item added to list
    :param Reference item: Actual entry
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "flag": {"class_name": "CodeableConcept", "is_contained": False},
        "item": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        flag: "CodeableConcept" = None,
        deleted: "bool" = None,
        date: "str" = None,
        item: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.flag = flag
        self.deleted = deleted
        self.date = date
        self.item = item

    @classmethod
    def from_dict(cls, data: dict) -> "List":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "List":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class List(DomainResource):
    """A list is a curated collection of resources.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str status: current | retired | entered-in-error
    :param str mode: working | snapshot | changes
    :param str title: Descriptive name for the list
    :param CodeableConcept code: What the purpose of this list is
    :param Reference subject: If all resources have the same subject
    :param Reference encounter: Context in which list created
    :param str date: When the list was prepared
    :param Reference source: Who and/or what defined the list contents (aka Author)
    :param CodeableConcept orderedBy: What order the list has
    :param Annotation note: Comments about the list
    :param Entry entry: Entries in the list
    :param CodeableConcept emptyReason: Why list is empty
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
        "orderedBy": {"class_name": "CodeableConcept", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "entry": {"class_name": "Entry", "is_contained": True},
        "emptyReason": {"class_name": "CodeableConcept", "is_contained": False},
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
        identifier: list["Identifier"] = None,
        status: "str" = None,
        mode: "str" = None,
        title: "str" = None,
        code: "CodeableConcept" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        date: "str" = None,
        source: "Reference" = None,
        orderedBy: "CodeableConcept" = None,
        note: list["Annotation"] = None,
        entry: list["Entry"] = None,
        emptyReason: "CodeableConcept" = None,
    ):
        self.resourceType = resourceType or "List"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status
        self.mode = mode
        self.title = title
        self.code = code
        self.subject = subject
        self.encounter = encounter
        self.date = date
        self.source = source
        self.orderedBy = orderedBy
        self.note = note or []
        self.entry = entry or []
        self.emptyReason = emptyReason

    @classmethod
    def from_dict(cls, data: dict) -> "List":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "List":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
