"""
Generated class for NamingSystem. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class UniqueId(BaseModel):
    """Indicates how the system may be identified when referenced in electronic exchange.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: oid | uuid | uri | other
    :param str value: The unique identifier
    :param bool preferred: Is this the id that should be used for this type
    :param str comment: Notes about identifier usage
    :param Period period: When is identifier valid?
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "str" = None,
        value: "str" = None,
        preferred: "bool" = None,
        comment: "str" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.value = value
        self.preferred = preferred
        self.comment = comment
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "NamingSystem":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "NamingSystem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class NamingSystem(DomainResource):
    """A curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc.  Represents a "System" used within the Identifier and Coding data types.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str name: Name for this naming system (computer friendly)
    :param str status: draft | active | retired | unknown
    :param str kind: codesystem | identifier | root
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str responsible: Who maintains system namespace?
    :param CodeableConcept type: e.g. driver,  provider,  patient, bank etc.
    :param str description: Natural language description of the naming system
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for naming system (if applicable)
    :param str usage: How/where is it used
    :param UniqueId uniqueId: Unique identifiers used for system
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "uniqueId": {"class_name": "UniqueId", "is_contained": True},
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
        name: "str" = None,
        status: "str" = None,
        kind: "str" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        responsible: "str" = None,
        type: "CodeableConcept" = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        usage: "str" = None,
        uniqueId: list["UniqueId"] = None,
    ):
        self.resourceType = resourceType or "NamingSystem"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.status = status
        self.kind = kind
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.responsible = responsible
        self.type = type
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.usage = usage
        self.uniqueId = uniqueId or []

    @classmethod
    def from_dict(cls, data: dict) -> "NamingSystem":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "NamingSystem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
