"""
Generated class for Slot. 
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


class Slot(DomainResource):
    """A slot of time on a schedule that may be available for booking appointments.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this item
    :param CodeableConcept serviceCategory: A broad categorization of the service that is to be performed during this appointment
    :param CodeableConcept serviceType: The type of appointments that can be booked into this slot (ideally this would be an identifiable service - which is at a location, rather than the location itself). If provided then this overrides the value provided on the availability resource
    :param CodeableConcept specialty: The specialty of a practitioner that would be required to perform the service requested in this appointment
    :param CodeableConcept appointmentType: The style of appointment or patient that may be booked in the slot (not service type)
    :param Reference schedule: The schedule resource that this slot defines an interval of status information
    :param str status: busy | free | busy-unavailable | busy-tentative | entered-in-error
    :param str start: Date/Time that the slot is to begin
    :param str end: Date/Time that the slot is to conclude
    :param bool overbooked: This slot has already been overbooked, appointments are unlikely to be accepted for this time
    :param str comment: Comments on the slot to describe any extended information. Such as custom constraints on the slot
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "serviceCategory": {"class_name": "CodeableConcept", "is_contained": False},
        "serviceType": {"class_name": "CodeableConcept", "is_contained": False},
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
        "appointmentType": {"class_name": "CodeableConcept", "is_contained": False},
        "schedule": {"class_name": "Reference", "is_contained": False},
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
        serviceCategory: list["CodeableConcept"] = None,
        serviceType: list["CodeableConcept"] = None,
        specialty: list["CodeableConcept"] = None,
        appointmentType: "CodeableConcept" = None,
        schedule: "Reference" = None,
        status: "str" = None,
        start: "str" = None,
        end: "str" = None,
        overbooked: "bool" = None,
        comment: "str" = None,
    ):
        self.resourceType = resourceType or "Slot"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.serviceCategory = serviceCategory or []
        self.serviceType = serviceType or []
        self.specialty = specialty or []
        self.appointmentType = appointmentType
        self.schedule = schedule
        self.status = status
        self.start = start
        self.end = end
        self.overbooked = overbooked
        self.comment = comment

    @classmethod
    def from_dict(cls, data: dict) -> "Slot":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Slot":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
