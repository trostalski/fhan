"""
Generated class for MedicinalProductPharmaceutical. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Characteristics(ModelBase):
    """ Characteristics e.g. a products onset of action.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: A coded characteristic
    :param 'CodeableConcept' status: The status of characteristic e.g. assigned or pending
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  status: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.status: 'CodeableConcept' = status 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Characteristics":
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


    
        
    
        
    
    

class WithdrawalPeriod(ModelBase):
    """ A species specific time during which consumption of animal product is not appropriate.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' tissue: Coded expression for the type of tissue for which the withdrawal period applues, e.g. meat, milk
    :param 'Quantity' value: A value for the time
    :param str supportingInformation: Extra information about the withdrawal period
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  tissue: 'CodeableConcept' = None,  value: 'Quantity' = None,  supportingInformation: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.tissue: 'CodeableConcept' = tissue 
        self.value: 'Quantity' = value 
        self.supportingInformation: str = supportingInformation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "WithdrawalPeriod":
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


  
    
    

class TargetSpecies(ModelBase):
    """ A species for which this route applies.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Coded expression for the species
    :param list['WithdrawalPeriod'] withdrawalPeriod: A species specific time during which consumption of animal product is not appropriate
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  withdrawalPeriod: list['WithdrawalPeriod'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.withdrawalPeriod: list['WithdrawalPeriod'] = withdrawalPeriod or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "TargetSpecies":
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


  
    
    

class RouteOfAdministration(ModelBase):
    """ The path by which the pharmaceutical product is taken into or makes contact with the body.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Coded expression for the route
    :param 'Quantity' firstDose: The first dose (dose quantity) administered in humans can be specified, for a product under investigation, using a numerical value and its unit of measurement
    :param 'Quantity' maxSingleDose: The maximum single dose that can be administered as per the protocol of a clinical trial can be specified using a numerical value and its unit of measurement
    :param 'Quantity' maxDosePerDay: The maximum dose per day (maximum dose quantity to be administered in any one 24-h period) that can be administered as per the protocol referenced in the clinical trial authorisation
    :param 'Ratio' maxDosePerTreatmentPeriod: The maximum dose per treatment period that can be administered as per the protocol referenced in the clinical trial authorisation
    :param 'Duration' maxTreatmentPeriod: The maximum treatment period during which an Investigational Medicinal Product can be administered as per the protocol referenced in the clinical trial authorisation
    :param list['TargetSpecies'] targetSpecies: A species for which this route applies
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  firstDose: 'Quantity' = None,  maxSingleDose: 'Quantity' = None,  maxDosePerDay: 'Quantity' = None,  maxDosePerTreatmentPeriod: 'Ratio' = None,  maxTreatmentPeriod: 'Duration' = None,  targetSpecies: list['TargetSpecies'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.firstDose: 'Quantity' = firstDose 
        self.maxSingleDose: 'Quantity' = maxSingleDose 
        self.maxDosePerDay: 'Quantity' = maxDosePerDay 
        self.maxDosePerTreatmentPeriod: 'Ratio' = maxDosePerTreatmentPeriod 
        self.maxTreatmentPeriod: 'Duration' = maxTreatmentPeriod 
        self.targetSpecies: list['TargetSpecies'] = targetSpecies or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RouteOfAdministration":
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


class MedicinalProductPharmaceutical(DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose form.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: An identifier for the pharmaceutical medicinal product
    :param 'CodeableConcept' administrableDoseForm: The administrable dose form, after necessary reconstitution
    :param 'CodeableConcept' unitOfPresentation: Todo
    :param list['Reference'] ingredient: Ingredient
    :param list['Reference'] device: Accompanying device
    :param list['Characteristics'] characteristics: Characteristics e.g. a products onset of action
    :param list['RouteOfAdministration'] routeOfAdministration: The path by which the pharmaceutical product is taken into or makes contact with the body
    """
    def __init__(self, resourceType: str = "MedicinalProductPharmaceutical",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  administrableDoseForm: 'CodeableConcept' = None,  unitOfPresentation: 'CodeableConcept' = None,  ingredient: list['Reference'] = None,  device: list['Reference'] = None,  characteristics: list['Characteristics'] = None,  routeOfAdministration: list['RouteOfAdministration'] = None, ):
        self.resourceType: str = resourceType or "MedicinalProductPharmaceutical"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.administrableDoseForm: 'CodeableConcept' = administrableDoseForm 
        self.unitOfPresentation: 'CodeableConcept' = unitOfPresentation 
        self.ingredient: list['Reference'] = ingredient or []
        self.device: list['Reference'] = device or []
        self.characteristics: list['Characteristics'] = characteristics or []
        self.routeOfAdministration: list['RouteOfAdministration'] = routeOfAdministration or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductPharmaceutical":
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