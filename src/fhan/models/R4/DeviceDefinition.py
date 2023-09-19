"""
Generated class for DeviceDefinition. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.ProductShelfLife import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Meta import *


@dataclass
class DeviceDefinition:
    """
    The characteristics, operational status and capabilities of a medical-related component of a medical device.
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
    
    udiDeviceIdentifier: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    deviceIdentifier: str = None
    
    issuer: str = None
    
    jurisdiction: str = None
    
    manufacturerstring: str = None
    
    manufacturerstring: "Reference" = None
    
    deviceName: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: str = None
    
    modelNumber: str = None
    
    type: "CodeableConcept" = None
    
    specialization: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    systemType: str = None
    
    version: str = None
    
    version: str = None
    
    safety: "CodeableConcept" = None
    
    shelfLifeStorage: "ProductShelfLife" = None
    
    physicalCharacteristics: "ProdCharacteristic" = None
    
    languageCode: "CodeableConcept" = None
    
    capability: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    description: "CodeableConcept" = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueCode: "CodeableConcept" = None
    
    owner: "Reference" = None
    
    contact: "ContactPoint" = None
    
    url: str = None
    
    onlineInformation: str = None
    
    note: "Annotation" = None
    
    quantity: "Quantity" = None
    
    parentDevice: "Reference" = None
    
    material: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substance: "CodeableConcept" = None
    
    alternate: bool = None
    
    allergenicIndicator: bool = None
    