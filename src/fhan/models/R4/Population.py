"""
Generated class for Population. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Range import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *


@dataclass
class Population(Element):
    """ Base StructureDefinition for Population Type: A populatioof people with some set of grouping criteria.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Range ageRange: The age of the specific population
    :param CodeableConcept gender: The gender of the specific population
    :param CodeableConcept race: Race of the specific population
    :param CodeableConcept physiologicalCondition: The existing physiological conditions of the specific population to which this applies
    """

    resourceType: str = "Population"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    ageRange: "Range" = Range()
    
    gender: "CodeableConcept" = CodeableConcept()
    
    race: "CodeableConcept" = CodeableConcept()
    
    physiologicalCondition: "CodeableConcept" = CodeableConcept()
    