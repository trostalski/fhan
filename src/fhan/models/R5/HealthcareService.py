"""
Generated class for HealthcareService. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Availability import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class HealthcareService:
    """ The details of a healthcare service available at a location or in a catalog.  In the case where there is a hierarchy of services (for example, Lab -> Pathology -> Wound Cultures), this can be represented using a set of linked HealthcareServices.
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
    :param Reference offeredIn: The service within which this service is offered
    :param CodeableConcept category: Broad category of service being performed or delivered
    :param CodeableConcept type: Type of service that may be delivered or performed
    :param CodeableConcept specialty: Specialties handled by the HealthcareService
    :param Reference location: Location(s) where service may be provided
    :param str name: Description of service as presented to a consumer while searching
    :param str comment: Additional description and/or any specific issues not covered elsewhere
    :param str extraDetails: Extra details about the service that can't be placed in the other fields
    :param Attachment photo: Facilitates quick identification of the service
    :param ExtendedContactDetail contact: Official contact details for the HealthcareService
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
    :param Availability availability: Times the healthcare service is available (including exceptions)
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
    
    offeredIn: "Reference" = None
    
    category: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    specialty: "CodeableConcept" = None
    
    location: "Reference" = None
    
    name: str = None
    
    comment: str = None
    
    extraDetails: str = None
    
    photo: "Attachment" = None
    
    contact: "ExtendedContactDetail" = None
    
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
    
    availability: "Availability" = None
    
    endpoint: "Reference" = None
    