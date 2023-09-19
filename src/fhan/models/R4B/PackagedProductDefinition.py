"""
Generated class for PackagedProductDefinition. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Duration import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.CodeableReference import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.MarketingStatus import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class PackagedProductDefinition:
    """
    A medically related item or items, in a container or package.
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
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    packageFor: "Reference" = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    containedItemQuantity: "Quantity" = None
    
    description: str = None
    
    legalStatusOfSupply: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    marketingStatus: "MarketingStatus" = None
    
    characteristic: "CodeableConcept" = None
    
    copackagedIndicator: bool = None
    
    manufacturer: "Reference" = None
    
    package: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    quantity: int = None
    
    material: "CodeableConcept" = None
    
    alternateMaterial: "CodeableConcept" = None
    
    shelfLifeStorage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    periodDuration: "Duration" = None
    
    periodDuration: str = None
    
    specialPrecautionsForStorage: "CodeableConcept" = None
    
    manufacturer: "Reference" = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Attachment" = None
    
    containedItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    item: "CodeableReference" = None
    
    amount: "Quantity" = None
    
    package: "BackboneElement" = None
    