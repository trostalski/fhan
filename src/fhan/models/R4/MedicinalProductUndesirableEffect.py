"""
Generated class for MedicinalProductUndesirableEffect. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Population import *
from fhan.models.R4.Meta import *


@dataclass
class MedicinalProductUndesirableEffect:
    """
    Describe the undesirable effects of the medicinal product.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    subject: "Reference" = None
    
    symptomConditionEffect: "CodeableConcept" = None
    
    classification: "CodeableConcept" = None
    
    frequencyOfOccurrence: "CodeableConcept" = None
    
    population: "Population" = None
    