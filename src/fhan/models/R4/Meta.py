"""
Generated class for Meta. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Meta(ModelBase):
    """ Base StructureDefinition for Meta Type: The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str versionId: Version specific identifier
    :param str lastUpdated: When the resource version last changed
    :param str source: Identifies where the resource comes from
    :param str profile: Profiles this resource claims to conform to
    :param list['Coding'] security: Security Labels applied to this resource
    :param list['Coding'] tag: Tags applied to this resource
    """
    def __init__(self, resourceType: str = "Meta",  id: str = None,  extension: list['Extension'] = None,  versionId: str = None,  lastUpdated: str = None,  source: str = None,  profile: str = None,  security: list['Coding'] = None,  tag: list['Coding'] = None, ):
        self.resourceType: str = resourceType or "Meta"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.versionId: str = versionId 
        self.lastUpdated: str = lastUpdated 
        self.source: str = source 
        self.profile: str = profile or []
        self.security: list['Coding'] = security or []
        self.tag: list['Coding'] = tag or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Meta":
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