"""
Generated class for SubstanceReferenceInformation. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Resource import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class GeneElement(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Todo
    :param 'Identifier' element: Todo
    :param 'Reference' source: Todo
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  element: 'Identifier' = None,  source: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.element: 'Identifier' = element 
        self.source: list['Reference'] = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "GeneElement":
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


  
    
    

class Gene(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' geneSequenceOrigin: Todo
    :param 'CodeableConcept' gene: Todo
    :param 'Reference' source: Todo
    :param 'GeneElement' geneElement: Todo
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  geneSequenceOrigin: 'CodeableConcept' = None,  gene: 'CodeableConcept' = None,  source: 'Reference' = None,  geneElement: 'GeneElement' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.geneSequenceOrigin: 'CodeableConcept' = geneSequenceOrigin 
        self.gene: 'CodeableConcept' = gene 
        self.source: list['Reference'] = source or []
        self.geneElement: list['GeneElement'] = geneElement or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Gene":
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


    
    

class Classification(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' domain: Todo
    :param 'CodeableConcept' classification: Todo
    :param 'CodeableConcept' subtype: Todo
    :param 'Reference' source: Todo
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  domain: 'CodeableConcept' = None,  classification: 'CodeableConcept' = None,  subtype: 'CodeableConcept' = None,  source: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.domain: 'CodeableConcept' = domain 
        self.classification: 'CodeableConcept' = classification 
        self.subtype: list['CodeableConcept'] = subtype or []
        self.source: list['Reference'] = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Classification":
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


    
    

class Target(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' target: Todo
    :param 'CodeableConcept' type: Todo
    :param 'CodeableConcept' interaction: Todo
    :param 'CodeableConcept' organism: Todo
    :param 'CodeableConcept' organismType: Todo
    :param 'Quantity' amountQuantity: Todo
    :param 'Range' amountRange: Todo
    :param str amountString: Todo
    :param 'CodeableConcept' amountType: Todo
    :param 'Reference' source: Todo
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  target: 'Identifier' = None,  type: 'CodeableConcept' = None,  interaction: 'CodeableConcept' = None,  organism: 'CodeableConcept' = None,  organismType: 'CodeableConcept' = None,  amountQuantity: 'Quantity' = None,  amountRange: 'Range' = None,  amountString: str = None,  amountType: 'CodeableConcept' = None,  source: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.target: 'Identifier' = target 
        self.type: 'CodeableConcept' = type 
        self.interaction: 'CodeableConcept' = interaction 
        self.organism: 'CodeableConcept' = organism 
        self.organismType: 'CodeableConcept' = organismType 
        self.amountQuantity: 'Quantity' = amountQuantity 
        self.amountRange: 'Range' = amountRange 
        self.amountString: str = amountString 
        self.amountType: 'CodeableConcept' = amountType 
        self.source: list['Reference'] = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Target":
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


class SubstanceReferenceInformation(DomainResource):
    """ Todo.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param str comment: Todo
    :param 'Gene' gene: Todo
    :param 'Classification' classification: Todo
    :param 'Target' target: Todo
    """
    def __init__(self, resourceType: str = "SubstanceReferenceInformation",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  comment: str = None,  gene: 'Gene' = None,  classification: 'Classification' = None,  target: 'Target' = None, ):
        self.resourceType: str = resourceType or "SubstanceReferenceInformation"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.comment: str = comment 
        self.gene: list['Gene'] = gene or []
        self.classification: list['Classification'] = classification or []
        self.target: list['Target'] = target or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceReferenceInformation":
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