"""
Generated class for InsurancePlan. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Money import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Address import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class Contact(BaseModel):
    """ The contact for the health insurance product for a certain purpose.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' purpose: The type of contact
    :param 'HumanName' name: A name associated with the contact
    :param 'ContactPoint' telecom: Contact details (telephone, email, etc.)  for a contact
    :param 'Address' address: Visiting or postal addresses for the contact
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  purpose: 'CodeableConcept' = None,  name: 'HumanName' = None,  telecom: 'ContactPoint' = None,  address: 'Address' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.purpose: 'CodeableConcept' = purpose 
        self.name: 'HumanName' = name 
        self.telecom: list['ContactPoint'] = telecom or []
        self.address: 'Address' = address 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
        
    
        
    
    

class Limit(BaseModel):
    """ The specific limits on the benefit.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Quantity' value: Maximum value allowed
    :param 'CodeableConcept' code: Benefit limit details
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  value: 'Quantity' = None,  code: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.value: 'Quantity' = value 
        self.code: 'CodeableConcept' = code 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Limit":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


  
    
    

class Benefit(BaseModel):
    """ Specific benefits under this type of coverage.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of benefit
    :param str requirement: Referral requirements
    :param 'Limit' limit: Benefit limits
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  requirement: str = None,  limit: 'Limit' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.requirement: str = requirement 
        self.limit: list['Limit'] = limit or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Benefit":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


  
    
    

class Coverage(BaseModel):
    """ Details about the coverage offered by the insurance product.:param 'Reference' coverageArea: Where product applies
    :param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of coverage
    :param 'Reference' network: What networks provide coverage
    :param 'Benefit' benefit: List of benefits
    """
    def __init__(self,  coverageArea: 'Reference' = None,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  network: 'Reference' = None,  benefit: 'Benefit' = None, ):
        self.coverageArea: list['Reference'] = coverageArea or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.network: list['Reference'] = network or []
        self.benefit: list['Benefit'] = benefit or []
        

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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
        
    
    

class GeneralCost(BaseModel):
    """ Overall costs associated with the plan.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of cost
    :param int groupSize: Number of enrollees
    :param 'Money' cost: Cost value
    :param str comment: Additional cost information
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  groupSize: int = None,  cost: 'Money' = None,  comment: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.groupSize: int = groupSize 
        self.cost: 'Money' = cost 
        self.comment: str = comment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "GeneralCost":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
        
    
        
    
    

class Cost(BaseModel):
    """ List of the costs associated with a specific benefit.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of cost
    :param 'CodeableConcept' applicability: in-network | out-of-network | other
    :param 'CodeableConcept' qualifiers: Additional information about the cost
    :param 'Quantity' value: The actual cost value
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  applicability: 'CodeableConcept' = None,  qualifiers: 'CodeableConcept' = None,  value: 'Quantity' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.applicability: 'CodeableConcept' = applicability 
        self.qualifiers: list['CodeableConcept'] = qualifiers or []
        self.value: 'Quantity' = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Cost":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


  
    
    

class Benefit(BaseModel):
    """ List of the specific benefits under this category of benefit.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of specific benefit
    :param 'Cost' cost: List of the costs
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  cost: 'Cost' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.cost: list['Cost'] = cost or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Benefit":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


  
    
    

class SpecificCost(BaseModel):
    """ Costs associated with the coverage provided by the product.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' category: General category of benefit
    :param 'Benefit' benefit: Benefits list
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  category: 'CodeableConcept' = None,  benefit: 'Benefit' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.category: 'CodeableConcept' = category 
        self.benefit: list['Benefit'] = benefit or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SpecificCost":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


  
    
    

class Plan(BaseModel):
    """ Details about an insurance plan.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Business Identifier for Product
    :param 'CodeableConcept' type: Type of plan
    :param 'Reference' coverageArea: Where product applies
    :param 'Reference' network: What networks provide coverage
    :param 'GeneralCost' generalCost: Overall costs
    :param 'SpecificCost' specificCost: Specific costs
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  type: 'CodeableConcept' = None,  coverageArea: 'Reference' = None,  network: 'Reference' = None,  generalCost: 'GeneralCost' = None,  specificCost: 'SpecificCost' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.type: 'CodeableConcept' = type 
        self.coverageArea: list['Reference'] = coverageArea or []
        self.network: list['Reference'] = network or []
        self.generalCost: list['GeneralCost'] = generalCost or []
        self.specificCost: list['SpecificCost'] = specificCost or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Plan":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


class InsurancePlan(DomainResource):
    """ Details of a Health Insurance product/plan provided by an organization.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Business Identifier for Product
    :param str status: draft | active | retired | unknown
    :param 'CodeableConcept' type: Kind of product
    :param str name: Official name
    :param str alias: Alternate names
    :param 'Period' period: When the product is available
    :param 'Reference' ownedBy: Plan issuer
    :param 'Reference' administeredBy: Product administrator
    :param 'Reference' coverageArea: Where product applies
    :param 'Contact' contact: Contact for the product
    :param 'Reference' endpoint: Technical endpoint
    :param 'Reference' network: What networks are Included
    :param 'Coverage' coverage: Coverage details
    :param 'Plan' plan: Plan details
    """
    def __init__(self, resourceType: str = "InsurancePlan",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  status: str = None,  type: 'CodeableConcept' = None,  name: str = None,  alias: str = None,  period: 'Period' = None,  ownedBy: 'Reference' = None,  administeredBy: 'Reference' = None,  coverageArea: 'Reference' = None,  contact: 'Contact' = None,  endpoint: 'Reference' = None,  network: 'Reference' = None,  coverage: 'Coverage' = None,  plan: 'Plan' = None, ):
        self.resourceType: str = resourceType or "InsurancePlan"
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
        self.type: list['CodeableConcept'] = type or []
        self.name: str = name 
        self.alias: list[str] = alias or []
        self.period: 'Period' = period 
        self.ownedBy: 'Reference' = ownedBy 
        self.administeredBy: 'Reference' = administeredBy 
        self.coverageArea: list['Reference'] = coverageArea or []
        self.contact: list['Contact'] = contact or []
        self.endpoint: list['Reference'] = endpoint or []
        self.network: list['Reference'] = network or []
        self.coverage: list['Coverage'] = coverage or []
        self.plan: list['Plan'] = plan or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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