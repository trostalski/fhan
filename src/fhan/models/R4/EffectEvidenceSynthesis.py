"""
Generated class for EffectEvidenceSynthesis. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class sampleSize(Element):
    """ A description of the size of the sample involved in the synthesis.
    :param BackboneElement sampleSize: What sample size was involved?
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of sample size
    :param int numberOfStudies: How many studies?
    :param int numberOfParticipants: How many participants?
    """
    sampleSize: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    numberOfStudies: int = None
    
    numberOfParticipants: int = None
    
@dataclass
class resultsByExposure(Element):
    """ A description of the results for each exposure considered in the effect estimate.
    :param BackboneElement resultsByExposure: What was the result per exposure?
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of results by exposure
    :param str exposureState: exposure | exposure-alternative
    :param CodeableConcept variantState: Variant exposure states
    :param Reference riskEvidenceSynthesis: Risk evidence synthesis
    """
    resultsByExposure: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    exposureState: str = None
    
    variantState: "CodeableConcept" = None
    
    riskEvidenceSynthesis: "Reference" = None
    
@dataclass
class effectEstimate(Element):
    """ The estimated effect of the exposure variant.
    :param BackboneElement effectEstimate: What was the estimated effect
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of effect estimate
    :param CodeableConcept type: Type of efffect estimate
    :param CodeableConcept variantState: Variant exposure states
    :param float value: Point estimate
    :param CodeableConcept unitOfMeasure: What unit is the outcome described in?
    :param BackboneElement precisionEstimate: How precise the estimate is
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of precision estimate
    :param float level: Level of confidence interval
    :param float _from: Lower bound
    :param float to: Upper bound
    """
    effectEstimate: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    type: "CodeableConcept" = None
    
    variantState: "CodeableConcept" = None
    
    value: float = None
    
    unitOfMeasure: "CodeableConcept" = None
    
    precisionEstimate: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    level: float = None
    
    _from: float = None
    
    to: float = None
    
@dataclass
class precisionEstimate(Element):
    """ A description of the precision of the estimate for the effect.
    :param BackboneElement precisionEstimate: How precise the estimate is
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of precision estimate
    :param float level: Level of confidence interval
    :param float _from: Lower bound
    :param float to: Upper bound
    """
    precisionEstimate: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    level: float = None
    
    _from: float = None
    
    to: float = None
    
@dataclass
class certainty(Element):
    """ A description of the certainty of the effect estimate.
    :param BackboneElement certainty: How certain is the effect
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
    certainty: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    rating: list["CodeableConcept"] = None
    
    note: list["Annotation"] = None
    
    certaintySubcomponent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    rating: list["CodeableConcept"] = None
    
    note: list["Annotation"] = None
    
@dataclass
class certaintySubcomponent(Element):
    """ A description of a component of the overall certainty.
    :param BackboneElement certaintySubcomponent: A component that contributes to the overall certainty
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of subcomponent of certainty rating
    :param CodeableConcept rating: Subcomponent certainty rating
    :param Annotation note: Used for footnotes or explanatory notes
    """
    certaintySubcomponent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    rating: list["CodeableConcept"] = None
    
    note: list["Annotation"] = None
    


@dataclass
class EffectEvidenceSynthesis(ModelBase):
    """ The EffectEvidenceSynthesis resource describes the difference in an outcome between exposures states in a population where the effect estimate is derived from a combination of research studies.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this effect evidence synthesis, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the effect evidence synthesis
    :param str version: Business version of the effect evidence synthesis
    :param str name: Name for this effect evidence synthesis (computer friendly)
    :param str title: Name for this effect evidence synthesis (human friendly)
    :param str status: draft | active | retired | unknown
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the effect evidence synthesis
    :param Annotation note: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for effect evidence synthesis (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the effect evidence synthesis was approved by publisher
    :param str lastReviewDate: When the effect evidence synthesis was last reviewed
    :param Period effectivePeriod: When the effect evidence synthesis is expected to be used
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
    :param Reference exposureAlternative: What comparison exposure?
    :param Reference outcome: What outcome?
    :param BackboneElement sampleSize: What sample size was involved?
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of sample size
    :param int numberOfStudies: How many studies?
    :param int numberOfParticipants: How many participants?
    :param BackboneElement resultsByExposure: What was the result per exposure?
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of results by exposure
    :param str exposureState: exposure | exposure-alternative
    :param CodeableConcept variantState: Variant exposure states
    :param Reference riskEvidenceSynthesis: Risk evidence synthesis
    :param BackboneElement effectEstimate: What was the estimated effect
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of effect estimate
    :param CodeableConcept type: Type of efffect estimate
    :param CodeableConcept variantState: Variant exposure states
    :param float value: Point estimate
    :param CodeableConcept unitOfMeasure: What unit is the outcome described in?
    :param BackboneElement precisionEstimate: How precise the estimate is
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of precision estimate
    :param float level: Level of confidence interval
    :param float _from: Lower bound
    :param float to: Upper bound
    :param BackboneElement certainty: How certain is the effect
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
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    identifier: list["Identifier"] = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    description: str = None
    
    note: list["Annotation"] = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    topic: list["CodeableConcept"] = None
    
    author: list["ContactDetail"] = None
    
    editor: list["ContactDetail"] = None
    
    reviewer: list["ContactDetail"] = None
    
    endorser: list["ContactDetail"] = None
    
    relatedArtifact: list["RelatedArtifact"] = None
    
    synthesisType: "CodeableConcept" = None
    
    studyType: "CodeableConcept" = None
    
    population: "Reference" = None
    
    exposure: "Reference" = None
    
    exposureAlternative: "Reference" = None
    
    outcome: "Reference" = None
    
    sampleSize: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    numberOfStudies: int = None
    
    numberOfParticipants: int = None
    
    resultsByExposure: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    exposureState: str = None
    
    variantState: "CodeableConcept" = None
    
    riskEvidenceSynthesis: "Reference" = None
    
    effectEstimate: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    type: "CodeableConcept" = None
    
    variantState: "CodeableConcept" = None
    
    value: float = None
    
    unitOfMeasure: "CodeableConcept" = None
    
    precisionEstimate: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    level: float = None
    
    _from: float = None
    
    to: float = None
    
    certainty: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    rating: list["CodeableConcept"] = None
    
    note: list["Annotation"] = None
    
    certaintySubcomponent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    rating: list["CodeableConcept"] = None
    
    note: list["Annotation"] = None
    