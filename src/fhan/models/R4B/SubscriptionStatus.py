"""
Generated class for SubscriptionStatus. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class SubscriptionStatus:
    """
    The SubscriptionStatus resource describes the state of a Subscription during notifications.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    status: str = None
    
    type: str = None
    
    eventsSinceSubscriptionStart: str = None
    
    notificationEvent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    eventNumber: str = None
    
    timestamp: str = None
    
    focus: "Reference" = None
    
    additionalContext: "Reference" = None
    
    subscription: "Reference" = None
    
    topic: str = None
    
    error: "CodeableConcept" = None
    