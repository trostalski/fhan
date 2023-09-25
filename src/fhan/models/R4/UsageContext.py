"""
Generated class for UsageContext. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Quantity import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import ModelBase

class UsageContext(ModelBase):
    """ Base StructureDefinition for UsageContext Type: Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact. This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific context of care (e.g., venue, care setting, provider of care).
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'Coding' code: Type of context being specified
    :param 'CodeableConcept' valueCodeableConcept: Value that defines the context
    :param 'Quantity' valueQuantity: Value that defines the context
    :param 'Range' valueRange: Value that defines the context
    :param 'Reference' valueReference: Value that defines the context
    """
    def __init__(self, resourceType: str = "UsageContext",  id: str = None,  extension: list['Extension'] = None,  code: 'Coding' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueReference: 'Reference' = None, ):
        self.resourceType: str = resourceType or "UsageContext"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.code: 'Coding' = code 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueRange: 'Range' = valueRange 
        self.valueReference: 'Reference' = valueReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "UsageContext":
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