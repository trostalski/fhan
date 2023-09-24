"""
Generated class for Element. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *

@dataclass
class Element:
    """ Base StructureDefinition for Element Type: Base definition for all elements in a resource.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    """

    resourceType: str = "Element"
    id: str = None
    
    extension: list["Extension"] = None
    