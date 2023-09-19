"""
Generated class for Element. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *


@dataclass
class Element:
    """
    Base StructureDefinition for Element Type: Base definition for all elements in a resource.
    """
    id: str = None
    
    extension: "Extension" = None
    