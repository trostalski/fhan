"""
Generated class for AuditEvent. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Meta import *


@dataclass
class AuditEvent:
    """
    Defines the elements to be supported within the AuditEvent resource in order to conform with the Electronic Health Record System Functional Model Record Lifecycle Event standard
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
    