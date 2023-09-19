"""
Generated class for BiologicallyDerivedProduct. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class BiologicallyDerivedProduct:
    """
    A material substance originating from a biological entity intended to be transplanted or infused
into another (possibly the same) biological entity.
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
    
    productCategory: str = None
    
    productCode: "CodeableConcept" = None
    
    status: str = None
    
    request: "Reference" = None
    
    quantity: int = None
    
    parent: "Reference" = None
    
    collection: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    collector: "Reference" = None
    
    source: "Reference" = None
    
    collecteddateTime: str = None
    
    collecteddateTime: "Period" = None
    
    processing: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    procedure: "CodeableConcept" = None
    
    additive: "Reference" = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
    manipulation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
    storage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    temperature: float = None
    
    scale: str = None
    
    duration: "Period" = None
    