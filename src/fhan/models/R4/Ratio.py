"""
Generated class for Ratio. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *


@dataclass
class Ratio:
    """
    Base StructureDefinition for Ratio Type: A relationship of two Quantity values - expressed as a numerator and a denominator.
    """
    id: str = None
    
    extension: "Extension" = None
    
    numerator: "Quantity" = None
    
    denominator: "Quantity" = None
    