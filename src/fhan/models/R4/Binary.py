"""
Generated class for Binary. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Reference import *
from fhan.models.R4.Meta import *
from fhan.models.R4.DomainResource import *


class Binary(DomainResource):
    """ A resource that represents the data of a single raw artifact as digital content accessible in its native format.  A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param str contentType: MimeType of the binary content
    :param 'Reference' securityContext: Identifies another resource to use as proxy when enforcing access control
    :param str data: The actual content
    """
    def __init__(self, resourceType: str = "Binary",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  contentType: str = None,  securityContext: 'Reference' = None,  data: str = None, ):
        self.resourceType: str = resourceType or "Binary"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.contentType: str = contentType 
        self.securityContext: 'Reference' = securityContext 
        self.data: str = data 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Binary":
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