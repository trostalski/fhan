"""
Generated class for PrimitiveType. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Extension import *


@dataclass
class PrimitiveType:
    """ PrimitiveType Type: The base type for all re-useable types defined that have a simple property.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    
    """
    id: str = None
    
    extension: "Extension" = None
    