"""
Generated class for Identifier. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel

class Identifier(BaseModel):
    """ Base StructureDefinition for Identifier Type: An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business identifiers.
    :param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param str use: usual | official | temp | secondary | old (If known)
    :param 'CodeableConcept' type: Description of identifier
    :param str system: The namespace for the identifier value
    :param str value: The value that is unique
    :param 'Period' period: Time period when id is/was valid for use
    :param 'Reference' assigner: Organization that issued id (may be just text)
    """
    def __init__(self, resourceType: str = "Identifier",  id: str = None,  extension: 'Extension' = None,  use: str = None,  type: 'CodeableConcept' = None,  system: str = None,  value: str = None,  period: 'Period' = None,  assigner: 'Reference' = None, ):
        self.resourceType: str = resourceType or "Identifier"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.use: str = use 
        self.type: 'CodeableConcept' = type 
        self.system: str = system 
        self.value: str = value 
        self.period: 'Period' = period 
        self.assigner: 'Reference' = assigner 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Identifier":
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