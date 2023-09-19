"""
Generated class for Narrative. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *



@dataclass
class Narrative(Element):
    """ Base StructureDefinition for Narrative Type: A human-readable summary of the resource conveying the essential clinical and business information for the resource.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str status: generated | extensions | additional | empty
    :param str div: Limited xhtml content
    """
    id: str = None
    
    extension: "Extension" = None
    
    status: str = None
    
    div: str = None
    