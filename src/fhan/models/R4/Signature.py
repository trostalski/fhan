"""
Generated class for Signature. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Reference import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Signature(ModelBase):
    """ Base StructureDefinition for Signature Type: A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Coding'] type: Indication of the reason the entity signed the object(s)
    :param str when: When the signature was created
    :param 'Reference' who: Who signed
    :param 'Reference' onBehalfOf: The party represented
    :param str targetFormat: The technical format of the signed resources
    :param str sigFormat: The technical format of the signature
    :param str data: The actual signature content (XML DigSig. JWS, picture, etc.)
    """
    def __init__(self, resourceType: str = "Signature",  id: str = None,  extension: list['Extension'] = None,  type: list['Coding'] = None,  when: str = None,  who: 'Reference' = None,  onBehalfOf: 'Reference' = None,  targetFormat: str = None,  sigFormat: str = None,  data: str = None, ):
        self.resourceType: str = resourceType or "Signature"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: list['Coding'] = type or []
        self.when: str = when 
        self.who: 'Reference' = who 
        self.onBehalfOf: 'Reference' = onBehalfOf 
        self.targetFormat: str = targetFormat 
        self.sigFormat: str = sigFormat 
        self.data: str = data 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Signature":
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