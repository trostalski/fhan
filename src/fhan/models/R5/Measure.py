"""
Generated class for Measure. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Expression import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Measure:
    """ Enforces the minimum information set for the measure metadata required by HL7 and other organizations that share and publish measures
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Extension
    :param Extension extension:knowledgeCapability: shareable | computable | publishable | executable
    :param Extension extension:knowledgeRepresentationLevel: narrative | semi-structured | structured | executable
    :param Extension extension:artifactComment: Additional documentation, review, or usage guidance
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this measure, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the measure
    :param str version: Business version of the measure
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this measure (computer friendly)
    :param str title: Name for this measure (human friendly)
    :param str subtitle: Subordinate title of the measure
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param Reference subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str basis: Population basis
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the measure
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for measure (if applicable)
    :param str purpose: Why this measure is defined
    :param str usage: Describes the clinical usage of the measure
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the measure was approved by publisher
    :param str lastReviewDate: When the measure was last reviewed by the publisher
    :param Period effectivePeriod: When the measure is expected to be used
    :param CodeableConcept topic: The category of the measure, such as Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param str library: Logic used by the measure
    :param str disclaimer: Disclaimer for use of the measure or its referenced content
    :param CodeableConcept scoring: proportion | ratio | continuous-variable | cohort
    :param CodeableConcept scoringUnit: What units?
    :param CodeableConcept compositeScoring: opportunity | all-or-nothing | linear | weighted
    :param CodeableConcept type: process | outcome | structure | patient-reported-outcome | composite
    :param str riskAdjustment: How risk adjustment is applied for this measure
    :param str rateAggregation: How is rate aggregation performed for this measure
    :param str rationale: Detailed description of why the measure exists
    :param str clinicalRecommendationStatement: Summary of clinical guidelines
    :param CodeableConcept improvementNotation: increase | decrease
    :param BackboneElement term: Defined terms used in the measure documentation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: What term?
    :param str definition: Meaning of the term
    :param str guidance: Additional guidance for implementers (deprecated)
    :param BackboneElement group: Population criteria group
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for group in measure
    :param CodeableConcept code: Meaning of the group
    :param str description: Summary description
    :param CodeableConcept type: process | outcome | structure | patient-reported-outcome | composite
    :param CodeableConcept subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param Reference subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str basis: Population basis
    :param CodeableConcept scoring: proportion | ratio | continuous-variable | cohort
    :param CodeableConcept scoringUnit: What units?
    :param str rateAggregation: How is rate aggregation performed for this measure
    :param CodeableConcept improvementNotation: increase | decrease
    :param str library: Logic used by the measure group
    :param BackboneElement population: Population criteria
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for population in measure
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param str description: The human readable description of this population criteria
    :param Expression criteria: The criteria that defines this population
    :param Reference groupDefinition: A group resource that defines this population
    :param str inputPopulationId: Which population
    :param CodeableConcept aggregateMethod: Aggregation method for a measure score (e.g. sum, average, median, minimum, maximum, count)
    :param BackboneElement stratifier: Stratifier criteria for the measure
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for stratifier in measure
    :param CodeableConcept code: Meaning of the stratifier
    :param str description: The human readable description of this stratifier
    :param Expression criteria: How the measure should be stratified
    :param Reference groupDefinition: A group resource that defines this population
    :param BackboneElement component: Stratifier criteria component for the measure
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for stratifier component in measure
    :param CodeableConcept code: Meaning of the stratifier component
    :param str description: The human readable description of this stratifier component
    :param Expression criteria: Component of how the measure should be stratified
    :param Reference groupDefinition: A group resource that defines this population
    :param BackboneElement supplementalData: What other data should be reported with the measure
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for supplementalData in measure
    :param CodeableConcept code: Meaning of the supplemental data
    :param CodeableConcept usage: supplemental-data | risk-adjustment-factor
    :param str description: The human readable description of this supplemental data
    :param Expression criteria: Expression describing additional data to be reported
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    extension:knowledgeCapability: "Extension" = None
    
    extension:knowledgeRepresentationLevel: "Extension" = None
    
    extension:artifactComment: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    basis: str = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    usage: str = None
    
    copyright: str = None
    
    copyrightLabel: str = None
    
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
    
    disclaimer: str = None
    
    scoring: "CodeableConcept" = None
    
    scoringUnit: "CodeableConcept" = None
    
    compositeScoring: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    riskAdjustment: str = None
    
    rateAggregation: str = None
    
    rationale: str = None
    
    clinicalRecommendationStatement: str = None
    
    improvementNotation: "CodeableConcept" = None
    
    term: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    definition: str = None
    
    guidance: str = None
    
    group: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    description: str = None
    
    type: "CodeableConcept" = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    basis: str = None
    
    scoring: "CodeableConcept" = None
    
    scoringUnit: "CodeableConcept" = None
    
    rateAggregation: str = None
    
    improvementNotation: "CodeableConcept" = None
    
    library: str = None
    
    population: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    description: str = None
    
    criteria: "Expression" = None
    
    groupDefinition: "Reference" = None
    
    inputPopulationId: str = None
    
    aggregateMethod: "CodeableConcept" = None
    
    stratifier: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    description: str = None
    
    criteria: "Expression" = None
    
    groupDefinition: "Reference" = None
    
    component: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    description: str = None
    
    criteria: "Expression" = None
    
    groupDefinition: "Reference" = None
    
    supplementalData: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    usage: "CodeableConcept" = None
    
    description: str = None
    
    criteria: "Expression" = None
    