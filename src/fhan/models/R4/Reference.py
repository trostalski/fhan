"""
Generated class for Reference. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel

class Reference(BaseModel):
    """ Base StructureDefinition for Reference Type: A reference from one resource to another.
    :param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param str reference: Literal reference, Relative, internal or absolute URL
    :param str type: Type the reference refers to (e.g. "Patient")
    :param 'Identifier' identifier: Logical reference, when literal reference is not known
    :param str display: Text alternative for the resource
    """
    def __init__(self, resourceType: str = "Reference",  id: str = None,  extension: 'Extension' = None,  reference: str = None,  type: str = None,  identifier: 'Identifier' = None,  display: str = None, ):
        self.resourceType: str = resourceType or "Reference"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.reference: str = reference 
        self.type: str = type 
        self.identifier: 'Identifier' = identifier 
        self.display: str = display 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Reference":
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