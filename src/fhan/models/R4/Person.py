"""
Generated class for Person. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Address import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Link(ModelBase):
    """ Link to a resource that concerns the same actual person.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' target: The resource to which this actual person is associated
    :param str assurance: level1 | level2 | level3 | level4
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  target: 'Reference' = None,  assurance: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.target: 'Reference' = target 
        self.assurance: str = assurance 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Link":
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


class Person(DomainResource):
    """ Demographics and administrative information about a person independent of a specific health-related context.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: A human identifier for this person
    :param list['HumanName'] name: A name associated with the person
    :param list['ContactPoint'] telecom: A contact detail for the person
    :param str gender: male | female | other | unknown
    :param str birthDate: The date on which the person was born
    :param list['Address'] address: One or more addresses for the person
    :param 'Attachment' photo: Image of the person
    :param 'Reference' managingOrganization: The organization that is the custodian of the person record
    :param bool active: This person's record is in active use
    :param list['Link'] link: Link to a resource that concerns the same actual person
    """
    def __init__(self, resourceType: str = "Person",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  name: list['HumanName'] = None,  telecom: list['ContactPoint'] = None,  gender: str = None,  birthDate: str = None,  address: list['Address'] = None,  photo: 'Attachment' = None,  managingOrganization: 'Reference' = None,  active: bool = None,  link: list['Link'] = None, ):
        self.resourceType: str = resourceType or "Person"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.name: list['HumanName'] = name or []
        self.telecom: list['ContactPoint'] = telecom or []
        self.gender: str = gender 
        self.birthDate: str = birthDate 
        self.address: list['Address'] = address or []
        self.photo: 'Attachment' = photo 
        self.managingOrganization: 'Reference' = managingOrganization 
        self.active: bool = active 
        self.link: list['Link'] = link or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Person":
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