"""
Generated class for BackboneType. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Extension import *


@dataclass
class BackboneType:
    """ BackboneType Type: Base definition for the few data types that are allowed to carry modifier extensions.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    