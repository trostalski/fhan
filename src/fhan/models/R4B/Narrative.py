"""
Generated class for Narrative. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *


@dataclass
class Narrative:
    """
    Base StructureDefinition for Narrative Type: A human-readable summary of the resource conveying the essential clinical and business information for the resource.
    """
    id: str = None
    
    extension: "Extension" = None
    
    status: str = None
    
    div: str = None
    