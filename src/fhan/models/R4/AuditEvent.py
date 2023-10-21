"""
Generated class for AuditEvent. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Coding import *
from fhan.models.R4.DomainResource import *


class Network(BaseModel):
    """Logical network location for application activity, if the activity has a network location.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str address: Identifier for the network access point of the user device
    :param str type: The type of network access point
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
        address: "str" = None,
        type: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.address = address
        self.type = type

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Agent(BaseModel):
    """An actor taking an active role in the event or activity that is logged.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How agent participated
    :param CodeableConcept role: Agent role in the event
    :param Reference who: Identifier of who
    :param str altId: Alternative User identity
    :param str name: Human friendly name for the agent
    :param bool requestor: Whether user is initiator
    :param Reference location: Where
    :param str policy: Policy that authorized event
    :param Coding media: Type of media
    :param Network network: Logical network location for application activity
    :param CodeableConcept purposeOfUse: Reason given for this user
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "who": {"class_name": "Reference", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "media": {"class_name": "Coding", "is_contained": False},
        "network": {"class_name": "Network", "is_contained": True},
        "purposeOfUse": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        role: list["CodeableConcept"] = None,
        who: "Reference" = None,
        altId: "str" = None,
        name: "str" = None,
        requestor: "bool" = None,
        location: "Reference" = None,
        policy: list["str"] = None,
        media: "Coding" = None,
        network: "Network" = None,
        purposeOfUse: list["CodeableConcept"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.role = role or []
        self.who = who
        self.altId = altId
        self.name = name
        self.requestor = requestor
        self.location = location
        self.policy = policy or []
        self.media = media
        self.network = network
        self.purposeOfUse = purposeOfUse or []

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Source(BaseModel):
    """The system that is reporting the event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str site: Logical source location within the enterprise
    :param Reference observer: The identity of source detecting the event
    :param Coding type: The type of source where event originated
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "observer": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        site: "str" = None,
        observer: "Reference" = None,
        type: list["Coding"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.site = site
        self.observer = observer
        self.type = type or []

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Detail(BaseModel):
    """Tagged value pairs for conveying additional information about the entity.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: Name of the property
    :param str valueString: Property value
    :param str valueBase64Binary: Property value
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
        valueString: "str" = None,
        valueBase64Binary: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.valueString = valueString
        self.valueBase64Binary = valueBase64Binary

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Entity(BaseModel):
    """Specific instances of data or objects that have been accessed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference what: Specific instance of resource
    :param Coding type: Type of entity involved
    :param Coding role: What role the entity played
    :param Coding lifecycle: Life-cycle stage for the entity
    :param Coding securityLabel: Security labels on the entity
    :param str name: Descriptor for entity
    :param str description: Descriptive text
    :param str query: Query parameters
    :param Detail detail: Additional Information about the entity
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "what": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "Coding", "is_contained": False},
        "role": {"class_name": "Coding", "is_contained": False},
        "lifecycle": {"class_name": "Coding", "is_contained": False},
        "securityLabel": {"class_name": "Coding", "is_contained": False},
        "detail": {"class_name": "Detail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        what: "Reference" = None,
        type: "Coding" = None,
        role: "Coding" = None,
        lifecycle: "Coding" = None,
        securityLabel: list["Coding"] = None,
        name: "str" = None,
        description: "str" = None,
        query: "str" = None,
        detail: list["Detail"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.what = what
        self.type = type
        self.role = role
        self.lifecycle = lifecycle
        self.securityLabel = securityLabel or []
        self.name = name
        self.description = description
        self.query = query
        self.detail = detail or []

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AuditEvent(DomainResource):
    """A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Coding type: Type/identifier of event
    :param Coding subtype: More specific type/id for the event
    :param str action: Type of action performed during the event
    :param Period period: When the activity occurred
    :param str recorded: Time when the event was recorded
    :param str outcome: Whether the event succeeded or failed
    :param str outcomeDesc: Description of the event outcome
    :param CodeableConcept purposeOfEvent: The purposeOfUse of the event
    :param Agent agent: Actor involved in the event
    :param Source source: Audit Event Reporter
    :param Entity entity: Data or objects used
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "Coding", "is_contained": False},
        "subtype": {"class_name": "Coding", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "purposeOfEvent": {"class_name": "CodeableConcept", "is_contained": False},
        "agent": {"class_name": "Agent", "is_contained": True},
        "source": {"class_name": "Source", "is_contained": True},
        "entity": {"class_name": "Entity", "is_contained": True},
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
        type: "Coding" = None,
        subtype: list["Coding"] = None,
        action: "str" = None,
        period: "Period" = None,
        recorded: "str" = None,
        outcome: "str" = None,
        outcomeDesc: "str" = None,
        purposeOfEvent: list["CodeableConcept"] = None,
        agent: list["Agent"] = None,
        source: "Source" = None,
        entity: list["Entity"] = None,
    ):
        self.resourceType = resourceType or "AuditEvent"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.subtype = subtype or []
        self.action = action
        self.period = period
        self.recorded = recorded
        self.outcome = outcome
        self.outcomeDesc = outcomeDesc
        self.purposeOfEvent = purposeOfEvent or []
        self.agent = agent or []
        self.source = source
        self.entity = entity or []

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
