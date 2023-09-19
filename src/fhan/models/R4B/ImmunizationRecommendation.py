"""
Generated class for ImmunizationRecommendation. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class ImmunizationRecommendation:
    """
    A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with optional supporting justification.
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
    
    patient: "Reference" = None
    
    date: str = None
    
    authority: "Reference" = None
    
    recommendation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    vaccineCode: "CodeableConcept" = None
    
    targetDisease: "CodeableConcept" = None
    
    contraindicatedVaccineCode: "CodeableConcept" = None
    
    forecastStatus: "CodeableConcept" = None
    
    forecastReason: "CodeableConcept" = None
    
    dateCriterion: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    value: str = None
    
    description: str = None
    
    series: str = None
    
    doseNumberpositiveInt: int = None
    
    doseNumberpositiveInt: str = None
    
    seriesDosespositiveInt: int = None
    
    seriesDosespositiveInt: str = None
    
    supportingImmunization: "Reference" = None
    
    supportingPatientInformation: "Reference" = None
    