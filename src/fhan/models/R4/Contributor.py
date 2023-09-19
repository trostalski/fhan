"""
Generated class for Contributor. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *


@dataclass
class Contributor:
    """
    Base StructureDefinition for Contributor Type: A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.
    """
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    name: str = None
    
    contact: "ContactDetail" = None
    