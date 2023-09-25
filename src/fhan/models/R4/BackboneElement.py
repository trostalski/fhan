"""
Generated class for BackboneElement. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class BackboneElement(ModelBase):
    """ Base StructureDefinition for BackboneElement Type: Base definition for all elements that are defined inside a resource - but not those in a data type.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    def __init__(self, resourceType: str = "BackboneElement",  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None, ):
        self.resourceType: str = resourceType or "BackboneElement"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        