"""
Generated class for ResearchElementDefinition. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class ResearchElementDefinition:
    """
    The ResearchElementDefinition resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
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
    
    shortTitle: str = None
    
    subtitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    comment: str = None
    
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
    
    type: str = None
    
    variableType: str = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    definitionCodeableConcept: "CodeableConcept" = None
    
    definitionCodeableConcept: str = None
    
    definitionCodeableConcept: "Expression" = None
    
    definitionCodeableConcept: "DataRequirement" = None
    
    usageContext: "UsageContext" = None
    
    exclude: bool = None
    
    unitOfMeasure: "CodeableConcept" = None
    
    studyEffectiveDescription: str = None
    
    studyEffectivedateTime: str = None
    
    studyEffectivedateTime: "Period" = None
    
    studyEffectivedateTime: "Duration" = None
    
    studyEffectivedateTime: "Timing" = None
    
    studyEffectiveTimeFromStart: "Duration" = None
    
    studyEffectiveGroupMeasure: str = None
    
    participantEffectiveDescription: str = None
    
    participantEffectivedateTime: str = None
    
    participantEffectivedateTime: "Period" = None
    
    participantEffectivedateTime: "Duration" = None
    
    participantEffectivedateTime: "Timing" = None
    
    participantEffectiveTimeFromStart: "Duration" = None
    
    participantEffectiveGroupMeasure: str = None
    