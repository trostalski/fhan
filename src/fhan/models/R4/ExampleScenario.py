"""
Generated class for ExampleScenario. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class ExampleScenario:
    """
    Example of workflow instance.
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
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    copyright: str = None
    
    purpose: str = None
    
    actor: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    actorId: str = None
    
    type: str = None
    
    name: str = None
    
    description: str = None
    
    instance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    resourceId: str = None
    
    resourceType: str = None
    
    name: str = None
    
    description: str = None
    
    version: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    versionId: str = None
    
    description: str = None
    
    containedInstance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    resourceId: str = None
    
    versionId: str = None
    
    process: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    description: str = None
    
    preConditions: str = None
    
    postConditions: str = None
    
    step: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    process: "BackboneElement" = None
    
    pause: bool = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    number: str = None
    
    type: str = None
    
    name: str = None
    
    initiator: str = None
    
    receiver: str = None
    
    description: str = None
    
    initiatorActive: bool = None
    
    receiverActive: bool = None
    
    request: "BackboneElement" = None
    
    response: "BackboneElement" = None
    
    alternative: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    description: str = None
    
    step: "BackboneElement" = None
    
    workflow: str = None
    