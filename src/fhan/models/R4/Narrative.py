"""
Generated class for Narrative. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Narrative(ModelBase):
    """ Base StructureDefinition for Narrative Type: A human-readable summary of the resource conveying the essential clinical and business information for the resource.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str status: generated | extensions | additional | empty
    :param str div: Limited xhtml content
    """
    def __init__(self, resourceType: str = "Narrative",  id: str = None,  extension: list['Extension'] = None,  status: str = None,  div: str = None, ):
        self.resourceType: str = resourceType or "Narrative"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.status: str = status 
        self.div: str = div 
        