"""
Generated class for Ratio. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *



@dataclass
class Ratio(Element):
    """ Base StructureDefinition for Ratio Type: A relationship of two Quantity values - expressed as a numerator and a denominator.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity numerator: Numerator value
    :param Quantity denominator: Denominator value
    """
    id: str = None
    
    extension: "Extension" = None
    
    numerator: "Quantity" = None
    
    denominator: "Quantity" = None
    