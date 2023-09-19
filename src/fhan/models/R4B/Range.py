"""
Generated class for Range. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *


@dataclass
class Range:
    """
    Base StructureDefinition for Range Type: A set of ordered Quantities defined by a low and high limit.
    """
    id: str = None
    
    extension: "Extension" = None
    
    low: "Quantity" = None
    
    high: "Quantity" = None
    