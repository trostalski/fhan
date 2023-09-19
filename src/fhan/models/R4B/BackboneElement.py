"""
Generated class for BackboneElement. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *


@dataclass
class BackboneElement:
    """
    Base StructureDefinition for BackboneElement Type: Base definition for all elements that are defined inside a resource - but not those in a data type.
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    