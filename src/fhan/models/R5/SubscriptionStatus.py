"""
Generated class for SubscriptionStatus. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Reference import *


@dataclass
class SubscriptionStatus:
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
    :param BackboneElement notificationEvent: Detailed information about any events relevant to this notification
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int eventNumber: Sequencing index of this event
    :param str timestamp: The instant this event occurred
    :param Reference focus: Reference to the primary resource or information of this event
    :param Reference additionalContext: References related to the focus resource and/or context of this event
    :param Reference subscription: Reference to the Subscription responsible for this notification
    :param str topic: Reference to the SubscriptionTopic this notification relates to
    :param CodeableConcept error: List of errors on the subscription
    
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
    
    eventsSinceSubscriptionStart: int = None
    
    notificationEvent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    eventNumber: int = None
    
    timestamp: str = None
    
    focus: "Reference" = None
    
    additionalContext: "Reference" = None
    
    subscription: "Reference" = None
    
    topic: str = None
    
    error: "CodeableConcept" = None
    