"""
Generated class for Substance. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Ingredient(BaseModel):
    """ A substance can be composed of other substances.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio quantity: Optional amount (concentration)
    :param CodeableConcept substanceCodeableConcept: A component of the substance
    :param Reference substanceReference: A component of the substance
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "quantity": {"class_name": "Ratio", "is_contained": False},
        
        
        "substanceCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "substanceReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  quantity:  'Ratio'  = None,  substanceCodeableConcept:  'CodeableConcept'  = None,  substanceReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.quantity = quantity 
        self.substanceCodeableConcept = substanceCodeableConcept 
        self.substanceReference = substanceReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Substance":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Substance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Substance(DomainResource):
    """ A homogeneous material with a definite composition.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param bool instance: Is this an instance of a substance or a kind of one
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: What class/type of substance this is
    :param CodeableReference code: What substance this is
    :param str description: Textual description of the substance, comments
    :param str expiry: When no longer valid to use
    :param Quantity quantity: Amount of substance in the package
    :param Ingredient ingredient: Composition information about the substance
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "ingredient": {"class_name": "Ingredient", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instance:  'bool'  = None,  status:  'str'  = None,  category:  list['CodeableConcept']  = None,  code:  'CodeableReference'  = None,  description:  'str'  = None,  expiry:  'str'  = None,  quantity:  'Quantity'  = None,  ingredient:  list['Ingredient']  = None, ):
        self.resourceType = resourceType or "Substance"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instance = instance 
        self.status = status 
        self.category = category or []
        self.code = code 
        self.description = description 
        self.expiry = expiry 
        self.quantity = quantity 
        self.ingredient = ingredient or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Substance":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Substance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()