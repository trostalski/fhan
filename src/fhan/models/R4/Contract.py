"""
Generated class for Contract. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Money import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class ContentDefinition(BaseModel):
    """ Precusory content developed with a focus and intent of supporting the formation a Contract instance, which may be associated with and transformable into a Contract.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Content structure and use
    :param 'CodeableConcept' subType: Detailed Content Type Definition
    :param 'Reference' publisher: Publisher Entity
    :param str publicationDate: When published
    :param str publicationStatus: amended | appended | cancelled | disputed | entered-in-error | executable | executed | negotiable | offered | policy | rejected | renewed | revoked | resolved | terminated
    :param str copyright: Publication Ownership
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  subType: 'CodeableConcept' = None,  publisher: 'Reference' = None,  publicationDate: str = None,  publicationStatus: str = None,  copyright: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.subType: 'CodeableConcept' = subType 
        self.publisher: 'Reference' = publisher 
        self.publicationDate: str = publicationDate 
        self.publicationStatus: str = publicationStatus 
        self.copyright: str = copyright 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ContentDefinition":
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


    
        
    
    

class SecurityLabel(BaseModel):
    """ Security labels that protect the handling of information about the term and its elements, which may be specifically identified..:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Link to Security Labels
    :param 'Coding' classification: Confidentiality Protection
    :param 'Coding' category: Applicable Policy
    :param 'Coding' control: Handling Instructions
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  number: int = None,  classification: 'Coding' = None,  category: 'Coding' = None,  control: 'Coding' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.number: list[int] = number or []
        self.classification: 'Coding' = classification 
        self.category: list['Coding'] = category or []
        self.control: list['Coding'] = control or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SecurityLabel":
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


    
        
    
    

class Party(BaseModel):
    """ Offer Recipient.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' reference: Referenced entity
    :param 'CodeableConcept' role: Participant engagement type
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  reference: 'Reference' = None,  role: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.reference: list['Reference'] = reference or []
        self.role: 'CodeableConcept' = role 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Party":
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


    
    

class Answer(BaseModel):
    """ Response to offer text.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueBoolean: The actual answer response
    :param float valueDecimal: The actual answer response
    :param int valueInteger: The actual answer response
    :param str valueDate: The actual answer response
    :param str valueDateTime: The actual answer response
    :param str valueTime: The actual answer response
    :param str valueString: The actual answer response
    :param str valueUri: The actual answer response
    :param 'Attachment' valueAttachment: The actual answer response
    :param 'Coding' valueCoding: The actual answer response
    :param 'Quantity' valueQuantity: The actual answer response
    :param 'Reference' valueReference: The actual answer response
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  valueBoolean: bool = None,  valueDecimal: float = None,  valueInteger: int = None,  valueDate: str = None,  valueDateTime: str = None,  valueTime: str = None,  valueString: str = None,  valueUri: str = None,  valueAttachment: 'Attachment' = None,  valueCoding: 'Coding' = None,  valueQuantity: 'Quantity' = None,  valueReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.valueBoolean: bool = valueBoolean 
        self.valueDecimal: float = valueDecimal 
        self.valueInteger: int = valueInteger 
        self.valueDate: str = valueDate 
        self.valueDateTime: str = valueDateTime 
        self.valueTime: str = valueTime 
        self.valueString: str = valueString 
        self.valueUri: str = valueUri 
        self.valueAttachment: 'Attachment' = valueAttachment 
        self.valueCoding: 'Coding' = valueCoding 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueReference: 'Reference' = valueReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Answer":
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


  
    
    

class Offer(BaseModel):
    """ The matter of concern in the context of this provision of the agrement.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Offer business ID
    :param 'Party' party: Offer Recipient
    :param 'Reference' topic: Negotiable offer asset
    :param 'CodeableConcept' type: Contract Offer Type or Form
    :param 'CodeableConcept' decision: Accepting party choice
    :param 'CodeableConcept' decisionMode: How decision is conveyed
    :param 'Answer' answer: Response to offer text
    :param str text: Human readable offer text
    :param str linkId: Pointer to text
    :param int securityLabelNumber: Offer restriction numbers
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  party: 'Party' = None,  topic: 'Reference' = None,  type: 'CodeableConcept' = None,  decision: 'CodeableConcept' = None,  decisionMode: 'CodeableConcept' = None,  answer: 'Answer' = None,  text: str = None,  linkId: str = None,  securityLabelNumber: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.party: list['Party'] = party or []
        self.topic: 'Reference' = topic 
        self.type: 'CodeableConcept' = type 
        self.decision: 'CodeableConcept' = decision 
        self.decisionMode: list['CodeableConcept'] = decisionMode or []
        self.answer: list['Answer'] = answer or []
        self.text: str = text 
        self.linkId: list[str] = linkId or []
        self.securityLabelNumber: list[int] = securityLabelNumber or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Offer":
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


    
        
    
    

