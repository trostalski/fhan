"""
Generated class for Subscription. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Subscription:
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
    :param BackboneElement filterBy: Criteria for narrowing the subscription topic stream
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceType: Allowed Resource (reference to definition) for this Subscription filter
    :param str filterParameter: Filter label defined in SubscriptionTopic
    :param str comparator: eq | ne | gt | lt | ge | le | sa | eb | ap
    :param str modifier: missing | exact | contains | not | text | in | not-in | below | above | type | identifier | of-type | code-text | text-advanced | iterate
    :param str value: Literal value or resource path
    :param Coding channelType: Channel type for notifications
    :param str endpoint: Where the channel points to
    :param BackboneElement parameter: Channel type
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name (key) of the parameter
    :param str value: Value of the parameter to use or pass through
    :param int heartbeatPeriod: Interval in seconds to send 'heartbeat' notification
    :param int timeout: Timeout in seconds to attempt notification delivery
    :param str contentType: MIME type to send, or omit for no payload
    :param str content: empty | id-only | full-resource
    :param int maxCount: Maximum number of events that can be combined in a single notification
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    name: str = None
    
    status: str = None
    
    topic: str = None
    
    contact: "ContactPoint" = None
    
    end: str = None
    
    managingEntity: "Reference" = None
    
    reason: str = None
    
    filterBy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    resourceType: str = None
    
    filterParameter: str = None
    
    comparator: str = None
    
    modifier: str = None
    
    value: str = None
    
    channelType: "Coding" = None
    
    endpoint: str = None
    
    parameter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    value: str = None
    
    heartbeatPeriod: int = None
    
    timeout: int = None
    
    contentType: str = None
    
    content: str = None
    
    maxCount: int = None
    