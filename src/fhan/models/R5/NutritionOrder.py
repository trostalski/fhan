"""
Generated class for NutritionOrder. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class NutritionOrder:
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
    :param Reference basedOn: What this order fulfills
    :param Identifier groupIdentifier: Composite Request ID
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param Reference subject: Who requires the diet, formula or nutritional supplement
    :param Reference encounter: The encounter associated with this nutrition order
    :param Reference supportingInformation: Information to support fulfilling of the nutrition order
    :param str dateTime: Date and time the nutrition order was requested
    :param Reference orderer: Who ordered the diet, formula or nutritional supplement
    :param CodeableReference performer: Who is desired to perform the administration of what is being ordered
    :param Reference allergyIntolerance: List of the patient's food and nutrition-related allergies and intolerances
    :param CodeableConcept foodPreferenceModifier: Order-specific modifier about the type of food that should be given
    :param CodeableConcept excludeFoodModifier: Order-specific modifier about the type of food that should not be given
    :param bool outsideFoodAllowed: Capture when a food item is brought in by the patient and/or family
    :param BackboneElement oralDiet: Oral diet components
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of oral diet or diet restrictions that describe what can be consumed orally
    :param BackboneElement schedule: Scheduling information for oral diets
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Timing timing: Scheduled frequency of diet
    :param bool asNeeded: Take 'as needed'
    :param CodeableConcept asNeededFor: Take 'as needed' for x
    :param BackboneElement nutrient: Required  nutrient modifications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept modifier: Type of nutrient that is being modified
    :param Quantity amount: Quantity of the specified nutrient
    :param BackboneElement texture: Required  texture modifications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept modifier: Code to indicate how to alter the texture of the foods, e.g. pureed
    :param CodeableConcept foodType: Concepts that are used to identify an entity that is ingested for nutritional purposes
    :param CodeableConcept fluidConsistencyType: The required consistency of fluids and liquids provided to the patient
    :param str instruction: Instructions or additional information about the oral diet
    :param BackboneElement supplement: Supplement components
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference type: Type of supplement product requested
    :param str productName: Product or brand name of the nutritional supplement
    :param BackboneElement schedule: Scheduling information for supplements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Timing timing: Scheduled frequency of diet
    :param bool asNeeded: Take 'as needed'
    :param CodeableConcept asNeededFor: Take 'as needed' for x
    :param Quantity quantity: Amount of the nutritional supplement
    :param str instruction: Instructions or additional information about the oral supplement
    :param BackboneElement enteralFormula: Enteral formula components
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference baseFormulaType: Type of enteral or infant formula
    :param str baseFormulaProductName: Product or brand name of the enteral or infant formula
    :param CodeableReference deliveryDevice: Intended type of device for the administration
    :param BackboneElement additive: Components to add to the feeding
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference type: Type of modular component to add to the feeding
    :param str productName: Product or brand name of the modular additive
    :param Quantity quantity: Amount of additive to be given or mixed in
    :param Quantity caloricDensity: Amount of energy per specified volume that is required
    :param CodeableConcept routeOfAdministration: How the formula should enter the patient's gastrointestinal tract
    :param BackboneElement administration: Formula feeding instruction as structured data
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement schedule: Scheduling information for enteral formula products
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Timing timing: Scheduled frequency of enteral formula
    :param bool asNeeded: Take 'as needed'
    :param CodeableConcept asNeededFor: Take 'as needed' for x
    :param Quantity quantity: The volume of formula to provide
    :param Quantity rateQuantity: Speed with which the formula is provided per period of time
    :param Ratio rateQuantity: Speed with which the formula is provided per period of time
    :param Quantity maxVolumeToDeliver: Upper limit on formula volume per unit of time
    :param str administrationInstruction: Formula feeding instructions expressed as text
    :param Annotation note: Comments
    
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
    
    basedOn: "Reference" = None
    
    groupIdentifier: "Identifier" = None
    
    status: str = None
    
    intent: str = None
    
    priority: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    supportingInformation: "Reference" = None
    
    dateTime: str = None
    
    orderer: "Reference" = None
    
    performer: "CodeableReference" = None
    
    allergyIntolerance: "Reference" = None
    
    foodPreferenceModifier: "CodeableConcept" = None
    
    excludeFoodModifier: "CodeableConcept" = None
    
    outsideFoodAllowed: bool = None
    
    oralDiet: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    schedule: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    timing: "Timing" = None
    
    asNeeded: bool = None
    
    asNeededFor: "CodeableConcept" = None
    
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
    
    type: "CodeableReference" = None
    
    productName: str = None
    
    schedule: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    timing: "Timing" = None
    
    asNeeded: bool = None
    
    asNeededFor: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    instruction: str = None
    
    enteralFormula: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    baseFormulaType: "CodeableReference" = None
    
    baseFormulaProductName: str = None
    
    deliveryDevice: "CodeableReference" = None
    
    additive: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableReference" = None
    
    productName: str = None
    
    quantity: "Quantity" = None
    
    caloricDensity: "Quantity" = None
    
    routeOfAdministration: "CodeableConcept" = None
    
    administration: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    schedule: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    timing: "Timing" = None
    
    asNeeded: bool = None
    
    asNeededFor: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    rateQuantity: "Quantity" = None
    
    rateQuantity: "Ratio" = None
    
    maxVolumeToDeliver: "Quantity" = None
    
    administrationInstruction: str = None
    
    note: "Annotation" = None
    