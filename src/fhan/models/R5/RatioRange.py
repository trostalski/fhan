"""
Generated class for RatioRange. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Quantity import *
from fhan.models.R5.Extension import *


@dataclass
class RatioRange:
    """ RatioRange Type: A range of ratios expressed as a low and high numerator and a denominator.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity lowNumerator: Low Numerator limit
    :param Quantity highNumerator: High Numerator limit
    :param Quantity denominator: Denominator value
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    lowNumerator: "Quantity" = None
    
    highNumerator: "Quantity" = None
    
    denominator: "Quantity" = None
    