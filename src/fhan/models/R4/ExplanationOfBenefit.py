"""
Generated class for ExplanationOfBenefit. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Money import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Address import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class Related(BaseModel):
    """ Other claims which are related to this claim such as prior submissions or claims for related services or for the same event.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' claim: Reference to the related claim
    :param 'CodeableConcept' relationship: How the reference claim is related
    :param 'Identifier' reference: File or case reference
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  claim: 'Reference' = None,  relationship: 'CodeableConcept' = None,  reference: 'Identifier' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.claim: 'Reference' = claim 
        self.relationship: 'CodeableConcept' = relationship 
        self.reference: 'Identifier' = reference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Related":
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


    
    

class Payee(BaseModel):
    """ The party to be reimbursed for cost of the products and services according to the terms of the policy.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Category of recipient
    :param 'Reference' party: Recipient reference
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  party: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.party: 'Reference' = party 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Payee":
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


    
    

class CareTeam(BaseModel):
    """ The members of the team who provided the products and services.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Order of care team
    :param 'Reference' provider: Practitioner or organization
    :param bool responsible: Indicator of the lead practitioner
    :param 'CodeableConcept' role: Function within the team
    :param 'CodeableConcept' qualification: Practitioner credential or specialization
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  sequence: int = None,  provider: 'Reference' = None,  responsible: bool = None,  role: 'CodeableConcept' = None,  qualification: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.provider: 'Reference' = provider 
        self.responsible: bool = responsible 
        self.role: 'CodeableConcept' = role 
        self.qualification: 'CodeableConcept' = qualification 
        

    @classmethod
    def from_dict(cls, data: dict) -> "CareTeam":
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


    
    

class SupportingInfo(BaseModel):
    """ Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Information instance identifier
    :param 'CodeableConcept' category: Classification of the supplied information
    :param 'CodeableConcept' code: Type of information
    :param str timingDate: When it occurred
    :param 'Period' timingPeriod: When it occurred
    :param bool valueBoolean: Data to be provided
    :param str valueString: Data to be provided
    :param 'Quantity' valueQuantity: Data to be provided
    :param 'Attachment' valueAttachment: Data to be provided
    :param 'Reference' valueReference: Data to be provided
    :param 'Coding' reason: Explanation for the information
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  sequence: int = None,  category: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  timingDate: str = None,  timingPeriod: 'Period' = None,  valueBoolean: bool = None,  valueString: str = None,  valueQuantity: 'Quantity' = None,  valueAttachment: 'Attachment' = None,  valueReference: 'Reference' = None,  reason: 'Coding' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.category: 'CodeableConcept' = category 
        self.code: 'CodeableConcept' = code 
        self.timingDate: str = timingDate 
        self.timingPeriod: 'Period' = timingPeriod 
        self.valueBoolean: bool = valueBoolean 
        self.valueString: str = valueString 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueAttachment: 'Attachment' = valueAttachment 
        self.valueReference: 'Reference' = valueReference 
        self.reason: 'Coding' = reason 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SupportingInfo":
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


    
    

class Diagnosis(BaseModel):
    """ Information about diagnoses relevant to the claim items.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Diagnosis instance identifier
    :param 'CodeableConcept' diagnosisCodeableConcept: Nature of illness or problem
    :param 'Reference' diagnosisReference: Nature of illness or problem
    :param 'CodeableConcept' type: Timing or nature of the diagnosis
    :param 'CodeableConcept' onAdmission: Present on admission
    :param 'CodeableConcept' packageCode: Package billing code
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  sequence: int = None,  diagnosisCodeableConcept: 'CodeableConcept' = None,  diagnosisReference: 'Reference' = None,  type: 'CodeableConcept' = None,  onAdmission: 'CodeableConcept' = None,  packageCode: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.diagnosisCodeableConcept: 'CodeableConcept' = diagnosisCodeableConcept 
        self.diagnosisReference: 'Reference' = diagnosisReference 
        self.type: list['CodeableConcept'] = type or []
        self.onAdmission: 'CodeableConcept' = onAdmission 
        self.packageCode: 'CodeableConcept' = packageCode 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Diagnosis":
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


    
    