class Context(BaseModel):
    """ Circumstance of the asset.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' reference: Creator,custodian or owner
    :param 'CodeableConcept' code: Codeable asset context
    :param str text: Context description
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  reference: 'Reference' = None,  code: 'CodeableConcept' = None,  text: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.reference: 'Reference' = reference 
        self.code: list['CodeableConcept'] = code or []
        self.text: str = text 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Context":
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


    
    

class ValuedItem(BaseModel):
    """ Contract Valued Item List.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' entityCodeableConcept: Contract Valued Item Type
    :param 'Reference' entityReference: Contract Valued Item Type
    :param 'Identifier' identifier: Contract Valued Item Number
    :param str effectiveTime: Contract Valued Item Effective Tiem
    :param 'Quantity' quantity: Count of Contract Valued Items
    :param 'Money' unitPrice: Contract Valued Item fee, charge, or cost
    :param float factor: Contract Valued Item Price Scaling Factor
    :param float points: Contract Valued Item Difficulty Scaling Factor
    :param 'Money' net: Total Contract Valued Item Value
    :param str payment: Terms of valuation
    :param str paymentDate: When payment is due
    :param 'Reference' responsible: Who will make payment
    :param 'Reference' recipient: Who will receive payment
    :param str linkId: Pointer to specific item
    :param int securityLabelNumber: Security Labels that define affected terms
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  entityCodeableConcept: 'CodeableConcept' = None,  entityReference: 'Reference' = None,  identifier: 'Identifier' = None,  effectiveTime: str = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  points: float = None,  net: 'Money' = None,  payment: str = None,  paymentDate: str = None,  responsible: 'Reference' = None,  recipient: 'Reference' = None,  linkId: str = None,  securityLabelNumber: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.entityCodeableConcept: 'CodeableConcept' = entityCodeableConcept 
        self.entityReference: 'Reference' = entityReference 
        self.identifier: 'Identifier' = identifier 
        self.effectiveTime: str = effectiveTime 
        self.quantity: 'Quantity' = quantity 
        self.unitPrice: 'Money' = unitPrice 
        self.factor: float = factor 
        self.points: float = points 
        self.net: 'Money' = net 
        self.payment: str = payment 
        self.paymentDate: str = paymentDate 
        self.responsible: 'Reference' = responsible 
        self.recipient: 'Reference' = recipient 
        self.linkId: list[str] = linkId or []
        self.securityLabelNumber: list[int] = securityLabelNumber or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValuedItem":
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


  
    
    

class Asset(BaseModel):
    """ Contract Term Asset List.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' scope: Range of asset
    :param 'CodeableConcept' type: Asset category
    :param 'Reference' typeReference: Associated entities
    :param 'CodeableConcept' subtype: Asset sub-category
    :param 'Coding' relationship: Kinship of the asset
    :param 'Context' context: Circumstance of the asset
    :param str condition: Quality desctiption of asset
    :param 'CodeableConcept' periodType: Asset availability types
    :param 'Period' period: Time period of the asset
    :param 'Period' usePeriod: Time period
    :param str text: Asset clause or question text
    :param str linkId: Pointer to asset text
    :param int securityLabelNumber: Asset restriction numbers
    :param 'ValuedItem' valuedItem: Contract Valued Item List
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  scope: 'CodeableConcept' = None,  type: 'CodeableConcept' = None,  typeReference: 'Reference' = None,  subtype: 'CodeableConcept' = None,  relationship: 'Coding' = None,  context: 'Context' = None,  condition: str = None,  periodType: 'CodeableConcept' = None,  period: 'Period' = None,  usePeriod: 'Period' = None,  text: str = None,  linkId: str = None,  securityLabelNumber: int = None,  valuedItem: 'ValuedItem' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.scope: 'CodeableConcept' = scope 
        self.type: list['CodeableConcept'] = type or []
        self.typeReference: list['Reference'] = typeReference or []
        self.subtype: list['CodeableConcept'] = subtype or []
        self.relationship: 'Coding' = relationship 
        self.context: list['Context'] = context or []
        self.condition: str = condition 
        self.periodType: list['CodeableConcept'] = periodType or []
        self.period: list['Period'] = period or []
        self.usePeriod: list['Period'] = usePeriod or []
        self.text: str = text 
        self.linkId: list[str] = linkId or []
        self.securityLabelNumber: list[int] = securityLabelNumber or []
        self.valuedItem: list['ValuedItem'] = valuedItem or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Asset":
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


    
        
    
    

class Subject(BaseModel):
    """ Entity of the action.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' reference: Entity of the action
    :param 'CodeableConcept' role: Role type of the agent
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  reference: 'Reference' = None,  role: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.reference: list['Reference'] = reference or []
        self.role: 'CodeableConcept' = role 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Subject":
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


  
    
    

