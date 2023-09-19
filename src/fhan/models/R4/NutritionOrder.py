"""
Generated class for NutritionOrder. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class NutritionOrder:
    """
    A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
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
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    instantiates: str = None
    
    status: str = None
    
    intent: str = None
    
    patient: "Reference" = None
    
    encounter: "Reference" = None
    
    dateTime: str = None
    
    orderer: "Reference" = None
    
    allergyIntolerance: "Reference" = None
    
    foodPreferenceModifier: "CodeableConcept" = None
    
    excludeFoodModifier: "CodeableConcept" = None
    
    oralDiet: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    schedule: "Timing" = None
    
    nutrient: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    modifier: "CodeableConcept" = None
    
    amount: "Quantity" = None
    
    texture: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    modifier: "CodeableConcept" = None
    
    foodType: "CodeableConcept" = None
    
    fluidConsistencyType: "CodeableConcept" = None
    
    instruction: str = None
    
    supplement: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    productName: str = None
    
    schedule: "Timing" = None
    
    quantity: "Quantity" = None
    
    instruction: str = None
    
    enteralFormula: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    baseFormulaType: "CodeableConcept" = None
    
    baseFormulaProductName: str = None
    
    additiveType: "CodeableConcept" = None
    
    additiveProductName: str = None
    
    caloricDensity: "Quantity" = None
    
    routeofAdministration: "CodeableConcept" = None
    
    administration: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    schedule: "Timing" = None
    
    quantity: "Quantity" = None
    
    rateQuantity: "Quantity" = None
    
    rateQuantity: "Ratio" = None
    
    maxVolumeToDeliver: "Quantity" = None
    
    administrationInstruction: str = None
    
    note: "Annotation" = None
    