class Procedure(BaseModel):
    """ Procedures performed on the patient relevant to the billing items with the claim.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Procedure instance identifier
    :param 'CodeableConcept' type: Category of Procedure
    :param str date: When the procedure was performed
    :param 'CodeableConcept' procedureCodeableConcept: Specific clinical procedure
    :param 'Reference' procedureReference: Specific clinical procedure
    :param 'Reference' udi: Unique device identifier
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  sequence: int = None,  type: 'CodeableConcept' = None,  date: str = None,  procedureCodeableConcept: 'CodeableConcept' = None,  procedureReference: 'Reference' = None,  udi: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.type: list['CodeableConcept'] = type or []
        self.date: str = date 
        self.procedureCodeableConcept: 'CodeableConcept' = procedureCodeableConcept 
        self.procedureReference: 'Reference' = procedureReference 
        self.udi: list['Reference'] = udi or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Procedure":
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


    
    

class Insurance(BaseModel):
    """ Financial instruments for reimbursement for the health care products and services specified on the claim.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool focal: Coverage to be used for adjudication
    :param 'Reference' coverage: Insurance information
    :param str preAuthRef: Prior authorization reference number
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  focal: bool = None,  coverage: 'Reference' = None,  preAuthRef: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.focal: bool = focal 
        self.coverage: 'Reference' = coverage 
        self.preAuthRef: list[str] = preAuthRef or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Insurance":
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


    
    

class Accident(BaseModel):
    """ Details of a accident which resulted in injuries which required the products and services listed in the claim.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When the incident occurred
    :param 'CodeableConcept' type: The nature of the accident
    :param 'Address' locationAddress: Where the event occurred
    :param 'Reference' locationReference: Where the event occurred
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  date: str = None,  type: 'CodeableConcept' = None,  locationAddress: 'Address' = None,  locationReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.date: str = date 
        self.type: 'CodeableConcept' = type 
        self.locationAddress: 'Address' = locationAddress 
        self.locationReference: 'Reference' = locationReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Accident":
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


    
        
    
    

class Adjudication(BaseModel):
    """ If this item is a group then the values here are a summary of the adjudication of the detail items. If this item is a simple product or service then this is the result of the adjudication of this item.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' category: Type of adjudication information
    :param 'CodeableConcept' reason: Explanation of adjudication outcome
    :param 'Money' amount: Monetary amount
    :param float value: Non-monitary value
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  category: 'CodeableConcept' = None,  reason: 'CodeableConcept' = None,  amount: 'Money' = None,  value: float = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.category: 'CodeableConcept' = category 
        self.reason: 'CodeableConcept' = reason 
        self.amount: 'Money' = amount 
        self.value: float = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Adjudication":
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


    
        
    
    

