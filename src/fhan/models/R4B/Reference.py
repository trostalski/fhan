"""
Generated class for Reference. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Identifier import *


@dataclass
class Reference:
    """
    Base StructureDefinition for Reference Type: A reference from one resource to another.
    """
    id: str = None
    
    extension: "Extension" = None
    
    reference: str = None
    
    type: str = None
    
    identifier: "Identifier" = None
    
    display: str = None
    