"""
Generated class for Subscription. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Meta import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class FilterBy(BaseModel):
    """ The filter properties to be applied to narrow the subscription topic stream.  When multiple filters are applied, evaluates to true if all the conditions applicable to that resource are met; otherwise it returns false (i.e., logical AND).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceType: Allowed Resource (reference to definition) for this Subscription filter
    :param str filterParameter: Filter label defined in SubscriptionTopic
    :param str comparator: eq | ne | gt | lt | ge | le | sa | eb | ap
    :param str modifier: missing | exact | contains | not | text | in | not-in | below | above | type | identifier | of-type | code-text | text-advanced | iterate
    :param str value: Literal value or resource path
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  resourceType:  'str'  = None,  filterParameter:  'str'  = None,  comparator:  'str'  = None,  modifier:  'str'  = None,  value:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.resourceType = resourceType 
        self.filterParameter = filterParameter 
        self.comparator = comparator 
        self.modifier = modifier 
        self.value = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Subscription":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Subscription":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Parameter(BaseModel):
    """ Channel-dependent information to send as part of the notification (e.g., HTTP Headers).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name (key) of the parameter
    :param str value: Value of the parameter to use or pass through
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  value:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.value = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Subscription":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Subscription":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Subscription(DomainResource):
    """ The subscription resource describes a particular client's request to be notified about a SubscriptionTopic.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Additional identifiers (business identifier)
    :param str name: Human readable name for this subscription
    :param str status: requested | active | error | off | entered-in-error
    :param str topic: Reference to the subscription topic being subscribed to
    :param ContactPoint contact: Contact details for source (e.g. troubleshooting)
    :param str end: When to automatically delete the subscription
    :param Reference managingEntity: Entity responsible for Subscription changes
    :param str reason: Description of why this subscription was created
    :param FilterBy filterBy: Criteria for narrowing the subscription topic stream
    :param Coding channelType: Channel type for notifications
    :param str endpoint: Where the channel points to
    :param Parameter parameter: Channel type
    :param int heartbeatPeriod: Interval in seconds to send 'heartbeat' notification
    :param int timeout: Timeout in seconds to attempt notification delivery
    :param str contentType: MIME type to send, or omit for no payload
    :param str content: empty | id-only | full-resource
    :param int maxCount: Maximum number of events that can be combined in a single notification
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        "contact": {"class_name": "ContactPoint", "is_contained": False},
        
        
        
        "managingEntity": {"class_name": "Reference", "is_contained": False},
        
        
        
        "filterBy": {"class_name": "FilterBy", "is_contained": True},
        
        
        "channelType": {"class_name": "Coding", "is_contained": False},
        
        
        
        "parameter": {"class_name": "Parameter", "is_contained": True},
        
        
        
        
        
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  name:  'str'  = None,  status:  'str'  = None,  topic:  'str'  = None,  contact:  list['ContactPoint']  = None,  end:  'str'  = None,  managingEntity:  'Reference'  = None,  reason:  'str'  = None,  filterBy:  list['FilterBy']  = None,  channelType:  'Coding'  = None,  endpoint:  'str'  = None,  parameter:  list['Parameter']  = None,  heartbeatPeriod:  'int'  = None,  timeout:  'int'  = None,  contentType:  'str'  = None,  content:  'str'  = None,  maxCount:  'int'  = None, ):
        self.resourceType = resourceType or "Subscription"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.name = name 
        self.status = status 
        self.topic = topic 
        self.contact = contact or []
        self.end = end 
        self.managingEntity = managingEntity 
        self.reason = reason 
        self.filterBy = filterBy or []
        self.channelType = channelType 
        self.endpoint = endpoint 
        self.parameter = parameter or []
        self.heartbeatPeriod = heartbeatPeriod 
        self.timeout = timeout 
        self.contentType = contentType 
        self.content = content 
        self.maxCount = maxCount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Subscription":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Subscription":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()