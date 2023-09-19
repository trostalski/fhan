"""
Generated class for Media. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


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
    