class SubDetail(BaseModel):
    """ Third-tier of goods and services.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Product or service provided
    :param 'CodeableConcept' revenue: Revenue or cost center code
    :param 'CodeableConcept' category: Benefit classification
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param 'CodeableConcept' modifier: Service/Product billing modifiers
    :param 'CodeableConcept' programCode: Program the product or service is provided under
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param 'Money' net: Total item cost
    :param 'Reference' udi: Unique device identifier
    :param int noteNumber: Applicable note numbers
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  sequence: int = None,  revenue: 'CodeableConcept' = None,  category: 'CodeableConcept' = None,  productOrService: 'CodeableConcept' = None,  modifier: 'CodeableConcept' = None,  programCode: 'CodeableConcept' = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  udi: 'Reference' = None,  noteNumber: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.revenue: 'CodeableConcept' = revenue 
        self.category: 'CodeableConcept' = category 
        self.productOrService: 'CodeableConcept' = productOrService 
        self.modifier: list['CodeableConcept'] = modifier or []
        self.programCode: list['CodeableConcept'] = programCode or []
        self.quantity: 'Quantity' = quantity 
        self.unitPrice: 'Money' = unitPrice 
        self.factor: float = factor 
        self.net: 'Money' = net 
        self.udi: list['Reference'] = udi or []
        self.noteNumber: list[int] = noteNumber or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubDetail":
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


  
    
    

class Detail(BaseModel):
    """ Second-tier of goods and services.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Product or service provided
    :param 'CodeableConcept' revenue: Revenue or cost center code
    :param 'CodeableConcept' category: Benefit classification
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param 'CodeableConcept' modifier: Service/Product billing modifiers
    :param 'CodeableConcept' programCode: Program the product or service is provided under
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param 'Money' net: Total item cost
    :param 'Reference' udi: Unique device identifier
    :param int noteNumber: Applicable note numbers
    :param 'SubDetail' subDetail: Additional items
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  sequence: int = None,  revenue: 'CodeableConcept' = None,  category: 'CodeableConcept' = None,  productOrService: 'CodeableConcept' = None,  modifier: 'CodeableConcept' = None,  programCode: 'CodeableConcept' = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  udi: 'Reference' = None,  noteNumber: int = None,  subDetail: 'SubDetail' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.revenue: 'CodeableConcept' = revenue 
        self.category: 'CodeableConcept' = category 
        self.productOrService: 'CodeableConcept' = productOrService 
        self.modifier: list['CodeableConcept'] = modifier or []
        self.programCode: list['CodeableConcept'] = programCode or []
        self.quantity: 'Quantity' = quantity 
        self.unitPrice: 'Money' = unitPrice 
        self.factor: float = factor 
        self.net: 'Money' = net 
        self.udi: list['Reference'] = udi or []
        self.noteNumber: list[int] = noteNumber or []
        self.subDetail: list['SubDetail'] = subDetail or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Detail":
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


  
    
    

