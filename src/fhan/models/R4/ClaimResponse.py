"""
Generated class for ClaimResponse. 
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
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Address import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Adjudication(BaseModel):
    """ If this item is a group then the values here are a summary of the adjudication of the detail items. If this item is a simple product or service then this is the result of the adjudication of this item.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' category: Type of adjudication information
    :param 'CodeableConcept' reason: Explanation of adjudication outcome
    :param 'Money' amount: Monetary amount
    :param float value: Non-monetary value
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
    """ A sub-detail adjudication of a simple product or service.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int subDetailSequence: Claim sub-detail instance identifier
    :param int noteNumber: Applicable note numbers
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  subDetailSequence: int = None,  noteNumber: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.subDetailSequence: int = subDetailSequence 
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
    """ A claim detail. Either a simple (a product or service) or a 'group' of sub-details which are simple items.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int detailSequence: Claim detail instance identifier
    :param int noteNumber: Applicable note numbers
    :param 'SubDetail' subDetail: Adjudication for claim sub-details
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  detailSequence: int = None,  noteNumber: int = None,  subDetail: 'SubDetail' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.detailSequence: int = detailSequence 
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
    :param int itemSequence: Claim item instance identifier
    :param int noteNumber: Applicable note numbers
    :param 'Adjudication' adjudication: Adjudication details
    :param 'Detail' detail: Adjudication for claim details
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  itemSequence: int = None,  noteNumber: int = None,  adjudication: 'Adjudication' = None,  detail: 'Detail' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemSequence: int = itemSequence 
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
    :param int subdetailSequence: Subdetail sequence number
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
    :param 'Detail' detail: Insurer added line details
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  itemSequence: int = None,  detailSequence: int = None,  subdetailSequence: int = None,  provider: 'Reference' = None,  productOrService: 'CodeableConcept' = None,  modifier: 'CodeableConcept' = None,  programCode: 'CodeableConcept' = None,  servicedDate: str = None,  servicedPeriod: 'Period' = None,  locationCodeableConcept: 'CodeableConcept' = None,  locationAddress: 'Address' = None,  locationReference: 'Reference' = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  net: 'Money' = None,  bodySite: 'CodeableConcept' = None,  subSite: 'CodeableConcept' = None,  noteNumber: int = None,  detail: 'Detail' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemSequence: list[int] = itemSequence or []
        self.detailSequence: list[int] = detailSequence or []
        self.subdetailSequence: list[int] = subdetailSequence or []
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
    :param 'CodeableConcept' adjustmentReason: Explanation for the adjustment
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


    
    

class Insurance(BaseModel):
    """ Financial instruments for reimbursement for the health care products and services specified on the claim.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Insurance instance identifier
    :param bool focal: Coverage to be used for adjudication
    :param 'Reference' coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    :param 'Reference' claimResponse: Adjudication results
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  sequence: int = None,  focal: bool = None,  coverage: 'Reference' = None,  businessArrangement: str = None,  claimResponse: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.focal: bool = focal 
        self.coverage: 'Reference' = coverage 
        self.businessArrangement: str = businessArrangement 
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


    
    

class Error(BaseModel):
    """ Errors encountered during the processing of the adjudication.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Item sequence number
    :param int detailSequence: Detail sequence number
    :param int subDetailSequence: Subdetail sequence number
    :param 'CodeableConcept' code: Error code detailing processing issues
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  itemSequence: int = None,  detailSequence: int = None,  subDetailSequence: int = None,  code: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemSequence: int = itemSequence 
        self.detailSequence: int = detailSequence 
        self.subDetailSequence: int = subDetailSequence 
        self.code: 'CodeableConcept' = code 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Error":
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


class ClaimResponse(DomainResource):
    """ This resource provides the adjudication details from the processing of a Claim resource.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Business Identifier for a claim response
    :param str status: active | cancelled | draft | entered-in-error
    :param 'CodeableConcept' type: More granular claim type
    :param 'CodeableConcept' subType: More granular claim type
    :param str use: claim | preauthorization | predetermination
    :param 'Reference' patient: The recipient of the products and services
    :param str created: Response creation date
    :param 'Reference' insurer: Party responsible for reimbursement
    :param 'Reference' requestor: Party responsible for the claim
    :param 'Reference' request: Id of resource triggering adjudication
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param str preAuthRef: Preauthorization reference
    :param 'Period' preAuthPeriod: Preauthorization reference effective period
    :param 'CodeableConcept' payeeType: Party to be paid any benefits payable
    :param 'Item' item: Adjudication for claim line items
    :param 'AddItem' addItem: Insurer added line items
    :param 'Total' total: Adjudication totals
    :param 'Payment' payment: Payment Details
    :param 'CodeableConcept' fundsReserve: Funds reserved status
    :param 'CodeableConcept' formCode: Printed form identifier
    :param 'Attachment' form: Printed reference or actual form
    :param 'ProcessNote' processNote: Note concerning adjudication
    :param 'Reference' communicationRequest: Request for additional information
    :param 'Insurance' insurance: Patient insurance information
    :param 'Error' error: Processing errors
    """
    def __init__(self, resourceType: str = "ClaimResponse",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  status: str = None,  type: 'CodeableConcept' = None,  subType: 'CodeableConcept' = None,  use: str = None,  patient: 'Reference' = None,  created: str = None,  insurer: 'Reference' = None,  requestor: 'Reference' = None,  request: 'Reference' = None,  outcome: str = None,  disposition: str = None,  preAuthRef: str = None,  preAuthPeriod: 'Period' = None,  payeeType: 'CodeableConcept' = None,  item: 'Item' = None,  addItem: 'AddItem' = None,  total: 'Total' = None,  payment: 'Payment' = None,  fundsReserve: 'CodeableConcept' = None,  formCode: 'CodeableConcept' = None,  form: 'Attachment' = None,  processNote: 'ProcessNote' = None,  communicationRequest: 'Reference' = None,  insurance: 'Insurance' = None,  error: 'Error' = None, ):
        self.resourceType: str = resourceType or "ClaimResponse"
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
        self.created: str = created 
        self.insurer: 'Reference' = insurer 
        self.requestor: 'Reference' = requestor 
        self.request: 'Reference' = request 
        self.outcome: str = outcome 
        self.disposition: str = disposition 
        self.preAuthRef: str = preAuthRef 
        self.preAuthPeriod: 'Period' = preAuthPeriod 
        self.payeeType: 'CodeableConcept' = payeeType 
        self.item: list['Item'] = item or []
        self.addItem: list['AddItem'] = addItem or []
        self.total: list['Total'] = total or []
        self.payment: 'Payment' = payment 
        self.fundsReserve: 'CodeableConcept' = fundsReserve 
        self.formCode: 'CodeableConcept' = formCode 
        self.form: 'Attachment' = form 
        self.processNote: list['ProcessNote'] = processNote or []
        self.communicationRequest: list['Reference'] = communicationRequest or []
        self.insurance: list['Insurance'] = insurance or []
        self.error: list['Error'] = error or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
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