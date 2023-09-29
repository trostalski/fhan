"""
Generated class for SubscriptionStatus. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Meta import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class NotificationEvent(BaseModel):
    """ Detailed information about events relevant to this subscription notification.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int eventNumber: Sequencing index of this event
    :param str timestamp: The instant this event occurred
    :param Reference focus: Reference to the primary resource or information of this event
    :param Reference additionalContext: References related to the focus resource and/or context of this event
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "focus": {"class_name": "Reference", "is_contained": False},
        
        
        "additionalContext": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  eventNumber:  'int'  = None,  timestamp:  'str'  = None,  focus:  'Reference'  = None,  additionalContext:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.eventNumber = eventNumber 
        self.timestamp = timestamp 
        self.focus = focus 
        self.additionalContext = additionalContext or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubscriptionStatus":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubscriptionStatus":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubscriptionStatus(DomainResource):
    """ The SubscriptionStatus resource describes the state of a Subscription during notifications. It is not persisted.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str status: requested | active | error | off | entered-in-error
    :param str type: handshake | heartbeat | event-notification | query-status | query-event
    :param int eventsSinceSubscriptionStart: Events since the Subscription was created
    :param NotificationEvent notificationEvent: Detailed information about any events relevant to this notification
    :param Reference subscription: Reference to the Subscription responsible for this notification
    :param str topic: Reference to the SubscriptionTopic this notification relates to
    :param CodeableConcept error: List of errors on the subscription
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        "notificationEvent": {"class_name": "NotificationEvent", "is_contained": True},
        
        
        "subscription": {"class_name": "Reference", "is_contained": False},
        
        
        
        "error": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  status:  'str'  = None,  type:  'str'  = None,  eventsSinceSubscriptionStart:  'int'  = None,  notificationEvent:  list['NotificationEvent']  = None,  subscription:  'Reference'  = None,  topic:  'str'  = None,  error:  list['CodeableConcept']  = None, ):
        self.resourceType = resourceType or "SubscriptionStatus"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.status = status 
        self.type = type 
        self.eventsSinceSubscriptionStart = eventsSinceSubscriptionStart 
        self.notificationEvent = notificationEvent or []
        self.subscription = subscription 
        self.topic = topic 
        self.error = error or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubscriptionStatus":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubscriptionStatus":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()