"""
Generated class for ProdCharacteristic. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Quantity import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *


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
    