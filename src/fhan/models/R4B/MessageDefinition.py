"""
Generated class for MessageDefinition. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.CodeableConcept import *


@dataclass
class MessageDefinition:
    """
    Defines the characteristics of a message that can be shared between systems, including the type of event that initiates the message, the content to be transmitted and what response(s), if any, are permitted.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    replaces: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    base: str = None
    
    parent: str = None
    
    eventCoding: "Coding" = None
    
    eventCoding: str = None
    
    category: str = None
    
    focus: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    profile: str = None
    
    min: int = None
    
    max: str = None
    
    responseRequired: str = None
    
    allowedResponse: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    message: str = None
    
    situation: str = None
    
    graph: str = None
    