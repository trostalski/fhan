"""
Generated class for DeviceUseStatement. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class DeviceUseStatement:
    """
    A record of a device being used by a patient where the record is the result of a report from the patient or another clinician.
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
    