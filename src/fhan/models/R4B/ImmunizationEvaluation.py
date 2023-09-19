"""
Generated class for ImmunizationEvaluation. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class ImmunizationEvaluation:
    """
    Describes a comparison of an immunization event against published recommendations to determine if the administration is "valid" in relation to those  recommendations.
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
    
    patient: "Reference" = None
    
    date: str = None
    
    authority: "Reference" = None
    
    targetDisease: "CodeableConcept" = None
    
    immunizationEvent: "Reference" = None
    
    doseStatus: "CodeableConcept" = None
    
    doseStatusReason: "CodeableConcept" = None
    
    description: str = None
    
    series: str = None
    
    doseNumberpositiveInt: int = None
    
    doseNumberpositiveInt: str = None
    
    seriesDosespositiveInt: int = None
    
    seriesDosespositiveInt: str = None
    