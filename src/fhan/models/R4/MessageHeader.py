"""
Generated class for MessageHeader. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Coding import *
from fhan.models.R4.DomainResource import *


class Destination(BaseModel):
    """The destination application which the message is intended for.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of system
    :param Reference target: Particular delivery destination within the destination
    :param str endpoint: Actual destination address or id
    :param Reference receiver: Intended "real-world" recipient for the data
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "target": {"class_name": "Reference", "is_contained": False},
        "receiver": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        target: "Reference" = None,
        endpoint: "str" = None,
        receiver: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.target = target
        self.endpoint = endpoint
        self.receiver = receiver

    @classmethod
    def from_dict(cls, data: dict) -> "MessageHeader":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MessageHeader":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Source(BaseModel):
    """The source application from which this message originated.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of system
    :param str software: Name of software running the system
    :param str version: Version of software running
    :param ContactPoint contact: Human contact for problems
    :param str endpoint: Actual message source address or id
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "contact": {"class_name": "ContactPoint", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        software: "str" = None,
        version: "str" = None,
        contact: "ContactPoint" = None,
        endpoint: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.software = software
        self.version = version
        self.contact = contact
        self.endpoint = endpoint

    @classmethod
    def from_dict(cls, data: dict) -> "MessageHeader":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MessageHeader":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Response(BaseModel):
    """Information about the message that this message is a response to.  Only present if this message is a response.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str identifier: Id of original message
    :param str code: ok | transient-error | fatal-error
    :param Reference details: Specific list of hints/warnings/errors
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "details": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: "str" = None,
        code: "str" = None,
        details: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.code = code
        self.details = details

    @classmethod
    def from_dict(cls, data: dict) -> "MessageHeader":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MessageHeader":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MessageHeader(DomainResource):
    """The header for a message exchange that is either requesting or responding to an action.  The reference(s) that are the subject of the action as well as other information related to the action are typically transmitted in a bundle in which the MessageHeader resource instance is the first resource in the bundle.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Coding eventCoding: Code for the event this message represents or link to event definition
    :param str eventUri: Code for the event this message represents or link to event definition
    :param Destination destination: Message destination application(s)
    :param Reference sender: Real world sender of the message
    :param Reference enterer: The source of the data entry
    :param Reference author: The source of the decision
    :param Source source: Message source application
    :param Reference responsible: Final responsibility for event
    :param CodeableConcept reason: Cause of event
    :param Response response: If this is a reply to prior message
    :param Reference focus: The actual content of the message
    :param str definition: Link to the definition for this message
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "eventCoding": {"class_name": "Coding", "is_contained": False},
        "destination": {"class_name": "Destination", "is_contained": True},
        "sender": {"class_name": "Reference", "is_contained": False},
        "enterer": {"class_name": "Reference", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "source": {"class_name": "Source", "is_contained": True},
        "responsible": {"class_name": "Reference", "is_contained": False},
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        "response": {"class_name": "Response", "is_contained": True},
        "focus": {"class_name": "Reference", "is_contained": False},
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
        eventCoding: "Coding" = None,
        eventUri: "str" = None,
        destination: list["Destination"] = None,
        sender: "Reference" = None,
        enterer: "Reference" = None,
        author: "Reference" = None,
        source: "Source" = None,
        responsible: "Reference" = None,
        reason: "CodeableConcept" = None,
        response: "Response" = None,
        focus: list["Reference"] = None,
        definition: "str" = None,
    ):
        self.resourceType = resourceType or "MessageHeader"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.eventCoding = eventCoding
        self.eventUri = eventUri
        self.destination = destination or []
        self.sender = sender
        self.enterer = enterer
        self.author = author
        self.source = source
        self.responsible = responsible
        self.reason = reason
        self.response = response
        self.focus = focus or []
        self.definition = definition

    @classmethod
    def from_dict(cls, data: dict) -> "MessageHeader":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MessageHeader":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
