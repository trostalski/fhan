"""
Generated class for ParticipantContactable. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Address import *
from fhan.models.R5.ContactPoint import *
from fhan.models.generator_models import BaseModel

class ParticipantContactable(BaseModel):
    """ Logical Model: A pattern followed by resources that represent a participant that can be contacted.
    :param ContactPoint telecom: A contact detail for the {{title}}
    :param Address address: An address for the {{title}}
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        
        
        "address": {"class_name": "Address", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  telecom:  list['ContactPoint']  = None,  address:  list['Address']  = None, ):
        self.resourceType = resourceType or "ParticipantContactable"
        self.telecom = telecom or []
        self.address = address or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ParticipantContactable":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ParticipantContactable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()