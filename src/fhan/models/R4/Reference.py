"""
Generated class for Reference. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *


@dataclass
class Reference(Element):
    """ Base StructureDefinition for Reference Type: A reference from one resource to another.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str reference: Literal reference, Relative, internal or absolute URL
    :param str type: Type the reference refers to (e.g. "Patient")
    :param Identifier identifier: Logical reference, when literal reference is not known
    :param str display: Text alternative for the resource
    """

    resourceType: str = "Reference"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    reference: str = None
    
    type: str = None
    
    identifier: "Identifier" = Identifier()
    
    display: str = None
    