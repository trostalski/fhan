"""
Generated class for TriggerDefinition. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Expression import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import ModelBase

class TriggerDefinition(ModelBase):
    """ Base StructureDefinition for TriggerDefinition Type: A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str type: named-event | periodic | data-changed | data-added | data-modified | data-removed | data-accessed | data-access-ended
    :param str name: Name or URI that identifies the event
    :param 'Timing' timingTiming: Timing of the event
    :param 'Reference' timingReference: Timing of the event
    :param str timingDate: Timing of the event
    :param str timingDateTime: Timing of the event
    :param list['DataRequirement'] data: Triggering data of the event (multiple = 'and')
    :param 'Expression' condition: Whether the event triggers (boolean expression)
    """
    def __init__(self, resourceType: str = "TriggerDefinition",  id: str = None,  extension: list['Extension'] = None,  type: str = None,  name: str = None,  timingTiming: 'Timing' = None,  timingReference: 'Reference' = None,  timingDate: str = None,  timingDateTime: str = None,  data: list['DataRequirement'] = None,  condition: 'Expression' = None, ):
        self.resourceType: str = resourceType or "TriggerDefinition"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: str = type 
        self.name: str = name 
        self.timingTiming: 'Timing' = timingTiming 
        self.timingReference: 'Reference' = timingReference 
        self.timingDate: str = timingDate 
        self.timingDateTime: str = timingDateTime 
        self.data: list['DataRequirement'] = data or []
        self.condition: 'Expression' = condition 
        

    @classmethod
    def from_dict(cls, data: dict) -> "TriggerDefinition":
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