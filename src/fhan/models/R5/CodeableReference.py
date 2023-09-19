"""
Generated class for CodeableReference. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Reference import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *


@dataclass
class CodeableReference:
    """ CodeableReference Type: A reference to a resource (by instance), or instead, a reference to a concept defined in a terminology or ontology (by class).
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param CodeableConcept concept: Reference to a concept (by class)
    :param Reference reference: Reference to a resource (by instance)
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    concept: "CodeableConcept" = None
    
    reference: "Reference" = None
    