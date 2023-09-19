"""
Generated class for RequestGroup. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Duration import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Age import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *


@dataclass
class RequestGroup:
    """
    A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
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
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    replaces: "Reference" = None
    
    groupIdentifier: "Identifier" = None
    
    status: str = None
    
    intent: str = None
    
    priority: str = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    authoredOn: str = None
    
    author: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    note: "Annotation" = None
    
    action: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    prefix: str = None
    
    title: str = None
    
    description: str = None
    
    textEquivalent: str = None
    
    priority: str = None
    
    code: "CodeableConcept" = None
    
    documentation: "RelatedArtifact" = None
    
    condition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    kind: str = None
    
    expression: "Expression" = None
    
    relatedAction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    actionId: str = None
    
    relationship: str = None
    
    offsetDuration: "Duration" = None
    
    offsetDuration: "Range" = None
    
    timingdateTime: str = None
    
    timingdateTime: "Age" = None
    
    timingdateTime: "Period" = None
    
    timingdateTime: "Duration" = None
    
    timingdateTime: "Range" = None
    
    timingdateTime: "Timing" = None
    
    participant: "Reference" = None
    
    type: "CodeableConcept" = None
    
    groupingBehavior: str = None
    
    selectionBehavior: str = None
    
    requiredBehavior: str = None
    
    precheckBehavior: str = None
    
    cardinalityBehavior: str = None
    
    resource: "Reference" = None
    
    action: "BackboneElement" = None
    