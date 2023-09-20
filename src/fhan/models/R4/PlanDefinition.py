"""
Generated class for PlanDefinition. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.Age import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Meta import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Expression import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Element import *
from fhan.models.R4.Range import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class Target(Element):
    """ Indicates what should be done and within what timeframe.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept measure: The parameter whose value is to be tracked
    :param Quantity detailQuantity: The target value to be achieved
    :param Duration due: Reach goal within
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    measure: "CodeableConcept" = None
    detailQuantity: "Quantity" = None
    due: "Duration" = None
    

  
    
    
@dataclass
class Goal(Element):
    """ Goals that describe what the activities within the plan are intended to achieve. For example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: E.g. Treatment, dietary, behavioral
    :param CodeableConcept description: Code or text describing the goal
    :param CodeableConcept priority: high-priority | medium-priority | low-priority
    :param CodeableConcept start: When goal pursuit begins
    :param CodeableConcept addresses: What does the goal address
    :param RelatedArtifact documentation: Supporting documentation for the goal
    :param Target target: Target outcome for the goal
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    category: "CodeableConcept" = None
    description: "CodeableConcept" = None
    priority: "CodeableConcept" = None
    start: "CodeableConcept" = None
    addresses: list[CodeableConcept] = None
    documentation: list[RelatedArtifact] = None
    target: list[Target] = None
    

    
        
    
    
@dataclass
class Condition(Element):
    """ An expression that describes applicability criteria or start/stop conditions for the action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str kind: applicability | start | stop
    :param Expression expression: Boolean-valued expression
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    kind: str = None
    expression: "Expression" = None
    

    
    
@dataclass
class RelatedAction(Element):
    """ A relationship to another action such as "before" or "30-60 minutes after start of".:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str actionId: What action is this related to
    :param str relationship: before-start | before | before-end | concurrent-with-start | concurrent | concurrent-with-end | after-start | after | after-end
    :param Duration offsetDuration: Time offset for the relationship
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    actionId: str = None
    
    relationship: str = None
    offsetDuration: "Duration" = None
    

    
    
@dataclass
class Participant(Element):
    """ Indicates who should participate in performing the action described.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: patient | practitioner | related-person | device
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    type: str = None
    role: "CodeableConcept" = None
    

    
    
@dataclass
class DynamicValue(Element):
    """ Customizations that should be applied to the statically defined resource. For example, if the dosage of a medication must be computed based on the patient's weight, a customization would be used to specify an expression that calculated the weight, and the path on the resource that would contain the result.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: The path to the element to be set dynamically
    :param Expression expression: An expression that provides the dynamic value for the customization
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    path: str = None
    expression: "Expression" = None
    

  
    
    
@dataclass
class Action(Element):
    """ An action or group of actions to be taken as part of the plan.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
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
    :param TriggerDefinition trigger: When the action should be triggered
    :param Condition condition: Whether or not the action is applicable
    :param DataRequirement input: Input data requirements
    :param DataRequirement output: Output data definition
    :param RelatedAction relatedAction: Relationship to another action
    :param str timingDateTime: When the action should take place
    :param Participant participant: Who should participate in the action
    :param CodeableConcept type: create | update | remove | fire-event
    :param str groupingBehavior: visual-group | logical-group | sentence-group
    :param str selectionBehavior: any | all | all-or-none | exactly-one | at-most-one | one-or-more
    :param str requiredBehavior: must | could | must-unless-documented
    :param str precheckBehavior: yes | no
    :param str cardinalityBehavior: single | multiple
    :param str definitionCanonical: Description of the activity to be performed
    :param str transform: Transform to apply the template
    :param DynamicValue dynamicValue: Dynamic aspects of the definition
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    prefix: str = None
    
    title: str = None
    
    description: str = None
    
    textEquivalent: str = None
    
    priority: str = None
    code: list[CodeableConcept] = None
    reason: list[CodeableConcept] = None
    documentation: list[RelatedArtifact] = None
    
    goalId: str = None
    subjectCodeableConcept: "CodeableConcept" = None
    trigger: list[TriggerDefinition] = None
    condition: list[Condition] = None
    input: list[DataRequirement] = None
    output: list[DataRequirement] = None
    relatedAction: list[RelatedAction] = None
    
    timingDateTime: str = None
    participant: list[Participant] = None
    type: "CodeableConcept" = None
    
    groupingBehavior: str = None
    
    selectionBehavior: str = None
    
    requiredBehavior: str = None
    
    precheckBehavior: str = None
    
    cardinalityBehavior: str = None
    
    definitionCanonical: str = None
    
    transform: str = None
    dynamicValue: list[DynamicValue] = None
    

@dataclass
class PlanDefinition(ModelBase):
    """ Enforces the minimum information set for the plan definition metadata required by HL7 and other organizations that share and publish plan definitions
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this plan definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the plan definition
    :param str version: Business version of the plan definition
    :param str name: Name for this plan definition (computer friendly)
    :param str title: Name for this plan definition (human friendly)
    :param str subtitle: Subordinate title of the plan definition
    :param CodeableConcept type: order-set | clinical-protocol | eca-rule | workflow-definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: Type of individual the plan definition is focused on
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the plan definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for plan definition (if applicable)
    :param str purpose: Why this plan definition is defined
    :param str usage: Describes the clinical usage of the plan
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the plan definition was approved by publisher
    :param str lastReviewDate: When the plan definition was last reviewed
    :param Period effectivePeriod: When the plan definition is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations
    :param str library: Logic used by the plan definition
    :param Goal goal: What the plan is trying to accomplish
    :param Action action: Action defined by the plan
    """

    resourceType: str = "PlanDefinition"
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
    
    type: "CodeableConcept" = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
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
    
    goal: list["Goal"] = None
    
    action: list["Action"] = None
    