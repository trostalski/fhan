"""
Generated class for Period. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *


@dataclass
class Period:
    """
    Base StructureDefinition for Period Type: A time period defined by a start and end date and optionally time.
    """
    id: str = None
    
    extension: "Extension" = None
    
    start: str = None
    
    end: str = None
    