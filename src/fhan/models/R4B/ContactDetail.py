"""
Generated class for ContactDetail. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.ContactPoint import *


@dataclass
class ContactDetail:
    """
    Base StructureDefinition for ContactDetail Type: Specifies contact information for a person or organization.
    """
    id: str = None
    
    extension: "Extension" = None
    
    name: str = None
    
    telecom: "ContactPoint" = None
    