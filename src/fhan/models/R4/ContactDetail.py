"""
Generated class for ContactDetail. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class ContactDetail(ModelBase):
    """ Base StructureDefinition for ContactDetail Type: Specifies contact information for a person or organization.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str name: Name of an individual to contact
    :param list['ContactPoint'] telecom: Contact details for individual or organization
    """
    def __init__(self, resourceType: str = "ContactDetail",  id: str = None,  extension: list['Extension'] = None,  name: str = None,  telecom: list['ContactPoint'] = None, ):
        self.resourceType: str = resourceType or "ContactDetail"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.name: str = name 
        self.telecom: list['ContactPoint'] = telecom or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ContactDetail":
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