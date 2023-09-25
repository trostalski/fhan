"""
Generated class for VisionPrescription. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Prism(ModelBase):
    """ Allows for adjustment on two axis.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param float amount: Amount of adjustment
    :param str base: up | down | in | out
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  amount: float = None,  base: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.amount: float = amount 
        self.base: str = base 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Prism":
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


  
    
    

class LensSpecification(ModelBase):
    """ Contain the details of  the individual lens specifications and serves as the authorization for the fullfillment by certified professionals.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' product: Product to be supplied
    :param str eye: right | left
    :param float sphere: Power of the lens
    :param float cylinder: Lens power for astigmatism
    :param int axis: Lens meridian which contain no power for astigmatism
    :param list['Prism'] prism: Eye alignment compensation
    :param float add: Added power for multifocal levels
    :param float power: Contact lens power
    :param float backCurve: Contact lens back curvature
    :param float diameter: Contact lens diameter
    :param 'Quantity' duration: Lens wear duration
    :param str color: Color required
    :param str brand: Brand required
    :param list['Annotation'] note: Notes for coatings
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  product: 'CodeableConcept' = None,  eye: str = None,  sphere: float = None,  cylinder: float = None,  axis: int = None,  prism: list['Prism'] = None,  add: float = None,  power: float = None,  backCurve: float = None,  diameter: float = None,  duration: 'Quantity' = None,  color: str = None,  brand: str = None,  note: list['Annotation'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.product: 'CodeableConcept' = product 
        self.eye: str = eye 
        self.sphere: float = sphere 
        self.cylinder: float = cylinder 
        self.axis: int = axis 
        self.prism: list['Prism'] = prism or []
        self.add: float = add 
        self.power: float = power 
        self.backCurve: float = backCurve 
        self.diameter: float = diameter 
        self.duration: 'Quantity' = duration 
        self.color: str = color 
        self.brand: str = brand 
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "LensSpecification":
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


class VisionPrescription(DomainResource):
    """ An authorization for the provision of glasses and/or contact lenses to a patient.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for vision prescription
    :param str status: active | cancelled | draft | entered-in-error
    :param str created: Response creation date
    :param 'Reference' patient: Who prescription is for
    :param 'Reference' encounter: Created during encounter / admission / stay
    :param str dateWritten: When prescription was authorized
    :param 'Reference' prescriber: Who authorized the vision prescription
    :param list['LensSpecification'] lensSpecification: Vision lens authorization
    """
    def __init__(self, resourceType: str = "VisionPrescription",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  created: str = None,  patient: 'Reference' = None,  encounter: 'Reference' = None,  dateWritten: str = None,  prescriber: 'Reference' = None,  lensSpecification: list['LensSpecification'] = None, ):
        self.resourceType: str = resourceType or "VisionPrescription"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.created: str = created 
        self.patient: 'Reference' = patient 
        self.encounter: 'Reference' = encounter 
        self.dateWritten: str = dateWritten 
        self.prescriber: 'Reference' = prescriber 
        self.lensSpecification: list['LensSpecification'] = lensSpecification or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "VisionPrescription":
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