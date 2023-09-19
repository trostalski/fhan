"""
Generated class for MedicinalProductIngredient. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class MedicinalProductIngredient:
    """
    An ingredient of a manufactured item or pharmaceutical product.
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
    
    role: "CodeableConcept" = None
    
    allergenicIndicator: bool = None
    
    manufacturer: "Reference" = None
    
    specifiedSubstance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    group: "CodeableConcept" = None
    
    confidentiality: "CodeableConcept" = None
    
    strength: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    presentation: "Ratio" = None
    
    presentationLowLimit: "Ratio" = None
    
    concentration: "Ratio" = None
    
    concentrationLowLimit: "Ratio" = None
    
    measurementPoint: str = None
    
    country: "CodeableConcept" = None
    
    referenceStrength: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substance: "CodeableConcept" = None
    
    strength: "Ratio" = None
    
    strengthLowLimit: "Ratio" = None
    
    measurementPoint: str = None
    
    country: "CodeableConcept" = None
    
    substance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    strength: "BackboneElement" = None
    