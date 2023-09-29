"""
Generated class for Medication. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Ingredient(BaseModel):
    """ Identifies a particular constituent of interest in the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: The ingredient (substance or medication) that the ingredient.strength relates to
    :param bool isActive: Active ingredient indicator
    :param Ratio strengthRatio: Quantity of ingredient present
    :param CodeableConcept strengthCodeableConcept: Quantity of ingredient present
    :param Quantity strengthQuantity: Quantity of ingredient present
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "item": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        "strengthRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        "strengthCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "strengthQuantity": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  item:  'CodeableReference'  = None,  isActive:  'bool'  = None,  strengthRatio:  'Ratio'  = None,  strengthCodeableConcept:  'CodeableConcept'  = None,  strengthQuantity:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.item = item 
        self.isActive = isActive 
        self.strengthRatio = strengthRatio 
        self.strengthCodeableConcept = strengthCodeableConcept 
        self.strengthQuantity = strengthQuantity 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Medication":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Medication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Batch(BaseModel):
    """ Information that only applies to packages (not products).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lotNumber: Identifier assigned to batch
    :param str expirationDate: When batch will expire
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  lotNumber:  'str'  = None,  expirationDate:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.lotNumber = lotNumber 
        self.expirationDate = expirationDate 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Medication":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Medication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Medication(DomainResource):
    """ This resource is primarily used for the identification and definition of a medication, including ingredients, for the purposes of prescribing, dispensing, and administering a medication as well as for making statements about medication use.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this medication
    :param CodeableConcept code: Codes that identify this medication
    :param str status: active | inactive | entered-in-error
    :param Reference marketingAuthorizationHolder: Organization that has authorization to market medication
    :param CodeableConcept doseForm: powder | tablets | capsule +
    :param Quantity totalVolume: When the specified product code does not infer a package size, this is the specific amount of drug in the product
    :param Ingredient ingredient: Active or inactive ingredient
    :param Batch batch: Details about packaged medications
    :param Reference definition: Knowledge about this medication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "marketingAuthorizationHolder": {"class_name": "Reference", "is_contained": False},
        
        
        "doseForm": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "totalVolume": {"class_name": "Quantity", "is_contained": False},
        
        
        "ingredient": {"class_name": "Ingredient", "is_contained": True},
        
        
        "batch": {"class_name": "Batch", "is_contained": True},
        
        
        "definition": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  code:  'CodeableConcept'  = None,  status:  'str'  = None,  marketingAuthorizationHolder:  'Reference'  = None,  doseForm:  'CodeableConcept'  = None,  totalVolume:  'Quantity'  = None,  ingredient:  list['Ingredient']  = None,  batch:  'Batch'  = None,  definition:  'Reference'  = None, ):
        self.resourceType = resourceType or "Medication"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.code = code 
        self.status = status 
        self.marketingAuthorizationHolder = marketingAuthorizationHolder 
        self.doseForm = doseForm 
        self.totalVolume = totalVolume 
        self.ingredient = ingredient or []
        self.batch = batch 
        self.definition = definition 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Medication":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Medication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()