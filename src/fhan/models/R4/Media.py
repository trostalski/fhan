"""
Generated class for Media. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Media:
    """
    A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided by direct reference.
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
    
    type: "CodeableConcept" = None
    
    modality: "CodeableConcept" = None
    
    view: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    createddateTime: str = None
    
    createddateTime: "Period" = None
    
    issued: str = None
    
    operator: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    bodySite: "CodeableConcept" = None
    
    deviceName: str = None
    
    device: "Reference" = None
    
    height: int = None
    
    width: int = None
    
    frames: int = None
    
    duration: float = None
    
    content: "Attachment" = None
    
    note: "Annotation" = None
    