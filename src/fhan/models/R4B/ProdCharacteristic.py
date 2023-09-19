"""
Generated class for ProdCharacteristic. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Attachment import *


@dataclass
class ProdCharacteristic:
    """
    Base StructureDefinition for ProdCharacteristic Type: The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    height: "Quantity" = None
    
    width: "Quantity" = None
    
    depth: "Quantity" = None
    
    weight: "Quantity" = None
    
    nominalVolume: "Quantity" = None
    
    externalDiameter: "Quantity" = None
    
    shape: str = None
    
    color: str = None
    
    imprint: str = None
    
    image: "Attachment" = None
    
    scoring: "CodeableConcept" = None
    