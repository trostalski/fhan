"""
Generated class for AppointmentResponse. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class AppointmentResponse:
    """
    A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
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
    
    appointment: "Reference" = None
    
    start: str = None
    
    end: str = None
    
    participantType: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    participantStatus: str = None
    
    comment: str = None
    