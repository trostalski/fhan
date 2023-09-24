"""
Generated class for Ratio. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.generator_models import ModelBase

class Ratio(ModelBase):
    """ Base StructureDefinition for Ratio Type: A relationship of two Quantity values - expressed as a numerator and a denominator.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'Quantity' numerator: Numerator value
    :param 'Quantity' denominator: Denominator value
    """
    def __init__(self, resourceType: str = "Ratio",  id: str = None,  extension: list['Extension'] = None,  numerator: 'Quantity' = None,  denominator: 'Quantity' = None, ):
        self.resourceType: str = resourceType or "Ratio"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.numerator: 'Quantity' = numerator 
        self.denominator: 'Quantity' = denominator 
        