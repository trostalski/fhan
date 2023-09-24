"""
Generated class for Money. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Money(ModelBase):
    """ Base StructureDefinition for Money Type: An amount of economic utility in some recognized currency.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str currency: ISO 4217 Currency Code
    """
    def __init__(self, resourceType: str = "Money",  id: str = None,  extension: list['Extension'] = None,  value: float = None,  currency: str = None, ):
        self.resourceType: str = resourceType or "Money"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.value: float = value 
        self.currency: str = currency 
        