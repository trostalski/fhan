"""
Generated class for VirtualServiceDetail. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Extension import *
from fhan.models.generator_models import BaseModel

class VirtualServiceDetail(BaseModel):
    """ VirtualServiceDetail Type: Virtual Service Contact Details.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding channelType: Channel Type
    :param str addressUrl: Contact address/number
    :param str addressString: Contact address/number
    :param ContactPoint addressContactPoint: Contact address/number
    :param ExtendedContactDetail addressExtendedContactDetail: Contact address/number
    :param str additionalInfo: Address to see alternative connection details
    :param int maxParticipants: Maximum number of participants supported by the virtual service
    :param str sessionKey: Session Key required by the virtual service
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "channelType": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        "addressContactPoint": {"class_name": "ContactPoint", "is_contained": False},
        
        
        "addressExtendedContactDetail": {"class_name": "ExtendedContactDetail", "is_contained": False},
        
        
        
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  channelType:  'Coding'  = None,  addressUrl:  'str'  = None,  addressString:  'str'  = None,  addressContactPoint:  'ContactPoint'  = None,  addressExtendedContactDetail:  'ExtendedContactDetail'  = None,  additionalInfo:  list['str']  = None,  maxParticipants:  'int'  = None,  sessionKey:  'str'  = None, ):
        self.resourceType = resourceType or "VirtualServiceDetail"
        self.id = id 
        self.extension = extension or []
        self.channelType = channelType 
        self.addressUrl = addressUrl 
        self.addressString = addressString 
        self.addressContactPoint = addressContactPoint 
        self.addressExtendedContactDetail = addressExtendedContactDetail 
        self.additionalInfo = additionalInfo or []
        self.maxParticipants = maxParticipants 
        self.sessionKey = sessionKey 
        

    @classmethod
    def from_dict(cls, data: dict) -> "VirtualServiceDetail":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "VirtualServiceDetail":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()