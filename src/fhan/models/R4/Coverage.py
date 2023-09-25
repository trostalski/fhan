"""
Generated class for Coverage. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Money import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class _class(ModelBase):
    """ A suite of underwriter specific classifiers.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of class such as 'group' or 'plan'
    :param str value: Value associated with the type
    :param str name: Human readable description of the type and value
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  value: str = None,  name: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.value: str = value 
        self.name: str = name 
        

    @classmethod
    def from_dict(cls, data: dict) -> "_class":
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


    
        
    
    

class Exception(ModelBase):
    """ A suite of codes indicating exceptions or reductions to patient costs and their effective periods.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Exception category
    :param 'Period' period: The effective period of the exception
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  period: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.period: 'Period' = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Exception":
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


  
    
    

class CostToBeneficiary(ModelBase):
    """ A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Cost category
    :param 'Quantity' valueQuantity: The amount or percentage due from the beneficiary
    :param 'Money' valueMoney: The amount or percentage due from the beneficiary
    :param list['Exception'] exception: Exceptions for patient payments
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  valueQuantity: 'Quantity' = None,  valueMoney: 'Money' = None,  exception: list['Exception'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueMoney: 'Money' = valueMoney 
        self.exception: list['Exception'] = exception or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "CostToBeneficiary":
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


class Coverage(DomainResource):
    """ Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for the coverage
    :param str status: active | cancelled | draft | entered-in-error
    :param 'CodeableConcept' type: Coverage category such as medical or accident
    :param 'Reference' policyHolder: Owner of the policy
    :param 'Reference' subscriber: Subscriber to the policy
    :param str subscriberId: ID assigned to the subscriber
    :param 'Reference' beneficiary: Plan beneficiary
    :param str dependent: Dependent number
    :param 'CodeableConcept' relationship: Beneficiary relationship to the subscriber
    :param 'Period' period: Coverage start and end dates
    :param list['Reference'] payor: Issuer of the policy
    :param list['_class'] _class: Additional coverage classifications
    :param int order: Relative order of the coverage
    :param str network: Insurer network
    :param list['CostToBeneficiary'] costToBeneficiary: Patient payments for services/products
    :param bool subrogation: Reimbursement to insurer
    :param list['Reference'] contract: Contract details
    """
    def __init__(self, resourceType: str = "Coverage",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  type: 'CodeableConcept' = None,  policyHolder: 'Reference' = None,  subscriber: 'Reference' = None,  subscriberId: str = None,  beneficiary: 'Reference' = None,  dependent: str = None,  relationship: 'CodeableConcept' = None,  period: 'Period' = None,  payor: list['Reference'] = None,  _class: list['_class'] = None,  order: int = None,  network: str = None,  costToBeneficiary: list['CostToBeneficiary'] = None,  subrogation: bool = None,  contract: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "Coverage"
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
        self.type: 'CodeableConcept' = type 
        self.policyHolder: 'Reference' = policyHolder 
        self.subscriber: 'Reference' = subscriber 
        self.subscriberId: str = subscriberId 
        self.beneficiary: 'Reference' = beneficiary 
        self.dependent: str = dependent 
        self.relationship: 'CodeableConcept' = relationship 
        self.period: 'Period' = period 
        self.payor: list['Reference'] = payor or []
        self._class: list['_class'] = _class or []
        self.order: int = order 
        self.network: str = network 
        self.costToBeneficiary: list['CostToBeneficiary'] = costToBeneficiary or []
        self.subrogation: bool = subrogation 
        self.contract: list['Reference'] = contract or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
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