class Item(BaseModel):
    """ A claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-details.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param int careTeamSequence: Applicable care team members
    :param int diagnosisSequence: Applicable diagnoses
    :param int procedureSequence: Applicable procedures
    :param int informationSequence: Applicable exception and supporting information
    :param 'CodeableConcept' revenue: Revenue or cost center code
    :param 'CodeableConcept' category: Benefit classification
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param 'CodeableConcept' modifier: Product or service billing modifiers
    :param 'CodeableConcept' programCode: Program the product or service is provided under
    :param str servicedDate: Date or dates of service or product delivery
    :param 'Period' servicedPeriod: Date or dates of service or product delivery
    :param 'CodeableConcept' locationCodeableConcept: Place of service or where product was supplied
    :param 'Address' locationAddress: Place of service or where product was supplied
    :param 'Reference' locationReference: Place of service or where product was supplied
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param 'Money' net: Total item cost
    :param 'Reference' udi: Unique device identifier
    :param 'CodeableConcept' bodySite: Anatomical location
    :param 'CodeableConcept' subSite: Anatomical sub-location
    :param 'Reference' encounter: Encounters related to this billed item
    :param int noteNumber: Applicable note numbers
    :param 'Adjudication' adjudication: Adjudication details
    :param 'Detail' detail: Additional items
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  sequence: int = None,  careTeamSequence: int = None,  diagnosisSequence: int = None,  procedureSequence: int = None,  informationSequence: int = None,  revenue: 'CodeableConcept' = None,  category: 'CodeableConcept' = None,  productOrService: 'CodeableConcept' = None,  modifier: 'CodeableConcept' = None,  programCode: 'CodeableConcept' = None,  servicedDate: str = None,  servicedPeriod: 'Period' = None,  locationCodeableConcept: 'CodeableConcept' = None,  locationAddress: 'Address' = None,  locationReference: 'Reference' = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  udi: 'Reference' = None,  bodySite: 'CodeableConcept' = None,  subSite: 'CodeableConcept' = None,  encounter: 'Reference' = None,  noteNumber: int = None,  adjudication: 'Adjudication' = None,  detail: 'Detail' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.careTeamSequence: list[int] = careTeamSequence or []
        self.diagnosisSequence: list[int] = diagnosisSequence or []
        self.procedureSequence: list[int] = procedureSequence or []
        self.informationSequence: list[int] = informationSequence or []
        self.revenue: 'CodeableConcept' = revenue 
        self.category: 'CodeableConcept' = category 
        self.productOrService: 'CodeableConcept' = productOrService 
        self.modifier: list['CodeableConcept'] = modifier or []
        self.programCode: list['CodeableConcept'] = programCode or []
        self.servicedDate: str = servicedDate 
        self.servicedPeriod: 'Period' = servicedPeriod 
        self.locationCodeableConcept: 'CodeableConcept' = locationCodeableConcept 
        self.locationAddress: 'Address' = locationAddress 
        self.locationReference: 'Reference' = locationReference 
        self.quantity: 'Quantity' = quantity 
        self.unitPrice: 'Money' = unitPrice 
        self.factor: float = factor 
        self.net: 'Money' = net 
        self.udi: list['Reference'] = udi or []
        self.bodySite: 'CodeableConcept' = bodySite 
        self.subSite: list['CodeableConcept'] = subSite or []
        self.encounter: list['Reference'] = encounter or []
        self.noteNumber: list[int] = noteNumber or []
        self.adjudication: list['Adjudication'] = adjudication or []
        self.detail: list['Detail'] = detail or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Item":
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


    
        
    
        
    
    

class SubDetail(BaseModel):
    """ The third-tier service adjudications for payor added services.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param 'CodeableConcept' modifier: Service/Product billing modifiers
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param 'Money' net: Total item cost
    :param int noteNumber: Applicable note numbers
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  productOrService: 'CodeableConcept' = None,  modifier: 'CodeableConcept' = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  noteNumber: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.productOrService: 'CodeableConcept' = productOrService 
        self.modifier: list['CodeableConcept'] = modifier or []
        self.quantity: 'Quantity' = quantity 
        self.unitPrice: 'Money' = unitPrice 
        self.factor: float = factor 
        self.net: 'Money' = net 
        self.noteNumber: list[int] = noteNumber or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubDetail":
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


  
    
    

class Detail(BaseModel):
    """ The second-tier service adjudications for payor added services.:param int detailSequence: Detail sequence number
    :param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param 'CodeableConcept' modifier: Service/Product billing modifiers
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param 'Money' net: Total item cost
    :param int noteNumber: Applicable note numbers
    :param 'SubDetail' subDetail: Insurer added line items
    """
    def __init__(self,  detailSequence: int = None,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  productOrService: 'CodeableConcept' = None,  modifier: 'CodeableConcept' = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  noteNumber: int = None,  subDetail: 'SubDetail' = None, ):
        self.detailSequence: list[int] = detailSequence or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.productOrService: 'CodeableConcept' = productOrService 
        self.modifier: list['CodeableConcept'] = modifier or []
        self.quantity: 'Quantity' = quantity 
        self.unitPrice: 'Money' = unitPrice 
        self.factor: float = factor 
        self.net: 'Money' = net 
        self.noteNumber: list[int] = noteNumber or []
        self.subDetail: list['SubDetail'] = subDetail or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Detail":
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


  
    
    

