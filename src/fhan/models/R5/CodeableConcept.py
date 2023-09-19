"""
Generated class for CodeableConcept. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Extension import *
from fhan.models.R5.Coding import *


@dataclass
class CodeableConcept:
    """ CodeableConcept Type: A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding coding: Code defined by a terminology system
    :param str text: Plain text representation of the concept
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    coding: "Coding" = None
    
    text: str = None
    