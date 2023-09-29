"""
Generated class for Product. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Element import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Quantity import *
from fhan.models.generator_models import BaseModel

    
    

class Instance(BaseModel):
    """ Conveys instance-level information about this product item. One or several physical, countable instances or occurrences of the product.:param Quantity quantity: The amount of items
    :param Identifier identifier: The identifier for the physical instance, typically a serial number
    :param str lotNumber: The identification of the batch or lot of the product
    :param str expiry: The expiry date or date and time for the product
    :param Reference subject: Individual the product is associated with, or which has used the product
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  quantity:  'Quantity'  = None,  identifier:  list['Identifier']  = None,  lotNumber:  'str'  = None,  expiry:  'str'  = None,  subject:  'Reference'  = None, ):
        self.quantity = quantity 
        self.identifier = identifier or []
        self.lotNumber = lotNumber 
        self.expiry = expiry 
        self.subject = subject 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Product":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Product(BaseModel):
    """ Logical Model: A pattern to be followed by resources that represent a product used in healthcare, for clinical or operational purposes.
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: A category or class of the product
    :param CodeableConcept code: A code designating a specific type of product
    :param Reference manufacturer: Manufacturer, representative or officially responsible for the product
    :param Instance instance: One or several physical instances or occurrences of the product
    :param Annotation note: Comments made about the product
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        
        
        "instance": {"class_name": "Instance", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  status:  'str'  = None,  category:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  manufacturer:  list['Reference']  = None,  instance:  'Instance'  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "Product"
        self.status = status 
        self.category = category or []
        self.code = code 
        self.manufacturer = manufacturer or []
        self.instance = instance 
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Product":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()