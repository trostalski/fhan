"""
Generated class for DeviceRequest. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Range import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Parameter(Element):
    """ Specific parameters for the ordered item.  For example, the prism value for lenses.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Device detail
    :param CodeableConcept valueCodeableConcept: Value of detail
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    valueCodeableConcept: "CodeableConcept" = None
    

@dataclass
class DeviceRequest(ModelBase):
    """ Represents a request for a patient to employ a medical device. The device may be an implantable device, or an external assistive device, such as a walker.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Request identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: What request fulfills
    :param Reference priorRequest: What request replaces
    :param Identifier groupIdentifier: Identifier of composite request
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param Reference codeReference: Device requested
    :param Parameter parameter: Device details
    :param Reference subject: Focus of request
    :param Reference encounter: Encounter motivating request
    :param str occurrenceDateTime: Desired time or schedule for use
    :param str authoredOn: When recorded
    :param Reference requester: Who/what is requesting diagnostics
    :param CodeableConcept performerType: Filler role
    :param Reference performer: Requested Filler
    :param CodeableConcept reasonCode: Coded Reason for request
    :param Reference reasonReference: Linked Reason for request
    :param Reference insurance: Associated insurance coverage
    :param Reference supportingInfo: Additional clinical information
    :param Annotation note: Notes or comments
    :param Reference relevantHistory: Request provenance
    """

    resourceType: str = "DeviceRequest"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: list["Reference"] = None
    
    priorRequest: list["Reference"] = None
    
    groupIdentifier: "Identifier" = None
    
    status: str = None
    
    intent: str = None
    
    priority: str = None
    
    codeReference: "Reference" = None
    
    parameter: list["Parameter"] = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrenceDateTime: str = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    performerType: "CodeableConcept" = None
    
    performer: "Reference" = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    insurance: list["Reference"] = None
    
    supportingInfo: list["Reference"] = None
    
    note: list["Annotation"] = None
    
    relevantHistory: list["Reference"] = None
    