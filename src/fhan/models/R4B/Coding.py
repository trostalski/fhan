"""
Generated class for Coding. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *


@dataclass
class Coding:
    """
    Base StructureDefinition for Coding Type: A reference to a code defined by a terminology system.
    """
    id: str = None
    
    extension: "Extension" = None
    
    system: str = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    
    userSelected: bool = None
    