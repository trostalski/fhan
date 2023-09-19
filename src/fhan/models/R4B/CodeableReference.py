"""
Generated class for CodeableReference. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class CodeableReference:
    """
    Base StructureDefinition for CodeableReference Type: A reference to a resource (by instance), or instead, a reference to a concept defined in a terminology or ontology (by class).
    """
    id: str = None
    
    extension: "Extension" = None
    
    concept: "CodeableConcept" = None
    
    reference: "Reference" = None
    