"""
Generated class for Reference. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *


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
    