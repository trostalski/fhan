"""
Generated class for Population. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Range import *
from fhan.models.R4.Element import *




@dataclass
class Population(Element):
    """ Base StructureDefinition for Population Type: A populatioof people with some set of grouping criteria.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Range ageRange: The age of the specific population
    :param CodeableConcept ageRange: The age of the specific population
    :param CodeableConcept gender: The gender of the specific population
    :param CodeableConcept race: Race of the specific population
    :param CodeableConcept physiologicalCondition: The existing physiological conditions of the specific population to which this applies
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    ageRange: "Range" = None
    
    ageRange: "CodeableConcept" = None
    
    gender: "CodeableConcept" = None
    
    race: "CodeableConcept" = None
    
    physiologicalCondition: "CodeableConcept" = None
    