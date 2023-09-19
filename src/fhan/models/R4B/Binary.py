"""
Generated class for Binary. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Reference import *


@dataclass
class Binary:
    """
    A resource that represents the data of a single raw artifact as digital content accessible in its native format.  A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    contentType: str = None
    
    securityContext: "Reference" = None
    
    data: str = None
    