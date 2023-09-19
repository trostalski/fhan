"""
Generated class for Evidence. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class Evidence:
    """ The Evidence Resource provides a machine-interpretable expression of an evidence concept including the evidence variables (e.g., population, exposures/interventions, comparators, outcomes, measured variables, confounding variables), the statistics, and the certainty of this evidence.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this evidence, represented as a globally unique URI
    :param Identifier identifier: Additional identifier for the summary
    :param str version: Business version of this summary
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this summary (machine friendly)
    :param str title: Name for this summary (human friendly)
    :param Reference citeAsReference: Citation for this evidence
    :param str citeAsReference: Citation for this evidence
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str approvalDate: When the summary was approved by publisher
    :param str lastReviewDate: When the summary was last reviewed by the publisher
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param UsageContext useContext: The context that the content is intended to support
    :param str purpose: Why this Evidence is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param RelatedArtifact relatedArtifact: Link or citation to artifact associated with the summary
    :param str description: Description of the particular summary
    :param str assertion: Declarative description of the Evidence
    :param Annotation note: Footnotes and/or explanatory notes
    :param BackboneElement variableDefinition: Evidence variable such as population, exposure, or outcome
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: A text description or summary of the variable
    :param Annotation note: Footnotes and/or explanatory notes
    :param CodeableConcept variableRole: population | subpopulation | exposure | referenceExposure | measuredVariable | confounder
    :param Reference observed: Definition of the actual variable related to the statistic(s)
    :param Reference intended: Definition of the intended variable related to the Evidence
    :param CodeableConcept directnessMatch: low | moderate | high | exact
    :param CodeableConcept synthesisType: The method to combine studies
    :param CodeableConcept studyDesign: The design of the study that produced this evidence
    :param BackboneElement statistic: Values and parameters for a single statistic
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of content
    :param Annotation note: Footnotes and/or explanatory notes
    :param CodeableConcept statisticType: Type of statistic, e.g., relative risk
    :param CodeableConcept category: Associated category for categorical variable
    :param Quantity quantity: Statistic value
    :param int numberOfEvents: The number of events associated with the statistic
    :param int numberAffected: The number of participants affected
    :param BackboneElement sampleSize: Number of samples in the statistic
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of sample size for statistic
    :param Annotation note: Footnote or explanatory note about the sample size
    :param int numberOfStudies: Number of contributing studies
    :param int numberOfParticipants: Cumulative number of participants
    :param int knownDataCount: Number of participants with known results for measured variables
    :param BackboneElement attributeEstimate: An attribute of the Statistic
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of the attribute estimate
    :param Annotation note: Footnote or explanatory note about the estimate
    :param CodeableConcept type: The type of attribute estimate, e.g., confidence interval or p value
    :param Quantity quantity: The singular quantity of the attribute estimate, for attribute estimates represented as single values; also used to report unit of measure
    :param float level: Level of confidence interval, e.g., 0.95 for 95% confidence interval
    :param Range range: Lower and upper bound values of the attribute estimate
    :param BackboneElement attributeEstimate: An attribute of the Statistic
    :param BackboneElement modelCharacteristic: An aspect of the statistical model
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Model specification
    :param Quantity value: Numerical value to complete model specification
    :param BackboneElement variable: A variable adjusted for in the adjusted analysis
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference variableDefinition: Description of the variable
    :param str handling: continuous | dichotomous | ordinal | polychotomous
    :param CodeableConcept valueCategory: Description for grouping of ordinal or polychotomous variables
    :param Quantity valueQuantity: Discrete value for grouping of ordinal or polychotomous variables
    :param Range valueRange: Range of values for grouping of ordinal or polychotomous variables
    :param BackboneElement attributeEstimate: An attribute of the Statistic
    :param BackboneElement certainty: Certainty or quality of the evidence
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of certainty
    :param Annotation note: Footnotes and/or explanatory notes
    :param CodeableConcept type: Aspect of certainty being rated
    :param CodeableConcept rating: Assessment or judgement of the aspect
    :param str rater: Individual or group who did the rating
    :param BackboneElement subcomponent: Certainty or quality of the evidence
    
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
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    citeAsReference: "Reference" = None
    
    citeAsReference: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    useContext: "UsageContext" = None
    
    purpose: str = None
    
    copyright: str = None
    
    copyrightLabel: str = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    description: str = None
    
    assertion: str = None
    
    note: "Annotation" = None
    
    variableDefinition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    variableRole: "CodeableConcept" = None
    
    observed: "Reference" = None
    
    intended: "Reference" = None
    
    directnessMatch: "CodeableConcept" = None
    
    synthesisType: "CodeableConcept" = None
    
    studyDesign: "CodeableConcept" = None
    
    statistic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    statisticType: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    numberOfEvents: int = None
    
    numberAffected: int = None
    
    sampleSize: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    numberOfStudies: int = None
    
    numberOfParticipants: int = None
    
    knownDataCount: int = None
    
    attributeEstimate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    level: float = None
    
    range: "Range" = None
    
    attributeEstimate: "BackboneElement" = None
    
    modelCharacteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    value: "Quantity" = None
    
    variable: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    variableDefinition: "Reference" = None
    
    handling: str = None
    
    valueCategory: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueRange: "Range" = None
    
    attributeEstimate: "BackboneElement" = None
    
    certainty: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    type: "CodeableConcept" = None
    
    rating: "CodeableConcept" = None
    
    rater: str = None
    
    subcomponent: "BackboneElement" = None
    