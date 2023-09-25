"""
Generated class for Specimen. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Collection(ModelBase):
    """ Details concerning the specimen collection.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' collector: Who collected the specimen
    :param str collectedDateTime: Collection time
    :param 'Period' collectedPeriod: Collection time
    :param 'Duration' duration: How long it took to collect specimen
    :param 'Quantity' quantity: The quantity of specimen collected
    :param 'CodeableConcept' method: Technique used to perform collection
    :param 'CodeableConcept' bodySite: Anatomical collection site
    :param 'CodeableConcept' fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    :param 'Duration' fastingStatusDuration: Whether or how long patient abstained from food and/or drink
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  collector: 'Reference' = None,  collectedDateTime: str = None,  collectedPeriod: 'Period' = None,  duration: 'Duration' = None,  quantity: 'Quantity' = None,  method: 'CodeableConcept' = None,  bodySite: 'CodeableConcept' = None,  fastingStatusCodeableConcept: 'CodeableConcept' = None,  fastingStatusDuration: 'Duration' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.collector: 'Reference' = collector 
        self.collectedDateTime: str = collectedDateTime 
        self.collectedPeriod: 'Period' = collectedPeriod 
        self.duration: 'Duration' = duration 
        self.quantity: 'Quantity' = quantity 
        self.method: 'CodeableConcept' = method 
        self.bodySite: 'CodeableConcept' = bodySite 
        self.fastingStatusCodeableConcept: 'CodeableConcept' = fastingStatusCodeableConcept 
        self.fastingStatusDuration: 'Duration' = fastingStatusDuration 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Collection":
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


    
    

class Processing(ModelBase):
    """ Details concerning processing and processing steps for the specimen.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of procedure
    :param 'CodeableConcept' procedure: Indicates the treatment step  applied to the specimen
    :param list['Reference'] additive: Material used in the processing step
    :param str timeDateTime: Date and time of specimen processing
    :param 'Period' timePeriod: Date and time of specimen processing
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  description: str = None,  procedure: 'CodeableConcept' = None,  additive: list['Reference'] = None,  timeDateTime: str = None,  timePeriod: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.description: str = description 
        self.procedure: 'CodeableConcept' = procedure 
        self.additive: list['Reference'] = additive or []
        self.timeDateTime: str = timeDateTime 
        self.timePeriod: 'Period' = timePeriod 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Processing":
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


    
    

class Container(ModelBase):
    """ The container holding the specimen.  The recursive nature of containers; i.e. blood in tube in tray in rack is not addressed here.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['Identifier'] identifier: Id for the container
    :param str description: Textual description of the container
    :param 'CodeableConcept' type: Kind of container directly associated with specimen
    :param 'Quantity' capacity: Container volume or size
    :param 'Quantity' specimenQuantity: Quantity of specimen within container
    :param 'CodeableConcept' additiveCodeableConcept: Additive associated with container
    :param 'Reference' additiveReference: Additive associated with container
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  description: str = None,  type: 'CodeableConcept' = None,  capacity: 'Quantity' = None,  specimenQuantity: 'Quantity' = None,  additiveCodeableConcept: 'CodeableConcept' = None,  additiveReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.description: str = description 
        self.type: 'CodeableConcept' = type 
        self.capacity: 'Quantity' = capacity 
        self.specimenQuantity: 'Quantity' = specimenQuantity 
        self.additiveCodeableConcept: 'CodeableConcept' = additiveCodeableConcept 
        self.additiveReference: 'Reference' = additiveReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Container":
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


class Specimen(DomainResource):
    """ A sample to be used for analysis.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Identifier
    :param 'Identifier' accessionIdentifier: Identifier assigned by the lab
    :param str status: available | unavailable | unsatisfactory | entered-in-error
    :param 'CodeableConcept' type: Kind of material that forms the specimen
    :param 'Reference' subject: Where the specimen came from. This may be from patient(s), from a location (e.g., the source of an environmental sample), or a sampling of a substance or a device
    :param str receivedTime: The time when specimen was received for processing
    :param list['Reference'] parent: Specimen from which this specimen originated
    :param list['Reference'] request: Why the specimen was collected
    :param 'Collection' collection: Collection details
    :param list['Processing'] processing: Processing and processing step details
    :param list['Container'] container: Direct container of specimen (tube/slide, etc.)
    :param list['CodeableConcept'] condition: State of the specimen
    :param list['Annotation'] note: Comments
    """
    def __init__(self, resourceType: str = "Specimen",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  accessionIdentifier: 'Identifier' = None,  status: str = None,  type: 'CodeableConcept' = None,  subject: 'Reference' = None,  receivedTime: str = None,  parent: list['Reference'] = None,  request: list['Reference'] = None,  collection: 'Collection' = None,  processing: list['Processing'] = None,  container: list['Container'] = None,  condition: list['CodeableConcept'] = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "Specimen"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.accessionIdentifier: 'Identifier' = accessionIdentifier 
        self.status: str = status 
        self.type: 'CodeableConcept' = type 
        self.subject: 'Reference' = subject 
        self.receivedTime: str = receivedTime 
        self.parent: list['Reference'] = parent or []
        self.request: list['Reference'] = request or []
        self.collection: 'Collection' = collection 
        self.processing: list['Processing'] = processing or []
        self.container: list['Container'] = container or []
        self.condition: list['CodeableConcept'] = condition or []
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
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