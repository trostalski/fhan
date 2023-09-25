"""
Generated class for ImagingStudy. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Performer(ModelBase):
    """ Indicates who or what performed the series and how they were involved.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' function: Type of performance
    :param 'Reference' actor: Who performed the series
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  function: 'CodeableConcept' = None,  actor: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.function: 'CodeableConcept' = function 
        self.actor: 'Reference' = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Performer":
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


    
    

class Instance(ModelBase):
    """ A single SOP instance within the series, e.g. an image, or presentation state.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM SOP Instance UID
    :param 'Coding' sopClass: DICOM class type
    :param int number: The number of this instance in the series
    :param str title: Description of instance
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  uid: str = None,  sopClass: 'Coding' = None,  number: int = None,  title: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.uid: str = uid 
        self.sopClass: 'Coding' = sopClass 
        self.number: int = number 
        self.title: str = title 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Instance":
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


  
    
    

class Series(ModelBase):
    """ Each study has one or more series of images or other content.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM Series Instance UID for the series
    :param int number: Numeric identifier of this series
    :param 'Coding' modality: The modality of the instances in the series
    :param str description: A short human readable summary of the series
    :param int numberOfInstances: Number of Series Related Instances
    :param list['Reference'] endpoint: Series access endpoint
    :param 'Coding' bodySite: Body part examined
    :param 'Coding' laterality: Body part laterality
    :param list['Reference'] specimen: Specimen imaged
    :param str started: When the series started
    :param list['Performer'] performer: Who performed the series
    :param list['Instance'] instance: A single SOP instance from the series
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  uid: str = None,  number: int = None,  modality: 'Coding' = None,  description: str = None,  numberOfInstances: int = None,  endpoint: list['Reference'] = None,  bodySite: 'Coding' = None,  laterality: 'Coding' = None,  specimen: list['Reference'] = None,  started: str = None,  performer: list['Performer'] = None,  instance: list['Instance'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.uid: str = uid 
        self.number: int = number 
        self.modality: 'Coding' = modality 
        self.description: str = description 
        self.numberOfInstances: int = numberOfInstances 
        self.endpoint: list['Reference'] = endpoint or []
        self.bodySite: 'Coding' = bodySite 
        self.laterality: 'Coding' = laterality 
        self.specimen: list['Reference'] = specimen or []
        self.started: str = started 
        self.performer: list['Performer'] = performer or []
        self.instance: list['Instance'] = instance or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Series":
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


class ImagingStudy(DomainResource):
    """ Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study may have multiple series of different modalities.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Identifiers for the whole study
    :param str status: registered | available | cancelled | entered-in-error | unknown
    :param list['Coding'] modality: All series modality if actual acquisition modalities
    :param 'Reference' subject: Who or what is the subject of the study
    :param 'Reference' encounter: Encounter with which this imaging study is associated
    :param str started: When the study was started
    :param list['Reference'] basedOn: Request fulfilled
    :param 'Reference' referrer: Referring physician
    :param list['Reference'] interpreter: Who interpreted images
    :param list['Reference'] endpoint: Study access endpoint
    :param int numberOfSeries: Number of Study Related Series
    :param int numberOfInstances: Number of Study Related Instances
    :param 'Reference' procedureReference: The performed Procedure reference
    :param list['CodeableConcept'] procedureCode: The performed procedure code
    :param 'Reference' location: Where ImagingStudy occurred
    :param list['CodeableConcept'] reasonCode: Why the study was requested
    :param list['Reference'] reasonReference: Why was study performed
    :param list['Annotation'] note: User-defined comments
    :param str description: Institution-generated description
    :param list['Series'] series: Each study has one or more series of instances
    """
    def __init__(self, resourceType: str = "ImagingStudy",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  modality: list['Coding'] = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  started: str = None,  basedOn: list['Reference'] = None,  referrer: 'Reference' = None,  interpreter: list['Reference'] = None,  endpoint: list['Reference'] = None,  numberOfSeries: int = None,  numberOfInstances: int = None,  procedureReference: 'Reference' = None,  procedureCode: list['CodeableConcept'] = None,  location: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  note: list['Annotation'] = None,  description: str = None,  series: list['Series'] = None, ):
        self.resourceType: str = resourceType or "ImagingStudy"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.modality: list['Coding'] = modality or []
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.started: str = started 
        self.basedOn: list['Reference'] = basedOn or []
        self.referrer: 'Reference' = referrer 
        self.interpreter: list['Reference'] = interpreter or []
        self.endpoint: list['Reference'] = endpoint or []
        self.numberOfSeries: int = numberOfSeries 
        self.numberOfInstances: int = numberOfInstances 
        self.procedureReference: 'Reference' = procedureReference 
        self.procedureCode: list['CodeableConcept'] = procedureCode or []
        self.location: 'Reference' = location 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.note: list['Annotation'] = note or []
        self.description: str = description 
        self.series: list['Series'] = series or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingStudy":
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