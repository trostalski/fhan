"""
Generated class for Identifier. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Element import *


@dataclass
class Identifier(Element):
    """ Base StructureDefinition for Identifier Type: An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business identifiers.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str use: usual | official | temp | secondary | old (If known)
    :param CodeableConcept type: Description of identifier
    :param str system: The namespace for the identifier value
    :param str value: The value that is unique
    :param Period period: Time period when id is/was valid for use
    :param Reference assigner: Organization that issued id (may be just text)
    """

    resourceType: str = "Identifier"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    use: str = None
    
    type: "CodeableConcept" = CodeableConcept()
    
    system: str = None
    
    value: str = None
    
    period: "Period" = Period()
    
    assigner: "Reference" = Reference()
    