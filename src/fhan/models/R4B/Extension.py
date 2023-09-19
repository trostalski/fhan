"""
Generated class for Extension. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.CodeableConcept import *


@dataclass
class Extension:
    """
    Distinguishes the type of involvement of the performer in the event. For example, 'author',  'verifier' or 'responsible party'.
    """
    id: str = None
    
    extension: "Extension" = None
    
    url: str = None
    
    valueCodeableConcept: "CodeableConcept" = None
    