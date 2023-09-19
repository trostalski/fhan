"""
Generated class for Transport. 
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
class Transport:
    """ Record of transport.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param str instantiatesCanonical: Formal definition of transport
    :param str instantiatesUri: Formal definition of transport
    :param Reference basedOn: Request fulfilled by this transport
    :param Identifier groupIdentifier: Requisition or grouper id
    :param Reference partOf: Part of referenced event
    :param str status: in-progress | completed | abandoned | cancelled | planned | entered-in-error
    :param CodeableConcept statusReason: Reason for current status
    :param str intent: unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept code: Transport Type
    :param str description: Human-readable explanation of transport
    :param Reference focus: What transport is acting on
    :param Reference for: Beneficiary of the Transport
    :param Reference encounter: Healthcare event during which this transport originated
    :param str completionTime: Completion time of the event (the occurrence)
    :param str authoredOn: Transport Creation Date
    :param str lastModified: Transport Last Modified Date
    :param Reference requester: Who is asking for transport to be done
    :param CodeableConcept performerType: Requested performer
    :param Reference owner: Responsible individual
    :param Reference location: Where transport occurs
    :param Reference insurance: Associated insurance coverage
    :param Annotation note: Comments made about the transport
    :param Reference relevantHistory: Key events in history of the Transport
    :param BackboneElement restriction: Constraints on fulfillment transports
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int repetitions: How many times to repeat
    :param Period period: When fulfillment sought
    :param Reference recipient: For whom is fulfillment sought?
    :param BackboneElement input: Information used to perform transport
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Label for the input
    :param str valuebase64Binary: Content to use in performing the transport
    :param bool valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param float valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param int valuebase64Binary: Content to use in performing the transport
    :param int valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param int valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param int valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param str valuebase64Binary: Content to use in performing the transport
    :param Address valuebase64Binary: Content to use in performing the transport
    :param Age valuebase64Binary: Content to use in performing the transport
    :param Annotation valuebase64Binary: Content to use in performing the transport
    :param Attachment valuebase64Binary: Content to use in performing the transport
    :param CodeableConcept valuebase64Binary: Content to use in performing the transport
    :param CodeableReference valuebase64Binary: Content to use in performing the transport
    :param Coding valuebase64Binary: Content to use in performing the transport
    :param ContactPoint valuebase64Binary: Content to use in performing the transport
    :param Count valuebase64Binary: Content to use in performing the transport
    :param Distance valuebase64Binary: Content to use in performing the transport
    :param Duration valuebase64Binary: Content to use in performing the transport
    :param HumanName valuebase64Binary: Content to use in performing the transport
    :param Identifier valuebase64Binary: Content to use in performing the transport
    :param Money valuebase64Binary: Content to use in performing the transport
    :param Period valuebase64Binary: Content to use in performing the transport
    :param Quantity valuebase64Binary: Content to use in performing the transport
    :param Range valuebase64Binary: Content to use in performing the transport
    :param Ratio valuebase64Binary: Content to use in performing the transport
    :param RatioRange valuebase64Binary: Content to use in performing the transport
    :param Reference valuebase64Binary: Content to use in performing the transport
    :param SampledData valuebase64Binary: Content to use in performing the transport
    :param Signature valuebase64Binary: Content to use in performing the transport
    :param Timing valuebase64Binary: Content to use in performing the transport
    :param ContactDetail valuebase64Binary: Content to use in performing the transport
    :param DataRequirement valuebase64Binary: Content to use in performing the transport
    :param Expression valuebase64Binary: Content to use in performing the transport
    :param ParameterDefinition valuebase64Binary: Content to use in performing the transport
    :param RelatedArtifact valuebase64Binary: Content to use in performing the transport
    :param TriggerDefinition valuebase64Binary: Content to use in performing the transport
    :param UsageContext valuebase64Binary: Content to use in performing the transport
    :param Availability valuebase64Binary: Content to use in performing the transport
    :param ExtendedContactDetail valuebase64Binary: Content to use in performing the transport
    :param Dosage valuebase64Binary: Content to use in performing the transport
    :param Meta valuebase64Binary: Content to use in performing the transport
    :param BackboneElement output: Information produced as part of transport
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
    :param Reference requestedLocation: The desired location
    :param Reference currentLocation: The entity current location
    :param CodeableReference reason: Why transport is needed
    :param Reference history: Parent (or preceding) transport
    
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
    
    statusReason: "CodeableConcept" = None
    
    intent: str = None
    
    priority: str = None
    
    code: "CodeableConcept" = None
    
    description: str = None
    
    focus: "Reference" = None
    
    for: "Reference" = None
    
    encounter: "Reference" = None
    
    completionTime: str = None
    
    authoredOn: str = None
    
    lastModified: str = None
    
    requester: "Reference" = None
    
    performerType: "CodeableConcept" = None
    
    owner: "Reference" = None
    
    location: "Reference" = None
    
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
    
    requestedLocation: "Reference" = None
    
    currentLocation: "Reference" = None
    
    reason: "CodeableReference" = None
    
    history: "Reference" = None
    