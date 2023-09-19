"""
Generated class for RequestOrchestration. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Age import *
from fhan.models.R5.Expression import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.DataRequirement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *


@dataclass
class RequestOrchestration:
    """ A set of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfills plan, proposal, or order
    :param Reference replaces: Request(s) replaced by this request
    :param Identifier groupIdentifier: Composite request this is part of
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept code: What's being requested/ordered
    :param Reference subject: Who the request orchestration is about
    :param Reference encounter: Created as part of
    :param str authoredOn: When the request orchestration was authored
    :param Reference author: Device or practitioner that authored the request orchestration
    :param CodeableReference reason: Why the request orchestration is needed
    :param Reference goal: What goals
    :param Annotation note: Additional notes about the response
    :param BackboneElement action: Proposed actions, if any
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific item from the PlanDefinition
    :param str prefix: User-visible prefix for the action (e.g. 1. or A.)
    :param str title: User-visible title
    :param str description: Short description of the action
    :param str textEquivalent: Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept code: Code representing the meaning of the action or sub-actions
    :param RelatedArtifact documentation: Supporting documentation for the intended performer of the action
    :param Reference goal: What goals
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
    :param str targetId: What action this is related to
    :param str relationship: before | before-start | before-end | concurrent | concurrent-with-start | concurrent-with-end | after | after-start | after-end
    :param str endRelationship: before | before-start | before-end | concurrent | concurrent-with-start | concurrent-with-end | after | after-start | after-end
    :param Duration offsetDuration: Time offset for the relationship
    :param Range offsetDuration: Time offset for the relationship
    :param str timingdateTime: When the action should take place
    :param Age timingdateTime: When the action should take place
    :param Period timingdateTime: When the action should take place
    :param Duration timingdateTime: When the action should take place
    :param Range timingdateTime: When the action should take place
    :param Timing timingdateTime: When the action should take place
    :param CodeableReference location: Where it should happen
    :param BackboneElement participant: Who should perform the action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: careteam | device | group | healthcareservice | location | organization | patient | practitioner | practitionerrole | relatedperson
    :param str typeCanonical: Who or what can participate
    :param Reference typeReference: Who or what can participate
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent, etc
    :param CodeableConcept function: E.g. Author, Reviewer, Witness, etc
    :param str actorcanonical: Who/what is participating?
    :param Reference actorcanonical: Who/what is participating?
    :param CodeableConcept type: create | update | remove | fire-event
    :param str groupingBehavior: visual-group | logical-group | sentence-group
    :param str selectionBehavior: any | all | all-or-none | exactly-one | at-most-one | one-or-more
    :param str requiredBehavior: must | could | must-unless-documented
    :param str precheckBehavior: yes | no
    :param str cardinalityBehavior: single | multiple
    :param Reference resource: The target of the action
    :param str definitioncanonical: Description of the activity to be performed
    :param str definitioncanonical: Description of the activity to be performed
    :param str transform: Transform to apply the template
    :param BackboneElement dynamicValue: Dynamic aspects of the definition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: The path to the element to be set dynamically
    :param Expression expression: An expression that provides the dynamic value for the customization
    :param BackboneElement action: Proposed actions, if any
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    replaces: "Reference" = None
    
    groupIdentifier: "Identifier" = None
    
    status: str = None
    
    intent: str = None
    
    priority: str = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    authoredOn: str = None
    
    author: "Reference" = None
    
    reason: "CodeableReference" = None
    
    goal: "Reference" = None
    
    note: "Annotation" = None
    
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
    
    documentation: "RelatedArtifact" = None
    
    goal: "Reference" = None
    
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
    
    timingdateTime: str = None
    
    timingdateTime: "Age" = None
    
    timingdateTime: "Period" = None
    
    timingdateTime: "Duration" = None
    
    timingdateTime: "Range" = None
    
    timingdateTime: "Timing" = None
    
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
    
    actorcanonical: str = None
    
    actorcanonical: "Reference" = None
    
    type: "CodeableConcept" = None
    
    groupingBehavior: str = None
    
    selectionBehavior: str = None
    
    requiredBehavior: str = None
    
    precheckBehavior: str = None
    
    cardinalityBehavior: str = None
    
    resource: "Reference" = None
    
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
    