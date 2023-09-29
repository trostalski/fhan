"""
Generated class for MessageHeader. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Destination(BaseModel):
    """ The destination application which the message is intended for.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str endpointUrl: Actual destination address or Endpoint resource
    :param Reference endpointReference: Actual destination address or Endpoint resource
    :param str name: Name of system
    :param Reference target: Particular delivery destination within the destination
    :param Reference receiver: Intended "real-world" recipient for the data
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "endpointReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        "target": {"class_name": "Reference", "is_contained": False},
        
        
        "receiver": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  endpointUrl:  'str'  = None,  endpointReference:  'Reference'  = None,  name:  'str'  = None,  target:  'Reference'  = None,  receiver:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.endpointUrl = endpointUrl 
        self.endpointReference = endpointReference 
        self.name = name 
        self.target = target 
        self.receiver = receiver 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MessageHeader":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MessageHeader":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Source(BaseModel):
    """ The source application from which this message originated.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str endpointUrl: Actual source address or Endpoint resource
    :param Reference endpointReference: Actual source address or Endpoint resource
    :param str name: Name of system
    :param str software: Name of software running the system
    :param str version: Version of software running
    :param ContactPoint contact: Human contact for problems
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "endpointReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "contact": {"class_name": "ContactPoint", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  endpointUrl:  'str'  = None,  endpointReference:  'Reference'  = None,  name:  'str'  = None,  software:  'str'  = None,  version:  'str'  = None,  contact:  'ContactPoint'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.endpointUrl = endpointUrl 
        self.endpointReference = endpointReference 
        self.name = name 
        self.software = software 
        self.version = version 
        self.contact = contact 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MessageHeader":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MessageHeader":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Response(BaseModel):
    """ Information about the message that this message is a response to.  Only present if this message is a response.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Bundle.identifier of original message
    :param str code: ok | transient-error | fatal-error
    :param Reference details: Specific list of hints/warnings/errors
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "details": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  'Identifier'  = None,  code:  'str'  = None,  details:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier 
        self.code = code 
        self.details = details 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MessageHeader":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MessageHeader":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MessageHeader(DomainResource):
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
    :param str eventCanonical: Event code or link to EventDefinition
    :param Destination destination: Message destination application(s)
    :param Reference sender: Real world sender of the message
    :param Reference author: The source of the decision
    :param Source source: Message source application
    :param Reference responsible: Final responsibility for event
    :param CodeableConcept reason: Cause of event
    :param Response response: If this is a reply to prior message
    :param Reference focus: The actual content of the message
    :param str definition: Link to the definition for this message
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "eventCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        "destination": {"class_name": "Destination", "is_contained": True},
        
        
        "sender": {"class_name": "Reference", "is_contained": False},
        
        
        "author": {"class_name": "Reference", "is_contained": False},
        
        
        "source": {"class_name": "Source", "is_contained": True},
        
        
        "responsible": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "response": {"class_name": "Response", "is_contained": True},
        
        
        "focus": {"class_name": "Reference", "is_contained": False},
        
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  eventCoding:  'Coding'  = None,  eventCanonical:  'str'  = None,  destination:  list['Destination']  = None,  sender:  'Reference'  = None,  author:  'Reference'  = None,  source:  'Source'  = None,  responsible:  'Reference'  = None,  reason:  'CodeableConcept'  = None,  response:  'Response'  = None,  focus:  list['Reference']  = None,  definition:  'str'  = None, ):
        self.resourceType = resourceType or "MessageHeader"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.eventCoding = eventCoding 
        self.eventCanonical = eventCanonical 
        self.destination = destination or []
        self.sender = sender 
        self.author = author 
        self.source = source 
        self.responsible = responsible 
        self.reason = reason 
        self.response = response 
        self.focus = focus or []
        self.definition = definition 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MessageHeader":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MessageHeader":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()