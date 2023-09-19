"""
Generated class for MedicinalProductManufactured. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Meta import *


@dataclass
class MedicinalProductManufactured:
    """
    The manufactured item as contained in the packaged medicinal product.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    manufacturedDoseForm: "CodeableConcept" = None
    
    unitOfPresentation: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    manufacturer: "Reference" = None
    
    ingredient: "Reference" = None
    
    physicalCharacteristics: "ProdCharacteristic" = None
    
    otherCharacteristics: "CodeableConcept" = None
    