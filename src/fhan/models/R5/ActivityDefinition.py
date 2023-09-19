"""
Generated class for ActivityDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Range import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Dosage import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Expression import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Age import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *


@dataclass
class ActivityDefinition:
    """ This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this activity definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the activity definition
    :param str version: Business version of the activity definition
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this activity definition (computer friendly)
    :param str title: Name for this activity definition (human friendly)
    :param str subtitle: Subordinate title of the activity definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: Type of individual the activity definition is intended for
    :param Reference subjectCodeableConcept: Type of individual the activity definition is intended for
    :param str subjectCodeableConcept: Type of individual the activity definition is intended for
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the activity definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for activity definition (if applicable)
    :param str purpose: Why this activity definition is defined
    :param str usage: Describes the clinical usage of the activity definition
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the activity definition was approved by publisher
    :param str lastReviewDate: When the activity definition was last reviewed by the publisher
    :param Period effectivePeriod: When the activity definition is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param str library: Logic used by the activity definition
    :param str kind: Kind of resource
    :param str profile: What profile the resource needs to conform to
    :param CodeableConcept code: Detail type of activity
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if the activity should not be performed
    :param Timing timingTiming: When activity is to occur
    :param Age timingTiming: When activity is to occur
    :param Range timingTiming: When activity is to occur
    :param Duration timingTiming: When activity is to occur
    :param bool asNeededboolean: Preconditions for service
    :param CodeableConcept asNeededboolean: Preconditions for service
    :param CodeableReference location: Where it should happen
    :param BackboneElement participant: Who should participate in the action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: careteam | device | group | healthcareservice | location | organization | patient | practitioner | practitionerrole | relatedperson
    :param str typeCanonical: Who or what can participate
    :param Reference typeReference: Who or what can participate
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent, etc
    :param CodeableConcept function: E.g. Author, Reviewer, Witness, etc
    :param Reference productReference: What's administered/supplied
    :param CodeableConcept productReference: What's administered/supplied
    :param Quantity quantity: How much is administered/consumed/supplied
    :param Dosage dosage: Detailed dosage instructions
    :param CodeableConcept bodySite: What part of body to perform on
    :param str specimenRequirement: What specimens are required to perform this action
    :param str observationRequirement: What observations are required to perform this action
    :param str observationResultRequirement: What observations must be produced by this action
    :param str transform: Transform to apply the template
    :param BackboneElement dynamicValue: Dynamic aspects of the definition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: The path to the element to be set dynamically
    :param Expression expression: An expression that provides the dynamic value for the customization
    
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
    
    kind: str = None
    
    profile: str = None
    
    code: "CodeableConcept" = None
    
    intent: str = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    timingTiming: "Timing" = None
    
    timingTiming: "Age" = None
    
    timingTiming: "Range" = None
    
    timingTiming: "Duration" = None
    
    asNeededboolean: bool = None
    
    asNeededboolean: "CodeableConcept" = None
    
    location: "CodeableReference" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    typeCanonical: str = None
    
    typeReference: "Reference" = None
    
    role: "CodeableConcept" = None
    
    function: "CodeableConcept" = None
    
    productReference: "Reference" = None
    
    productReference: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    dosage: "Dosage" = None
    
    bodySite: "CodeableConcept" = None
    
    specimenRequirement: str = None
    
    observationRequirement: str = None
    
    observationResultRequirement: str = None
    
    transform: str = None
    
    dynamicValue: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    path: str = None
    
    expression: "Expression" = None
    