"""
Generated class for Claim. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Address import *
from fhan.models.R4.Money import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Related(ModelBase):
    """ Other claims which are related to this claim such as prior submissions or claims for related services or for the same event.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' claim: Reference to the related claim
    :param 'CodeableConcept' relationship: How the reference claim is related
    :param 'Identifier' reference: File or case reference
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  claim: 'Reference' = None,  relationship: 'CodeableConcept' = None,  reference: 'Identifier' = None, ):
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


    
    

class Payee(ModelBase):
    """ The party to be reimbursed for cost of the products and services according to the terms of the policy.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Category of recipient
    :param 'Reference' party: Recipient reference
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  party: 'Reference' = None, ):
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


    
    

class CareTeam(ModelBase):
    """ The members of the team who provided the products and services.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Order of care team
    :param 'Reference' provider: Practitioner or organization
    :param bool responsible: Indicator of the lead practitioner
    :param 'CodeableConcept' role: Function within the team
    :param 'CodeableConcept' qualification: Practitioner credential or specialization
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  provider: 'Reference' = None,  responsible: bool = None,  role: 'CodeableConcept' = None,  qualification: 'CodeableConcept' = None, ):
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


    
    

class SupportingInfo(ModelBase):
    """ Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
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
    :param 'CodeableConcept' reason: Explanation for the information
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  category: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  timingDate: str = None,  timingPeriod: 'Period' = None,  valueBoolean: bool = None,  valueString: str = None,  valueQuantity: 'Quantity' = None,  valueAttachment: 'Attachment' = None,  valueReference: 'Reference' = None,  reason: 'CodeableConcept' = None, ):
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
        self.reason: 'CodeableConcept' = reason 
        

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


    
    

class Diagnosis(ModelBase):
    """ Information about diagnoses relevant to the claim items.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Diagnosis instance identifier
    :param 'CodeableConcept' diagnosisCodeableConcept: Nature of illness or problem
    :param 'Reference' diagnosisReference: Nature of illness or problem
    :param list['CodeableConcept'] type: Timing or nature of the diagnosis
    :param 'CodeableConcept' onAdmission: Present on admission
    :param 'CodeableConcept' packageCode: Package billing code
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  diagnosisCodeableConcept: 'CodeableConcept' = None,  diagnosisReference: 'Reference' = None,  type: list['CodeableConcept'] = None,  onAdmission: 'CodeableConcept' = None,  packageCode: 'CodeableConcept' = None, ):
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


    
    

class Procedure(ModelBase):
    """ Procedures performed on the patient relevant to the billing items with the claim.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Procedure instance identifier
    :param list['CodeableConcept'] type: Category of Procedure
    :param str date: When the procedure was performed
    :param 'CodeableConcept' procedureCodeableConcept: Specific clinical procedure
    :param 'Reference' procedureReference: Specific clinical procedure
    :param list['Reference'] udi: Unique device identifier
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  type: list['CodeableConcept'] = None,  date: str = None,  procedureCodeableConcept: 'CodeableConcept' = None,  procedureReference: 'Reference' = None,  udi: list['Reference'] = None, ):
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


    
    

class Insurance(ModelBase):
    """ Financial instruments for reimbursement for the health care products and services specified on the claim.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Insurance instance identifier
    :param bool focal: Coverage to be used for adjudication
    :param 'Identifier' identifier: Pre-assigned Claim number
    :param 'Reference' coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    :param str preAuthRef: Prior authorization reference number
    :param 'Reference' claimResponse: Adjudication results
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  focal: bool = None,  identifier: 'Identifier' = None,  coverage: 'Reference' = None,  businessArrangement: str = None,  preAuthRef: str = None,  claimResponse: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.focal: bool = focal 
        self.identifier: 'Identifier' = identifier 
        self.coverage: 'Reference' = coverage 
        self.businessArrangement: str = businessArrangement 
        self.preAuthRef: str = preAuthRef or []
        self.claimResponse: 'Reference' = claimResponse 
        

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


    
    

