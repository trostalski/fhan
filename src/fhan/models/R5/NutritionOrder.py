"""
Generated class for NutritionOrder. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class Schedule(BaseModel):
    """ Schedule information for an oral diet.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Timing timing: Scheduled frequency of diet
    :param bool asNeeded: Take 'as needed'
    :param CodeableConcept asNeededFor: Take 'as needed' for x
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "timing": {"class_name": "Timing", "is_contained": False},
        
        
        
        "asNeededFor": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  timing:  list['Timing']  = None,  asNeeded:  'bool'  = None,  asNeededFor:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.timing = timing or []
        self.asNeeded = asNeeded 
        self.asNeededFor = asNeededFor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Nutrient(BaseModel):
    """ Class that defines the quantity and type of nutrient modifications (for example carbohydrate, fiber or sodium) required for the oral diet.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept modifier: Type of nutrient that is being modified
    :param Quantity amount: Quantity of the specified nutrient
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "amount": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  modifier:  'CodeableConcept'  = None,  amount:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.modifier = modifier 
        self.amount = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Texture(BaseModel):
    """ Class that describes any texture modifications required for the patient to safely consume various types of solid foods.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept modifier: Code to indicate how to alter the texture of the foods, e.g. pureed
    :param CodeableConcept foodType: Concepts that are used to identify an entity that is ingested for nutritional purposes
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "foodType": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  modifier:  'CodeableConcept'  = None,  foodType:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.modifier = modifier 
        self.foodType = foodType 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class OralDiet(BaseModel):
    """ Diet given orally in contrast to enteral (tube) feeding.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of oral diet or diet restrictions that describe what can be consumed orally
    :param Schedule schedule: Scheduling information for oral diets
    :param Nutrient nutrient: Required  nutrient modifications
    :param Texture texture: Required  texture modifications
    :param CodeableConcept fluidConsistencyType: The required consistency of fluids and liquids provided to the patient
    :param str instruction: Instructions or additional information about the oral diet
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "schedule": {"class_name": "Schedule", "is_contained": True},
        
        
        "nutrient": {"class_name": "Nutrient", "is_contained": True},
        
        
        "texture": {"class_name": "Texture", "is_contained": True},
        
        
        "fluidConsistencyType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  list['CodeableConcept']  = None,  schedule:  'Schedule'  = None,  nutrient:  list['Nutrient']  = None,  texture:  list['Texture']  = None,  fluidConsistencyType:  list['CodeableConcept']  = None,  instruction:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type or []
        self.schedule = schedule 
        self.nutrient = nutrient or []
        self.texture = texture or []
        self.fluidConsistencyType = fluidConsistencyType or []
        self.instruction = instruction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Schedule(BaseModel):
    """ Schedule information for a supplement.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Timing timing: Scheduled frequency of diet
    :param bool asNeeded: Take 'as needed'
    :param CodeableConcept asNeededFor: Take 'as needed' for x
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "timing": {"class_name": "Timing", "is_contained": False},
        
        
        
        "asNeededFor": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  timing:  list['Timing']  = None,  asNeeded:  'bool'  = None,  asNeededFor:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.timing = timing or []
        self.asNeeded = asNeeded 
        self.asNeededFor = asNeededFor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Supplement(BaseModel):
    """ Oral nutritional products given in order to add further nutritional value to the patient's diet.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference type: Type of supplement product requested
    :param str productName: Product or brand name of the nutritional supplement
    :param Schedule schedule: Scheduling information for supplements
    :param Quantity quantity: Amount of the nutritional supplement
    :param str instruction: Instructions or additional information about the oral supplement
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        "schedule": {"class_name": "Schedule", "is_contained": True},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableReference'  = None,  productName:  'str'  = None,  schedule:  'Schedule'  = None,  quantity:  'Quantity'  = None,  instruction:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.productName = productName 
        self.schedule = schedule 
        self.quantity = quantity 
        self.instruction = instruction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Additive(BaseModel):
    """ Indicates modular components to be provided in addition or mixed with the base formula.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference type: Type of modular component to add to the feeding
    :param str productName: Product or brand name of the modular additive
    :param Quantity quantity: Amount of additive to be given or mixed in
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableReference'  = None,  productName:  'str'  = None,  quantity:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.productName = productName 
        self.quantity = quantity 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Schedule(BaseModel):
    """ Schedule information for an enteral formula.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Timing timing: Scheduled frequency of enteral formula
    :param bool asNeeded: Take 'as needed'
    :param CodeableConcept asNeededFor: Take 'as needed' for x
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "timing": {"class_name": "Timing", "is_contained": False},
        
        
        
        "asNeededFor": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  timing:  list['Timing']  = None,  asNeeded:  'bool'  = None,  asNeededFor:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.timing = timing or []
        self.asNeeded = asNeeded 
        self.asNeededFor = asNeededFor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Administration(BaseModel):
    """ Formula administration instructions as structured data.  This repeating structure allows for changing the administration rate or volume over time for both bolus and continuous feeding.  An example of this would be an instruction to increase the rate of continuous feeding every 2 hours.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Schedule schedule: Scheduling information for enteral formula products
    :param Quantity quantity: The volume of formula to provide
    :param Quantity rateQuantity: Speed with which the formula is provided per period of time
    :param Ratio rateRatio: Speed with which the formula is provided per period of time
    :param str administrationInstruction: Formula feeding instructions expressed as text
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "schedule": {"class_name": "Schedule", "is_contained": True},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "rateQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "rateRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  schedule:  'Schedule'  = None,  quantity:  'Quantity'  = None,  rateQuantity:  'Quantity'  = None,  rateRatio:  'Ratio'  = None,  administrationInstruction:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.schedule = schedule 
        self.quantity = quantity 
        self.rateQuantity = rateQuantity 
        self.rateRatio = rateRatio 
        self.administrationInstruction = administrationInstruction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class EnteralFormula(BaseModel):
    """ Feeding provided through the gastrointestinal tract via a tube, catheter, or stoma that delivers nutrition distal to the oral cavity.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference baseFormulaType: Type of enteral or infant formula
    :param str baseFormulaProductName: Product or brand name of the enteral or infant formula
    :param CodeableReference deliveryDevice: Intended type of device for the administration
    :param Additive additive: Components to add to the feeding
    :param Quantity caloricDensity: Amount of energy per specified volume that is required
    :param CodeableConcept routeOfAdministration: How the formula should enter the patient's gastrointestinal tract
    :param Administration administration: Formula feeding instruction as structured data
    :param Quantity maxVolumeToDeliver: Upper limit on formula volume per unit of time
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "baseFormulaType": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        "deliveryDevice": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "additive": {"class_name": "Additive", "is_contained": True},
        
        
        "caloricDensity": {"class_name": "Quantity", "is_contained": False},
        
        
        "routeOfAdministration": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "administration": {"class_name": "Administration", "is_contained": True},
        
        
        "maxVolumeToDeliver": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  baseFormulaType:  'CodeableReference'  = None,  baseFormulaProductName:  'str'  = None,  deliveryDevice:  list['CodeableReference']  = None,  additive:  list['Additive']  = None,  caloricDensity:  'Quantity'  = None,  routeOfAdministration:  'CodeableConcept'  = None,  administration:  list['Administration']  = None,  maxVolumeToDeliver:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.baseFormulaType = baseFormulaType 
        self.baseFormulaProductName = baseFormulaProductName 
        self.deliveryDevice = deliveryDevice or []
        self.additive = additive or []
        self.caloricDensity = caloricDensity 
        self.routeOfAdministration = routeOfAdministration 
        self.administration = administration or []
        self.maxVolumeToDeliver = maxVolumeToDeliver 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class NutritionOrder(DomainResource):
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
    :param OralDiet oralDiet: Oral diet components
    :param Supplement supplement: Supplement components
    :param EnteralFormula enteralFormula: Enteral formula components
    :param Annotation note: Comments
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "groupIdentifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        "supportingInformation": {"class_name": "Reference", "is_contained": False},
        
        
        
        "orderer": {"class_name": "Reference", "is_contained": False},
        
        
        "performer": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "allergyIntolerance": {"class_name": "Reference", "is_contained": False},
        
        
        "foodPreferenceModifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "excludeFoodModifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "oralDiet": {"class_name": "OralDiet", "is_contained": True},
        
        
        "supplement": {"class_name": "Supplement", "is_contained": True},
        
        
        "enteralFormula": {"class_name": "EnteralFormula", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instantiatesCanonical:  list['str']  = None,  instantiatesUri:  list['str']  = None,  instantiates:  list['str']  = None,  basedOn:  list['Reference']  = None,  groupIdentifier:  'Identifier'  = None,  status:  'str'  = None,  intent:  'str'  = None,  priority:  'str'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  supportingInformation:  list['Reference']  = None,  dateTime:  'str'  = None,  orderer:  'Reference'  = None,  performer:  list['CodeableReference']  = None,  allergyIntolerance:  list['Reference']  = None,  foodPreferenceModifier:  list['CodeableConcept']  = None,  excludeFoodModifier:  list['CodeableConcept']  = None,  outsideFoodAllowed:  'bool'  = None,  oralDiet:  'OralDiet'  = None,  supplement:  list['Supplement']  = None,  enteralFormula:  'EnteralFormula'  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "NutritionOrder"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.instantiates = instantiates or []
        self.basedOn = basedOn or []
        self.groupIdentifier = groupIdentifier 
        self.status = status 
        self.intent = intent 
        self.priority = priority 
        self.subject = subject 
        self.encounter = encounter 
        self.supportingInformation = supportingInformation or []
        self.dateTime = dateTime 
        self.orderer = orderer 
        self.performer = performer or []
        self.allergyIntolerance = allergyIntolerance or []
        self.foodPreferenceModifier = foodPreferenceModifier or []
        self.excludeFoodModifier = excludeFoodModifier or []
        self.outsideFoodAllowed = outsideFoodAllowed 
        self.oralDiet = oralDiet 
        self.supplement = supplement or []
        self.enteralFormula = enteralFormula 
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionOrder":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()