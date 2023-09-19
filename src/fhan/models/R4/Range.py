"""
Generated class for Range. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *


@dataclass
class Range:
    """
    Base StructureDefinition for Range Type: A set of ordered Quantities defined by a low and high limit.
    """
    id: str = None
    
    extension: "Extension" = None
    
    low: "Quantity" = None
    
    high: "Quantity" = None
    