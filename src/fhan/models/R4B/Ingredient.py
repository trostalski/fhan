"""
Generated class for Ingredient. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.RatioRange import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.CodeableReference import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Ratio import *
from fhan.models.R4B.Reference import *


@dataclass
class Ingredient:
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
    
    status: str = None
    
    for: "Reference" = None
    
    role: "CodeableConcept" = None
    
    function: "CodeableConcept" = None
    
    allergenicIndicator: bool = None
    
    manufacturer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: str = None
    
    manufacturer: "Reference" = None
    
    substance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableReference" = None
    
    strength: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    presentationRatio: "Ratio" = None
    
    presentationRatio: "RatioRange" = None
    
    textPresentation: str = None
    
    concentrationRatio: "Ratio" = None
    
    concentrationRatio: "RatioRange" = None
    
    textConcentration: str = None
    
    measurementPoint: str = None
    
    country: "CodeableConcept" = None
    
    referenceStrength: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substance: "CodeableReference" = None
    
    strengthRatio: "Ratio" = None
    
    strengthRatio: "RatioRange" = None
    
    measurementPoint: str = None
    
    country: "CodeableConcept" = None
    