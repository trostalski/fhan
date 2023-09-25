"""
Generated class for SpecimenDefinition. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
        
    
    

class Additive(ModelBase):
    """ Substance introduced in the kind of container to preserve, maintain or enhance the specimen. Examples: Formalin, Citrate, EDTA.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' additiveCodeableConcept: Additive associated with container
    :param 'Reference' additiveReference: Additive associated with container
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  additiveCodeableConcept: 'CodeableConcept' = None,  additiveReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.additiveCodeableConcept: 'CodeableConcept' = additiveCodeableConcept 
        self.additiveReference: 'Reference' = additiveReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Additive":
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
    """ The specimen's container.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' material: Container material
    :param 'CodeableConcept' type: Kind of container associated with the kind of specimen
    :param 'CodeableConcept' cap: Color of container cap
    :param str description: Container description
    :param 'Quantity' capacity: Container capacity
    :param 'Quantity' minimumVolumeQuantity: Minimum volume
    :param str minimumVolumeString: Minimum volume
    :param list['Additive'] additive: Additive associated with container
    :param str preparation: Specimen container preparation
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  material: 'CodeableConcept' = None,  type: 'CodeableConcept' = None,  cap: 'CodeableConcept' = None,  description: str = None,  capacity: 'Quantity' = None,  minimumVolumeQuantity: 'Quantity' = None,  minimumVolumeString: str = None,  additive: list['Additive'] = None,  preparation: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.material: 'CodeableConcept' = material 
        self.type: 'CodeableConcept' = type 
        self.cap: 'CodeableConcept' = cap 
        self.description: str = description 
        self.capacity: 'Quantity' = capacity 
        self.minimumVolumeQuantity: 'Quantity' = minimumVolumeQuantity 
        self.minimumVolumeString: str = minimumVolumeString 
        self.additive: list['Additive'] = additive or []
        self.preparation: str = preparation 
        

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


    
    

class Handling(ModelBase):
    """ Set of instructions for preservation/transport of the specimen at a defined temperature interval, prior the testing process.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' temperatureQualifier: Temperature qualifier
    :param 'Range' temperatureRange: Temperature range
    :param 'Duration' maxDuration: Maximum preservation time
    :param str instruction: Preservation instruction
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  temperatureQualifier: 'CodeableConcept' = None,  temperatureRange: 'Range' = None,  maxDuration: 'Duration' = None,  instruction: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.temperatureQualifier: 'CodeableConcept' = temperatureQualifier 
        self.temperatureRange: 'Range' = temperatureRange 
        self.maxDuration: 'Duration' = maxDuration 
        self.instruction: str = instruction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Handling":
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


  
    
    

class TypeTested(ModelBase):
    """ Specimen conditioned in a container as expected by the testing laboratory.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool isDerived: Primary or secondary specimen
    :param 'CodeableConcept' type: Type of intended specimen
    :param str preference: preferred | alternate
    :param 'Container' container: The specimen's container
    :param str requirement: Specimen requirements
    :param 'Duration' retentionTime: Specimen retention time
    :param list['CodeableConcept'] rejectionCriterion: Rejection criterion
    :param list['Handling'] handling: Specimen handling before testing
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  isDerived: bool = None,  type: 'CodeableConcept' = None,  preference: str = None,  container: 'Container' = None,  requirement: str = None,  retentionTime: 'Duration' = None,  rejectionCriterion: list['CodeableConcept'] = None,  handling: list['Handling'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.isDerived: bool = isDerived 
        self.type: 'CodeableConcept' = type 
        self.preference: str = preference 
        self.container: 'Container' = container 
        self.requirement: str = requirement 
        self.retentionTime: 'Duration' = retentionTime 
        self.rejectionCriterion: list['CodeableConcept'] = rejectionCriterion or []
        self.handling: list['Handling'] = handling or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "TypeTested":
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


class SpecimenDefinition(DomainResource):
    """ A kind of specimen with associated set of requirements.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Business identifier of a kind of specimen
    :param 'CodeableConcept' typeCollected: Kind of material to collect
    :param list['CodeableConcept'] patientPreparation: Patient preparation for collection
    :param str timeAspect: Time aspect for collection
    :param list['CodeableConcept'] collection: Specimen collection procedure
    :param list['TypeTested'] typeTested: Specimen in container intended for testing by lab
    """
    def __init__(self, resourceType: str = "SpecimenDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  typeCollected: 'CodeableConcept' = None,  patientPreparation: list['CodeableConcept'] = None,  timeAspect: str = None,  collection: list['CodeableConcept'] = None,  typeTested: list['TypeTested'] = None, ):
        self.resourceType: str = resourceType or "SpecimenDefinition"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.typeCollected: 'CodeableConcept' = typeCollected 
        self.patientPreparation: list['CodeableConcept'] = patientPreparation or []
        self.timeAspect: str = timeAspect 
        self.collection: list['CodeableConcept'] = collection or []
        self.typeTested: list['TypeTested'] = typeTested or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SpecimenDefinition":
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