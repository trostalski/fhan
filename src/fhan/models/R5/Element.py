"""
Generated class for Element. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Extension import *


@dataclass
class Element:
    """ Element Type: Base definition for all elements in a resource.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    
    """
    id: str = None
    
    extension: "Extension" = None
    