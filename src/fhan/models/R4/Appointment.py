"""
Generated class for Appointment. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Participant(BaseModel):
    """List of participants involved in the appointment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Role of participant in the appointment
    :param Reference actor: Person, Location/HealthcareService or Device
    :param str required: required | optional | information-only
    :param str status: accepted | declined | tentative | needs-action
    :param Period period: Participation period of the actor
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: list["CodeableConcept"] = None,
        actor: "Reference" = None,
        required: "str" = None,
        status: "str" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type or []
        self.actor = actor
        self.required = required
        self.status = status
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Appointment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Appointment(DomainResource):
    """A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this item
    :param str status: proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist
    :param CodeableConcept cancelationReason: The coded reason for the appointment being cancelled
    :param CodeableConcept serviceCategory: A broad categorization of the service that is to be performed during this appointment
    :param CodeableConcept serviceType: The specific service that is to be performed during this appointment
    :param CodeableConcept specialty: The specialty of a practitioner that would be required to perform the service requested in this appointment
    :param CodeableConcept appointmentType: The style of appointment or patient that has been booked in the slot (not service type)
    :param CodeableConcept reasonCode: Coded reason this appointment is scheduled
    :param Reference reasonReference: Reason the appointment is to take place (resource)
    :param int priority: Used to make informed decisions if needing to re-prioritize
    :param str description: Shown on a subject line in a meeting request, or appointment list
    :param Reference supportingInformation: Additional information to support the appointment
    :param str start: When appointment is to take place
    :param str end: When appointment is to conclude
    :param int minutesDuration: Can be less than start/end (e.g. estimate)
    :param Reference slot: The slots that this appointment is filling
    :param str created: The date that this appointment was initially created
    :param str comment: Additional comments
    :param str patientInstruction: Detailed information and instructions for the patient
    :param Reference basedOn: The service request this appointment is allocated to assess
    :param Participant participant: Participants involved in appointment
    :param Period requestedPeriod: Potential date/time interval(s) requested to allocate the appointment within
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "cancelationReason": {"class_name": "CodeableConcept", "is_contained": False},
        "serviceCategory": {"class_name": "CodeableConcept", "is_contained": False},
        "serviceType": {"class_name": "CodeableConcept", "is_contained": False},
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
        "appointmentType": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "supportingInformation": {"class_name": "Reference", "is_contained": False},
        "slot": {"class_name": "Reference", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "participant": {"class_name": "Participant", "is_contained": True},
        "requestedPeriod": {"class_name": "Period", "is_contained": False},
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
        cancelationReason: "CodeableConcept" = None,
        serviceCategory: list["CodeableConcept"] = None,
        serviceType: list["CodeableConcept"] = None,
        specialty: list["CodeableConcept"] = None,
        appointmentType: "CodeableConcept" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        priority: "int" = None,
        description: "str" = None,
        supportingInformation: list["Reference"] = None,
        start: "str" = None,
        end: "str" = None,
        minutesDuration: "int" = None,
        slot: list["Reference"] = None,
        created: "str" = None,
        comment: "str" = None,
        patientInstruction: "str" = None,
        basedOn: list["Reference"] = None,
        participant: list["Participant"] = None,
        requestedPeriod: list["Period"] = None,
    ):
        self.resourceType = resourceType or "Appointment"
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
        self.cancelationReason = cancelationReason
        self.serviceCategory = serviceCategory or []
        self.serviceType = serviceType or []
        self.specialty = specialty or []
        self.appointmentType = appointmentType
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.priority = priority
        self.description = description
        self.supportingInformation = supportingInformation or []
        self.start = start
        self.end = end
        self.minutesDuration = minutesDuration
        self.slot = slot or []
        self.created = created
        self.comment = comment
        self.patientInstruction = patientInstruction
        self.basedOn = basedOn or []
        self.participant = participant or []
        self.requestedPeriod = requestedPeriod or []

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Appointment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
