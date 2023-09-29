"""
Generated class for ManufacturedItemDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.MarketingStatus import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Property(BaseModel):
    """ General characteristics of this item.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of characteristic
    :param CodeableConcept valueCodeableConcept: A value for the characteristic
    :param Quantity valueQuantity: A value for the characteristic
    :param str valueDate: A value for the characteristic
    :param bool valueBoolean: A value for the characteristic
    :param str valueMarkdown: A value for the characteristic
    :param Attachment valueAttachment: A value for the characteristic
    :param Reference valueReference: A value for the characteristic
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        
        
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        
        
        "valueReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueDate:  'str'  = None,  valueBoolean:  'bool'  = None,  valueMarkdown:  'str'  = None,  valueAttachment:  'Attachment'  = None,  valueReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueQuantity = valueQuantity 
        self.valueDate = valueDate 
        self.valueBoolean = valueBoolean 
        self.valueMarkdown = valueMarkdown 
        self.valueAttachment = valueAttachment 
        self.valueReference = valueReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ManufacturedItemDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ManufacturedItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Constituent(BaseModel):
    """ A reference to a constituent of the manufactured item as a whole, linked here so that its component location within the item can be indicated. This not where the item's ingredient are primarily stated (for which see Ingredient.for or ManufacturedItemDefinition.ingredient).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity amount: The measurable amount of the substance, expressable in different ways (e.g. by mass or volume)
    :param CodeableConcept location: The physical location of the constituent/ingredient within the component
    :param CodeableConcept function: The function of this constituent within the component e.g. binder
    :param CodeableReference hasIngredient: The ingredient that is the constituent of the given component
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "amount": {"class_name": "Quantity", "is_contained": False},
        
        
        "location": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "hasIngredient": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  amount:  list['Quantity']  = None,  location:  list['CodeableConcept']  = None,  function:  list['CodeableConcept']  = None,  hasIngredient:  list['CodeableReference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.amount = amount or []
        self.location = location or []
        self.function = function or []
        self.hasIngredient = hasIngredient or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ManufacturedItemDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ManufacturedItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Component(BaseModel):
    """ Physical parts of the manufactured item, that it is intrisically made from. This is distinct from the ingredients that are part of its chemical makeup.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Defining type of the component e.g. shell, layer, ink
    :param CodeableConcept function: The function of this component within the item e.g. delivers active ingredient, masks taste
    :param Quantity amount: The measurable amount of total quantity of all substances in the component, expressable in different ways (e.g. by mass or volume)
    :param Constituent constituent: A reference to a constituent of the manufactured item as a whole, linked here so that its component location within the item can be indicated. This not where the item's ingredient are primarily stated (for which see Ingredient.for or ManufacturedItemDefinition.ingredient)
    :param Property property: General characteristics of this component
    :param Component component: A component that this component contains or is made from
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "amount": {"class_name": "Quantity", "is_contained": False},
        
        
        "constituent": {"class_name": "Constituent", "is_contained": True},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "component": {"class_name": "Component", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  function:  list['CodeableConcept']  = None,  amount:  list['Quantity']  = None,  constituent:  list['Constituent']  = None,  property:  list['Property']  = None,  component:  list['Component']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.function = function or []
        self.amount = amount or []
        self.constituent = constituent or []
        self.property = property or []
        self.component = component or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ManufacturedItemDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ManufacturedItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ManufacturedItemDefinition(DomainResource):
    """ The definition and characteristics of a medicinal manufactured item, such as a tablet or capsule, as contained in a packaged medicinal product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param str status: draft | active | retired | unknown
    :param str name: A descriptive name applied to this item
    :param CodeableConcept manufacturedDoseForm: Dose form as manufactured (before any necessary transformation)
    :param CodeableConcept unitOfPresentation: The “real-world” units in which the quantity of the item is described
    :param Reference manufacturer: Manufacturer of the item, one of several possible
    :param MarketingStatus marketingStatus: Allows specifying that an item is on the market for sale, or that it is not available, and the dates and locations associated
    :param CodeableConcept ingredient: The ingredients of this manufactured item. Only needed if these are not specified by incoming references from the Ingredient resource
    :param Property property: General characteristics of this item
    :param Component component: Physical parts of the manufactured item, that it is intrisically made from. This is distinct from the ingredients that are part of its chemical makeup
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "manufacturedDoseForm": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "unitOfPresentation": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        
        
        "marketingStatus": {"class_name": "MarketingStatus", "is_contained": False},
        
        
        "ingredient": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "component": {"class_name": "Component", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  name:  'str'  = None,  manufacturedDoseForm:  'CodeableConcept'  = None,  unitOfPresentation:  'CodeableConcept'  = None,  manufacturer:  list['Reference']  = None,  marketingStatus:  list['MarketingStatus']  = None,  ingredient:  list['CodeableConcept']  = None,  property:  list['Property']  = None,  component:  list['Component']  = None, ):
        self.resourceType = resourceType or "ManufacturedItemDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status 
        self.name = name 
        self.manufacturedDoseForm = manufacturedDoseForm 
        self.unitOfPresentation = unitOfPresentation 
        self.manufacturer = manufacturer or []
        self.marketingStatus = marketingStatus or []
        self.ingredient = ingredient or []
        self.property = property or []
        self.component = component or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ManufacturedItemDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ManufacturedItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()