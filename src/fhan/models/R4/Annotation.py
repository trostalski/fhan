"""
Generated class for Annotation. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *



@dataclass
class Annotation(Element):
    """ Base StructureDefinition for Annotation Type: A  text note which also  contains information about who made the statement and when.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Reference authorReference: Individual responsible for the annotation
    :param str authorReference: Individual responsible for the annotation
    :param str time: When the annotation was made
    :param str text: The annotation  - text content (as markdown)
    """
    id: str = None
    
    extension: "Extension" = None
    
    authorReference: "Reference" = None
    
    authorReference: str = None
    
    time: str = None
    
    text: str = None
    