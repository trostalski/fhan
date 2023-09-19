"""
Generated class for ProductShelfLife. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Identifier import *


@dataclass
class ProductShelfLife:
    """
    Base StructureDefinition for ProductShelfLife Type: The shelf-life and storage information for a medicinal product item or container can be described using this class.
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    period: "Quantity" = None
    
    specialPrecautionsForStorage: "CodeableConcept" = None
    