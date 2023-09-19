"""
Generated class for Identifier. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Reference import *


@dataclass
class Identifier:
    """
    Base StructureDefinition for Identifier Type: An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business identifiers.
    """
    id: str = None
    
    extension: "Extension" = None
    
    use: str = None
    
    type: "CodeableConcept" = None
    
    system: str = None
    
    value: str = None
    
    period: "Period" = None
    
    assigner: "Reference" = None
    