"""
Generated class for PractitionerRole. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class AvailableTime(BaseModel):
    """A collection of times the practitioner is available or performing this role at the location and/or healthcareservice.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: Always available? e.g. 24 hour service
    :param str availableStartTime: Opening time of day (ignored if allDay = true)
    :param str availableEndTime: Closing time of day (ignored if allDay = true)
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
        daysOfWeek: list["str"] = None,
        allDay: "bool" = None,
        availableStartTime: "str" = None,
        availableEndTime: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.daysOfWeek = daysOfWeek or []
        self.allDay = allDay
        self.availableStartTime = availableStartTime
        self.availableEndTime = availableEndTime

    @classmethod
    def from_dict(cls, data: dict) -> "PractitionerRole":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "PractitionerRole":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class NotAvailable(BaseModel):
    """The practitioner is not available or performing this role during this period of time due to the provided reason.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Reason presented to the user explaining why time not available
    :param Period during: Service not available from this date
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "during": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        description: "str" = None,
        during: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.during = during

    @classmethod
    def from_dict(cls, data: dict) -> "PractitionerRole":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "PractitionerRole":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PractitionerRole(DomainResource):
    """A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifiers that are specific to a role/location
    :param bool active: Whether this practitioner role record is in active use
    :param Period period: The period during which the practitioner is authorized to perform in these role(s)
    :param Reference practitioner: Practitioner that is able to provide the defined services for the organization
    :param Reference organization: Organization where the roles are available
    :param CodeableConcept code: Roles which this practitioner may perform
    :param CodeableConcept specialty: Specific specialty of the practitioner
    :param Reference location: The location(s) at which this practitioner provides care
    :param Reference healthcareService: The list of healthcare services that this worker provides for this role's Organization/Location(s)
    :param ContactPoint telecom: Contact details that are specific to the role/location/service
    :param AvailableTime availableTime: Times the Service Site is available
    :param NotAvailable notAvailable: Not available during this time due to provided reason
    :param str availabilityExceptions: Description of availability exceptions
    :param Reference endpoint: Technical endpoints providing access to services operated for the practitioner with this role
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "practitioner": {"class_name": "Reference", "is_contained": False},
        "organization": {"class_name": "Reference", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "healthcareService": {"class_name": "Reference", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "availableTime": {"class_name": "AvailableTime", "is_contained": True},
        "notAvailable": {"class_name": "NotAvailable", "is_contained": True},
        "endpoint": {"class_name": "Reference", "is_contained": False},
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
        active: "bool" = None,
        period: "Period" = None,
        practitioner: "Reference" = None,
        organization: "Reference" = None,
        code: list["CodeableConcept"] = None,
        specialty: list["CodeableConcept"] = None,
        location: list["Reference"] = None,
        healthcareService: list["Reference"] = None,
        telecom: list["ContactPoint"] = None,
        availableTime: list["AvailableTime"] = None,
        notAvailable: list["NotAvailable"] = None,
        availabilityExceptions: "str" = None,
        endpoint: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "PractitionerRole"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.active = active
        self.period = period
        self.practitioner = practitioner
        self.organization = organization
        self.code = code or []
        self.specialty = specialty or []
        self.location = location or []
        self.healthcareService = healthcareService or []
        self.telecom = telecom or []
        self.availableTime = availableTime or []
        self.notAvailable = notAvailable or []
        self.availabilityExceptions = availabilityExceptions
        self.endpoint = endpoint or []

    @classmethod
    def from_dict(cls, data: dict) -> "PractitionerRole":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "PractitionerRole":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
