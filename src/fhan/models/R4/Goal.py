"""
Generated class for Goal. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.generator_models import ModelBase


@dataclass
class Goal(ModelBase):
    """ Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this goal
    :param str lifecycleStatus: proposed | planned | accepted | active | on-hold | completed | cancelled | entered-in-error | rejected
    :param CodeableConcept achievementStatus: in-progress | improving | worsening | no-change | achieved | sustaining | not-achieved | no-progress | not-attainable
    :param CodeableConcept category: E.g. Treatment, dietary, behavioral, etc.
    :param CodeableConcept priority: high-priority | medium-priority | low-priority
    :param CodeableConcept description: Code or text describing goal
    :param Reference subject: Who this goal is intended for
    :param str startdate: When goal pursuit begins
    :param CodeableConcept startdate: When goal pursuit begins
    :param BackboneElement target: Target outcome for the goal
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept measure: The parameter whose value is being tracked
    :param Quantity detailQuantity: The target value to be achieved
    :param Range detailQuantity: The target value to be achieved
    :param CodeableConcept detailQuantity: The target value to be achieved
    :param str detailQuantity: The target value to be achieved
    :param bool detailQuantity: The target value to be achieved
    :param int detailQuantity: The target value to be achieved
    :param Ratio detailQuantity: The target value to be achieved
    :param str duedate: Reach goal on or before
    :param Duration duedate: Reach goal on or before
    :param str statusDate: When goal status took effect
    :param str statusReason: Reason for current status
    :param Reference expressedBy: Who's responsible for creating Goal?
    :param Reference addresses: Issues addressed by this goal
    :param Annotation note: Comments about the goal
    :param CodeableConcept outcomeCode: What result was achieved regarding the goal?
    :param Reference outcomeReference: Observation that resulted from goal
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
    
    lifecycleStatus: str = None
    
    achievementStatus: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    priority: "CodeableConcept" = None
    
    description: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    startdate: str = None
    
    startdate: "CodeableConcept" = None
    
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
    
    duedate: str = None
    
    duedate: "Duration" = None
    
    statusDate: str = None
    
    statusReason: str = None
    
    expressedBy: "Reference" = None
    
    addresses: "Reference" = None
    
    note: "Annotation" = None
    
    outcomeCode: "CodeableConcept" = None
    
    outcomeReference: "Reference" = None
    