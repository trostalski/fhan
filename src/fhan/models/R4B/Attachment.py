"""
Generated class for Attachment. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *


@dataclass
class Attachment:
    """
    Base StructureDefinition for Attachment Type: For referring to data content defined in other formats.
    """
    id: str = None
    
    extension: "Extension" = None
    
    contentType: str = None
    
    language: str = None
    
    data: str = None
    
    url: str = None
    
    size: int = None
    
    hash: str = None
    
    title: str = None
    
    creation: str = None
    