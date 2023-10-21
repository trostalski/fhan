"""
Generated class for VerificationResult. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Signature import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class PrimarySource(BaseModel):
    """Information about the primary source(s) involved in validation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference who: Reference to the primary source
    :param CodeableConcept type: Type of primary source (License Board; Primary Education; Continuing Education; Postal Service; Relationship owner; Registration Authority; legal source; issuing source; authoritative source)
    :param CodeableConcept communicationMethod: Method for exchanging information with the primary source
    :param CodeableConcept validationStatus: successful | failed | unknown
    :param str validationDate: When the target was validated against the primary source
    :param CodeableConcept canPushUpdates: yes | no | undetermined
    :param CodeableConcept pushTypeAvailable: specific | any | source
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "who": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "communicationMethod": {"class_name": "CodeableConcept", "is_contained": False},
        "validationStatus": {"class_name": "CodeableConcept", "is_contained": False},
        "canPushUpdates": {"class_name": "CodeableConcept", "is_contained": False},
        "pushTypeAvailable": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        who: "Reference" = None,
        type: list["CodeableConcept"] = None,
        communicationMethod: list["CodeableConcept"] = None,
        validationStatus: "CodeableConcept" = None,
        validationDate: "str" = None,
        canPushUpdates: "CodeableConcept" = None,
        pushTypeAvailable: list["CodeableConcept"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.who = who
        self.type = type or []
        self.communicationMethod = communicationMethod or []
        self.validationStatus = validationStatus
        self.validationDate = validationDate
        self.canPushUpdates = canPushUpdates
        self.pushTypeAvailable = pushTypeAvailable or []

    @classmethod
    def from_dict(cls, data: dict) -> "VerificationResult":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "VerificationResult":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Attestation(BaseModel):
    """Information about the entity attesting to information.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference who: The individual or organization attesting to information
    :param Reference onBehalfOf: When the who is asserting on behalf of another (organization or individual)
    :param CodeableConcept communicationMethod: The method by which attested information was submitted/retrieved
    :param str date: The date the information was attested to
    :param str sourceIdentityCertificate: A digital identity certificate associated with the attestation source
    :param str proxyIdentityCertificate: A digital identity certificate associated with the proxy entity submitting attested information on behalf of the attestation source
    :param Signature proxySignature: Proxy signature
    :param Signature sourceSignature: Attester signature
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "who": {"class_name": "Reference", "is_contained": False},
        "onBehalfOf": {"class_name": "Reference", "is_contained": False},
        "communicationMethod": {"class_name": "CodeableConcept", "is_contained": False},
        "proxySignature": {"class_name": "Signature", "is_contained": False},
        "sourceSignature": {"class_name": "Signature", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        who: "Reference" = None,
        onBehalfOf: "Reference" = None,
        communicationMethod: "CodeableConcept" = None,
        date: "str" = None,
        sourceIdentityCertificate: "str" = None,
        proxyIdentityCertificate: "str" = None,
        proxySignature: "Signature" = None,
        sourceSignature: "Signature" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.who = who
        self.onBehalfOf = onBehalfOf
        self.communicationMethod = communicationMethod
        self.date = date
        self.sourceIdentityCertificate = sourceIdentityCertificate
        self.proxyIdentityCertificate = proxyIdentityCertificate
        self.proxySignature = proxySignature
        self.sourceSignature = sourceSignature

    @classmethod
    def from_dict(cls, data: dict) -> "VerificationResult":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "VerificationResult":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Validator(BaseModel):
    """Information about the entity validating information.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference organization: Reference to the organization validating information
    :param str identityCertificate: A digital identity certificate associated with the validator
    :param Signature attestationSignature: Validator signature
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "organization": {"class_name": "Reference", "is_contained": False},
        "attestationSignature": {"class_name": "Signature", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        organization: "Reference" = None,
        identityCertificate: "str" = None,
        attestationSignature: "Signature" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.organization = organization
        self.identityCertificate = identityCertificate
        self.attestationSignature = attestationSignature

    @classmethod
    def from_dict(cls, data: dict) -> "VerificationResult":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "VerificationResult":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class VerificationResult(DomainResource):
    """Describes validation requirements, source(s), status and dates for one or more elements.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference target: A resource that was validated
    :param str targetLocation: The fhirpath location(s) within the resource that was validated
    :param CodeableConcept need: none | initial | periodic
    :param str status: attested | validated | in-process | req-revalid | val-fail | reval-fail
    :param str statusDate: When the validation status was updated
    :param CodeableConcept validationType: nothing | primary | multiple
    :param CodeableConcept validationProcess: The primary process by which the target is validated (edit check; value set; primary source; multiple sources; standalone; in context)
    :param Timing frequency: Frequency of revalidation
    :param str lastPerformed: The date/time validation was last completed (including failed validations)
    :param str nextScheduled: The date when target is next validated, if appropriate
    :param CodeableConcept failureAction: fatal | warn | rec-only | none
    :param PrimarySource primarySource: Information about the primary source(s) involved in validation
    :param Attestation attestation: Information about the entity attesting to information
    :param Validator validator: Information about the entity validating information
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "target": {"class_name": "Reference", "is_contained": False},
        "need": {"class_name": "CodeableConcept", "is_contained": False},
        "validationType": {"class_name": "CodeableConcept", "is_contained": False},
        "validationProcess": {"class_name": "CodeableConcept", "is_contained": False},
        "frequency": {"class_name": "Timing", "is_contained": False},
        "failureAction": {"class_name": "CodeableConcept", "is_contained": False},
        "primarySource": {"class_name": "PrimarySource", "is_contained": True},
        "attestation": {"class_name": "Attestation", "is_contained": True},
        "validator": {"class_name": "Validator", "is_contained": True},
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
        targetLocation: list["str"] = None,
        need: "CodeableConcept" = None,
        status: "str" = None,
        statusDate: "str" = None,
        validationType: "CodeableConcept" = None,
        validationProcess: list["CodeableConcept"] = None,
        frequency: "Timing" = None,
        lastPerformed: "str" = None,
        nextScheduled: "str" = None,
        failureAction: "CodeableConcept" = None,
        primarySource: list["PrimarySource"] = None,
        attestation: "Attestation" = None,
        validator: list["Validator"] = None,
    ):
        self.resourceType = resourceType or "VerificationResult"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.target = target or []
        self.targetLocation = targetLocation or []
        self.need = need
        self.status = status
        self.statusDate = statusDate
        self.validationType = validationType
        self.validationProcess = validationProcess or []
        self.frequency = frequency
        self.lastPerformed = lastPerformed
        self.nextScheduled = nextScheduled
        self.failureAction = failureAction
        self.primarySource = primarySource or []
        self.attestation = attestation
        self.validator = validator or []

    @classmethod
    def from_dict(cls, data: dict) -> "VerificationResult":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "VerificationResult":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
