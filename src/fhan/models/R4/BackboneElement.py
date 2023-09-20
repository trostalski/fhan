"""
Generated class for BackboneElement. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *




@dataclass
class BackboneElement(Element):
    """ Base StructureDefinition for BackboneElement Type: Base definition for all elements that are defined inside a resource - but not those in a data type.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    