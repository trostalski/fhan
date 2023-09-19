"""
Generated class for Annotation. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Reference import *
from fhan.models.R5.Extension import *


@dataclass
class Annotation:
    """ Annotation Type: A  text note which also  contains information about who made the statement and when.
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
    