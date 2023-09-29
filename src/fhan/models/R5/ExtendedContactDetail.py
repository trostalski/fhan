"""
Generated class for ExtendedContactDetail. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Address import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.HumanName import *
from fhan.models.R5.Period import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Extension import *
from fhan.models.generator_models import BaseModel

class ExtendedContactDetail(BaseModel):
    """ ExtendedContactDetail Type: Specifies contact information for a specific purpose over a period of time, might be handled/monitored by a specific named person or organization.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param CodeableConcept purpose: The type of contact
    :param HumanName name: Name of an individual to contact
    :param ContactPoint telecom: Contact details (e.g.phone/fax/url)
    :param Address address: Address for the contact
    :param Reference organization: This contact detail is handled/monitored by a specific organization
    :param Period period: Period that this contact was valid for usage
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "purpose": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "name": {"class_name": "HumanName", "is_contained": False},
        
        
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        
        
        "address": {"class_name": "Address", "is_contained": False},
        
        
        "organization": {"class_name": "Reference", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  purpose:  'CodeableConcept'  = None,  name:  list['HumanName']  = None,  telecom:  list['ContactPoint']  = None,  address:  'Address'  = None,  organization:  'Reference'  = None,  period:  'Period'  = None, ):
        self.resourceType = resourceType or "ExtendedContactDetail"
        self.id = id 
        self.extension = extension or []
        self.purpose = purpose 
        self.name = name or []
        self.telecom = telecom or []
        self.address = address 
        self.organization = organization 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExtendedContactDetail":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExtendedContactDetail":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()