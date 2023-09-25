"""
Generated class for Attachment. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Attachment(ModelBase):
    """ Base StructureDefinition for Attachment Type: For referring to data content defined in other formats.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str contentType: Mime type of the content, with charset etc.
    :param str language: Human language of the content (BCP-47)
    :param str data: Data inline, base64ed
    :param str url: Uri where the data can be found
    :param int size: Number of bytes of content (if url provided)
    :param str hash: Hash of the data (sha-1, base64ed)
    :param str title: Label to display in place of the data
    :param str creation: Date attachment was first created
    """
    def __init__(self, resourceType: str = "Attachment",  id: str = None,  extension: list['Extension'] = None,  contentType: str = None,  language: str = None,  data: str = None,  url: str = None,  size: int = None,  hash: str = None,  title: str = None,  creation: str = None, ):
        self.resourceType: str = resourceType or "Attachment"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.contentType: str = contentType 
        self.language: str = language 
        self.data: str = data 
        self.url: str = url 
        self.size: int = size 
        self.hash: str = hash 
        self.title: str = title 
        self.creation: str = creation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Attachment":
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