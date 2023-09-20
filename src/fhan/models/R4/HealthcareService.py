"""
Generated class for HealthcareService. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class eligibility(Element):
    """ Does this service have specific eligibility requirements that need to be met in order to use the service?
    :param BackboneElement eligibility: Specific eligibility requirements required to use the service
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded value for the eligibility
    :param str comment: Describes the eligibility conditions for the service
    """
    eligibility: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    comment: str = None
    
@dataclass
class availableTime(Element):
    """ A collection of times that the Service Site is available.
    :param BackboneElement availableTime: Times the Service Site is available
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: Always available? e.g. 24 hour service
    :param str availableStartTime: Opening time of day (ignored if allDay = true)
    :param str availableEndTime: Closing time of day (ignored if allDay = true)
    """
    availableTime: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    daysOfWeek: str = None
    
    allDay: bool = None
    
    availableStartTime: str = None
    
    availableEndTime: str = None
    
@dataclass
class notAvailable(Element):
    """ The HealthcareService is not available during this period of time due to the provided reason.
    :param BackboneElement notAvailable: Not available during this time due to provided reason
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Reason presented to the user explaining why time not available
    :param Period during: Service not available from this date
    """
    notAvailable: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    during: "Period" = None
    


@dataclass
class HealthcareService(ModelBase):
    """ The details of a healthcare service available at a location.
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
    :param BackboneElement eligibility: Specific eligibility requirements required to use the service
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded value for the eligibility
    :param str comment: Describes the eligibility conditions for the service
    :param CodeableConcept program: Programs that this service is applicable to
    :param CodeableConcept characteristic: Collection of characteristics (attributes)
    :param CodeableConcept communication: The language that this service is offered in
    :param CodeableConcept referralMethod: Ways that the service accepts referrals
    :param bool appointmentRequired: If an appointment is required for access to this service
    :param BackboneElement availableTime: Times the Service Site is available
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: Always available? e.g. 24 hour service
    :param str availableStartTime: Opening time of day (ignored if allDay = true)
    :param str availableEndTime: Closing time of day (ignored if allDay = true)
    :param BackboneElement notAvailable: Not available during this time due to provided reason
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Reason presented to the user explaining why time not available
    :param Period during: Service not available from this date
    :param str availabilityExceptions: Description of availability exceptions
    :param Reference endpoint: Technical endpoints providing access to electronic services operated for the healthcare service
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    active: bool = None
    
    providedBy: "Reference" = None
    
    category: list["CodeableConcept"] = None
    
    type: list["CodeableConcept"] = None
    
    specialty: list["CodeableConcept"] = None
    
    location: list["Reference"] = None
    
    name: str = None
    
    comment: str = None
    
    extraDetails: str = None
    
    photo: "Attachment" = None
    
    telecom: list["ContactPoint"] = None
    
    coverageArea: list["Reference"] = None
    
    serviceProvisionCode: list["CodeableConcept"] = None
    
    eligibility: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    comment: str = None
    
    program: list["CodeableConcept"] = None
    
    characteristic: list["CodeableConcept"] = None
    
    communication: list["CodeableConcept"] = None
    
    referralMethod: list["CodeableConcept"] = None
    
    appointmentRequired: bool = None
    
    availableTime: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    daysOfWeek: str = None
    
    allDay: bool = None
    
    availableStartTime: str = None
    
    availableEndTime: str = None
    
    notAvailable: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    during: "Period" = None
    
    availabilityExceptions: str = None
    
    endpoint: list["Reference"] = None
    