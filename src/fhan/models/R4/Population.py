"""
Generated class for Population. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Population(ModelBase):
    """ Base StructureDefinition for Population Type: A populatioof people with some set of grouping criteria.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Range' ageRange: The age of the specific population
    :param 'CodeableConcept' ageCodeableConcept: The age of the specific population
    :param 'CodeableConcept' gender: The gender of the specific population
    :param 'CodeableConcept' race: Race of the specific population
    :param 'CodeableConcept' physiologicalCondition: The existing physiological conditions of the specific population to which this applies
    """
    def __init__(self, resourceType: str = "Population",  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  ageRange: 'Range' = None,  ageCodeableConcept: 'CodeableConcept' = None,  gender: 'CodeableConcept' = None,  race: 'CodeableConcept' = None,  physiologicalCondition: 'CodeableConcept' = None, ):
        self.resourceType: str = resourceType or "Population"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.ageRange: 'Range' = ageRange 
        self.ageCodeableConcept: 'CodeableConcept' = ageCodeableConcept 
        self.gender: 'CodeableConcept' = gender 
        self.race: 'CodeableConcept' = race 
        self.physiologicalCondition: 'CodeableConcept' = physiologicalCondition 
        