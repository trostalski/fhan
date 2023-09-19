"""
Generated class for Ratio. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Quantity import *
from fhan.models.R5.Extension import *


@dataclass
class Ratio:
    """ Ratio Type: A relationship of two Quantity values - expressed as a numerator and a denominator.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity numerator: Numerator value
    :param Quantity denominator: Denominator value
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    numerator: "Quantity" = None
    
    denominator: "Quantity" = None
    