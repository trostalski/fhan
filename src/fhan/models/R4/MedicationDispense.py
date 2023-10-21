"""
Generated class for MedicationDispense. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Performer(BaseModel):
    """Indicates who or what performed the event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Who performed the dispense and what they did
    :param Reference actor: Individual who was performing
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        function: "CodeableConcept" = None,
        actor: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function
        self.actor = actor

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationDispense":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationDispense":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Substitution(BaseModel):
    """Indicates whether or not substitution was made as part of the dispense.  In some cases, substitution will be expected but does not happen, in other cases substitution is not expected but does happen.  This block explains what substitution did or did not happen and why.  If nothing is specified, substitution was not done.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool wasSubstituted: Whether a substitution was or was not performed on the dispense
    :param CodeableConcept type: Code signifying whether a different drug was dispensed from what was prescribed
    :param CodeableConcept reason: Why was substitution made
    :param Reference responsibleParty: Who is responsible for the substitution
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        "responsibleParty": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        wasSubstituted: "bool" = None,
        type: "CodeableConcept" = None,
        reason: list["CodeableConcept"] = None,
        responsibleParty: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.wasSubstituted = wasSubstituted
        self.type = type
        self.reason = reason or []
        self.responsibleParty = responsibleParty or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationDispense":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationDispense":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicationDispense(DomainResource):
    """Indicates that a medication product is to be or has been dispensed for a named person/patient.  This includes a description of the medication product (supply) provided and the instructions for administering the medication.  The medication dispense is the result of a pharmacy system responding to a medication order.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param Reference partOf: Event that dispense is part of
    :param str status: preparation | in-progress | cancelled | on-hold | completed | entered-in-error | stopped | declined | unknown
    :param CodeableConcept statusReasonCodeableConcept: Why a dispense was not performed
    :param Reference statusReasonReference: Why a dispense was not performed
    :param CodeableConcept category: Type of medication dispense
    :param CodeableConcept medicationCodeableConcept: What medication was supplied
    :param Reference medicationReference: What medication was supplied
    :param Reference subject: Who the dispense is for
    :param Reference context: Encounter / Episode associated with event
    :param Reference supportingInformation: Information that supports the dispensing of the medication
    :param Performer performer: Who performed event
    :param Reference location: Where the dispense occurred
    :param Reference authorizingPrescription: Medication order that authorizes the dispense
    :param CodeableConcept type: Trial fill, partial fill, emergency fill, etc.
    :param Quantity quantity: Amount dispensed
    :param Quantity daysSupply: Amount of medication expressed as a timing amount
    :param str whenPrepared: When product was packaged and reviewed
    :param str whenHandedOver: When product was given out
    :param Reference destination: Where the medication was sent
    :param Reference receiver: Who collected the medication
    :param Annotation note: Information about the dispense
    :param Dosage dosageInstruction: How the medication is to be used by the patient or administered by the caregiver
    :param Substitution substitution: Whether a substitution was performed on the dispense
    :param Reference detectedIssue: Clinical issue with action
    :param Reference eventHistory: A list of relevant lifecycle events
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "statusReasonCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "statusReasonReference": {"class_name": "Reference", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "medicationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "medicationReference": {"class_name": "Reference", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "context": {"class_name": "Reference", "is_contained": False},
        "supportingInformation": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Performer", "is_contained": True},
        "location": {"class_name": "Reference", "is_contained": False},
        "authorizingPrescription": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "daysSupply": {"class_name": "Quantity", "is_contained": False},
        "destination": {"class_name": "Reference", "is_contained": False},
        "receiver": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "dosageInstruction": {"class_name": "Dosage", "is_contained": False},
        "substitution": {"class_name": "Substitution", "is_contained": True},
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
        partOf: list["Reference"] = None,
        status: "str" = None,
        statusReasonCodeableConcept: "CodeableConcept" = None,
        statusReasonReference: "Reference" = None,
        category: "CodeableConcept" = None,
        medicationCodeableConcept: "CodeableConcept" = None,
        medicationReference: "Reference" = None,
        subject: "Reference" = None,
        context: "Reference" = None,
        supportingInformation: list["Reference"] = None,
        performer: list["Performer"] = None,
        location: "Reference" = None,
        authorizingPrescription: list["Reference"] = None,
        type: "CodeableConcept" = None,
        quantity: "Quantity" = None,
        daysSupply: "Quantity" = None,
        whenPrepared: "str" = None,
        whenHandedOver: "str" = None,
        destination: "Reference" = None,
        receiver: list["Reference"] = None,
        note: list["Annotation"] = None,
        dosageInstruction: list["Dosage"] = None,
        substitution: "Substitution" = None,
        detectedIssue: list["Reference"] = None,
        eventHistory: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "MedicationDispense"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.partOf = partOf or []
        self.status = status
        self.statusReasonCodeableConcept = statusReasonCodeableConcept
        self.statusReasonReference = statusReasonReference
        self.category = category
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference
        self.subject = subject
        self.context = context
        self.supportingInformation = supportingInformation or []
        self.performer = performer or []
        self.location = location
        self.authorizingPrescription = authorizingPrescription or []
        self.type = type
        self.quantity = quantity
        self.daysSupply = daysSupply
        self.whenPrepared = whenPrepared
        self.whenHandedOver = whenHandedOver
        self.destination = destination
        self.receiver = receiver or []
        self.note = note or []
        self.dosageInstruction = dosageInstruction or []
        self.substitution = substitution
        self.detectedIssue = detectedIssue or []
        self.eventHistory = eventHistory or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationDispense":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationDispense":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
