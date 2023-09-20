"""
Generated class for ActivityDefinition. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.UsageContext import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Resource import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Period import *
from fhan.models.R4.Range import *
from fhan.models.R4.Reference import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Expression import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Age import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase

@dataclass
class participant(Element):
    """ Indicates who should participate in performing the action described.
    :param BackboneElement participant: Who should participate in the action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: patient | practitioner | related-person | device
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent, etc.
    """
    participant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    role: "CodeableConcept" = None
    
@dataclass
class dynamicValue(Element):
    """ Dynamic values that will be evaluated to produce values for elements of the resulting resource. For example, if the dosage of a medication must be computed based on the patient's weight, a dynamic value would be used to specify an expression that calculated the weight, and the path on the request resource that would contain the result.
    :param BackboneElement dynamicValue: Dynamic aspects of the definition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: The path to the element to be set dynamically
    :param Expression expression: An expression that provides the dynamic value for the customization
    """
    dynamicValue: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    path: str = None
    
    expression: "Expression" = None
    


@dataclass
class ActivityDefinition(ModelBase):
    """ Enforces the minimum information set for the activity definition metadata required by HL7 and other organizations that share and publish activity definitions
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
    :param str name: Name for this activity definition (computer friendly)
    :param str title: Name for this activity definition (human friendly)
    :param str subtitle: Subordinate title of the activity definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: Type of individual the activity definition is intended for
    :param Reference subjectCodeableConcept: Type of individual the activity definition is intended for
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the activity definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for activity definition (if applicable)
    :param str purpose: Why this activity definition is defined
    :param str usage: Describes the clinical usage of the activity definition
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the activity definition was approved by publisher
    :param str lastReviewDate: When the activity definition was last reviewed
    :param Period effectivePeriod: When the activity definition is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param str library: Logic used by the activity definition
    :param str kind: Kind of resource
    :param str profile: What profile the resource needs to conform to
    :param CodeableConcept code: Detail type of activity
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if the activity should not be performed
    :param Timing timingTiming: When activity is to occur
    :param str timingTiming: When activity is to occur
    :param Age timingTiming: When activity is to occur
    :param Period timingTiming: When activity is to occur
    :param Range timingTiming: When activity is to occur
    :param Duration timingTiming: When activity is to occur
    :param Reference location: Where it should happen
    :param BackboneElement participant: Who should participate in the action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: patient | practitioner | related-person | device
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent, etc.
    :param Reference productReference: What's administered/supplied
    :param CodeableConcept productReference: What's administered/supplied
    :param Quantity quantity: How much is administered/consumed/supplied
    :param Dosage dosage: Detailed dosage instructions
    :param CodeableConcept bodySite: What part of body to perform on
    :param Reference specimenRequirement: What specimens are required to perform this action
    :param Reference observationRequirement: What observations are required to perform this action
    :param Reference observationResultRequirement: What observations must be produced by this action
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
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    identifier: list["Identifier"] = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    description: str = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    purpose: str = None
    
    usage: str = None
    
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
    
    participant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    role: "CodeableConcept" = None
    
    productReference: "Reference" = None
    
    productReference: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    dosage: list["Dosage"] = None
    
    bodySite: list["CodeableConcept"] = None
    
    specimenRequirement: list["Reference"] = None
    
    observationRequirement: list["Reference"] = None
    
    observationResultRequirement: list["Reference"] = None
    
    transform: str = None
    
    dynamicValue: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    path: str = None
    
    expression: "Expression" = None
    