class Action(BaseModel):
    """ An actor taking a role in an activity for which it can be assigned some degree of responsibility for the activity taking place.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool doNotPerform: True if the term prohibits the  action
    :param 'CodeableConcept' type: Type or form of the action
    :param 'Subject' subject: Entity of the action
    :param 'CodeableConcept' intent: Purpose for the Contract Term Action
    :param str linkId: Pointer to specific item
    :param 'CodeableConcept' status: State of the action
    :param 'Reference' context: Episode associated with action
    :param str contextLinkId: Pointer to specific item
    :param str occurrenceDateTime: When action happens
    :param 'Period' occurrencePeriod: When action happens
    :param 'Timing' occurrenceTiming: When action happens
    :param 'Reference' requester: Who asked for action
    :param str requesterLinkId: Pointer to specific item
    :param 'CodeableConcept' performerType: Kind of service performer
    :param 'CodeableConcept' performerRole: Competency of the performer
    :param 'Reference' performer: Actor that wil execute (or not) the action
    :param str performerLinkId: Pointer to specific item
    :param 'CodeableConcept' reasonCode: Why is action (not) needed?
    :param 'Reference' reasonReference: Why is action (not) needed?
    :param str reason: Why action is to be performed
    :param str reasonLinkId: Pointer to specific item
    :param 'Annotation' note: Comments about the action
    :param int securityLabelNumber: Action restriction numbers
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  doNotPerform: bool = None,  type: 'CodeableConcept' = None,  subject: 'Subject' = None,  intent: 'CodeableConcept' = None,  linkId: str = None,  status: 'CodeableConcept' = None,  context: 'Reference' = None,  contextLinkId: str = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  occurrenceTiming: 'Timing' = None,  requester: 'Reference' = None,  requesterLinkId: str = None,  performerType: 'CodeableConcept' = None,  performerRole: 'CodeableConcept' = None,  performer: 'Reference' = None,  performerLinkId: str = None,  reasonCode: 'CodeableConcept' = None,  reasonReference: 'Reference' = None,  reason: str = None,  reasonLinkId: str = None,  note: 'Annotation' = None,  securityLabelNumber: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.doNotPerform: bool = doNotPerform 
        self.type: 'CodeableConcept' = type 
        self.subject: list['Subject'] = subject or []
        self.intent: 'CodeableConcept' = intent 
        self.linkId: list[str] = linkId or []
        self.status: 'CodeableConcept' = status 
        self.context: 'Reference' = context 
        self.contextLinkId: list[str] = contextLinkId or []
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.occurrenceTiming: 'Timing' = occurrenceTiming 
        self.requester: list['Reference'] = requester or []
        self.requesterLinkId: list[str] = requesterLinkId or []
        self.performerType: list['CodeableConcept'] = performerType or []
        self.performerRole: 'CodeableConcept' = performerRole 
        self.performer: 'Reference' = performer 
        self.performerLinkId: list[str] = performerLinkId or []
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.reason: list[str] = reason or []
        self.reasonLinkId: list[str] = reasonLinkId or []
        self.note: list['Annotation'] = note or []
        self.securityLabelNumber: list[int] = securityLabelNumber or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Action":
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


  
    
    

class Term(BaseModel):
    """ One or more Contract Provisions, which may be related and conveyed as a group, and may contain nested groups.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Contract Term Number
    :param str issued: Contract Term Issue Date Time
    :param 'Period' applies: Contract Term Effective Time
    :param 'CodeableConcept' topicCodeableConcept: Term Concern
    :param 'Reference' topicReference: Term Concern
    :param 'CodeableConcept' type: Contract Term Type or Form
    :param 'CodeableConcept' subType: Contract Term Type specific classification
    :param str text: Term Statement
    :param 'SecurityLabel' securityLabel: Protection for the Term
    :param 'Offer' offer: Context of the Contract term
    :param 'Asset' asset: Contract Term Asset List
    :param 'Action' action: Entity being ascribed responsibility
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  issued: str = None,  applies: 'Period' = None,  topicCodeableConcept: 'CodeableConcept' = None,  topicReference: 'Reference' = None,  type: 'CodeableConcept' = None,  subType: 'CodeableConcept' = None,  text: str = None,  securityLabel: 'SecurityLabel' = None,  offer: 'Offer' = None,  asset: 'Asset' = None,  action: 'Action' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.issued: str = issued 
        self.applies: 'Period' = applies 
        self.topicCodeableConcept: 'CodeableConcept' = topicCodeableConcept 
        self.topicReference: 'Reference' = topicReference 
        self.type: 'CodeableConcept' = type 
        self.subType: 'CodeableConcept' = subType 
        self.text: str = text 
        self.securityLabel: list['SecurityLabel'] = securityLabel or []
        self.offer: 'Offer' = offer 
        self.asset: list['Asset'] = asset or []
        self.action: list['Action'] = action or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Term":
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


    
        
    
    

class SecurityLabel(BaseModel):
    """ Security labels that protect the handling of information about the term and its elements, which may be specifically identified..:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Link to Security Labels
    :param 'Coding' classification: Confidentiality Protection
    :param 'Coding' category: Applicable Policy
    :param 'Coding' control: Handling Instructions
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  number: int = None,  classification: 'Coding' = None,  category: 'Coding' = None,  control: 'Coding' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.number: list[int] = number or []
        self.classification: 'Coding' = classification 
        self.category: list['Coding'] = category or []
        self.control: list['Coding'] = control or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SecurityLabel":
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


    
        
    
    

class Party(BaseModel):
    """ Offer Recipient.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' reference: Referenced entity
    :param 'CodeableConcept' role: Participant engagement type
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  reference: 'Reference' = None,  role: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.reference: list['Reference'] = reference or []
        self.role: 'CodeableConcept' = role 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Party":
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


    
    

class Answer(BaseModel):
    """ Response to offer text.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueBoolean: The actual answer response
    :param float valueDecimal: The actual answer response
    :param int valueInteger: The actual answer response
    :param str valueDate: The actual answer response
    :param str valueDateTime: The actual answer response
    :param str valueTime: The actual answer response
    :param str valueString: The actual answer response
    :param str valueUri: The actual answer response
    :param 'Attachment' valueAttachment: The actual answer response
    :param 'Coding' valueCoding: The actual answer response
    :param 'Quantity' valueQuantity: The actual answer response
    :param 'Reference' valueReference: The actual answer response
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  valueBoolean: bool = None,  valueDecimal: float = None,  valueInteger: int = None,  valueDate: str = None,  valueDateTime: str = None,  valueTime: str = None,  valueString: str = None,  valueUri: str = None,  valueAttachment: 'Attachment' = None,  valueCoding: 'Coding' = None,  valueQuantity: 'Quantity' = None,  valueReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.valueBoolean: bool = valueBoolean 
        self.valueDecimal: float = valueDecimal 
        self.valueInteger: int = valueInteger 
        self.valueDate: str = valueDate 
        self.valueDateTime: str = valueDateTime 
        self.valueTime: str = valueTime 
        self.valueString: str = valueString 
        self.valueUri: str = valueUri 
        self.valueAttachment: 'Attachment' = valueAttachment 
        self.valueCoding: 'Coding' = valueCoding 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueReference: 'Reference' = valueReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Answer":
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


  
    
    

class Offer(BaseModel):
    """ The matter of concern in the context of this provision of the agrement.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Offer business ID
    :param 'Party' party: Offer Recipient
    :param 'Reference' topic: Negotiable offer asset
    :param 'CodeableConcept' type: Contract Offer Type or Form
    :param 'CodeableConcept' decision: Accepting party choice
    :param 'CodeableConcept' decisionMode: How decision is conveyed
    :param 'Answer' answer: Response to offer text
    :param str text: Human readable offer text
    :param str linkId: Pointer to text
    :param int securityLabelNumber: Offer restriction numbers
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  party: 'Party' = None,  topic: 'Reference' = None,  type: 'CodeableConcept' = None,  decision: 'CodeableConcept' = None,  decisionMode: 'CodeableConcept' = None,  answer: 'Answer' = None,  text: str = None,  linkId: str = None,  securityLabelNumber: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.party: list['Party'] = party or []
        self.topic: 'Reference' = topic 
        self.type: 'CodeableConcept' = type 
        self.decision: 'CodeableConcept' = decision 
        self.decisionMode: list['CodeableConcept'] = decisionMode or []
        self.answer: list['Answer'] = answer or []
        self.text: str = text 
        self.linkId: list[str] = linkId or []
        self.securityLabelNumber: list[int] = securityLabelNumber or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Offer":
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


    
        
    
    

