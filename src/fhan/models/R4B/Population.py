"""
Generated class for Population. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Range import *


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
    