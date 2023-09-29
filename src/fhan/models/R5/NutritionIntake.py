"""
Generated class for NutritionIntake. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class ConsumedItem(BaseModel):
    """ What food or fluid product or item was consumed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of food or fluid product
    :param CodeableReference nutritionProduct: Code that identifies the food or fluid product that was consumed
    :param Timing schedule: Scheduled frequency of consumption
    :param Quantity amount: Quantity of the specified food
    :param Quantity rate: Rate at which enteral feeding was administered
    :param bool notConsumed: Flag to indicate if the food or fluid item was refused or otherwise not consumed
    :param CodeableConcept notConsumedReason: Reason food or fluid was not consumed
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "nutritionProduct": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "schedule": {"class_name": "Timing", "is_contained": False},
        
        
        "amount": {"class_name": "Quantity", "is_contained": False},
        
        
        "rate": {"class_name": "Quantity", "is_contained": False},
        
        
        
        "notConsumedReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  nutritionProduct:  'CodeableReference'  = None,  schedule:  'Timing'  = None,  amount:  'Quantity'  = None,  rate:  'Quantity'  = None,  notConsumed:  'bool'  = None,  notConsumedReason:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.nutritionProduct = nutritionProduct 
        self.schedule = schedule 
        self.amount = amount 
        self.rate = rate 
        self.notConsumed = notConsumed 
        self.notConsumedReason = notConsumedReason 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionIntake":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionIntake":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class IngredientLabel(BaseModel):
    """ Total nutrient amounts for the whole meal, product, serving, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference nutrient: Total nutrient consumed
    :param Quantity amount: Total amount of nutrient consumed
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "nutrient": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "amount": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  nutrient:  'CodeableReference'  = None,  amount:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.nutrient = nutrient 
        self.amount = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionIntake":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionIntake":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Performer(BaseModel):
    """ Who performed the intake and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performer
    :param Reference actor: Who performed the intake
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  function:  'CodeableConcept'  = None,  actor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function 
        self.actor = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionIntake":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionIntake":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class NutritionIntake(DomainResource):
    """ A record of food or fluid that is being consumed by a patient.  A NutritionIntake may indicate that the patient may be consuming the food or fluid now or has consumed the food or fluid in the past.  The source of this information can be the patient, significant other (such as a family member or spouse), or a clinician.  A common scenario where this information is captured is during the history taking process during a patient visit or stay or through an app that tracks food or fluids consumed.   The consumption information may come from sources such as the patient's memory, from a nutrition label,  or from a clinician documenting observed intake.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfils plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept code: Code representing an overall type of nutrition intake
    :param Reference subject: Who is/was consuming the food or fluid
    :param Reference encounter: Encounter associated with NutritionIntake
    :param str occurrenceDateTime: The date/time or interval when the food or fluid is/was consumed
    :param Period occurrencePeriod: The date/time or interval when the food or fluid is/was consumed
    :param str recorded: When the intake was recorded
    :param bool reportedBoolean: Person or organization that provided the information about the consumption of this food or fluid
    :param Reference reportedReference: Person or organization that provided the information about the consumption of this food or fluid
    :param ConsumedItem consumedItem: What food or fluid product or item was consumed
    :param IngredientLabel ingredientLabel: Total nutrient for the whole meal, product, serving
    :param Performer performer: Who was performed in the intake
    :param Reference location: Where the intake occurred
    :param Reference derivedFrom: Additional supporting information
    :param CodeableReference reason: Reason for why the food or fluid is /was consumed
    :param Annotation note: Further information about the consumption
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
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        
        "reportedReference": {"class_name": "Reference", "is_contained": False},
        
        
        "consumedItem": {"class_name": "ConsumedItem", "is_contained": True},
        
        
        "ingredientLabel": {"class_name": "IngredientLabel", "is_contained": True},
        
        
        "performer": {"class_name": "Performer", "is_contained": True},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "derivedFrom": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instantiatesCanonical:  list['str']  = None,  instantiatesUri:  list['str']  = None,  basedOn:  list['Reference']  = None,  partOf:  list['Reference']  = None,  status:  'str'  = None,  statusReason:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  occurrenceDateTime:  'str'  = None,  occurrencePeriod:  'Period'  = None,  recorded:  'str'  = None,  reportedBoolean:  'bool'  = None,  reportedReference:  'Reference'  = None,  consumedItem:  list['ConsumedItem']  = None,  ingredientLabel:  list['IngredientLabel']  = None,  performer:  list['Performer']  = None,  location:  'Reference'  = None,  derivedFrom:  list['Reference']  = None,  reason:  list['CodeableReference']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "NutritionIntake"
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
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.status = status 
        self.statusReason = statusReason or []
        self.code = code 
        self.subject = subject 
        self.encounter = encounter 
        self.occurrenceDateTime = occurrenceDateTime 
        self.occurrencePeriod = occurrencePeriod 
        self.recorded = recorded 
        self.reportedBoolean = reportedBoolean 
        self.reportedReference = reportedReference 
        self.consumedItem = consumedItem or []
        self.ingredientLabel = ingredientLabel or []
        self.performer = performer or []
        self.location = location 
        self.derivedFrom = derivedFrom or []
        self.reason = reason or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionIntake":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionIntake":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()