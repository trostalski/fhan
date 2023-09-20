"""
Generated class for CodeableConcept. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.Extension import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *




@dataclass
class CodeableConcept(Element):
    """ Base StructureDefinition for CodeableConcept Type: A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding coding: Code defined by a terminology system
    :param str text: Plain text representation of the concept
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    coding: list["Coding"] = None
    
    text: str = None
    