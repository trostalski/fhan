"""
Generated class for PlanDefinition. 
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
from fhan.models.R5.Ratio import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Expression import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.DataRequirement import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.TriggerDefinition import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Age import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *


@dataclass
class PlanDefinition:
    """ Defines a PlanDefinition that implements the behavior for a CDS Hooks service
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Extension
    :param Extension extension:cdsHooksEndpoint: Service endpoint
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this plan definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the plan definition
    :param str version: Business version of the plan definition
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this plan definition (computer friendly)
    :param str title: Name for this plan definition (human friendly)
    :param str subtitle: Subordinate title of the plan definition
    :param CodeableConcept type: order-set | clinical-protocol | eca-rule | workflow-definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: Type of individual the plan definition is focused on
    :param Reference subjectCodeableConcept: Type of individual the plan definition is focused on
    :param str subjectCodeableConcept: Type of individual the plan definition is focused on
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the plan definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for plan definition (if applicable)
    :param str purpose: Why this plan definition is defined
    :param str usage: Describes the clinical usage of the plan
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the plan definition was approved by publisher
    :param str lastReviewDate: When the plan definition was last reviewed by the publisher
    :param Period effectivePeriod: When the plan definition is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations
    :param str library: Logic used by the plan definition
    :param BackboneElement goal: What the plan is trying to accomplish
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: E.g. Treatment, dietary, behavioral
    :param CodeableConcept description: Code or text describing the goal
    :param CodeableConcept priority: high-priority | medium-priority | low-priority
    :param CodeableConcept start: When goal pursuit begins
    :param CodeableConcept addresses: What does the goal address
    :param RelatedArtifact documentation: Supporting documentation for the goal
    :param BackboneElement target: Target outcome for the goal
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept measure: The parameter whose value is to be tracked
    :param Quantity detailQuantity: The target value to be achieved
    :param Range detailQuantity: The target value to be achieved
    :param CodeableConcept detailQuantity: The target value to be achieved
    :param str detailQuantity: The target value to be achieved
    :param bool detailQuantity: The target value to be achieved
    :param int detailQuantity: The target value to be achieved
    :param Ratio detailQuantity: The target value to be achieved
    :param Duration due: Reach goal within
    :param BackboneElement actor: Actors within the plan
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: User-visible title
    :param str description: Describes the actor
    :param BackboneElement option: Who or what can be this actor
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: careteam | device | group | healthcareservice | location | organization | patient | practitioner | practitionerrole | relatedperson
    :param str typeCanonical: Who or what can participate
    :param Reference typeReference: Who or what can participate
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent
    :param BackboneElement action: Action defined by the plan
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for the action in the PlanDefinition
    :param str prefix: User-visible prefix for the action (e.g. 1. or A.)
    :param str title: User-visible title
    :param str description: Brief description of the action
    :param str textEquivalent: Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept code: Code representing the meaning of the action or sub-actions
    :param CodeableConcept reason: Why the action should be performed
    :param RelatedArtifact documentation: Supporting documentation for the intended performer of the action
    :param str goalId: What goals this action supports
    :param CodeableConcept subjectCodeableConcept: Type of individual the action is focused on
    :param Reference subjectCodeableConcept: Type of individual the action is focused on
    :param str subjectCodeableConcept: Type of individual the action is focused on
    :param TriggerDefinition trigger: When the action should be triggered
    :param BackboneElement condition: Whether or not the action is applicable
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str kind: applicability | start | stop
    :param Expression expression: Boolean-valued expression
    :param BackboneElement input: Input data requirements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: User-visible title
    :param DataRequirement requirement: What data is provided
    :param str relatedData: What data is provided
    :param BackboneElement output: Output data definition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: User-visible title
    :param DataRequirement requirement: What data is provided
    :param str relatedData: What data is provided
    :param BackboneElement relatedAction: Relationship to another action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str targetId: What action is this related to
    :param str relationship: before | before-start | before-end | concurrent | concurrent-with-start | concurrent-with-end | after | after-start | after-end
    :param str endRelationship: before | before-start | before-end | concurrent | concurrent-with-start | concurrent-with-end | after | after-start | after-end
    :param Duration offsetDuration: Time offset for the relationship
    :param Range offsetDuration: Time offset for the relationship
    :param Age timingAge: When the action should take place
    :param Duration timingAge: When the action should take place
    :param Range timingAge: When the action should take place
    :param Timing timingAge: When the action should take place
    :param CodeableReference location: Where it should happen
    :param BackboneElement participant: Who should participate in the action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str actorId: What actor
    :param str type: careteam | device | group | healthcareservice | location | organization | patient | practitioner | practitionerrole | relatedperson
    :param str typeCanonical: Who or what can participate
    :param Reference typeReference: Who or what can participate
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent
    :param CodeableConcept function: E.g. Author, Reviewer, Witness, etc
    :param CodeableConcept type: create | update | remove | fire-event
    :param str groupingBehavior: visual-group | logical-group | sentence-group
    :param str selectionBehavior: any | all | all-or-none | exactly-one | at-most-one | one-or-more
    :param str requiredBehavior: must | could | must-unless-documented
    :param str precheckBehavior: yes | no
    :param str cardinalityBehavior: single | multiple
    :param str definitioncanonical: Description of the activity to be performed
    :param str definitioncanonical: Description of the activity to be performed
    :param str transform: Transform to apply the template
    :param BackboneElement dynamicValue: Dynamic aspects of the definition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: The path to the element to be set dynamically
    :param Expression expression: An expression that provides the dynamic value for the customization
    :param BackboneElement action: Action defined by the plan
    :param bool asNeededboolean: Preconditions for service
    :param CodeableConcept asNeededboolean: Preconditions for service
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    extension:cdsHooksEndpoint: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    type: "CodeableConcept" = None
    
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
    
    goal: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    description: "CodeableConcept" = None
    
    priority: "CodeableConcept" = None
    
    start: "CodeableConcept" = None
    
    addresses: "CodeableConcept" = None
    
    documentation: "RelatedArtifact" = None
    
    target: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    measure: "CodeableConcept" = None
    
    detailQuantity: "Quantity" = None
    
    detailQuantity: "Range" = None
    
    detailQuantity: "CodeableConcept" = None
    
    detailQuantity: str = None
    
    detailQuantity: bool = None
    
    detailQuantity: int = None
    
    detailQuantity: "Ratio" = None
    
    due: "Duration" = None
    
    actor: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    description: str = None
    
    option: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    typeCanonical: str = None
    
    typeReference: "Reference" = None
    
    role: "CodeableConcept" = None
    
    action: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    prefix: str = None
    
    title: str = None
    
    description: str = None
    
    textEquivalent: str = None
    
    priority: str = None
    
    code: "CodeableConcept" = None
    
    reason: "CodeableConcept" = None
    
    documentation: "RelatedArtifact" = None
    
    goalId: str = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    subjectCodeableConcept: str = None
    
    trigger: "TriggerDefinition" = None
    
    condition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    kind: str = None
    
    expression: "Expression" = None
    
    input: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    requirement: "DataRequirement" = None
    
    relatedData: str = None
    
    output: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    requirement: "DataRequirement" = None
    
    relatedData: str = None
    
    relatedAction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    targetId: str = None
    
    relationship: str = None
    
    endRelationship: str = None
    
    offsetDuration: "Duration" = None
    
    offsetDuration: "Range" = None
    
    timingAge: "Age" = None
    
    timingAge: "Duration" = None
    
    timingAge: "Range" = None
    
    timingAge: "Timing" = None
    
    location: "CodeableReference" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    actorId: str = None
    
    type: str = None
    
    typeCanonical: str = None
    
    typeReference: "Reference" = None
    
    role: "CodeableConcept" = None
    
    function: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    groupingBehavior: str = None
    
    selectionBehavior: str = None
    
    requiredBehavior: str = None
    
    precheckBehavior: str = None
    
    cardinalityBehavior: str = None
    
    definitioncanonical: str = None
    
    definitioncanonical: str = None
    
    transform: str = None
    
    dynamicValue: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    path: str = None
    
    expression: "Expression" = None
    
    action: "BackboneElement" = None
    
    asNeededboolean: bool = None
    
    asNeededboolean: "CodeableConcept" = None
    