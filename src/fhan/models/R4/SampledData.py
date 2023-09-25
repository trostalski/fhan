"""
Generated class for SampledData. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class SampledData(ModelBase):
    """ Base StructureDefinition for SampledData Type: A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'Quantity' origin: Zero value and units
    :param float period: Number of milliseconds between samples
    :param float factor: Multiply data by this before adding to origin
    :param float lowerLimit: Lower limit of detection
    :param float upperLimit: Upper limit of detection
    :param int dimensions: Number of sample points at each time point
    :param str data: Decimal values with spaces, or "E" | "U" | "L"
    """
    def __init__(self, resourceType: str = "SampledData",  id: str = None,  extension: list['Extension'] = None,  origin: 'Quantity' = None,  period: float = None,  factor: float = None,  lowerLimit: float = None,  upperLimit: float = None,  dimensions: int = None,  data: str = None, ):
        self.resourceType: str = resourceType or "SampledData"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.origin: 'Quantity' = origin 
        self.period: float = period 
        self.factor: float = factor 
        self.lowerLimit: float = lowerLimit 
        self.upperLimit: float = upperLimit 
        self.dimensions: int = dimensions 
        self.data: str = data 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SampledData":
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