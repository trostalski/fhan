"""
Generated class for RatioRange. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *


@dataclass
class RatioRange:
    """
    Base StructureDefinition for RatioRange Type: A range of ratios expressed as a low and high numerator and a denominator.
    """
    id: str = None
    
    extension: "Extension" = None
    
    lowNumerator: "Quantity" = None
    
    highNumerator: "Quantity" = None
    
    denominator: "Quantity" = None
    