class Context(BaseModel):
    """ Circumstance of the asset.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' reference: Creator,custodian or owner
    :param 'CodeableConcept' code: Codeable asset context
    :param str text: Context description
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  reference: 'Reference' = None,  code: 'CodeableConcept' = None,  text: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.reference: 'Reference' = reference 
        self.code: list['CodeableConcept'] = code or []
        self.text: str = text 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Context":
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


    
    

class ValuedItem(BaseModel):
    """ Contract Valued Item List.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' entityCodeableConcept: Contract Valued Item Type
    :param 'Reference' entityReference: Contract Valued Item Type
    :param 'Identifier' identifier: Contract Valued Item Number
    :param str effectiveTime: Contract Valued Item Effective Tiem
    :param 'Quantity' quantity: Count of Contract Valued Items
    :param 'Money' unitPrice: Contract Valued Item fee, charge, or cost
    :param float factor: Contract Valued Item Price Scaling Factor
    :param float points: Contract Valued Item Difficulty Scaling Factor
    :param 'Money' net: Total Contract Valued Item Value
    :param str payment: Terms of valuation
    :param str paymentDate: When payment is due
    :param 'Reference' responsible: Who will make payment
    :param 'Reference' recipient: Who will receive payment
    :param str linkId: Pointer to specific item
    :param int securityLabelNumber: Security Labels that define affected terms
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  entityCodeableConcept: 'CodeableConcept' = None,  entityReference: 'Reference' = None,  identifier: 'Identifier' = None,  effectiveTime: str = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  factor: float = None,  points: float = None,  net: 'Money' = None,  payment: str = None,  paymentDate: str = None,  responsible: 'Reference' = None,  recipient: 'Reference' = None,  linkId: str = None,  securityLabelNumber: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.entityCodeableConcept: 'CodeableConcept' = entityCodeableConcept 
        self.entityReference: 'Reference' = entityReference 
        self.identifier: 'Identifier' = identifier 
        self.effectiveTime: str = effectiveTime 
        self.quantity: 'Quantity' = quantity 
        self.unitPrice: 'Money' = unitPrice 
        self.factor: float = factor 
        self.points: float = points 
        self.net: 'Money' = net 
        self.payment: str = payment 
        self.paymentDate: str = paymentDate 
        self.responsible: 'Reference' = responsible 
        self.recipient: 'Reference' = recipient 
        self.linkId: list[str] = linkId or []
        self.securityLabelNumber: list[int] = securityLabelNumber or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValuedItem":
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


  
    
    

class Asset(BaseModel):
    """ Contract Term Asset List.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' scope: Range of asset
    :param 'CodeableConcept' type: Asset category
    :param 'Reference' typeReference: Associated entities
    :param 'CodeableConcept' subtype: Asset sub-category
    :param 'Coding' relationship: Kinship of the asset
    :param 'Context' context: Circumstance of the asset
    :param str condition: Quality desctiption of asset
    :param 'CodeableConcept' periodType: Asset availability types
    :param 'Period' period: Time period of the asset
    :param 'Period' usePeriod: Time period
    :param str text: Asset clause or question text
    :param str linkId: Pointer to asset text
    :param int securityLabelNumber: Asset restriction numbers
    :param 'ValuedItem' valuedItem: Contract Valued Item List
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  scope: 'CodeableConcept' = None,  type: 'CodeableConcept' = None,  typeReference: 'Reference' = None,  subtype: 'CodeableConcept' = None,  relationship: 'Coding' = None,  context: 'Context' = None,  condition: str = None,  periodType: 'CodeableConcept' = None,  period: 'Period' = None,  usePeriod: 'Period' = None,  text: str = None,  linkId: str = None,  securityLabelNumber: int = None,  valuedItem: 'ValuedItem' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.scope: 'CodeableConcept' = scope 
        self.type: list['CodeableConcept'] = type or []
        self.typeReference: list['Reference'] = typeReference or []
        self.subtype: list['CodeableConcept'] = subtype or []
        self.relationship: 'Coding' = relationship 
        self.context: list['Context'] = context or []
        self.condition: str = condition 
        self.periodType: list['CodeableConcept'] = periodType or []
        self.period: list['Period'] = period or []
        self.usePeriod: list['Period'] = usePeriod or []
        self.text: str = text 
        self.linkId: list[str] = linkId or []
        self.securityLabelNumber: list[int] = securityLabelNumber or []
        self.valuedItem: list['ValuedItem'] = valuedItem or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Asset":
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


    
        
    
    

class Subject(BaseModel):
    """ Entity of the action.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' reference: Entity of the action
    :param 'CodeableConcept' role: Role type of the agent
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  reference: 'Reference' = None,  role: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.reference: list['Reference'] = reference or []
        self.role: 'CodeableConcept' = role 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Subject":
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


  
    
    

