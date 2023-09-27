"""
Generated class for CodeableConcept. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel

class CodeableConcept(BaseModel):
    """ Base StructureDefinition for CodeableConcept Type: A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
    :param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Coding' coding: Code defined by a terminology system
    :param str text: Plain text representation of the concept
    """
    def __init__(self, resourceType: str = "CodeableConcept",  id: str = None,  extension: 'Extension' = None,  coding: 'Coding' = None,  text: str = None, ):
        self.resourceType: str = resourceType or "CodeableConcept"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.coding: list['Coding'] = coding or []
        self.text: str = text 
        

    @classmethod
    def from_dict(cls, data: dict) -> "CodeableConcept":
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