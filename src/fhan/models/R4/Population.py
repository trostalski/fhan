"""
Generated class for Population. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *


@dataclass
class Population:
    """
    Base StructureDefinition for Population Type: A populatioof people with some set of grouping criteria.
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    ageRange: "Range" = None
    
    ageRange: "CodeableConcept" = None
    
    gender: "CodeableConcept" = None
    
    race: "CodeableConcept" = None
    
    physiologicalCondition: "CodeableConcept" = None
    