"""
Generated class for Annotation. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Annotation(ModelBase):
    """ Base StructureDefinition for Annotation Type: A  text note which also  contains information about who made the statement and when.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'Reference' authorReference: Individual responsible for the annotation
    :param str authorString: Individual responsible for the annotation
    :param str time: When the annotation was made
    :param str text: The annotation  - text content (as markdown)
    """
    def __init__(self, resourceType: str = "Annotation",  id: str = None,  extension: list['Extension'] = None,  authorReference: 'Reference' = None,  authorString: str = None,  time: str = None,  text: str = None, ):
        self.resourceType: str = resourceType or "Annotation"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.authorReference: 'Reference' = authorReference 
        self.authorString: str = authorString 
        self.time: str = time 
        self.text: str = text 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Annotation":
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