class Action(BaseModel):
    """ An actor taking a role in an activity for which it can be assigned some degree of responsibility for the activity taking place.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool doNotPerform: True if the term prohibits the  action
    :param 'CodeableConcept' type: Type or form of the action
    :param 'Subject' subject: Entity of the action
    :param 'CodeableConcept' intent: Purpose for the Contract Term Action
    :param str linkId: Pointer to specific item
    :param 'CodeableConcept' status: State of the action
    :param 'Reference' context: Episode associated with action
    :param str contextLinkId: Pointer to specific item
    :param str occurrenceDateTime: When action happens
    :param 'Period' occurrencePeriod: When action happens
    :param 'Timing' occurrenceTiming: When action happens
    :param 'Reference' requester: Who asked for action
    :param str requesterLinkId: Pointer to specific item
    :param 'CodeableConcept' performerType: Kind of service performer
    :param 'CodeableConcept' performerRole: Competency of the performer
    :param 'Reference' performer: Actor that wil execute (or not) the action
    :param str performerLinkId: Pointer to specific item
    :param 'CodeableConcept' reasonCode: Why is action (not) needed?
    :param 'Reference' reasonReference: Why is action (not) needed?
    :param str reason: Why action is to be performed
    :param str reasonLinkId: Pointer to specific item
    :param 'Annotation' note: Comments about the action
    :param int securityLabelNumber: Action restriction numbers
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  doNotPerform: bool = None,  type: 'CodeableConcept' = None,  subject: 'Subject' = None,  intent: 'CodeableConcept' = None,  linkId: str = None,  status: 'CodeableConcept' = None,  context: 'Reference' = None,  contextLinkId: str = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  occurrenceTiming: 'Timing' = None,  requester: 'Reference' = None,  requesterLinkId: str = None,  performerType: 'CodeableConcept' = None,  performerRole: 'CodeableConcept' = None,  performer: 'Reference' = None,  performerLinkId: str = None,  reasonCode: 'CodeableConcept' = None,  reasonReference: 'Reference' = None,  reason: str = None,  reasonLinkId: str = None,  note: 'Annotation' = None,  securityLabelNumber: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.doNotPerform: bool = doNotPerform 
        self.type: 'CodeableConcept' = type 
        self.subject: list['Subject'] = subject or []
        self.intent: 'CodeableConcept' = intent 
        self.linkId: list[str] = linkId or []
        self.status: 'CodeableConcept' = status 
        self.context: 'Reference' = context 
        self.contextLinkId: list[str] = contextLinkId or []
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.occurrenceTiming: 'Timing' = occurrenceTiming 
        self.requester: list['Reference'] = requester or []
        self.requesterLinkId: list[str] = requesterLinkId or []
        self.performerType: list['CodeableConcept'] = performerType or []
        self.performerRole: 'CodeableConcept' = performerRole 
        self.performer: 'Reference' = performer 
        self.performerLinkId: list[str] = performerLinkId or []
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.reason: list[str] = reason or []
        self.reasonLinkId: list[str] = reasonLinkId or []
        self.note: list['Annotation'] = note or []
        self.securityLabelNumber: list[int] = securityLabelNumber or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Action":
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


  
    
    

class Group(BaseModel):
    """ One or more Contract Provisions, which may be related and conveyed as a group, and may contain nested groups.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Contract Term Number
    :param str issued: Contract Term Issue Date Time
    :param 'Period' applies: Contract Term Effective Time
    :param 'CodeableConcept' topicCodeableConcept: Term Concern
    :param 'Reference' topicReference: Term Concern
    :param 'CodeableConcept' type: Contract Term Type or Form
    :param 'CodeableConcept' subType: Contract Term Type specific classification
    :param str text: Term Statement
    :param 'SecurityLabel' securityLabel: Protection for the Term
    :param 'Offer' offer: Context of the Contract term
    :param 'Asset' asset: Contract Term Asset List
    :param 'Action' action: Entity being ascribed responsibility
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  issued: str = None,  applies: 'Period' = None,  topicCodeableConcept: 'CodeableConcept' = None,  topicReference: 'Reference' = None,  type: 'CodeableConcept' = None,  subType: 'CodeableConcept' = None,  text: str = None,  securityLabel: 'SecurityLabel' = None,  offer: 'Offer' = None,  asset: 'Asset' = None,  action: 'Action' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.issued: str = issued 
        self.applies: 'Period' = applies 
        self.topicCodeableConcept: 'CodeableConcept' = topicCodeableConcept 
        self.topicReference: 'Reference' = topicReference 
        self.type: 'CodeableConcept' = type 
        self.subType: 'CodeableConcept' = subType 
        self.text: str = text 
        self.securityLabel: list['SecurityLabel'] = securityLabel or []
        self.offer: 'Offer' = offer 
        self.asset: list['Asset'] = asset or []
        self.action: list['Action'] = action or []
        

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


    
    

