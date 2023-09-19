"""
Generated class for MessageHeader. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.ContactPoint import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class MessageHeader:
    """
    The header for a message exchange that is either requesting or responding to an action.  The reference(s) that are the subject of the action as well as other information related to the action are typically transmitted in a bundle in which the MessageHeader resource instance is the first resource in the bundle.
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
    
    name: str = None
    
    target: "Reference" = None
    
    endpoint: str = None
    
    receiver: "Reference" = None
    
    sender: "Reference" = None
    
    enterer: "Reference" = None
    
    author: "Reference" = None
    
    source: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    software: str = None
    
    version: str = None
    
    contact: "ContactPoint" = None
    
    endpoint: str = None
    
    responsible: "Reference" = None
    
    reason: "CodeableConcept" = None
    
    response: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: str = None
    
    code: str = None
    
    details: "Reference" = None
    
    focus: "Reference" = None
    
    definition: str = None
    