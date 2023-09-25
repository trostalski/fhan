"""
Generated class for Period. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Period(ModelBase):
    """ Base StructureDefinition for Period Type: A time period defined by a start and end date and optionally time.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str start: Starting time with inclusive boundary
    :param str end: End time with inclusive boundary, if not ongoing
    """
    def __init__(self, resourceType: str = "Period",  id: str = None,  extension: list['Extension'] = None,  start: str = None,  end: str = None, ):
        self.resourceType: str = resourceType or "Period"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.start: str = start 
        self.end: str = end 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Period":
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