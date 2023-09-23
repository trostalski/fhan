"""
Generated class for NutritionOrder. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class Nutrient(Element):
    """ Class that defines the quantity and type of nutrient modifications (for example carbohydrate, fiber or sodium) required for the oral diet.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept modifier: Type of nutrient that is being modified
    :param Quantity amount: Quantity of the specified nutrient
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    modifier: "CodeableConcept" = CodeableConcept()
    amount: "Quantity" = Quantity()
    

    
    
@dataclass
class Texture(Element):
    """ Class that describes any texture modifications required for the patient to safely consume various types of solid foods.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept modifier: Code to indicate how to alter the texture of the foods, e.g. pureed
    :param CodeableConcept foodType: Concepts that are used to identify an entity that is ingested for nutritional purposes
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    modifier: "CodeableConcept" = CodeableConcept()
    foodType: "CodeableConcept" = CodeableConcept()
    

  
    
    
@dataclass
class OralDiet(Element):
    """ Diet given orally in contrast to enteral (tube) feeding.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of oral diet or diet restrictions that describe what can be consumed orally
    :param Timing schedule: Scheduled frequency of diet
    :param Nutrient nutrient: Required  nutrient modifications
    :param Texture texture: Required  texture modifications
    :param CodeableConcept fluidConsistencyType: The required consistency of fluids and liquids provided to the patient
    :param str instruction: Instructions or additional information about the oral diet
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    type: list[CodeableConcept] = CodeableConcept() 
    schedule: list[Timing] = Timing() 
    nutrient: list[Nutrient] = Nutrient() 
    texture: list[Texture] = Texture() 
    fluidConsistencyType: list[CodeableConcept] = CodeableConcept() 
    
    instruction: str = None
    

    
    
@dataclass
class Supplement(Element):
    """ Oral nutritional products given in order to add further nutritional value to the patient's diet.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of supplement product requested
    :param str productName: Product or brand name of the nutritional supplement
    :param Timing schedule: Scheduled frequency of supplement
    :param Quantity quantity: Amount of the nutritional supplement
    :param str instruction: Instructions or additional information about the oral supplement
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    type: "CodeableConcept" = CodeableConcept()
    
    productName: str = None
    schedule: list[Timing] = Timing() 
    quantity: "Quantity" = Quantity()
    
    instruction: str = None
    

    
        
    
    
@dataclass
class Administration(Element):
    """ Formula administration instructions as structured data.  This repeating structure allows for changing the administration rate or volume over time for both bolus and continuous feeding.  An example of this would be an instruction to increase the rate of continuous feeding every 2 hours.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Timing schedule: Scheduled frequency of enteral feeding
    :param Quantity quantity: The volume of formula to provide
    :param Quantity rateQuantity: Speed with which the formula is provided per period of time
    :param str administrationInstruction: Formula feeding instructions expressed as text
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    schedule: "Timing" = Timing()
    quantity: "Quantity" = Quantity()
    rateQuantity: "Quantity" = Quantity()
    
    administrationInstruction: str = None
    

  
    
    
@dataclass
class EnteralFormula(Element):
    """ Feeding provided through the gastrointestinal tract via a tube, catheter, or stoma that delivers nutrition distal to the oral cavity.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept baseFormulaType: Type of enteral or infant formula
    :param str baseFormulaProductName: Product or brand name of the enteral or infant formula
    :param CodeableConcept additiveType: Type of modular component to add to the feeding
    :param str additiveProductName: Product or brand name of the modular additive
    :param Quantity caloricDensity: Amount of energy per specified volume that is required
    :param CodeableConcept routeofAdministration: How the formula should enter the patient's gastrointestinal tract
    :param Administration administration: Formula feeding instruction as structured data
    :param Quantity maxVolumeToDeliver: Upper limit on formula volume per unit of time
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    baseFormulaType: "CodeableConcept" = CodeableConcept()
    
    baseFormulaProductName: str = None
    additiveType: "CodeableConcept" = CodeableConcept()
    
    additiveProductName: str = None
    caloricDensity: "Quantity" = Quantity()
    routeofAdministration: "CodeableConcept" = CodeableConcept()
    administration: list[Administration] = Administration() 
    maxVolumeToDeliver: "Quantity" = Quantity()
    

@dataclass
class NutritionOrder(ModelBase):
    """ A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers assigned to this order
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param str instantiates: Instantiates protocol or definition
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param Reference patient: The person who requires the diet, formula or nutritional supplement
    :param Reference encounter: The encounter associated with this nutrition order
    :param str dateTime: Date and time the nutrition order was requested
    :param Reference orderer: Who ordered the diet, formula or nutritional supplement
    :param Reference allergyIntolerance: List of the patient's food and nutrition-related allergies and intolerances
    :param CodeableConcept foodPreferenceModifier: Order-specific modifier about the type of food that should be given
    :param CodeableConcept excludeFoodModifier: Order-specific modifier about the type of food that should not be given
    :param OralDiet oralDiet: Oral diet components
    :param Supplement supplement: Supplement components
    :param EnteralFormula enteralFormula: Enteral formula components
    :param Annotation note: Comments
    """

    resourceType: str = "NutritionOrder"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    instantiates: str = None
    
    status: str = None
    
    intent: str = None
    
    patient: "Reference" = Reference()
    
    encounter: "Reference" = Reference()
    
    dateTime: str = None
    
    orderer: "Reference" = Reference()
    
    allergyIntolerance: list[Reference] = Reference() 
    
    foodPreferenceModifier: list[CodeableConcept] = CodeableConcept() 
    
    excludeFoodModifier: list[CodeableConcept] = CodeableConcept() 
    
    oralDiet: "OralDiet" = OralDiet()
    
    supplement: list[Supplement] = Supplement() 
    
    enteralFormula: "EnteralFormula" = EnteralFormula()
    
    note: list[Annotation] = Annotation() 
    