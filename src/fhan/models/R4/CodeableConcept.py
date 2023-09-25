"""
Generated class for CodeableConcept. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class CodeableConcept(ModelBase):
    """ Base StructureDefinition for CodeableConcept Type: A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Coding'] coding: Code defined by a terminology system
    :param str text: Plain text representation of the concept
    """
    def __init__(self, resourceType: str = "CodeableConcept",  id: str = None,  extension: list['Extension'] = None,  coding: list['Coding'] = None,  text: str = None, ):
        self.resourceType: str = resourceType or "CodeableConcept"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.coding: list['Coding'] = coding or []
        self.text: str = text 
        