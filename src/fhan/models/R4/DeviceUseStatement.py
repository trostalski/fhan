"""
Generated class for DeviceUseStatement. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase


@dataclass
class DeviceUseStatement(ModelBase):
    """ A record of a device being used by a patient where the record is the result of a report from the patient or another clinician.
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
    :param str status: active | completed | entered-in-error +
    :param Reference subject: Patient using device
    :param Reference derivedFrom: Supporting information
    :param Timing timingTiming: How often  the device was used
    :param Period timingTiming: How often  the device was used
    :param str timingTiming: How often  the device was used
    :param str recordedOn: When statement was recorded
    :param Reference source: Who made the statement
    :param Reference device: Reference to device used
    :param CodeableConcept reasonCode: Why device was used
    :param Reference reasonReference: Why was DeviceUseStatement performed?
    :param CodeableConcept bodySite: Target body site
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
    
    subject: "Reference" = None
    
    derivedFrom: "Reference" = None
    
    timingTiming: "Timing" = None
    
    timingTiming: "Period" = None
    
    timingTiming: str = None
    
    recordedOn: str = None
    
    source: "Reference" = None
    
    device: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    bodySite: "CodeableConcept" = None
    
    note: "Annotation" = None
    