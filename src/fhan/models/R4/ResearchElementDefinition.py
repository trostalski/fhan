"""
Generated class for ResearchElementDefinition. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase


@dataclass
class ResearchElementDefinition(ModelBase):
    """ The ResearchElementDefinition resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this research element definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the research element definition
    :param str version: Business version of the research element definition
    :param str name: Name for this research element definition (computer friendly)
    :param str title: Name for this research element definition (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the ResearchElementDefinition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param Reference subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the research element definition
    :param str comment: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for research element definition (if applicable)
    :param str purpose: Why this research element definition is defined
    :param str usage: Describes the clinical usage of the ResearchElementDefinition
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the research element definition was approved by publisher
    :param str lastReviewDate: When the research element definition was last reviewed
    :param Period effectivePeriod: When the research element definition is expected to be used
    :param CodeableConcept topic: The category of the ResearchElementDefinition, such as Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param str library: Logic used by the ResearchElementDefinition
    :param str type: population | exposure | outcome
    :param str variableType: dichotomous | continuous | descriptive
    :param BackboneElement characteristic: What defines the members of the research element
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept definitionCodeableConcept: What code or expression defines members?
    :param str definitionCodeableConcept: What code or expression defines members?
    :param Expression definitionCodeableConcept: What code or expression defines members?
    :param DataRequirement definitionCodeableConcept: What code or expression defines members?
    :param UsageContext usageContext: What code/value pairs define members?
    :param bool exclude: Whether the characteristic includes or excludes members
    :param CodeableConcept unitOfMeasure: What unit is the outcome described in?
    :param str studyEffectiveDescription: What time period does the study cover
    :param str studyEffectivedateTime: What time period does the study cover
    :param Period studyEffectivedateTime: What time period does the study cover
    :param Duration studyEffectivedateTime: What time period does the study cover
    :param Timing studyEffectivedateTime: What time period does the study cover
    :param Duration studyEffectiveTimeFromStart: Observation time from study start
    :param str studyEffectiveGroupMeasure: mean | median | mean-of-mean | mean-of-median | median-of-mean | median-of-median
    :param str participantEffectiveDescription: What time period do participants cover
    :param str participantEffectivedateTime: What time period do participants cover
    :param Period participantEffectivedateTime: What time period do participants cover
    :param Duration participantEffectivedateTime: What time period do participants cover
    :param Timing participantEffectivedateTime: What time period do participants cover
    :param Duration participantEffectiveTimeFromStart: Observation time from study start
    :param str participantEffectiveGroupMeasure: mean | median | mean-of-mean | mean-of-median | median-of-mean | median-of-median
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
    