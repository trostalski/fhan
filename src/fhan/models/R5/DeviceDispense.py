"""
Generated class for DeviceDispense. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class DeviceDispense:
    """ Indicates that a device is to be or has been dispensed for a named person/patient.  This includes a description of the product (supply) provided and the instructions for using the device.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this dispensation
    :param Reference basedOn: The order or request that this dispense is fulfilling
    :param Reference partOf: The bigger event that this dispense is a part of
    :param str status: preparation | in-progress | cancelled | on-hold | completed | entered-in-error | stopped | declined | unknown
    :param CodeableReference statusReason: Why a dispense was or was not performed
    :param CodeableConcept category: Type of device dispense
    :param CodeableReference device: What device was supplied
    :param Reference subject: Who the dispense is for
    :param Reference receiver: Who collected the device or where the medication was delivered
    :param Reference encounter: Encounter associated with event
    :param Reference supportingInformation: Information that supports the dispensing of the device
    :param BackboneElement performer: Who performed event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Who performed the dispense and what they did
    :param Reference actor: Individual who was performing
    :param Reference location: Where the dispense occurred
    :param CodeableConcept type: Trial fill, partial fill, emergency fill, etc
    :param Quantity quantity: Amount dispensed
    :param str preparedDate: When product was packaged and reviewed
    :param str whenHandedOver: When product was given out
    :param Reference destination: Where the device was sent or should be sent
    :param Annotation note: Information about the dispense
    :param str usageInstruction: Full representation of the usage instructions
    :param Reference eventHistory: A list of relevant lifecycle events
    
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
    
    basedOn: "Reference" = None
    
    partOf: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableReference" = None
    
    category: "CodeableConcept" = None
    
    device: "CodeableReference" = None
    
    subject: "Reference" = None
    
    receiver: "Reference" = None
    
    encounter: "Reference" = None
    
    supportingInformation: "Reference" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    location: "Reference" = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    preparedDate: str = None
    
    whenHandedOver: str = None
    
    destination: "Reference" = None
    
    note: "Annotation" = None
    
    usageInstruction: str = None
    
    eventHistory: "Reference" = None
    