class Signer(BaseModel):
    """ Parties with legal standing in the Contract, including the principal parties, the grantor(s) and grantee(s), which are any person or organization bound by the contract, and any ancillary parties, which facilitate the execution of the contract such as a notary or witness.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Coding' type: Contract Signatory Role
    :param 'Reference' party: Contract Signatory Party
    :param 'Signature' signature: Contract Documentation Signature
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'Coding' = None,  party: 'Reference' = None,  signature: 'Signature' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'Coding' = type 
        self.party: 'Reference' = party 
        self.signature: list['Signature'] = signature or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Signer":
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


    
    

class Friendly(BaseModel):
    """ The "patient friendly language" versionof the Contract in whole or in parts. "Patient friendly language" means the representation of the Contract and Contract Provisions in a manner that is readily accessible and understandable by a layperson in accordance with best practices for communication styles that ensure that those agreeing to or signing the Contract understand the roles, actions, obligations, responsibilities, and implication of the agreement.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Attachment' contentAttachment: Easily comprehended representation of this Contract
    :param 'Reference' contentReference: Easily comprehended representation of this Contract
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  contentAttachment: 'Attachment' = None,  contentReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.contentAttachment: 'Attachment' = contentAttachment 
        self.contentReference: 'Reference' = contentReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Friendly":
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


    
    

class Legal(BaseModel):
    """ List of Legal expressions or representations of this Contract.:param 'CodeableConcept' legalState: Negotiation status
    :param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Attachment' contentAttachment: Contract Legal Text
    :param 'Reference' contentReference: Contract Legal Text
    :param 'Attachment' legallyBindingAttachment: Binding Contract
    :param 'Reference' legallyBindingReference: Binding Contract
    """
    def __init__(self,  legalState: 'CodeableConcept' = None,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  contentAttachment: 'Attachment' = None,  contentReference: 'Reference' = None,  legallyBindingAttachment: 'Attachment' = None,  legallyBindingReference: 'Reference' = None, ):
        self.legalState: 'CodeableConcept' = legalState 
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.contentAttachment: 'Attachment' = contentAttachment 
        self.contentReference: 'Reference' = contentReference 
        self.legallyBindingAttachment: 'Attachment' = legallyBindingAttachment 
        self.legallyBindingReference: 'Reference' = legallyBindingReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Legal":
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


    
    

