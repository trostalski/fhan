"""
Generated class for NutritionProduct. 
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
from fhan.models.R5.Ratio import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Nutrient(BaseModel):
    """ The product's nutritional information expressed by the nutrients.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: The (relevant) nutrients in the product
    :param Ratio amount: The amount of nutrient expressed in one or more units: X per pack / per serving / per dose
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "item": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "amount": {"class_name": "Ratio", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  item:  'CodeableReference'  = None,  amount:  list['Ratio']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.item = item 
        self.amount = amount or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionProduct":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Ingredient(BaseModel):
    """ Ingredients contained in this product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: The ingredient contained in the product
    :param Ratio amount: The amount of ingredient that is in the product
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "item": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "amount": {"class_name": "Ratio", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  item:  'CodeableReference'  = None,  amount:  list['Ratio']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.item = item 
        self.amount = amount or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionProduct":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Characteristic(BaseModel):
    """ Specifies descriptive properties of the nutrition product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code specifying the type of characteristic
    :param CodeableConcept valueCodeableConcept: The value of the characteristic
    :param str valueString: The value of the characteristic
    :param Quantity valueQuantity: The value of the characteristic
    :param str valueBase64Binary: The value of the characteristic
    :param Attachment valueAttachment: The value of the characteristic
    :param bool valueBoolean: The value of the characteristic
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueString:  'str'  = None,  valueQuantity:  'Quantity'  = None,  valueBase64Binary:  'str'  = None,  valueAttachment:  'Attachment'  = None,  valueBoolean:  'bool'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueString = valueString 
        self.valueQuantity = valueQuantity 
        self.valueBase64Binary = valueBase64Binary 
        self.valueAttachment = valueAttachment 
        self.valueBoolean = valueBoolean 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionProduct":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Instance(BaseModel):
    """ Conveys instance-level information about this product item. One or several physical, countable instances or occurrences of the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: The amount of items or instances
    :param Identifier identifier: The identifier for the physical instance, typically a serial number or manufacturer number
    :param str name: The name for the specific product
    :param str lotNumber: The identification of the batch or lot of the product
    :param str expiry: The expiry date or date and time for the product
    :param str useBy: The date until which the product is expected to be good for consumption
    :param Identifier biologicalSourceEvent: An identifier that supports traceability to the event during which material in this product from one or more biological entities was obtained or pooled
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        
        "biologicalSourceEvent": {"class_name": "Identifier", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  quantity:  'Quantity'  = None,  identifier:  list['Identifier']  = None,  name:  'str'  = None,  lotNumber:  'str'  = None,  expiry:  'str'  = None,  useBy:  'str'  = None,  biologicalSourceEvent:  'Identifier'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.quantity = quantity 
        self.identifier = identifier or []
        self.name = name 
        self.lotNumber = lotNumber 
        self.expiry = expiry 
        self.useBy = useBy 
        self.biologicalSourceEvent = biologicalSourceEvent 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionProduct":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class NutritionProduct(DomainResource):
    """ A food or supplement that is consumed by patients.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept code: A code that can identify the detailed nutrients and ingredients in a specific food product
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: Broad product groups or categories used to classify the product, such as Legume and Legume Products, Beverages, or Beef Products
    :param Reference manufacturer: Manufacturer, representative or officially responsible for the product
    :param Nutrient nutrient: The product's nutritional information expressed by the nutrients
    :param Ingredient ingredient: Ingredients contained in this product
    :param CodeableReference knownAllergen: Known or suspected allergens that are a part of this product
    :param Characteristic characteristic: Specifies descriptive properties of the nutrition product
    :param Instance instance: One or several physical instances or occurrences of the nutrition product
    :param Annotation note: Comments made about the product
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        
        
        "nutrient": {"class_name": "Nutrient", "is_contained": True},
        
        
        "ingredient": {"class_name": "Ingredient", "is_contained": True},
        
        
        "knownAllergen": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "characteristic": {"class_name": "Characteristic", "is_contained": True},
        
        
        "instance": {"class_name": "Instance", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  status:  'str'  = None,  category:  list['CodeableConcept']  = None,  manufacturer:  list['Reference']  = None,  nutrient:  list['Nutrient']  = None,  ingredient:  list['Ingredient']  = None,  knownAllergen:  list['CodeableReference']  = None,  characteristic:  list['Characteristic']  = None,  instance:  list['Instance']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "NutritionProduct"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.status = status 
        self.category = category or []
        self.manufacturer = manufacturer or []
        self.nutrient = nutrient or []
        self.ingredient = ingredient or []
        self.knownAllergen = knownAllergen or []
        self.characteristic = characteristic or []
        self.instance = instance or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionProduct":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "NutritionProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()