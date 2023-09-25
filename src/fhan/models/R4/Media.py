"""
Generated class for Media. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Media(DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided by direct reference.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Identifier(s) for the image
    :param list['Reference'] basedOn: Procedure that caused this media to be created
    :param list['Reference'] partOf: Part of referenced event
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param 'CodeableConcept' type: Classification of media as image, video, or audio
    :param 'CodeableConcept' modality: The type of acquisition equipment/process
    :param 'CodeableConcept' view: Imaging view, e.g. Lateral or Antero-posterior
    :param 'Reference' subject: Who/What this Media is a record of
    :param 'Reference' encounter: Encounter associated with media
    :param str createdDateTime: When Media was collected
    :param 'Period' createdPeriod: When Media was collected
    :param str issued: Date/Time this version was made available
    :param 'Reference' operator: The person who generated the image
    :param list['CodeableConcept'] reasonCode: Why was event performed?
    :param 'CodeableConcept' bodySite: Observed body part
    :param str deviceName: Name of the device/manufacturer
    :param 'Reference' device: Observing Device
    :param int height: Height of the image in pixels (photo/video)
    :param int width: Width of the image in pixels (photo/video)
    :param int frames: Number of frames if > 1 (photo)
    :param float duration: Length in seconds (audio / video)
    :param 'Attachment' content: Actual Media - reference or data
    :param list['Annotation'] note: Comments made about the media
    """
    def __init__(self, resourceType: str = "Media",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  basedOn: list['Reference'] = None,  partOf: list['Reference'] = None,  status: str = None,  type: 'CodeableConcept' = None,  modality: 'CodeableConcept' = None,  view: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  createdDateTime: str = None,  createdPeriod: 'Period' = None,  issued: str = None,  operator: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  bodySite: 'CodeableConcept' = None,  deviceName: str = None,  device: 'Reference' = None,  height: int = None,  width: int = None,  frames: int = None,  duration: float = None,  content: 'Attachment' = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "Media"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.basedOn: list['Reference'] = basedOn or []
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.type: 'CodeableConcept' = type 
        self.modality: 'CodeableConcept' = modality 
        self.view: 'CodeableConcept' = view 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.createdDateTime: str = createdDateTime 
        self.createdPeriod: 'Period' = createdPeriod 
        self.issued: str = issued 
        self.operator: 'Reference' = operator 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.bodySite: 'CodeableConcept' = bodySite 
        self.deviceName: str = deviceName 
        self.device: 'Reference' = device 
        self.height: int = height 
        self.width: int = width 
        self.frames: int = frames 
        self.duration: float = duration 
        self.content: 'Attachment' = content 
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Media":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance