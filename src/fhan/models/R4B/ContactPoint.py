"""
Generated class for ContactPoint. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Period import *


@dataclass
class ContactPoint:
    """
    Base StructureDefinition for ContactPoint Type: Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.
    """
    id: str = None
    
    extension: "Extension" = None
    
    system: str = None
    
    value: str = None
    
    use: str = None
    
    rank: int = None
    
    period: "Period" = None
    