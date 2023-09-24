"""
Generated class for Element. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Element(ModelBase):
    """ Base StructureDefinition for Element Type: Base definition for all elements in a resource.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    """
    def __init__(self, resourceType: str = "Element",  id: str = None,  extension: list['Extension'] = None, ):
        self.resourceType: str = resourceType or "Element"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        