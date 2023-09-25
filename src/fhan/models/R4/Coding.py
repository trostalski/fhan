"""
Generated class for Coding. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Coding(ModelBase):
    """ Base StructureDefinition for Coding Type: A reference to a code defined by a terminology system.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str system: Identity of the terminology system
    :param str version: Version of the system - if relevant
    :param str code: Symbol in syntax defined by the system
    :param str display: Representation defined by the system
    :param bool userSelected: If this coding was chosen directly by the user
    """
    def __init__(self, resourceType: str = "Coding",  id: str = None,  extension: list['Extension'] = None,  system: str = None,  version: str = None,  code: str = None,  display: str = None,  userSelected: bool = None, ):
        self.resourceType: str = resourceType or "Coding"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.system: str = system 
        self.version: str = version 
        self.code: str = code 
        self.display: str = display 
        self.userSelected: bool = userSelected 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Coding":
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