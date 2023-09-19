"""
Generated class for MedicinalProductPackaged. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.MarketingStatus import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.ProductShelfLife import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Meta import *


@dataclass
class MedicinalProductPackaged:
    """
    A medicinal product in a container or package.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    subject: "Reference" = None
    
    description: str = None
    
    legalStatusOfSupply: "CodeableConcept" = None
    
    marketingStatus: "MarketingStatus" = None
    
    marketingAuthorization: "Reference" = None
    
    manufacturer: "Reference" = None
    
    batchIdentifier: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    outerPackaging: "Identifier" = None
    
    immediatePackaging: "Identifier" = None
    
    packageItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    material: "CodeableConcept" = None
    
    alternateMaterial: "CodeableConcept" = None
    
    device: "Reference" = None
    
    manufacturedItem: "Reference" = None
    
    packageItem: "BackboneElement" = None
    
    physicalCharacteristics: "ProdCharacteristic" = None
    
    otherCharacteristics: "CodeableConcept" = None
    
    shelfLifeStorage: "ProductShelfLife" = None
    
    manufacturer: "Reference" = None
    