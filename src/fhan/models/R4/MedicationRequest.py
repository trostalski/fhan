"""
Generated class for MedicationRequest. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class InitialFill(BaseModel):
    """Indicates the quantity or duration for the first dispense of the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: First fill quantity
    :param Duration duration: First fill duration
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "duration": {"class_name": "Duration", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        quantity: "Quantity" = None,
        duration: "Duration" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.quantity = quantity
        self.duration = duration

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DispenseRequest(BaseModel):
    """Indicates the specific details for the dispense or medication supply part of a medication request (also known as a Medication Prescription or Medication Order).  Note that this information is not always sent with the order.  There may be in some settings (e.g. hospitals) institutional or system support for completing the dispense details in the pharmacy department.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param InitialFill initialFill: First fill details
    :param Duration dispenseInterval: Minimum period of time between dispenses
    :param Period validityPeriod: Time period supply is authorized for
    :param int numberOfRepeatsAllowed: Number of refills authorized
    :param Quantity quantity: Amount of medication to supply per dispense
    :param Duration expectedSupplyDuration: Number of days supply per dispense
    :param Reference performer: Intended dispenser
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "initialFill": {"class_name": "InitialFill", "is_contained": True},
        "dispenseInterval": {"class_name": "Duration", "is_contained": False},
        "validityPeriod": {"class_name": "Period", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "expectedSupplyDuration": {"class_name": "Duration", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        initialFill: "InitialFill" = None,
        dispenseInterval: "Duration" = None,
        validityPeriod: "Period" = None,
        numberOfRepeatsAllowed: "int" = None,
        quantity: "Quantity" = None,
        expectedSupplyDuration: "Duration" = None,
        performer: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.initialFill = initialFill
        self.dispenseInterval = dispenseInterval
        self.validityPeriod = validityPeriod
        self.numberOfRepeatsAllowed = numberOfRepeatsAllowed
        self.quantity = quantity
        self.expectedSupplyDuration = expectedSupplyDuration
        self.performer = performer

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Substitution(BaseModel):
    """Indicates whether or not substitution can or should be part of the dispense. In some cases, substitution must happen, in other cases substitution must not happen. This block explains the prescriber's intent. If nothing is specified substitution may be done.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool allowedBoolean: Whether substitution is allowed or not
    :param CodeableConcept allowedCodeableConcept: Whether substitution is allowed or not
    :param CodeableConcept reason: Why should (not) substitution be made
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "allowedCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        allowedBoolean: "bool" = None,
        allowedCodeableConcept: "CodeableConcept" = None,
        reason: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.allowedBoolean = allowedBoolean
        self.allowedCodeableConcept = allowedCodeableConcept
        self.reason = reason

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicationRequest(DomainResource):
    """An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External ids for this request
    :param str status: active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param str intent: proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
    :param CodeableConcept category: Type of medication usage
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if request is prohibiting action
    :param bool reportedBoolean: Reported rather than primary record
    :param Reference reportedReference: Reported rather than primary record
    :param CodeableConcept medicationCodeableConcept: Medication to be taken
    :param Reference medicationReference: Medication to be taken
    :param Reference subject: Who or group medication request is for
    :param Reference encounter: Encounter created as part of encounter/admission/stay
    :param Reference supportingInformation: Information to support ordering of the medication
    :param str authoredOn: When request was initially authored
    :param Reference requester: Who/What requested the Request
    :param Reference performer: Intended performer of administration
    :param CodeableConcept performerType: Desired kind of performer of the medication administration
    :param Reference recorder: Person who entered the request
    :param CodeableConcept reasonCode: Reason or indication for ordering or not ordering the medication
    :param Reference reasonReference: Condition or observation that supports why the prescription is being written
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: What request fulfills
    :param Identifier groupIdentifier: Composite request this is part of
    :param CodeableConcept courseOfTherapyType: Overall pattern of medication administration
    :param Reference insurance: Associated insurance coverage
    :param Annotation note: Information about the prescription
    :param Dosage dosageInstruction: How the medication should be taken
    :param DispenseRequest dispenseRequest: Medication supply authorization
    :param Substitution substitution: Any restrictions on medication substitution
    :param Reference priorPrescription: An order/prescription that is being replaced
    :param Reference detectedIssue: Clinical Issue with action
    :param Reference eventHistory: A list of events of interest in the lifecycle
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "reportedReference": {"class_name": "Reference", "is_contained": False},
        "medicationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "medicationReference": {"class_name": "Reference", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "supportingInformation": {"class_name": "Reference", "is_contained": False},
        "requester": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "performerType": {"class_name": "CodeableConcept", "is_contained": False},
        "recorder": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "groupIdentifier": {"class_name": "Identifier", "is_contained": False},
        "courseOfTherapyType": {"class_name": "CodeableConcept", "is_contained": False},
        "insurance": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "dosageInstruction": {"class_name": "Dosage", "is_contained": False},
        "dispenseRequest": {"class_name": "DispenseRequest", "is_contained": True},
        "substitution": {"class_name": "Substitution", "is_contained": True},
        "priorPrescription": {"class_name": "Reference", "is_contained": False},
        "detectedIssue": {"class_name": "Reference", "is_contained": False},
        "eventHistory": {"class_name": "Reference", "is_contained": False},
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
        statusReason: "CodeableConcept" = None,
        intent: "str" = None,
        category: list["CodeableConcept"] = None,
        priority: "str" = None,
        doNotPerform: "bool" = None,
        reportedBoolean: "bool" = None,
        reportedReference: "Reference" = None,
        medicationCodeableConcept: "CodeableConcept" = None,
        medicationReference: "Reference" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        supportingInformation: list["Reference"] = None,
        authoredOn: "str" = None,
        requester: "Reference" = None,
        performer: "Reference" = None,
        performerType: "CodeableConcept" = None,
        recorder: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        instantiatesCanonical: list["str"] = None,
        instantiatesUri: list["str"] = None,
        basedOn: list["Reference"] = None,
        groupIdentifier: "Identifier" = None,
        courseOfTherapyType: "CodeableConcept" = None,
        insurance: list["Reference"] = None,
        note: list["Annotation"] = None,
        dosageInstruction: list["Dosage"] = None,
        dispenseRequest: "DispenseRequest" = None,
        substitution: "Substitution" = None,
        priorPrescription: "Reference" = None,
        detectedIssue: list["Reference"] = None,
        eventHistory: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "MedicationRequest"
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
        self.statusReason = statusReason
        self.intent = intent
        self.category = category or []
        self.priority = priority
        self.doNotPerform = doNotPerform
        self.reportedBoolean = reportedBoolean
        self.reportedReference = reportedReference
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference
        self.subject = subject
        self.encounter = encounter
        self.supportingInformation = supportingInformation or []
        self.authoredOn = authoredOn
        self.requester = requester
        self.performer = performer
        self.performerType = performerType
        self.recorder = recorder
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.basedOn = basedOn or []
        self.groupIdentifier = groupIdentifier
        self.courseOfTherapyType = courseOfTherapyType
        self.insurance = insurance or []
        self.note = note or []
        self.dosageInstruction = dosageInstruction or []
        self.dispenseRequest = dispenseRequest
        self.substitution = substitution
        self.priorPrescription = priorPrescription
        self.detectedIssue = detectedIssue or []
        self.eventHistory = eventHistory or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
