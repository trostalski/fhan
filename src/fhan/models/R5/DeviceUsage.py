"""
Generated class for DeviceUsage. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class DeviceUsage:
    """ A record of a device being used by a patient where the record is the result of a report from the patient or a clinician.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier for this record
    :param Reference basedOn: Fulfills plan, proposal or order
    :param str status: active | completed | not-done | entered-in-error +
    :param CodeableConcept category: The category of the statement - classifying how the statement is made
    :param Reference patient: Patient using device
    :param Reference derivedFrom: Supporting information
    :param Reference context: The encounter or episode of care that establishes the context for this device use statement
    :param Timing timingTiming: How often  the device was used
    :param Period timingTiming: How often  the device was used
    :param str timingTiming: How often  the device was used
    :param str dateAsserted: When the statement was made (and recorded)
    :param CodeableConcept usageStatus: The status of the device usage, for example always, sometimes, never. This is not the same as the status of the statement
    :param CodeableConcept usageReason: The reason for asserting the usage status - for example forgot, lost, stolen, broken
    :param BackboneElement adherence: How device is being used
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: always | never | sometimes
    :param CodeableConcept reason: lost | stolen | prescribed | broken | burned | forgot
    :param Reference informationSource: Who made the statement
    :param CodeableReference device: Code or Reference to device used
    :param CodeableReference reason: Why device was used
    :param CodeableReference bodySite: Target body site
    :param Annotation note: Addition details (comments, instructions)
    
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
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    derivedFrom: "Reference" = None
    
    context: "Reference" = None
    
    timingTiming: "Timing" = None
    
    timingTiming: "Period" = None
    
    timingTiming: str = None
    
    dateAsserted: str = None
    
    usageStatus: "CodeableConcept" = None
    
    usageReason: "CodeableConcept" = None
    
    adherence: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    reason: "CodeableConcept" = None
    
    informationSource: "Reference" = None
    
    device: "CodeableReference" = None
    
    reason: "CodeableReference" = None
    
    bodySite: "CodeableReference" = None
    
    note: "Annotation" = None
    