"""
Generated class for Subscription. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Channel(BaseModel):
    """Details where to send notifications when resources are received that meet the criteria.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: rest-hook | websocket | email | sms | message
    :param str endpoint: Where the channel points to
    :param str payload: MIME type to send, or omit for no payload
    :param str header: Usage depends on the channel type
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
        type: "str" = None,
        endpoint: "str" = None,
        payload: "str" = None,
        header: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.endpoint = endpoint
        self.payload = payload
        self.header = header or []

    @classmethod
    def from_dict(cls, data: dict) -> "Subscription":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Subscription":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Subscription(DomainResource):
    """The subscription resource is used to define a push-based subscription from a server to another system. Once a subscription is registered with the server, the server checks every resource that is created or updated, and if the resource matches the given criteria, it sends a message on the defined "channel" so that another system can take an appropriate action.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str status: requested | active | error | off
    :param ContactPoint contact: Contact details for source (e.g. troubleshooting)
    :param str end: When to automatically delete the subscription
    :param str reason: Description of why this subscription was created
    :param str criteria: Rule for server push
    :param str error: Latest error note
    :param Channel channel: The channel on which to report matches to the criteria
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "contact": {"class_name": "ContactPoint", "is_contained": False},
        "channel": {"class_name": "Channel", "is_contained": True},
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
        status: "str" = None,
        contact: list["ContactPoint"] = None,
        end: "str" = None,
        reason: "str" = None,
        criteria: "str" = None,
        error: "str" = None,
        channel: "Channel" = None,
    ):
        self.resourceType = resourceType or "Subscription"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.status = status
        self.contact = contact or []
        self.end = end
        self.reason = reason
        self.criteria = criteria
        self.error = error
        self.channel = channel

    @classmethod
    def from_dict(cls, data: dict) -> "Subscription":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Subscription":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
