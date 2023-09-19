"""
Generated class for Money. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *


@dataclass
class Money:
    """
    Base StructureDefinition for Money Type: An amount of economic utility in some recognized currency.
    """
    id: str = None
    
    extension: "Extension" = None
    
    value: float = None
    
    currency: str = None
    