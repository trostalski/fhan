"""
Generated class for Appointment. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Appointment:
    """
    A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).
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
    
    status: str = None
    
    cancelationReason: "CodeableConcept" = None
    
    serviceCategory: "CodeableConcept" = None
    
    serviceType: "CodeableConcept" = None
    
    specialty: "CodeableConcept" = None
    
    appointmentType: "CodeableConcept" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    priority: int = None
    
    description: str = None
    
    supportingInformation: "Reference" = None
    
    start: str = None
    
    end: str = None
    
    minutesDuration: int = None
    
    slot: "Reference" = None
    
    created: str = None
    
    comment: str = None
    
    patientInstruction: str = None
    
    basedOn: "Reference" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    required: str = None
    
    status: str = None
    
    period: "Period" = None
    
    requestedPeriod: "Period" = None
    