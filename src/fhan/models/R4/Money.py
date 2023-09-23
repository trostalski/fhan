"""
Generated class for Money. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *


@dataclass
class Money(Element):
    """ Base StructureDefinition for Money Type: An amount of economic utility in some recognized currency.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str currency: ISO 4217 Currency Code
    """

    resourceType: str = "Money"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    value: float = None
    
    currency: str = None
    