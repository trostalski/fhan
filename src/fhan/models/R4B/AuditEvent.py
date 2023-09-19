"""
Generated class for AuditEvent. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class AuditEvent:
    """
    A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "Coding" = None
    
    subtype: "Coding" = None
    
    action: str = None
    
    period: "Period" = None
    
    recorded: str = None
    
    outcome: str = None
    
    outcomeDesc: str = None
    
    purposeOfEvent: "CodeableConcept" = None
    
    agent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    role: "CodeableConcept" = None
    
    who: "Reference" = None
    
    altId: str = None
    
    name: str = None
    
    requestor: bool = None
    
    location: "Reference" = None
    
    policy: str = None
    
    media: "Coding" = None
    
    network: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    address: str = None
    
    type: str = None
    
    purposeOfUse: "CodeableConcept" = None
    
    source: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    site: str = None
    
    observer: "Reference" = None
    
    type: "Coding" = None
    
    entity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    what: "Reference" = None
    
    type: "Coding" = None
    
    role: "Coding" = None
    
    lifecycle: "Coding" = None
    
    securityLabel: "Coding" = None
    
    name: str = None
    
    description: str = None
    
    query: str = None
    
    detail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    valuestring: str = None
    
    valuestring: str = None
    