class AddItem(BaseModel):
    """ The first-tier service adjudications for payor added product or service lines.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Item sequence number
    :param int detailSequence: Detail sequence number
    :param int subDetailSequence: Subdetail sequence number
    :param 'Reference' provider: Authorized providers
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param 'CodeableConcept' modifier: Service/Product billing modifiers
    :param 'CodeableConcept' programCode: Program the product or service is provided under
    :param str servicedDate: Date or dates of service or product delivery
    :param 'Period' servicedPeriod: Date or dates of service or product delivery
    :param 'CodeableConcept' locationCodeableConcept: Place of service or where product was supplied
    :param 'Address' locationAddress: Place of service or where product was supplied
    :param 'Reference' locationReference: Place of service or where product was supplied
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param 'Money' net: Total item cost
    :param 'CodeableConcept' bodySite: Anatomical location
    :param 'CodeableConcept' subSite: Anatomical sub-location
    :param int noteNumber: Applicable note numbers
    :param 'Detail' detail: Insurer added line items
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  itemSequence: int = None,  detailSequence: int = None,  subDetailSequence: int = None,  provider: 'Reference' = None,  productOrService: 'CodeableConcept' = None,  modifier: 'CodeableConcept' = None,  programCode: 'CodeableConcept' = None,  servicedDate: str = None,  servicedPeriod: 'Period' = None,  locationCodeableConcept: 'CodeableConcept' = None,  locationAddress: 'Address' = None,  locationReference: 'Reference' = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  bodySite: 'CodeableConcept' = None,  subSite: 'CodeableConcept' = None,  noteNumber: int = None,  detail: 'Detail' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemSequence: list[int] = itemSequence or []
        self.detailSequence: list[int] = detailSequence or []
        self.subDetailSequence: list[int] = subDetailSequence or []
        self.provider: list['Reference'] = provider or []
        self.productOrService: 'CodeableConcept' = productOrService 
        self.modifier: list['CodeableConcept'] = modifier or []
        self.programCode: list['CodeableConcept'] = programCode or []
        self.servicedDate: str = servicedDate 
        self.servicedPeriod: 'Period' = servicedPeriod 
        self.locationCodeableConcept: 'CodeableConcept' = locationCodeableConcept 
        self.locationAddress: 'Address' = locationAddress 
        self.locationReference: 'Reference' = locationReference 
        self.quantity: 'Quantity' = quantity 
        self.unitPrice: 'Money' = unitPrice 
        self.factor: float = factor 
        self.net: 'Money' = net 
        self.bodySite: 'CodeableConcept' = bodySite 
        self.subSite: list['CodeableConcept'] = subSite or []
        self.noteNumber: list[int] = noteNumber or []
        self.detail: list['Detail'] = detail or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AddItem":
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


    
    

class Total(BaseModel):
    """ Categorized monetary totals for the adjudication.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' category: Type of adjudication information
    :param 'Money' amount: Financial total for the category
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  category: 'CodeableConcept' = None,  amount: 'Money' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.category: 'CodeableConcept' = category 
        self.amount: 'Money' = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Total":
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


    
    

class Payment(BaseModel):
    """ Payment details for the adjudication of the claim.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Partial or complete payment
    :param 'Money' adjustment: Payment adjustment for non-claim issues
    :param 'CodeableConcept' adjustmentReason: Explanation for the variance
    :param str date: Expected date of payment
    :param 'Money' amount: Payable amount after adjustment
    :param 'Identifier' identifier: Business identifier for the payment
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  adjustment: 'Money' = None,  adjustmentReason: 'CodeableConcept' = None,  date: str = None,  amount: 'Money' = None,  identifier: 'Identifier' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.adjustment: 'Money' = adjustment 
        self.adjustmentReason: 'CodeableConcept' = adjustmentReason 
        self.date: str = date 
        self.amount: 'Money' = amount 
        self.identifier: 'Identifier' = identifier 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Payment":
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


    
    

class ProcessNote(BaseModel):
    """ A note that describes or explains adjudication results in a human readable form.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Note instance identifier
    :param str type: display | print | printoper
    :param str text: Note explanatory text
    :param 'CodeableConcept' language: Language of the text
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  number: int = None,  type: str = None,  text: str = None,  language: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.number: int = number 
        self.type: str = type 
        self.text: str = text 
        self.language: 'CodeableConcept' = language 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ProcessNote":
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


    
        
    
    

