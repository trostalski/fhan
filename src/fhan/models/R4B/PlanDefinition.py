"""
Generated class for PlanDefinition. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Duration import *
from fhan.models.R4B.RelatedArtifact import *
from fhan.models.R4B.TriggerDefinition import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.DataRequirement import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Expression import *
from fhan.models.R4B.Reference import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Timing import *
from fhan.models.R4B.Age import *
from fhan.models.R4B.Resource import *


@dataclass
class PlanDefinition:
    """
    Defines a PlanDefinition that implements the behavior for a CDS Hooks service
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    extension:cdsHooksEndpoint: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    type: "CodeableConcept" = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    subjectCodeableConcept: str = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    usage: str = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    topic: "CodeableConcept" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    library: str = None
    
    goal: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    description: "CodeableConcept" = None
    
    priority: "CodeableConcept" = None
    
    start: "CodeableConcept" = None
    
    addresses: "CodeableConcept" = None
    
    documentation: "RelatedArtifact" = None
    
    target: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    measure: "CodeableConcept" = None
    
    detailQuantity: "Quantity" = None
    
    detailQuantity: "Range" = None
    
    detailQuantity: "CodeableConcept" = None
    
    due: "Duration" = None
    
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
    
    reason: "CodeableConcept" = None
    
    documentation: "RelatedArtifact" = None
    
    goalId: str = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    subjectCodeableConcept: str = None
    
    trigger: "TriggerDefinition" = None
    
    condition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    kind: str = None
    
    expression: "Expression" = None
    
    input: "DataRequirement" = None
    
    output: "DataRequirement" = None
    
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
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    role: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    groupingBehavior: str = None
    
    selectionBehavior: str = None
    
    requiredBehavior: str = None
    
    precheckBehavior: str = None
    
    cardinalityBehavior: str = None
    
    definitioncanonical: str = None
    
    definitioncanonical: str = None
    
    transform: str = None
    
    dynamicValue: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    path: str = None
    
    expression: "Expression" = None
    
    action: "BackboneElement" = None
    