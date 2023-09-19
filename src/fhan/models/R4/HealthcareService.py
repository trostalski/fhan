"""
Generated class for HealthcareService. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    active: bool = None
    
    providedBy: "Reference" = None
    
    category: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    specialty: "CodeableConcept" = None
    
    location: "Reference" = None
    
    name: str = None
    
    comment: str = None
    
    extraDetails: str = None
    
    photo: "Attachment" = None
    
    telecom: "ContactPoint" = None
    
    coverageArea: "Reference" = None
    
    serviceProvisionCode: "CodeableConcept" = None
    
    eligibility: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    comment: str = None
    
    program: "CodeableConcept" = None
    
    characteristic: "CodeableConcept" = None
    
    communication: "CodeableConcept" = None
    
    referralMethod: "CodeableConcept" = None
    
    appointmentRequired: bool = None
    
    availableTime: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    daysOfWeek: str = None
    
    allDay: bool = None
    
    availableStartTime: str = None
    
    availableEndTime: str = None
    
    notAvailable: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    during: "Period" = None
    
    availabilityExceptions: str = None
    
    endpoint: "Reference" = None
    