class Financial(BaseModel):
    """ Benefits Used to date.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Benefit classification
    :param int allowedUnsignedInt: Benefits allowed
    :param str allowedString: Benefits allowed
    :param 'Money' allowedMoney: Benefits allowed
    :param int usedUnsignedInt: Benefits used
    :param 'Money' usedMoney: Benefits used
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  allowedUnsignedInt: int = None,  allowedString: str = None,  allowedMoney: 'Money' = None,  usedUnsignedInt: int = None,  usedMoney: 'Money' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.allowedUnsignedInt: int = allowedUnsignedInt 
        self.allowedString: str = allowedString 
        self.allowedMoney: 'Money' = allowedMoney 
        self.usedUnsignedInt: int = usedUnsignedInt 
        self.usedMoney: 'Money' = usedMoney 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Financial":
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


  
    
    

class BenefitBalance(BaseModel):
    """ Balance by Benefit Category.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' category: Benefit classification
    :param bool excluded: Excluded from the plan
    :param str name: Short name for the benefit
    :param str description: Description of the benefit or services covered
    :param 'CodeableConcept' network: In or out of network
    :param 'CodeableConcept' unit: Individual or family
    :param 'CodeableConcept' term: Annual or lifetime
    :param 'Financial' financial: Benefit Summary
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  category: 'CodeableConcept' = None,  excluded: bool = None,  name: str = None,  description: str = None,  network: 'CodeableConcept' = None,  unit: 'CodeableConcept' = None,  term: 'CodeableConcept' = None,  financial: 'Financial' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.category: 'CodeableConcept' = category 
        self.excluded: bool = excluded 
        self.name: str = name 
        self.description: str = description 
        self.network: 'CodeableConcept' = network 
        self.unit: 'CodeableConcept' = unit 
        self.term: 'CodeableConcept' = term 
        self.financial: list['Financial'] = financial or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "BenefitBalance":
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


