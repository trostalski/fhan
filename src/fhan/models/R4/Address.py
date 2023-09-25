"""
Generated class for Address. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Address(ModelBase):
    """ Base StructureDefinition for Address Type: An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str use: home | work | temp | old | billing - purpose of this address
    :param str type: postal | physical | both
    :param str text: Text representation of the address
    :param str line: Street name, number, direction & P.O. Box etc.
    :param str city: Name of city, town etc.
    :param str district: District name (aka county)
    :param str state: Sub-unit of country (abbreviations ok)
    :param str postalCode: Postal code for area
    :param str country: Country (e.g. can be ISO 3166 2 or 3 letter code)
    :param 'Period' period: Time period when address was/is in use
    """
    def __init__(self, resourceType: str = "Address",  id: str = None,  extension: list['Extension'] = None,  use: str = None,  type: str = None,  text: str = None,  line: str = None,  city: str = None,  district: str = None,  state: str = None,  postalCode: str = None,  country: str = None,  period: 'Period' = None, ):
        self.resourceType: str = resourceType or "Address"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.use: str = use 
        self.type: str = type 
        self.text: str = text 
        self.line: str = line or []
        self.city: str = city 
        self.district: str = district 
        self.state: str = state 
        self.postalCode: str = postalCode 
        self.country: str = country 
        self.period: 'Period' = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Address":
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