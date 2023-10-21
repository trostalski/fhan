"""
Generated class for Provenance. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Signature import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Agent(BaseModel):
    """An actor taking a role in an activity  for which it can be assigned some degree of responsibility for the activity taking place.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How the agent participated
    :param CodeableConcept role: What the agents role was
    :param Reference who: Who participated
    :param Reference onBehalfOf: Who the agent is representing
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "who": {"class_name": "Reference", "is_contained": False},
        "onBehalfOf": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        role: list["CodeableConcept"] = None,
        who: "Reference" = None,
        onBehalfOf: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.role = role or []
        self.who = who
        self.onBehalfOf = onBehalfOf

    @classmethod
    def from_dict(cls, data: dict) -> "Provenance":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Provenance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Entity(BaseModel):
    """An entity used in this activity.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str role: derivation | revision | quotation | source | removal
    :param Reference what: Identity of entity
    :param Agent agent: Entity is attributed to this agent
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "what": {"class_name": "Reference", "is_contained": False},
        "agent": {"class_name": "Agent", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        role: "str" = None,
        what: "Reference" = None,
        agent: list["Agent"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role
        self.what = what
        self.agent = agent or []

    @classmethod
    def from_dict(cls, data: dict) -> "Provenance":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Provenance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Provenance(DomainResource):
    """Provenance of a resource is a record that describes entities and processes involved in producing and delivering or otherwise influencing that resource. Provenance provides a critical foundation for assessing authenticity, enabling trust, and allowing reproducibility. Provenance assertions are a form of contextual metadata and can themselves become important records with their own provenance. Provenance statement indicates clinical significance in terms of confidence in authenticity, reliability, and trustworthiness, integrity, and stage in lifecycle (e.g. Document Completion - has the artifact been legally authenticated), all of which may impact security, privacy, and trust policies.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference target: Target Reference(s) (usually version specific)
    :param Period occurredPeriod: When the activity occurred
    :param str occurredDateTime: When the activity occurred
    :param str recorded: When the activity was recorded / updated
    :param str policy: Policy or plan the activity was defined by
    :param Reference location: Where the activity occurred, if relevant
    :param CodeableConcept reason: Reason the activity is occurring
    :param CodeableConcept activity: Activity that occurred
    :param Agent agent: Actor involved
    :param Entity entity: An entity used in this activity
    :param Signature signature: Signature on target
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "target": {"class_name": "Reference", "is_contained": False},
        "occurredPeriod": {"class_name": "Period", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        "activity": {"class_name": "CodeableConcept", "is_contained": False},
        "agent": {"class_name": "Agent", "is_contained": True},
        "entity": {"class_name": "Entity", "is_contained": True},
        "signature": {"class_name": "Signature", "is_contained": False},
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
        target: list["Reference"] = None,
        occurredPeriod: "Period" = None,
        occurredDateTime: "str" = None,
        recorded: "str" = None,
        policy: list["str"] = None,
        location: "Reference" = None,
        reason: list["CodeableConcept"] = None,
        activity: "CodeableConcept" = None,
        agent: list["Agent"] = None,
        entity: list["Entity"] = None,
        signature: list["Signature"] = None,
    ):
        self.resourceType = resourceType or "Provenance"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.target = target or []
        self.occurredPeriod = occurredPeriod
        self.occurredDateTime = occurredDateTime
        self.recorded = recorded
        self.policy = policy or []
        self.location = location
        self.reason = reason or []
        self.activity = activity
        self.agent = agent or []
        self.entity = entity or []
        self.signature = signature or []

    @classmethod
    def from_dict(cls, data: dict) -> "Provenance":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Provenance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
