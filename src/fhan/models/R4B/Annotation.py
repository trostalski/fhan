"""
Generated class for Annotation. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Reference import *


@dataclass
class Annotation:
    """
    Base StructureDefinition for Annotation Type: A  text note which also  contains information about who made the statement and when.
    """
    id: str = None
    
    extension: "Extension" = None
    
    authorReference: "Reference" = None
    
    authorReference: str = None
    
    time: str = None
    
    text: str = None
    