class Rule(BaseModel):
    """ List of Computable Policy Rule Language Representations of this Contract.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Attachment' contentAttachment: Computable Contract Rules
    :param 'Reference' contentReference: Computable Contract Rules
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  contentAttachment: 'Attachment' = None,  contentReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.contentAttachment: 'Attachment' = contentAttachment 
        self.contentReference: 'Reference' = contentReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Rule":
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


class Contract(DomainResource):
    """ Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Contract number
    :param str url: Basal definition
    :param str version: Business edition
    :param str status: amended | appended | cancelled | disputed | entered-in-error | executable | executed | negotiable | offered | policy | rejected | renewed | revoked | resolved | terminated
    :param 'CodeableConcept' legalState: Negotiation status
    :param 'Reference' instantiatesCanonical: Source Contract Definition
    :param str instantiatesUri: External Contract Definition
    :param 'CodeableConcept' contentDerivative: Content derived from the basal information
    :param str issued: When this Contract was issued
    :param 'Period' applies: Effective time
    :param 'CodeableConcept' expirationType: Contract cessation cause
    :param 'Reference' subject: Contract Target Entity
    :param 'Reference' authority: Authority under which this Contract has standing
    :param 'Reference' domain: A sphere of control governed by an authoritative jurisdiction, organization, or person
    :param 'Reference' site: Specific Location
    :param str name: Computer friendly designation
    :param str title: Human Friendly name
    :param str subtitle: Subordinate Friendly name
    :param str alias: Acronym or short name
    :param 'Reference' author: Source of Contract
    :param 'CodeableConcept' scope: Range of Legal Concerns
    :param 'CodeableConcept' topicCodeableConcept: Focus of contract interest
    :param 'Reference' topicReference: Focus of contract interest
    :param 'CodeableConcept' type: Legal instrument category
    :param 'CodeableConcept' subType: Subtype within the context of type
    :param 'ContentDefinition' contentDefinition: Contract precursor content
    :param 'Term' term: Contract Term List
    :param 'Group' group: Contract Term List
    :param 'Reference' supportingInfo: Extra Information
    :param 'Reference' relevantHistory: Key event in Contract History
    :param 'Signer' signer: Contract Signatory
    :param 'Friendly' friendly: Contract Friendly Language
    :param 'Legal' legal: Contract Legal Language
    :param 'Rule' rule: Computable Contract Language
    """
    def __init__(self, resourceType: str = "Contract",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  url: str = None,  version: str = None,  status: str = None,  legalState: 'CodeableConcept' = None,  instantiatesCanonical: 'Reference' = None,  instantiatesUri: str = None,  contentDerivative: 'CodeableConcept' = None,  issued: str = None,  applies: 'Period' = None,  expirationType: 'CodeableConcept' = None,  subject: 'Reference' = None,  authority: 'Reference' = None,  domain: 'Reference' = None,  site: 'Reference' = None,  name: str = None,  title: str = None,  subtitle: str = None,  alias: str = None,  author: 'Reference' = None,  scope: 'CodeableConcept' = None,  topicCodeableConcept: 'CodeableConcept' = None,  topicReference: 'Reference' = None,  type: 'CodeableConcept' = None,  subType: 'CodeableConcept' = None,  contentDefinition: 'ContentDefinition' = None,  term: 'Term' = None,  group: 'Group' = None,  supportingInfo: 'Reference' = None,  relevantHistory: 'Reference' = None,  signer: 'Signer' = None,  friendly: 'Friendly' = None,  legal: 'Legal' = None,  rule: 'Rule' = None, ):
        self.resourceType: str = resourceType or "Contract"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.url: str = url 
        self.version: str = version 
        self.status: str = status 
        self.legalState: 'CodeableConcept' = legalState 
        self.instantiatesCanonical: 'Reference' = instantiatesCanonical 
        self.instantiatesUri: str = instantiatesUri 
        self.contentDerivative: 'CodeableConcept' = contentDerivative 
        self.issued: str = issued 
        self.applies: 'Period' = applies 
        self.expirationType: 'CodeableConcept' = expirationType 
        self.subject: list['Reference'] = subject or []
        self.authority: list['Reference'] = authority or []
        self.domain: list['Reference'] = domain or []
        self.site: list['Reference'] = site or []
        self.name: str = name 
        self.title: str = title 
        self.subtitle: str = subtitle 
        self.alias: list[str] = alias or []
        self.author: 'Reference' = author 
        self.scope: 'CodeableConcept' = scope 
        self.topicCodeableConcept: 'CodeableConcept' = topicCodeableConcept 
        self.topicReference: 'Reference' = topicReference 
        self.type: 'CodeableConcept' = type 
        self.subType: list['CodeableConcept'] = subType or []
        self.contentDefinition: 'ContentDefinition' = contentDefinition 
        self.term: list['Term'] = term or []
        self.group: list['Group'] = group or []
        self.supportingInfo: list['Reference'] = supportingInfo or []
        self.relevantHistory: list['Reference'] = relevantHistory or []
        self.signer: list['Signer'] = signer or []
        self.friendly: list['Friendly'] = friendly or []
        self.legal: list['Legal'] = legal or []
        self.rule: list['Rule'] = rule or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
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