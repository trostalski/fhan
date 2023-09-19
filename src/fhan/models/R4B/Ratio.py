"""
Generated class for Ratio. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *


@dataclass
class Ratio:
    """
    Base StructureDefinition for Ratio Type: A relationship of two Quantity values - expressed as a numerator and a denominator.
    """
    id: str = None
    
    extension: "Extension" = None
    
    numerator: "Quantity" = None
    
    denominator: "Quantity" = None
    