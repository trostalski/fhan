"""
Generated class for DomainResource. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Narrative import *


@dataclass
class DomainResource:
    """
    A resource that includes narrative, extensions, and contained resources.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    