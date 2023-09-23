"""
Generated class for BackboneElement. 
Time: 2023-09-23 23:45:33
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

    resourceType: str = "BackboneElement"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    