"""
Generated class for HealthcareService. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Eligibility(BaseModel):
    """Does this service have specific eligibility requirements that need to be met in order to use the service?:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded value for the eligibility
    :param str comment: Describes the eligibility conditions for the service
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        comment: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.comment = comment

    @classmethod
    def from_dict(cls, data: dict) -> "HealthcareService":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "HealthcareService":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AvailableTime(BaseModel):
    """A collection of times that the Service Site is available.:param str id: Unique id for inter-element referencing
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
    def from_dict(cls, data: dict) -> "HealthcareService":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "HealthcareService":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class NotAvailable(BaseModel):
    """The HealthcareService is not available during this period of time due to the provided reason.:param str id: Unique id for inter-element referencing
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
    def from_dict(cls, data: dict) -> "HealthcareService":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "HealthcareService":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class HealthcareService(DomainResource):
    """The details of a healthcare service available at a location.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifiers for this item
    :param bool active: Whether this HealthcareService record is in active use
    :param Reference providedBy: Organization that provides this service
    :param CodeableConcept category: Broad category of service being performed or delivered
    :param CodeableConcept type: Type of service that may be delivered or performed
    :param CodeableConcept specialty: Specialties handled by the HealthcareService
    :param Reference location: Location(s) where service may be provided
    :param str name: Description of service as presented to a consumer while searching
    :param str comment: Additional description and/or any specific issues not covered elsewhere
    :param str extraDetails: Extra details about the service that can't be placed in the other fields
    :param Attachment photo: Facilitates quick identification of the service
    :param ContactPoint telecom: Contacts related to the healthcare service
    :param Reference coverageArea: Location(s) service is intended for/available to
    :param CodeableConcept serviceProvisionCode: Conditions under which service is available/offered
    :param Eligibility eligibility: Specific eligibility requirements required to use the service
    :param CodeableConcept program: Programs that this service is applicable to
    :param CodeableConcept characteristic: Collection of characteristics (attributes)
    :param CodeableConcept communication: The language that this service is offered in
    :param CodeableConcept referralMethod: Ways that the service accepts referrals
    :param bool appointmentRequired: If an appointment is required for access to this service
    :param AvailableTime availableTime: Times the Service Site is available
    :param NotAvailable notAvailable: Not available during this time due to provided reason
    :param str availabilityExceptions: Description of availability exceptions
    :param Reference endpoint: Technical endpoints providing access to electronic services operated for the healthcare service
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "providedBy": {"class_name": "Reference", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "photo": {"class_name": "Attachment", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "coverageArea": {"class_name": "Reference", "is_contained": False},
        "serviceProvisionCode": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "eligibility": {"class_name": "Eligibility", "is_contained": True},
        "program": {"class_name": "CodeableConcept", "is_contained": False},
        "characteristic": {"class_name": "CodeableConcept", "is_contained": False},
        "communication": {"class_name": "CodeableConcept", "is_contained": False},
        "referralMethod": {"class_name": "CodeableConcept", "is_contained": False},
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
        providedBy: "Reference" = None,
        category: list["CodeableConcept"] = None,
        type: list["CodeableConcept"] = None,
        specialty: list["CodeableConcept"] = None,
        location: list["Reference"] = None,
        name: "str" = None,
        comment: "str" = None,
        extraDetails: "str" = None,
        photo: "Attachment" = None,
        telecom: list["ContactPoint"] = None,
        coverageArea: list["Reference"] = None,
        serviceProvisionCode: list["CodeableConcept"] = None,
        eligibility: list["Eligibility"] = None,
        program: list["CodeableConcept"] = None,
        characteristic: list["CodeableConcept"] = None,
        communication: list["CodeableConcept"] = None,
        referralMethod: list["CodeableConcept"] = None,
        appointmentRequired: "bool" = None,
        availableTime: list["AvailableTime"] = None,
        notAvailable: list["NotAvailable"] = None,
        availabilityExceptions: "str" = None,
        endpoint: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "HealthcareService"
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
        self.providedBy = providedBy
        self.category = category or []
        self.type = type or []
        self.specialty = specialty or []
        self.location = location or []
        self.name = name
        self.comment = comment
        self.extraDetails = extraDetails
        self.photo = photo
        self.telecom = telecom or []
        self.coverageArea = coverageArea or []
        self.serviceProvisionCode = serviceProvisionCode or []
        self.eligibility = eligibility or []
        self.program = program or []
        self.characteristic = characteristic or []
        self.communication = communication or []
        self.referralMethod = referralMethod or []
        self.appointmentRequired = appointmentRequired
        self.availableTime = availableTime or []
        self.notAvailable = notAvailable or []
        self.availabilityExceptions = availabilityExceptions
        self.endpoint = endpoint or []

    @classmethod
    def from_dict(cls, data: dict) -> "HealthcareService":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "HealthcareService":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
