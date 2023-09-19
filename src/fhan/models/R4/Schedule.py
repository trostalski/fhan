"""
Generated class for Schedule. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Schedule:
    """
    A container for slots of time that may be available for booking appointments.
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
    
    serviceCategory: "CodeableConcept" = None
    
    serviceType: "CodeableConcept" = None
    
    specialty: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    planningHorizon: "Period" = None
    
    comment: str = None
    