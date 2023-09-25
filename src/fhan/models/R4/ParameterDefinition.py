"""
Generated class for ParameterDefinition. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class ParameterDefinition(ModelBase):
    """ Base StructureDefinition for ParameterDefinition Type: The parameters to the module. This collection specifies both the input and output parameters. Input parameters are provided by the caller as part of the $evaluate operation. Output parameters are included in the GuidanceResponse.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str name: Name used to access the parameter value
    :param str use: in | out
    :param int min: Minimum cardinality
    :param str max: Maximum cardinality (a number of *)
    :param str documentation: A brief description of the parameter
    :param str type: What type of value
    :param str profile: What profile the value is expected to be
    """
    def __init__(self, resourceType: str = "ParameterDefinition",  id: str = None,  extension: list['Extension'] = None,  name: str = None,  use: str = None,  min: int = None,  max: str = None,  documentation: str = None,  type: str = None,  profile: str = None, ):
        self.resourceType: str = resourceType or "ParameterDefinition"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.name: str = name 
        self.use: str = use 
        self.min: int = min 
        self.max: str = max 
        self.documentation: str = documentation 
        self.type: str = type 
        self.profile: str = profile 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ParameterDefinition":
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