"""
Generated class for MessageDefinition. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Coding import *
from fhan.models.R4.DomainResource import *


class Focus(BaseModel):
    """Identifies the resource (or resources) that are being addressed by the event.  For example, the Encounter for an admit message or two Account records for a merge.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Type of resource
    :param str profile: Profile that must be adhered to by focus
    :param int min: Minimum number of focuses of this type
    :param str max: Maximum number of focuses of this type
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        profile: "str" = None,
        min: "int" = None,
        max: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.profile = profile
        self.min = min
        self.max = max

    @classmethod
    def from_dict(cls, data: dict) -> "MessageDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MessageDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AllowedResponse(BaseModel):
    """Indicates what types of messages may be sent as an application-level response to this message.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str message: Reference to allowed message definition response
    :param str situation: When should this response be used
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        message: "str" = None,
        situation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.message = message
        self.situation = situation

    @classmethod
    def from_dict(cls, data: dict) -> "MessageDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MessageDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MessageDefinition(DomainResource):
    """Defines the characteristics of a message that can be shared between systems, including the type of event that initiates the message, the content to be transmitted and what response(s), if any, are permitted.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Business Identifier for a given MessageDefinition
    :param Identifier identifier: Primary key for the message definition on a given server
    :param str version: Business version of the message definition
    :param str name: Name for this message definition (computer friendly)
    :param str title: Name for this message definition (human friendly)
    :param str replaces: Takes the place of
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the message definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for message definition (if applicable)
    :param str purpose: Why this message definition is defined
    :param str copyright: Use and/or publishing restrictions
    :param str base: Definition this one is based on
    :param str parent: Protocol/workflow this is part of
    :param Coding eventCoding: Event code  or link to the EventDefinition
    :param str eventUri: Event code  or link to the EventDefinition
    :param str category: consequence | currency | notification
    :param Focus focus: Resource(s) that are the subject of the event
    :param str responseRequired: always | on-error | never | on-success
    :param AllowedResponse allowedResponse: Responses to this message
    :param str graph: Canonical reference to a GraphDefinition
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "eventCoding": {"class_name": "Coding", "is_contained": False},
        "focus": {"class_name": "Focus", "is_contained": True},
        "allowedResponse": {"class_name": "AllowedResponse", "is_contained": True},
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
        url: "str" = None,
        identifier: list["Identifier"] = None,
        version: "str" = None,
        name: "str" = None,
        title: "str" = None,
        replaces: list["str"] = None,
        status: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        copyright: "str" = None,
        base: "str" = None,
        parent: list["str"] = None,
        eventCoding: "Coding" = None,
        eventUri: "str" = None,
        category: "str" = None,
        focus: list["Focus"] = None,
        responseRequired: "str" = None,
        allowedResponse: list["AllowedResponse"] = None,
        graph: list["str"] = None,
    ):
        self.resourceType = resourceType or "MessageDefinition"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.identifier = identifier or []
        self.version = version
        self.name = name
        self.title = title
        self.replaces = replaces or []
        self.status = status
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.copyright = copyright
        self.base = base
        self.parent = parent or []
        self.eventCoding = eventCoding
        self.eventUri = eventUri
        self.category = category
        self.focus = focus or []
        self.responseRequired = responseRequired
        self.allowedResponse = allowedResponse or []
        self.graph = graph or []

    @classmethod
    def from_dict(cls, data: dict) -> "MessageDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MessageDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
