"""
Generated class for AppointmentResponse. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class AppointmentResponse(DomainResource):
    """A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this item
    :param Reference appointment: Appointment this response relates to
    :param str start: Time from appointment, or requested new start time
    :param str end: Time from appointment, or requested new end time
    :param CodeableConcept participantType: Role of participant in the appointment
    :param Reference actor: Person, Location, HealthcareService, or Device
    :param str participantStatus: accepted | declined | tentative | needs-action
    :param str comment: Additional comments
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "appointment": {"class_name": "Reference", "is_contained": False},
        "participantType": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
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
        appointment: "Reference" = None,
        start: "str" = None,
        end: "str" = None,
        participantType: list["CodeableConcept"] = None,
        actor: "Reference" = None,
        participantStatus: "str" = None,
        comment: "str" = None,
    ):
        self.resourceType = resourceType or "AppointmentResponse"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.appointment = appointment
        self.start = start
        self.end = end
        self.participantType = participantType or []
        self.actor = actor
        self.participantStatus = participantStatus
        self.comment = comment

    @classmethod
    def from_dict(cls, data: dict) -> "AppointmentResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AppointmentResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
