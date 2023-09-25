"""
Generated class for HumanName. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class HumanName(ModelBase):
    """ Base StructureDefinition for HumanName Type: A human's name with the ability to identify parts and usage.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str use: usual | official | temp | nickname | anonymous | old | maiden
    :param str text: Text representation of the full name
    :param str family: Family name (often called 'Surname')
    :param str given: Given names (not always 'first'). Includes middle names
    :param str prefix: Parts that come before the name
    :param str suffix: Parts that come after the name
    :param 'Period' period: Time period when name was/is in use
    """
    def __init__(self, resourceType: str = "HumanName",  id: str = None,  extension: list['Extension'] = None,  use: str = None,  text: str = None,  family: str = None,  given: str = None,  prefix: str = None,  suffix: str = None,  period: 'Period' = None, ):
        self.resourceType: str = resourceType or "HumanName"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.use: str = use 
        self.text: str = text 
        self.family: str = family 
        self.given: str = given or []
        self.prefix: str = prefix or []
        self.suffix: str = suffix or []
        self.period: 'Period' = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "HumanName":
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