class Accident(ModelBase):
    """ Details of an accident which resulted in injuries which required the products and services listed in the claim.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When the incident occurred
    :param 'CodeableConcept' type: The nature of the accident
    :param 'Address' locationAddress: Where the event occurred
    :param 'Reference' locationReference: Where the event occurred
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  date: str = None,  type: 'CodeableConcept' = None,  locationAddress: 'Address' = None,  locationReference: 'Reference' = None, ):
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


    
        
    
        
    
    

class SubDetail(ModelBase):
    """ A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple items.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param 'CodeableConcept' revenue: Revenue or cost center code
    :param 'CodeableConcept' category: Benefit classification
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param list['CodeableConcept'] modifier: Service/Product billing modifiers
    :param list['CodeableConcept'] programCode: Program the product or service is provided under
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param 'Money' net: Total item cost
    :param list['Reference'] udi: Unique device identifier
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  revenue: 'CodeableConcept' = None,  category: 'CodeableConcept' = None,  productOrService: 'CodeableConcept' = None,  modifier: list['CodeableConcept'] = None,  programCode: list['CodeableConcept'] = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  udi: list['Reference'] = None, ):
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


  
    
    

class Detail(ModelBase):
    """ A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple items.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param 'CodeableConcept' revenue: Revenue or cost center code
    :param 'CodeableConcept' category: Benefit classification
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param list['CodeableConcept'] modifier: Service/Product billing modifiers
    :param list['CodeableConcept'] programCode: Program the product or service is provided under
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param 'Money' net: Total item cost
    :param list['Reference'] udi: Unique device identifier
    :param list['SubDetail'] subDetail: Product or service provided
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  revenue: 'CodeableConcept' = None,  category: 'CodeableConcept' = None,  productOrService: 'CodeableConcept' = None,  modifier: list['CodeableConcept'] = None,  programCode: list['CodeableConcept'] = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  udi: list['Reference'] = None,  subDetail: list['SubDetail'] = None, ):
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


  
    
    

class Item(ModelBase):
    """ A claim line. Either a simple  product or service or a 'group' of details which can each be a simple items or groups of sub-details.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param int careTeamSequence: Applicable careTeam members
    :param int diagnosisSequence: Applicable diagnoses
    :param int procedureSequence: Applicable procedures
    :param int informationSequence: Applicable exception and supporting information
    :param 'CodeableConcept' revenue: Revenue or cost center code
    :param 'CodeableConcept' category: Benefit classification
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param list['CodeableConcept'] modifier: Product or service billing modifiers
    :param list['CodeableConcept'] programCode: Program the product or service is provided under
    :param str servicedDate: Date or dates of service or product delivery
    :param 'Period' servicedPeriod: Date or dates of service or product delivery
    :param 'CodeableConcept' locationCodeableConcept: Place of service or where product was supplied
    :param 'Address' locationAddress: Place of service or where product was supplied
    :param 'Reference' locationReference: Place of service or where product was supplied
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param 'Money' net: Total item cost
    :param list['Reference'] udi: Unique device identifier
    :param 'CodeableConcept' bodySite: Anatomical location
    :param list['CodeableConcept'] subSite: Anatomical sub-location
    :param list['Reference'] encounter: Encounters related to this billed item
    :param list['Detail'] detail: Product or service provided
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  careTeamSequence: int = None,  diagnosisSequence: int = None,  procedureSequence: int = None,  informationSequence: int = None,  revenue: 'CodeableConcept' = None,  category: 'CodeableConcept' = None,  productOrService: 'CodeableConcept' = None,  modifier: list['CodeableConcept'] = None,  programCode: list['CodeableConcept'] = None,  servicedDate: str = None,  servicedPeriod: 'Period' = None,  locationCodeableConcept: 'CodeableConcept' = None,  locationAddress: 'Address' = None,  locationReference: 'Reference' = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  udi: list['Reference'] = None,  bodySite: 'CodeableConcept' = None,  subSite: list['CodeableConcept'] = None,  encounter: list['Reference'] = None,  detail: list['Detail'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.careTeamSequence: int = careTeamSequence or []
        self.diagnosisSequence: int = diagnosisSequence or []
        self.procedureSequence: int = procedureSequence or []
        self.informationSequence: int = informationSequence or []
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


class Claim(DomainResource):
    """ A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for claim
    :param str status: active | cancelled | draft | entered-in-error
    :param 'CodeableConcept' type: Category or discipline
    :param 'CodeableConcept' subType: More granular claim type
    :param str use: claim | preauthorization | predetermination
    :param 'Reference' patient: The recipient of the products and services
    :param 'Period' billablePeriod: Relevant time frame for the claim
    :param str created: Resource creation date
    :param 'Reference' enterer: Author of the claim
    :param 'Reference' insurer: Target
    :param 'Reference' provider: Party responsible for the claim
    :param 'CodeableConcept' priority: Desired processing ugency
    :param 'CodeableConcept' fundsReserve: For whom to reserve funds
    :param list['Related'] related: Prior or corollary claims
    :param 'Reference' prescription: Prescription authorizing services and products
    :param 'Reference' originalPrescription: Original prescription if superseded by fulfiller
    :param 'Payee' payee: Recipient of benefits payable
    :param 'Reference' referral: Treatment referral
    :param 'Reference' facility: Servicing facility
    :param list['CareTeam'] careTeam: Members of the care team
    :param list['SupportingInfo'] supportingInfo: Supporting information
    :param list['Diagnosis'] diagnosis: Pertinent diagnosis information
    :param list['Procedure'] procedure: Clinical procedures performed
    :param list['Insurance'] insurance: Patient insurance information
    :param 'Accident' accident: Details of the event
    :param list['Item'] item: Product or service provided
    :param 'Money' total: Total claim cost
    """
    def __init__(self, resourceType: str = "Claim",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  type: 'CodeableConcept' = None,  subType: 'CodeableConcept' = None,  use: str = None,  patient: 'Reference' = None,  billablePeriod: 'Period' = None,  created: str = None,  enterer: 'Reference' = None,  insurer: 'Reference' = None,  provider: 'Reference' = None,  priority: 'CodeableConcept' = None,  fundsReserve: 'CodeableConcept' = None,  related: list['Related'] = None,  prescription: 'Reference' = None,  originalPrescription: 'Reference' = None,  payee: 'Payee' = None,  referral: 'Reference' = None,  facility: 'Reference' = None,  careTeam: list['CareTeam'] = None,  supportingInfo: list['SupportingInfo'] = None,  diagnosis: list['Diagnosis'] = None,  procedure: list['Procedure'] = None,  insurance: list['Insurance'] = None,  accident: 'Accident' = None,  item: list['Item'] = None,  total: 'Money' = None, ):
        self.resourceType: str = resourceType or "Claim"
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
        self.fundsReserve: 'CodeableConcept' = fundsReserve 
        self.related: list['Related'] = related or []
        self.prescription: 'Reference' = prescription 
        self.originalPrescription: 'Reference' = originalPrescription 
        self.payee: 'Payee' = payee 
        self.referral: 'Reference' = referral 
        self.facility: 'Reference' = facility 
        self.careTeam: list['CareTeam'] = careTeam or []
        self.supportingInfo: list['SupportingInfo'] = supportingInfo or []
        self.diagnosis: list['Diagnosis'] = diagnosis or []
        self.procedure: list['Procedure'] = procedure or []
        self.insurance: list['Insurance'] = insurance or []
        self.accident: 'Accident' = accident 
        self.item: list['Item'] = item or []
        self.total: 'Money' = total 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
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