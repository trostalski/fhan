"""
Generated class for MonetaryComponent. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Money import *
from fhan.models.R5.Extension import *
from fhan.models.generator_models import BaseModel

class MonetaryComponent(BaseModel):
    """ MonetaryComponent Type: Availability data for an {item}.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: base | surcharge | deduction | discount | tax | informational
    :param CodeableConcept code: Codes may be used to differentiate between kinds of taxes, surcharges, discounts etc.
    :param float factor: Factor used for calculating this component
    :param Money amount: Explicit value amount to be used
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "amount": {"class_name": "Money", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  type:  'str'  = None,  code:  'CodeableConcept'  = None,  factor:  'float'  = None,  amount:  'Money'  = None, ):
        self.resourceType = resourceType or "MonetaryComponent"
        self.id = id 
        self.extension = extension or []
        self.type = type 
        self.code = code 
        self.factor = factor 
        self.amount = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MonetaryComponent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MonetaryComponent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()