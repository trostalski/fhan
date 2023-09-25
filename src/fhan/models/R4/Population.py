"""
Generated class for Population. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Population(ModelBase):
    """ Base StructureDefinition for Population Type: A populatioof people with some set of grouping criteria.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Range' ageRange: The age of the specific population
    :param 'CodeableConcept' ageCodeableConcept: The age of the specific population
    :param 'CodeableConcept' gender: The gender of the specific population
    :param 'CodeableConcept' race: Race of the specific population
    :param 'CodeableConcept' physiologicalCondition: The existing physiological conditions of the specific population to which this applies
    """
    def __init__(self, resourceType: str = "Population",  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  ageRange: 'Range' = None,  ageCodeableConcept: 'CodeableConcept' = None,  gender: 'CodeableConcept' = None,  race: 'CodeableConcept' = None,  physiologicalCondition: 'CodeableConcept' = None, ):
        self.resourceType: str = resourceType or "Population"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.ageRange: 'Range' = ageRange 
        self.ageCodeableConcept: 'CodeableConcept' = ageCodeableConcept 
        self.gender: 'CodeableConcept' = gender 
        self.race: 'CodeableConcept' = race 
        self.physiologicalCondition: 'CodeableConcept' = physiologicalCondition 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Population":
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