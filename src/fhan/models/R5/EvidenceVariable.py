"""
Generated class for EvidenceVariable. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Expression import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class EvidenceVariable:
    """ The EvidenceVariable resource describes an element that knowledge (Evidence) is about.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this evidence variable, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the evidence variable
    :param str version: Business version of the evidence variable
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this evidence variable (computer friendly)
    :param str title: Name for this evidence variable (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the evidence variable
    :param Annotation note: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param str purpose: Why this EvidenceVariable is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the resource was approved by publisher
    :param str lastReviewDate: When the resource was last reviewed by the publisher
    :param Period effectivePeriod: When the resource is expected to be used
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param bool actual: Actual or conceptual
    :param BackboneElement characteristic: A defining factor of the EvidenceVariable
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Label for internal linking
    :param str description: Natural language description of the characteristic
    :param Annotation note: Used for footnotes or explanatory notes
    :param bool exclude: Whether the characteristic is an inclusion criterion or exclusion criterion
    :param Reference definitionReference: Defines the characteristic (without using type and value) by a Reference
    :param str definitionCanonical: Defines the characteristic (without using type and value) by a Canonical
    :param CodeableConcept definitionCodeableConcept: Defines the characteristic (without using type and value) by a CodeableConcept
    :param Expression definitionExpression: Defines the characteristic (without using type and value) by an expression
    :param str definitionId: Defines the characteristic (without using type and value) by an id
    :param BackboneElement definitionByTypeAndValue: Defines the characteristic using type and value
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Expresses the type of characteristic
    :param CodeableConcept method: Method for how the characteristic value was determined
    :param Reference device: Device used for determining characteristic
    :param CodeableConcept valueCodeableConcept: Defines the characteristic when coupled with characteristic.type
    :param bool valueCodeableConcept: Defines the characteristic when coupled with characteristic.type
    :param Quantity valueCodeableConcept: Defines the characteristic when coupled with characteristic.type
    :param Range valueCodeableConcept: Defines the characteristic when coupled with characteristic.type
    :param Reference valueCodeableConcept: Defines the characteristic when coupled with characteristic.type
    :param str valueCodeableConcept: Defines the characteristic when coupled with characteristic.type
    :param CodeableConcept offset: Reference point for valueQuantity or valueRange
    :param BackboneElement definitionByCombination: Used to specify how two or more characteristics are combined
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: all-of | any-of | at-least | at-most | statistical | net-effect | dataset
    :param int threshold: Provides the value of "n" when "at-least" or "at-most" codes are used
    :param BackboneElement characteristic: A defining factor of the EvidenceVariable
    :param Quantity instancesQuantity: Number of occurrences meeting the characteristic
    :param Range instancesQuantity: Number of occurrences meeting the characteristic
    :param Quantity durationQuantity: Length of time in which the characteristic is met
    :param Range durationQuantity: Length of time in which the characteristic is met
    :param BackboneElement timeFromEvent: Timing in which the characteristic is determined
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Human readable description
    :param Annotation note: Used for footnotes or explanatory notes
    :param CodeableConcept eventCodeableConcept: The event used as a base point (reference point) in time
    :param Reference eventCodeableConcept: The event used as a base point (reference point) in time
    :param str eventCodeableConcept: The event used as a base point (reference point) in time
    :param str eventCodeableConcept: The event used as a base point (reference point) in time
    :param Quantity quantity: Used to express the observation at a defined amount of time before or after the event
    :param Range range: Used to express the observation within a period before and/or after the event
    :param str handling: continuous | dichotomous | ordinal | polychotomous
    :param BackboneElement category: A grouping for ordinal or polychotomous variables
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Description of the grouping
    :param CodeableConcept valueCodeableConcept: Definition of the grouping
    :param Quantity valueCodeableConcept: Definition of the grouping
    :param Range valueCodeableConcept: Definition of the grouping
    
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
    
    shortTitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    useContext: "UsageContext" = None
    
    purpose: str = None
    
    copyright: str = None
    
    copyrightLabel: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    actual: bool = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    description: str = None
    
    note: "Annotation" = None
    
    exclude: bool = None
    
    definitionReference: "Reference" = None
    
    definitionCanonical: str = None
    
    definitionCodeableConcept: "CodeableConcept" = None
    
    definitionExpression: "Expression" = None
    
    definitionId: str = None
    
    definitionByTypeAndValue: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    method: "CodeableConcept" = None
    
    device: "Reference" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: "Range" = None
    
    valueCodeableConcept: "Reference" = None
    
    valueCodeableConcept: str = None
    
    offset: "CodeableConcept" = None
    
    definitionByCombination: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    threshold: int = None
    
    characteristic: "BackboneElement" = None
    
    instancesQuantity: "Quantity" = None
    
    instancesQuantity: "Range" = None
    
    durationQuantity: "Quantity" = None
    
    durationQuantity: "Range" = None
    
    timeFromEvent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    eventCodeableConcept: "CodeableConcept" = None
    
    eventCodeableConcept: "Reference" = None
    
    eventCodeableConcept: str = None
    
    eventCodeableConcept: str = None
    
    quantity: "Quantity" = None
    
    range: "Range" = None
    
    handling: str = None
    
    category: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: "Range" = None
    