"""
Generated class for Media. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

@dataclass
class Media(ModelBase):
    """ A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided by direct reference.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier(s) for the image
    :param Reference basedOn: Procedure that caused this media to be created
    :param Reference partOf: Part of referenced event
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param CodeableConcept type: Classification of media as image, video, or audio
    :param CodeableConcept modality: The type of acquisition equipment/process
    :param CodeableConcept view: Imaging view, e.g. Lateral or Antero-posterior
    :param Reference subject: Who/What this Media is a record of
    :param Reference encounter: Encounter associated with media
    :param str createdDateTime: When Media was collected
    :param str issued: Date/Time this version was made available
    :param Reference operator: The person who generated the image
    :param CodeableConcept reasonCode: Why was event performed?
    :param CodeableConcept bodySite: Observed body part
    :param str deviceName: Name of the device/manufacturer
    :param Reference device: Observing Device
    :param int height: Height of the image in pixels (photo/video)
    :param int width: Width of the image in pixels (photo/video)
    :param int frames: Number of frames if > 1 (photo)
    :param float duration: Length in seconds (audio / video)
    :param Attachment content: Actual Media - reference or data
    :param Annotation note: Comments made about the media
    """

    resourceType: str = "Media"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    basedOn: list["Reference"] = None
    
    partOf: list["Reference"] = None
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    modality: "CodeableConcept" = None
    
    view: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    createdDateTime: str = None
    
    issued: str = None
    
    operator: "Reference" = None
    
    reasonCode: list["CodeableConcept"] = None
    
    bodySite: "CodeableConcept" = None
    
    deviceName: str = None
    
    device: "Reference" = None
    
    height: int = None
    
    width: int = None
    
    frames: int = None
    
    duration: float = None
    
    content: "Attachment" = None
    
    note: list["Annotation"] = None
    