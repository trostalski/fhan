"""
Generated class for Slot. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Slot:
    """
    A slot of time on a schedule that may be available for booking appointments.
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
    
    serviceCategory: "CodeableConcept" = None
    
    serviceType: "CodeableConcept" = None
    
    specialty: "CodeableConcept" = None
    
    appointmentType: "CodeableConcept" = None
    
    schedule: "Reference" = None
    
    status: str = None
    
    start: str = None
    
    end: str = None
    
    overbooked: bool = None
    
    comment: str = None
    