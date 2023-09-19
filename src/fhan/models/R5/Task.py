"""
Generated class for Task. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Money import *
from fhan.models.R5.Address import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Distance import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Range import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Signature import *
from fhan.models.R5.Dosage import *
from fhan.models.R5.Availability import *
from fhan.models.R5.Count import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.HumanName import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Expression import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.DataRequirement import *
from fhan.models.R5.SampledData import *
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.TriggerDefinition import *
from fhan.models.R5.RatioRange import *
from fhan.models.R5.ParameterDefinition import *
from fhan.models.R5.Age import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *


@dataclass
class Task:
    """ A task to be performed.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Task Instance Identifier
    :param str instantiatesCanonical: Formal definition of task
    :param str instantiatesUri: Formal definition of task
    :param Reference basedOn: Request fulfilled by this task
    :param Identifier groupIdentifier: Requisition or grouper id
    :param Reference partOf: Composite task
    :param str status: draft | requested | received | accepted | +
    :param CodeableReference statusReason: Reason for current status
    :param CodeableConcept businessStatus: E.g. "Specimen collected", "IV prepped"
    :param str intent: unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if Task is prohibiting action
    :param CodeableConcept code: Task Type
    :param str description: Human-readable explanation of task
    :param Reference focus: What task is acting on
    :param Reference for: Beneficiary of the Task
    :param Reference encounter: Healthcare event during which this task originated
    :param Period requestedPeriod: When the task should be performed
    :param Period executionPeriod: Start and end time of execution
    :param str authoredOn: Task Creation Date
    :param str lastModified: Task Last Modified Date
    :param Reference requester: Who is asking for task to be done
    :param CodeableReference requestedPerformer: Who should perform Task
    :param Reference owner: Responsible individual
    :param BackboneElement performer: Who or what performed the task
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed the task
    :param Reference location: Where task occurs
    :param CodeableReference reason: Why task is needed
    :param Reference insurance: Associated insurance coverage
    :param Annotation note: Comments made about the task
    :param Reference relevantHistory: Key events in history of the Task
    :param BackboneElement restriction: Constraints on fulfillment tasks
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int repetitions: How many times to repeat
    :param Period period: When fulfillment is sought
    :param Reference recipient: For whom is fulfillment sought?
    :param BackboneElement input: Information used to perform task
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Label for the input
    :param str valuebase64Binary: Content to use in performing the task
    :param bool valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param float valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param int valuebase64Binary: Content to use in performing the task
    :param int valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param int valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param int valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param str valuebase64Binary: Content to use in performing the task
    :param Address valuebase64Binary: Content to use in performing the task
    :param Age valuebase64Binary: Content to use in performing the task
    :param Annotation valuebase64Binary: Content to use in performing the task
    :param Attachment valuebase64Binary: Content to use in performing the task
    :param CodeableConcept valuebase64Binary: Content to use in performing the task
    :param CodeableReference valuebase64Binary: Content to use in performing the task
    :param Coding valuebase64Binary: Content to use in performing the task
    :param ContactPoint valuebase64Binary: Content to use in performing the task
    :param Count valuebase64Binary: Content to use in performing the task
    :param Distance valuebase64Binary: Content to use in performing the task
    :param Duration valuebase64Binary: Content to use in performing the task
    :param HumanName valuebase64Binary: Content to use in performing the task
    :param Identifier valuebase64Binary: Content to use in performing the task
    :param Money valuebase64Binary: Content to use in performing the task
    :param Period valuebase64Binary: Content to use in performing the task
    :param Quantity valuebase64Binary: Content to use in performing the task
    :param Range valuebase64Binary: Content to use in performing the task
    :param Ratio valuebase64Binary: Content to use in performing the task
    :param RatioRange valuebase64Binary: Content to use in performing the task
    :param Reference valuebase64Binary: Content to use in performing the task
    :param SampledData valuebase64Binary: Content to use in performing the task
    :param Signature valuebase64Binary: Content to use in performing the task
    :param Timing valuebase64Binary: Content to use in performing the task
    :param ContactDetail valuebase64Binary: Content to use in performing the task
    :param DataRequirement valuebase64Binary: Content to use in performing the task
    :param Expression valuebase64Binary: Content to use in performing the task
    :param ParameterDefinition valuebase64Binary: Content to use in performing the task
    :param RelatedArtifact valuebase64Binary: Content to use in performing the task
    :param TriggerDefinition valuebase64Binary: Content to use in performing the task
    :param UsageContext valuebase64Binary: Content to use in performing the task
    :param Availability valuebase64Binary: Content to use in performing the task
    :param ExtendedContactDetail valuebase64Binary: Content to use in performing the task
    :param Dosage valuebase64Binary: Content to use in performing the task
    :param Meta valuebase64Binary: Content to use in performing the task
    :param BackboneElement output: Information produced as part of task
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Label for output
    :param str valuebase64Binary: Result of output
    :param bool valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param float valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param int valuebase64Binary: Result of output
    :param int valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param int valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param int valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param str valuebase64Binary: Result of output
    :param Address valuebase64Binary: Result of output
    :param Age valuebase64Binary: Result of output
    :param Annotation valuebase64Binary: Result of output
    :param Attachment valuebase64Binary: Result of output
    :param CodeableConcept valuebase64Binary: Result of output
    :param CodeableReference valuebase64Binary: Result of output
    :param Coding valuebase64Binary: Result of output
    :param ContactPoint valuebase64Binary: Result of output
    :param Count valuebase64Binary: Result of output
    :param Distance valuebase64Binary: Result of output
    :param Duration valuebase64Binary: Result of output
    :param HumanName valuebase64Binary: Result of output
    :param Identifier valuebase64Binary: Result of output
    :param Money valuebase64Binary: Result of output
    :param Period valuebase64Binary: Result of output
    :param Quantity valuebase64Binary: Result of output
    :param Range valuebase64Binary: Result of output
    :param Ratio valuebase64Binary: Result of output
    :param RatioRange valuebase64Binary: Result of output
    :param Reference valuebase64Binary: Result of output
    :param SampledData valuebase64Binary: Result of output
    :param Signature valuebase64Binary: Result of output
    :param Timing valuebase64Binary: Result of output
    :param ContactDetail valuebase64Binary: Result of output
    :param DataRequirement valuebase64Binary: Result of output
    :param Expression valuebase64Binary: Result of output
    :param ParameterDefinition valuebase64Binary: Result of output
    :param RelatedArtifact valuebase64Binary: Result of output
    :param TriggerDefinition valuebase64Binary: Result of output
    :param UsageContext valuebase64Binary: Result of output
    :param Availability valuebase64Binary: Result of output
    :param ExtendedContactDetail valuebase64Binary: Result of output
    :param Dosage valuebase64Binary: Result of output
    :param Meta valuebase64Binary: Result of output
    
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
    
    groupIdentifier: "Identifier" = None
    
    partOf: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableReference" = None
    
    businessStatus: "CodeableConcept" = None
    
    intent: str = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    code: "CodeableConcept" = None
    
    description: str = None
    
    focus: "Reference" = None
    
    for: "Reference" = None
    
    encounter: "Reference" = None
    
    requestedPeriod: "Period" = None
    
    executionPeriod: "Period" = None
    
    authoredOn: str = None
    
    lastModified: str = None
    
    requester: "Reference" = None
    
    requestedPerformer: "CodeableReference" = None
    
    owner: "Reference" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    location: "Reference" = None
    
    reason: "CodeableReference" = None
    
    insurance: "Reference" = None
    
    note: "Annotation" = None
    
    relevantHistory: "Reference" = None
    
    restriction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    repetitions: int = None
    
    period: "Period" = None
    
    recipient: "Reference" = None
    
    input: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: bool = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: float = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: "Address" = None
    
    valuebase64Binary: "Age" = None
    
    valuebase64Binary: "Annotation" = None
    
    valuebase64Binary: "Attachment" = None
    
    valuebase64Binary: "CodeableConcept" = None
    
    valuebase64Binary: "CodeableReference" = None
    
    valuebase64Binary: "Coding" = None
    
    valuebase64Binary: "ContactPoint" = None
    
    valuebase64Binary: "Count" = None
    
    valuebase64Binary: "Distance" = None
    
    valuebase64Binary: "Duration" = None
    
    valuebase64Binary: "HumanName" = None
    
    valuebase64Binary: "Identifier" = None
    
    valuebase64Binary: "Money" = None
    
    valuebase64Binary: "Period" = None
    
    valuebase64Binary: "Quantity" = None
    
    valuebase64Binary: "Range" = None
    
    valuebase64Binary: "Ratio" = None
    
    valuebase64Binary: "RatioRange" = None
    
    valuebase64Binary: "Reference" = None
    
    valuebase64Binary: "SampledData" = None
    
    valuebase64Binary: "Signature" = None
    
    valuebase64Binary: "Timing" = None
    
    valuebase64Binary: "ContactDetail" = None
    
    valuebase64Binary: "DataRequirement" = None
    
    valuebase64Binary: "Expression" = None
    
    valuebase64Binary: "ParameterDefinition" = None
    
    valuebase64Binary: "RelatedArtifact" = None
    
    valuebase64Binary: "TriggerDefinition" = None
    
    valuebase64Binary: "UsageContext" = None
    
    valuebase64Binary: "Availability" = None
    
    valuebase64Binary: "ExtendedContactDetail" = None
    
    valuebase64Binary: "Dosage" = None
    
    valuebase64Binary: "Meta" = None
    
    output: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: bool = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: float = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: "Address" = None
    
    valuebase64Binary: "Age" = None
    
    valuebase64Binary: "Annotation" = None
    
    valuebase64Binary: "Attachment" = None
    
    valuebase64Binary: "CodeableConcept" = None
    
    valuebase64Binary: "CodeableReference" = None
    
    valuebase64Binary: "Coding" = None
    
    valuebase64Binary: "ContactPoint" = None
    
    valuebase64Binary: "Count" = None
    
    valuebase64Binary: "Distance" = None
    
    valuebase64Binary: "Duration" = None
    
    valuebase64Binary: "HumanName" = None
    
    valuebase64Binary: "Identifier" = None
    
    valuebase64Binary: "Money" = None
    
    valuebase64Binary: "Period" = None
    
    valuebase64Binary: "Quantity" = None
    
    valuebase64Binary: "Range" = None
    
    valuebase64Binary: "Ratio" = None
    
    valuebase64Binary: "RatioRange" = None
    
    valuebase64Binary: "Reference" = None
    
    valuebase64Binary: "SampledData" = None
    
    valuebase64Binary: "Signature" = None
    
    valuebase64Binary: "Timing" = None
    
    valuebase64Binary: "ContactDetail" = None
    
    valuebase64Binary: "DataRequirement" = None
    
    valuebase64Binary: "Expression" = None
    
    valuebase64Binary: "ParameterDefinition" = None
    
    valuebase64Binary: "RelatedArtifact" = None
    
    valuebase64Binary: "TriggerDefinition" = None
    
    valuebase64Binary: "UsageContext" = None
    
    valuebase64Binary: "Availability" = None
    
    valuebase64Binary: "ExtendedContactDetail" = None
    
    valuebase64Binary: "Dosage" = None
    
    valuebase64Binary: "Meta" = None
    