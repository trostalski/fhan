"""
Generated class for Range. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.generator_models import ModelBase

class Range(ModelBase):
    """ Base StructureDefinition for Range Type: A set of ordered Quantities defined by a low and high limit.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'Quantity' low: Low limit
    :param 'Quantity' high: High limit
    """
    def __init__(self, resourceType: str = "Range",  id: str = None,  extension: list['Extension'] = None,  low: 'Quantity' = None,  high: 'Quantity' = None, ):
        self.resourceType: str = resourceType or "Range"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.low: 'Quantity' = low 
        self.high: 'Quantity' = high 
        