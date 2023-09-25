"""
Generated class for Group. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Characteristic(ModelBase):
    """ Identifies traits whose presence r absence is shared by members of the group.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Kind of characteristic
    :param 'CodeableConcept' valueCodeableConcept: Value held by characteristic
    :param bool valueBoolean: Value held by characteristic
    :param 'Quantity' valueQuantity: Value held by characteristic
    :param 'Range' valueRange: Value held by characteristic
    :param 'Reference' valueReference: Value held by characteristic
    :param bool exclude: Group includes or excludes
    :param 'Period' period: Period over which characteristic is tested
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueBoolean: bool = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueReference: 'Reference' = None,  exclude: bool = None,  period: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueBoolean: bool = valueBoolean 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueRange: 'Range' = valueRange 
        self.valueReference: 'Reference' = valueReference 
        self.exclude: bool = exclude 
        self.period: 'Period' = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Characteristic":
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


    
    

class Member(ModelBase):
    """ Identifies the resource instances that are members of the group.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' entity: Reference to the group member
    :param 'Period' period: Period member belonged to the group
    :param bool inactive: If member is no longer in group
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  entity: 'Reference' = None,  period: 'Period' = None,  inactive: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.entity: 'Reference' = entity 
        self.period: 'Period' = period 
        self.inactive: bool = inactive 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Member":
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


class Group(DomainResource):
    """ Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique id
    :param bool active: Whether this group's record is in active use
    :param str type: person | animal | practitioner | device | medication | substance
    :param bool actual: Descriptive or actual
    :param 'CodeableConcept' code: Kind of Group members
    :param str name: Label for Group
    :param int quantity: Number of members
    :param 'Reference' managingEntity: Entity that is the custodian of the Group's definition
    :param list['Characteristic'] characteristic: Include / Exclude group members by Trait
    :param list['Member'] member: Who or what is in group
    """
    def __init__(self, resourceType: str = "Group",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  active: bool = None,  type: str = None,  actual: bool = None,  code: 'CodeableConcept' = None,  name: str = None,  quantity: int = None,  managingEntity: 'Reference' = None,  characteristic: list['Characteristic'] = None,  member: list['Member'] = None, ):
        self.resourceType: str = resourceType or "Group"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.active: bool = active 
        self.type: str = type 
        self.actual: bool = actual 
        self.code: 'CodeableConcept' = code 
        self.name: str = name 
        self.quantity: int = quantity 
        self.managingEntity: 'Reference' = managingEntity 
        self.characteristic: list['Characteristic'] = characteristic or []
        self.member: list['Member'] = member or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Group":
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