"""
Generated class for MessageHeader. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Destination(Element):
    """ The destination application which the message is intended for.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of system
    :param Reference target: Particular delivery destination within the destination
    :param str endpoint: Actual destination address or id
    :param Reference receiver: Intended "real-world" recipient for the data
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    name: str = None
    target: "Reference" = None
    
    endpoint: str = None
    receiver: "Reference" = None
    

    
    
@dataclass
class Source(Element):
    """ The source application from which this message originated.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of system
    :param str software: Name of software running the system
    :param str version: Version of software running
    :param ContactPoint contact: Human contact for problems
    :param str endpoint: Actual message source address or id
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    name: str = None
    
    software: str = None
    
    version: str = None
    contact: "ContactPoint" = None
    
    endpoint: str = None
    

    
    
@dataclass
class Response(Element):
    """ Information about the message that this message is a response to.  Only present if this message is a response.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str identifier: Id of original message
    :param str code: ok | transient-error | fatal-error
    :param Reference details: Specific list of hints/warnings/errors
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    identifier: str = None
    
    code: str = None
    details: "Reference" = None
    
@dataclass
class MessageHeader(ModelBase):
    """ The header for a message exchange that is either requesting or responding to an action.  The reference(s) that are the subject of the action as well as other information related to the action are typically transmitted in a bundle in which the MessageHeader resource instance is the first resource in the bundle.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Coding eventCoding: Code for the event this message represents or link to event definition
    :param Destination destination: Message destination application(s)
    :param Reference sender: Real world sender of the message
    :param Reference enterer: The source of the data entry
    :param Reference author: The source of the decision
    :param Source source: Message source application
    :param Reference responsible: Final responsibility for event
    :param CodeableConcept reason: Cause of event
    :param Response response: If this is a reply to prior message
    :param Reference focus: The actual content of the message
    :param str definition: Link to the definition for this message
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    eventCoding: "Coding" = None
    
    destination: list["Destination"] = None
    
    sender: "Reference" = None
    
    enterer: "Reference" = None
    
    author: "Reference" = None
    
    source: "Source" = None
    
    responsible: "Reference" = None
    
    reason: "CodeableConcept" = None
    
    response: "Response" = None
    
    focus: list["Reference"] = None
    
    definition: str = None
    