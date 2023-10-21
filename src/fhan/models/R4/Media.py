"""
Generated class for Media. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Media(DomainResource):
    """A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided by direct reference.
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
    :param Period createdPeriod: When Media was collected
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

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "modality": {"class_name": "CodeableConcept", "is_contained": False},
        "view": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "createdPeriod": {"class_name": "Period", "is_contained": False},
        "operator": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        "device": {"class_name": "Reference", "is_contained": False},
        "content": {"class_name": "Attachment", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        basedOn: list["Reference"] = None,
        partOf: list["Reference"] = None,
        status: "str" = None,
        type: "CodeableConcept" = None,
        modality: "CodeableConcept" = None,
        view: "CodeableConcept" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        createdDateTime: "str" = None,
        createdPeriod: "Period" = None,
        issued: "str" = None,
        operator: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        bodySite: "CodeableConcept" = None,
        deviceName: "str" = None,
        device: "Reference" = None,
        height: "int" = None,
        width: "int" = None,
        frames: "int" = None,
        duration: "float" = None,
        content: "Attachment" = None,
        note: list["Annotation"] = None,
    ):
        self.resourceType = resourceType or "Media"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.status = status
        self.type = type
        self.modality = modality
        self.view = view
        self.subject = subject
        self.encounter = encounter
        self.createdDateTime = createdDateTime
        self.createdPeriod = createdPeriod
        self.issued = issued
        self.operator = operator
        self.reasonCode = reasonCode or []
        self.bodySite = bodySite
        self.deviceName = deviceName
        self.device = device
        self.height = height
        self.width = width
        self.frames = frames
        self.duration = duration
        self.content = content
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "Media":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Media":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
