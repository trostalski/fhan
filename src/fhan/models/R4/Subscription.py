"""
Generated class for Subscription. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Channel(Element):
    """ Details where to send notifications when resources are received that meet the criteria.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: rest-hook | websocket | email | sms | message
    :param str endpoint: Where the channel points to
    :param str payload: MIME type to send, or omit for no payload
    :param str header: Usage depends on the channel type
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    type: str = None
    
    endpoint: str = None
    
    payload: str = None
    
    header: str = None
    

@dataclass
class Subscription(ModelBase):
    """ The subscription resource is used to define a push-based subscription from a server to another system. Once a subscription is registered with the server, the server checks every resource that is created or updated, and if the resource matches the given criteria, it sends a message on the defined "channel" so that another system can take an appropriate action.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str status: requested | active | error | off
    :param ContactPoint contact: Contact details for source (e.g. troubleshooting)
    :param str end: When to automatically delete the subscription
    :param str reason: Description of why this subscription was created
    :param str criteria: Rule for server push
    :param str error: Latest error note
    :param Channel channel: The channel on which to report matches to the criteria
    """

    resourceType: str = "Subscription"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    status: str = None
    
    contact: list[ContactPoint] = ContactPoint() 
    
    end: str = None
    
    reason: str = None
    
    criteria: str = None
    
    error: str = None
    
    channel: "Channel" = Channel()
    