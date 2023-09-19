"""
Generated class for RequestGroup. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Age import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Meta import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase


@dataclass
class RequestGroup(ModelBase):
    """ A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
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
    :param Reference subject: Who the request group is about
    :param Reference encounter: Created as part of
    :param str authoredOn: When the request group was authored
    :param Reference author: Device or practitioner that authored the request group
    :param CodeableConcept reasonCode: Why the request group is needed
    :param Reference reasonReference: Why the request group is needed
    :param Annotation note: Additional notes about the response
    :param BackboneElement action: Proposed actions, if any
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str prefix: User-visible prefix for the action (e.g. 1. or A.)
    :param str title: User-visible title
    :param str description: Short description of the action
    :param str textEquivalent: Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept code: Code representing the meaning of the action or sub-actions
    :param RelatedArtifact documentation: Supporting documentation for the intended performer of the action
    :param BackboneElement condition: Whether or not the action is applicable
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str kind: applicability | start | stop
    :param Expression expression: Boolean-valued expression
    :param BackboneElement relatedAction: Relationship to another action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str actionId: What action this is related to
    :param str relationship: before-start | before | before-end | concurrent-with-start | concurrent | concurrent-with-end | after-start | after | after-end
    :param Duration offsetDuration: Time offset for the relationship
    :param Range offsetDuration: Time offset for the relationship
    :param str timingdateTime: When the action should take place
    :param Age timingdateTime: When the action should take place
    :param Period timingdateTime: When the action should take place
    :param Duration timingdateTime: When the action should take place
    :param Range timingdateTime: When the action should take place
    :param Timing timingdateTime: When the action should take place
    :param Reference participant: Who should perform the action
    :param CodeableConcept type: create | update | remove | fire-event
    :param str groupingBehavior: visual-group | logical-group | sentence-group
    :param str selectionBehavior: any | all | all-or-none | exactly-one | at-most-one | one-or-more
    :param str requiredBehavior: must | could | must-unless-documented
    :param str precheckBehavior: yes | no
    :param str cardinalityBehavior: single | multiple
    :param Reference resource: The target of the action
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
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    note: "Annotation" = None
    
    action: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    prefix: str = None
    
    title: str = None
    
    description: str = None
    
    textEquivalent: str = None
    
    priority: str = None
    
    code: "CodeableConcept" = None
    
    documentation: "RelatedArtifact" = None
    
    condition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    kind: str = None
    
    expression: "Expression" = None
    
    relatedAction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    actionId: str = None
    
    relationship: str = None
    
    offsetDuration: "Duration" = None
    
    offsetDuration: "Range" = None
    
    timingdateTime: str = None
    
    timingdateTime: "Age" = None
    
    timingdateTime: "Period" = None
    
    timingdateTime: "Duration" = None
    
    timingdateTime: "Range" = None
    
    timingdateTime: "Timing" = None
    
    participant: "Reference" = None
    
    type: "CodeableConcept" = None
    
    groupingBehavior: str = None
    
    selectionBehavior: str = None
    
    requiredBehavior: str = None
    
    precheckBehavior: str = None
    
    cardinalityBehavior: str = None
    
    resource: "Reference" = None
    
    action: "BackboneElement" = None
    