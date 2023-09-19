"""
Generated class for ActivityDefinition. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Dosage import *
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Duration import *
from fhan.models.R4B.RelatedArtifact import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.ContactDetail import *
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
class ActivityDefinition:
    """
    This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.
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
    
    subtitle: str = None
    
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
    
    kind: str = None
    
    profile: str = None
    
    code: "CodeableConcept" = None
    
    intent: str = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    timingTiming: "Timing" = None
    
    timingTiming: str = None
    
    timingTiming: "Age" = None
    
    timingTiming: "Period" = None
    
    timingTiming: "Range" = None
    
    timingTiming: "Duration" = None
    
    location: "Reference" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    role: "CodeableConcept" = None
    
    productReference: "Reference" = None
    
    productReference: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    dosage: "Dosage" = None
    
    bodySite: "CodeableConcept" = None
    
    specimenRequirement: "Reference" = None
    
    observationRequirement: "Reference" = None
    
    observationResultRequirement: "Reference" = None
    
    transform: str = None
    
    dynamicValue: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    path: str = None
    
    expression: "Expression" = None
    