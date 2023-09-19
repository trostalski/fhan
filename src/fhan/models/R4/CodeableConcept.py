"""
Generated class for CodeableConcept. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *


@dataclass
class CodeableConcept:
    """
    Base StructureDefinition for CodeableConcept Type: A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
    """
    id: str = None
    
    extension: "Extension" = None
    
    coding: "Coding" = None
    
    text: str = None
    