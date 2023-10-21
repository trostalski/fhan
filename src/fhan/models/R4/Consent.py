"""
Generated class for Consent. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Policy(BaseModel):
    """The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str authority: Enforcement source for policy
    :param str uri: Specific policy covered by this consent
    :param CodeableConcept policyRule: Regulation that this consents to
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "policyRule": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        authority: "str" = None,
        uri: "str" = None,
        policyRule: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.authority = authority
        self.uri = uri
        self.policyRule = policyRule

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Verification(BaseModel):
    """Whether a treatment instruction (e.g. artificial respiration yes or no) was verified with the patient, his/her family or another authorized person.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool verified: Has been verified
    :param Reference verifiedWith: Person who verified
    :param str verificationDate: When consent verified
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "verifiedWith": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        verified: "bool" = None,
        verifiedWith: "Reference" = None,
        verificationDate: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.verified = verified
        self.verifiedWith = verifiedWith
        self.verificationDate = verificationDate

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Actor(BaseModel):
    """Who or what is controlled by this rule. Use group to identify a set of actors by some property they share (e.g. 'admitting officers').:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: How the actor is involved
    :param Reference reference: Resource for the actor (or group, by role)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        role: "CodeableConcept" = None,
        reference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role
        self.reference = reference

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Data(BaseModel):
    """The resources controlled by this rule if specific resources are referenced.:param Period dataPeriod: Timeframe for data controlled by this rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str meaning: instance | related | dependents | authoredby
    :param Reference reference: The actual data reference
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "dataPeriod": {"class_name": "Period", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        dataPeriod: "Period" = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        meaning: "str" = None,
        reference: "Reference" = None,
    ):
        self.dataPeriod = dataPeriod
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.meaning = meaning
        self.reference = reference

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Provision(BaseModel):
    """An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: deny | permit
    :param Period period: Timeframe for this rule
    :param Actor actor: Who|what controlled by this rule (or group, by role)
    :param CodeableConcept action: Actions controlled by this rule
    :param Coding securityLabel: Security Labels that define affected resources
    :param Coding purpose: Context of activities covered by this rule
    :param Coding _class: e.g. Resource Type, Profile, CDA, etc.
    :param CodeableConcept code: e.g. LOINC or SNOMED CT code, etc. in the content
    :param Period dataPeriod: Timeframe for data controlled by this rule
    :param Data data: Data controlled by this rule
    :param Provision provision: Nested Exception Rules
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "actor": {"class_name": "Actor", "is_contained": True},
        "action": {"class_name": "CodeableConcept", "is_contained": False},
        "securityLabel": {"class_name": "Coding", "is_contained": False},
        "purpose": {"class_name": "Coding", "is_contained": False},
        "_class": {"class_name": "Coding", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "dataPeriod": {"class_name": "Period", "is_contained": False},
        "data": {"class_name": "Data", "is_contained": True},
        "provision": {"class_name": "Provision", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "str" = None,
        period: "Period" = None,
        actor: list["Actor"] = None,
        action: list["CodeableConcept"] = None,
        securityLabel: list["Coding"] = None,
        purpose: list["Coding"] = None,
        _class: list["Coding"] = None,
        code: list["CodeableConcept"] = None,
        dataPeriod: "Period" = None,
        data: list["Data"] = None,
        provision: list["Provision"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.period = period
        self.actor = actor or []
        self.action = action or []
        self.securityLabel = securityLabel or []
        self.purpose = purpose or []
        self._class = _class or []
        self.code = code or []
        self.dataPeriod = dataPeriod
        self.data = data or []
        self.provision = provision or []

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Consent(DomainResource):
    """A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier for this record (external references)
    :param str status: draft | proposed | active | rejected | inactive | entered-in-error
    :param CodeableConcept scope: Which of the four areas this resource covers (extensible)
    :param CodeableConcept category: Classification of the consent statement - for indexing/retrieval
    :param Reference patient: Who the consent applies to
    :param str dateTime: When this Consent was created or indexed
    :param Reference performer: Who is agreeing to the policy and rules
    :param Reference organization: Custodian of the consent
    :param Attachment sourceAttachment: Source from which this consent is taken
    :param Reference sourceReference: Source from which this consent is taken
    :param Policy policy: Policies covered by this consent
    :param Verification verification: Consent Verified by patient or family
    :param Provision provision: Constraints to the base Consent.policyRule
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "scope": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "organization": {"class_name": "Reference", "is_contained": False},
        "sourceAttachment": {"class_name": "Attachment", "is_contained": False},
        "sourceReference": {"class_name": "Reference", "is_contained": False},
        "policy": {"class_name": "Policy", "is_contained": True},
        "verification": {"class_name": "Verification", "is_contained": True},
        "provision": {"class_name": "Provision", "is_contained": True},
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
        scope: "CodeableConcept" = None,
        category: list["CodeableConcept"] = None,
        patient: "Reference" = None,
        dateTime: "str" = None,
        performer: list["Reference"] = None,
        organization: list["Reference"] = None,
        sourceAttachment: "Attachment" = None,
        sourceReference: "Reference" = None,
        policy: list["Policy"] = None,
        verification: list["Verification"] = None,
        provision: "Provision" = None,
    ):
        self.resourceType = resourceType or "Consent"
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
        self.scope = scope
        self.category = category or []
        self.patient = patient
        self.dateTime = dateTime
        self.performer = performer or []
        self.organization = organization or []
        self.sourceAttachment = sourceAttachment
        self.sourceReference = sourceReference
        self.policy = policy or []
        self.verification = verification or []
        self.provision = provision

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
