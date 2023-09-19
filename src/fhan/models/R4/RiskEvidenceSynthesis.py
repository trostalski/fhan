"""
Generated class for RiskEvidenceSynthesis. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class RiskEvidenceSynthesis(ModelBase):
    """ The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state where the risk estimate is derived from a combination of research studies.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this risk evidence synthesis, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the risk evidence synthesis
    :param str version: Business version of the risk evidence synthesis
    :param str name: Name for this risk evidence synthesis (computer friendly)
    :param str title: Name for this risk evidence synthesis (human friendly)
    :param str status: draft | active | retired | unknown
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the risk evidence synthesis
    :param Annotation note: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for risk evidence synthesis (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the risk evidence synthesis was approved by publisher
    :param str lastReviewDate: When the risk evidence synthesis was last reviewed
    :param Period effectivePeriod: When the risk evidence synthesis is expected to be used
    :param CodeableConcept topic: The category of the EffectEvidenceSynthesis, such as Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param CodeableConcept synthesisType: Type of synthesis
    :param CodeableConcept studyType: Type of study
    :param Reference population: What population?
    :param Reference exposure: What exposure?
    :param Reference outcome: What outcome?
    :param BackboneElement sampleSize: What sample size was involved?
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of sample size
    :param int numberOfStudies: How many studies?
    :param int numberOfParticipants: How many participants?
    :param BackboneElement riskEstimate: What was the estimated risk
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of risk estimate
    :param CodeableConcept type: Type of risk estimate
    :param float value: Point estimate
    :param CodeableConcept unitOfMeasure: What unit is the outcome described in?
    :param int denominatorCount: Sample size for group measured
    :param int numeratorCount: Number with the outcome
    :param BackboneElement precisionEstimate: How precise the estimate is
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of precision estimate
    :param float level: Level of confidence interval
    :param float _from: Lower bound
    :param float to: Upper bound
    :param BackboneElement certainty: How certain is the risk
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept rating: Certainty rating
    :param Annotation note: Used for footnotes or explanatory notes
    :param BackboneElement certaintySubcomponent: A component that contributes to the overall certainty
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of subcomponent of certainty rating
    :param CodeableConcept rating: Subcomponent certainty rating
    :param Annotation note: Used for footnotes or explanatory notes
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
    
    status: str = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
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
    
    synthesisType: "CodeableConcept" = None
    
    studyType: "CodeableConcept" = None
    
    population: "Reference" = None
    
    exposure: "Reference" = None
    
    outcome: "Reference" = None
    
    sampleSize: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    numberOfStudies: int = None
    
    numberOfParticipants: int = None
    
    riskEstimate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    type: "CodeableConcept" = None
    
    value: float = None
    
    unitOfMeasure: "CodeableConcept" = None
    
    denominatorCount: int = None
    
    numeratorCount: int = None
    
    precisionEstimate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    level: float = None
    
    _from: float = None
    
    to: float = None
    
    certainty: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    rating: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    certaintySubcomponent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    rating: "CodeableConcept" = None
    
    note: "Annotation" = None
    