class ExplanationOfBenefit(DomainResource):
    """ This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Business Identifier for the resource
    :param str status: active | cancelled | draft | entered-in-error
    :param 'CodeableConcept' type: Category or discipline
    :param 'CodeableConcept' subType: More granular claim type
    :param str use: claim | preauthorization | predetermination
    :param 'Reference' patient: The recipient of the products and services
    :param 'Period' billablePeriod: Relevant time frame for the claim
    :param str created: Response creation date
    :param 'Reference' enterer: Author of the claim
    :param 'Reference' insurer: Party responsible for reimbursement
    :param 'Reference' provider: Party responsible for the claim
    :param 'CodeableConcept' priority: Desired processing urgency
    :param 'CodeableConcept' fundsReserveRequested: For whom to reserve funds
    :param 'CodeableConcept' fundsReserve: Funds reserved status
    :param 'Related' related: Prior or corollary claims
    :param 'Reference' prescription: Prescription authorizing services or products
    :param 'Reference' originalPrescription: Original prescription if superceded by fulfiller
    :param 'Payee' payee: Recipient of benefits payable
    :param 'Reference' referral: Treatment Referral
    :param 'Reference' facility: Servicing Facility
    :param 'Reference' claim: Claim reference
    :param 'Reference' claimResponse: Claim response reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param str preAuthRef: Preauthorization reference
    :param 'Period' preAuthRefPeriod: Preauthorization in-effect period
    :param 'CareTeam' careTeam: Care Team members
    :param 'SupportingInfo' supportingInfo: Supporting information
    :param 'Diagnosis' diagnosis: Pertinent diagnosis information
    :param 'Procedure' procedure: Clinical procedures performed
    :param int precedence: Precedence (primary, secondary, etc.)
    :param 'Insurance' insurance: Patient insurance information
    :param 'Accident' accident: Details of the event
    :param 'Item' item: Product or service provided
    :param 'AddItem' addItem: Insurer added line items
    :param 'Total' total: Adjudication totals
    :param 'Payment' payment: Payment Details
    :param 'CodeableConcept' formCode: Printed form identifier
    :param 'Attachment' form: Printed reference or actual form
    :param 'ProcessNote' processNote: Note concerning adjudication
    :param 'Period' benefitPeriod: When the benefits are applicable
    :param 'BenefitBalance' benefitBalance: Balance by Benefit Category
    """
    def __init__(self, resourceType: str = "ExplanationOfBenefit",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  status: str = None,  type: 'CodeableConcept' = None,  subType: 'CodeableConcept' = None,  use: str = None,  patient: 'Reference' = None,  billablePeriod: 'Period' = None,  created: str = None,  enterer: 'Reference' = None,  insurer: 'Reference' = None,  provider: 'Reference' = None,  priority: 'CodeableConcept' = None,  fundsReserveRequested: 'CodeableConcept' = None,  fundsReserve: 'CodeableConcept' = None,  related: 'Related' = None,  prescription: 'Reference' = None,  originalPrescription: 'Reference' = None,  payee: 'Payee' = None,  referral: 'Reference' = None,  facility: 'Reference' = None,  claim: 'Reference' = None,  claimResponse: 'Reference' = None,  outcome: str = None,  disposition: str = None,  preAuthRef: str = None,  preAuthRefPeriod: 'Period' = None,  careTeam: 'CareTeam' = None,  supportingInfo: 'SupportingInfo' = None,  diagnosis: 'Diagnosis' = None,  procedure: 'Procedure' = None,  precedence: int = None,  insurance: 'Insurance' = None,  accident: 'Accident' = None,  item: 'Item' = None,  addItem: 'AddItem' = None,  total: 'Total' = None,  payment: 'Payment' = None,  formCode: 'CodeableConcept' = None,  form: 'Attachment' = None,  processNote: 'ProcessNote' = None,  benefitPeriod: 'Period' = None,  benefitBalance: 'BenefitBalance' = None, ):
        self.resourceType: str = resourceType or "ExplanationOfBenefit"
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
        self.subType: 'CodeableConcept' = subType 
        self.use: str = use 
        self.patient: 'Reference' = patient 
        self.billablePeriod: 'Period' = billablePeriod 
        self.created: str = created 
        self.enterer: 'Reference' = enterer 
        self.insurer: 'Reference' = insurer 
        self.provider: 'Reference' = provider 
        self.priority: 'CodeableConcept' = priority 
        self.fundsReserveRequested: 'CodeableConcept' = fundsReserveRequested 
        self.fundsReserve: 'CodeableConcept' = fundsReserve 
        self.related: list['Related'] = related or []
        self.prescription: 'Reference' = prescription 
        self.originalPrescription: 'Reference' = originalPrescription 
        self.payee: 'Payee' = payee 
        self.referral: 'Reference' = referral 
        self.facility: 'Reference' = facility 
        self.claim: 'Reference' = claim 
        self.claimResponse: 'Reference' = claimResponse 
        self.outcome: str = outcome 
        self.disposition: str = disposition 
        self.preAuthRef: list[str] = preAuthRef or []
        self.preAuthRefPeriod: list['Period'] = preAuthRefPeriod or []
        self.careTeam: list['CareTeam'] = careTeam or []
        self.supportingInfo: list['SupportingInfo'] = supportingInfo or []
        self.diagnosis: list['Diagnosis'] = diagnosis or []
        self.procedure: list['Procedure'] = procedure or []
        self.precedence: int = precedence 
        self.insurance: list['Insurance'] = insurance or []
        self.accident: 'Accident' = accident 
        self.item: list['Item'] = item or []
        self.addItem: list['AddItem'] = addItem or []
        self.total: list['Total'] = total or []
        self.payment: 'Payment' = payment 
        self.formCode: 'CodeableConcept' = formCode 
        self.form: 'Attachment' = form 
        self.processNote: list['ProcessNote'] = processNote or []
        self.benefitPeriod: 'Period' = benefitPeriod 
        self.benefitBalance: list['BenefitBalance'] = benefitBalance or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
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