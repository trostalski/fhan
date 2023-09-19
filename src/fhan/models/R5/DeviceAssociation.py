"""
Generated class for DeviceAssociation. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class DeviceAssociation:
    """ A record of association of a device.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Instance identifier
    :param Reference device: Reference to the devices associated with the patient or group
    :param CodeableConcept category: Describes the relationship between the device and subject
    :param CodeableConcept status: implanted | explanted | attached | entered-in-error | unknown
    :param CodeableConcept statusReason: The reasons given for the current association status
    :param Reference subject: The individual, group of individuals or device that the device is on or associated with
    :param Reference bodyStructure: Current anatomical location of the device in/on subject
    :param Period period: Begin and end dates and times for the device association
    :param BackboneElement operation: The details about the device when it is in use to describe its operation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept status: Device operational condition
    :param Reference operator: The individual performing the action enabled by the device
    :param Period period: Begin and end dates and times for the device's operation
    
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
    
    device: "Reference" = None
    
    category: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    statusReason: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    bodyStructure: "Reference" = None
    
    period: "Period" = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    status: "CodeableConcept" = None
    
    operator: "Reference" = None
    
    period: "Period" = None
    