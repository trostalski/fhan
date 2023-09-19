"""
Generated class for HealthcareService. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.ContactPoint import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class HealthcareService:
    """
    The details of a healthcare service available at a location.
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
    