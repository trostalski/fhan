"""
Generated class for ContactDetail. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *


@dataclass
class ContactDetail:
    """
    Base StructureDefinition for ContactDetail Type: Specifies contact information for a person or organization.
    """
    id: str = None
    
    extension: "Extension" = None
    
    name: str = None
    
    telecom: "ContactPoint" = None
    