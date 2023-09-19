"""
Generated class for MessageHeader. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class MessageHeader:
    """ The header for a message exchange that is either requesting or responding to an action.  The reference(s) that are the subject of the action as well as other information related to the action are typically transmitted in a bundle in which the MessageHeader resource instance is the first resource in the bundle.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Coding eventCoding: Event code or link to EventDefinition
    :param str eventCoding: Event code or link to EventDefinition
    :param BackboneElement destination: Message destination application(s)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str endpointurl: Actual destination address or Endpoint resource
    :param Reference endpointurl: Actual destination address or Endpoint resource
    :param str name: Name of system
    :param Reference target: Particular delivery destination within the destination
    :param Reference receiver: Intended "real-world" recipient for the data
    :param Reference sender: Real world sender of the message
    :param Reference author: The source of the decision
    :param BackboneElement source: Message source application
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str endpointurl: Actual source address or Endpoint resource
    :param Reference endpointurl: Actual source address or Endpoint resource
    :param str name: Name of system
    :param str software: Name of software running the system
    :param str version: Version of software running
    :param ContactPoint contact: Human contact for problems
    :param Reference responsible: Final responsibility for event
    :param CodeableConcept reason: Cause of event
    :param BackboneElement response: If this is a reply to prior message
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Bundle.identifier of original message
    :param str code: ok | transient-error | fatal-error
    :param Reference details: Specific list of hints/warnings/errors
    :param Reference focus: The actual content of the message
    :param str definition: Link to the definition for this message
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    eventCoding: "Coding" = None
    
    eventCoding: str = None
    
    destination: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    endpointurl: str = None
    
    endpointurl: "Reference" = None
    
    name: str = None
    
    target: "Reference" = None
    
    receiver: "Reference" = None
    
    sender: "Reference" = None
    
    author: "Reference" = None
    
    source: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    endpointurl: str = None
    
    endpointurl: "Reference" = None
    
    name: str = None
    
    software: str = None
    
    version: str = None
    
    contact: "ContactPoint" = None
    
    responsible: "Reference" = None
    
    reason: "CodeableConcept" = None
    
    response: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    code: str = None
    
    details: "Reference" = None
    
    focus: "Reference" = None
    
    definition: str = None
    