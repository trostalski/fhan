"""
Generated class for Distance. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *


@dataclass
class Distance:
    """
    Base StructureDefinition for Distance Type: A length - a value with a unit that is a physical distance.
    """
    id: str = None
    
    extension: "Extension" = None
    
    value: float = None
    
    comparator: str = None
    
    unit: str = None
    
    system: str = None
    
    code: str = None
    