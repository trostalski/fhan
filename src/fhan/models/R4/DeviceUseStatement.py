"""
Generated class for DeviceUseStatement. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Meta import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class DeviceUseStatement(DomainResource):
    """ A record of a device being used by a patient where the record is the result of a report from the patient or another clinician.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: External identifier for this record
    :param 'Reference' basedOn: Fulfills plan, proposal or order
    :param str status: active | completed | entered-in-error +
    :param 'Reference' subject: Patient using device
    :param 'Reference' derivedFrom: Supporting information
    :param 'Timing' timingTiming: How often  the device was used
    :param 'Period' timingPeriod: How often  the device was used
    :param str timingDateTime: How often  the device was used
    :param str recordedOn: When statement was recorded
    :param 'Reference' source: Who made the statement
    :param 'Reference' device: Reference to device used
    :param 'CodeableConcept' reasonCode: Why device was used
    :param 'Reference' reasonReference: Why was DeviceUseStatement performed?
    :param 'CodeableConcept' bodySite: Target body site
    :param 'Annotation' note: Addition details (comments, instructions)
    """
    def __init__(self, resourceType: str = "DeviceUseStatement",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  basedOn: 'Reference' = None,  status: str = None,  subject: 'Reference' = None,  derivedFrom: 'Reference' = None,  timingTiming: 'Timing' = None,  timingPeriod: 'Period' = None,  timingDateTime: str = None,  recordedOn: str = None,  source: 'Reference' = None,  device: 'Reference' = None,  reasonCode: 'CodeableConcept' = None,  reasonReference: 'Reference' = None,  bodySite: 'CodeableConcept' = None,  note: 'Annotation' = None, ):
        self.resourceType: str = resourceType or "DeviceUseStatement"
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
        self.status: str = status 
        self.subject: 'Reference' = subject 
        self.derivedFrom: list['Reference'] = derivedFrom or []
        self.timingTiming: 'Timing' = timingTiming 
        self.timingPeriod: 'Period' = timingPeriod 
        self.timingDateTime: str = timingDateTime 
        self.recordedOn: str = recordedOn 
        self.source: 'Reference' = source 
        self.device: 'Reference' = device 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.bodySite: 'CodeableConcept' = bodySite 
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceUseStatement":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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