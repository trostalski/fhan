"""
Generated class for DocumentManifest. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class Related(BaseModel):
    """ Related identifiers or resources associated with the DocumentManifest.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Identifiers of things that are related
    :param 'Reference' ref: Related Resource
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  ref: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.ref: 'Reference' = ref 
        

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


class DocumentManifest(DomainResource):
    """ A collection of documents compiled for a purpose together with metadata that applies to the collection.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' masterIdentifier: Unique Identifier for the set of documents
    :param 'Identifier' identifier: Other identifiers for the manifest
    :param str status: current | superseded | entered-in-error
    :param 'CodeableConcept' type: Kind of document set
    :param 'Reference' subject: The subject of the set of documents
    :param str created: When this document manifest created
    :param 'Reference' author: Who and/or what authored the DocumentManifest
    :param 'Reference' recipient: Intended to get notified about this set of documents
    :param str source: The source system/application/software
    :param str description: Human-readable description (title)
    :param 'Reference' content: Items in manifest
    :param 'Related' related: Related things
    """
    def __init__(self, resourceType: str = "DocumentManifest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  masterIdentifier: 'Identifier' = None,  identifier: 'Identifier' = None,  status: str = None,  type: 'CodeableConcept' = None,  subject: 'Reference' = None,  created: str = None,  author: 'Reference' = None,  recipient: 'Reference' = None,  source: str = None,  description: str = None,  content: 'Reference' = None,  related: 'Related' = None, ):
        self.resourceType: str = resourceType or "DocumentManifest"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.masterIdentifier: 'Identifier' = masterIdentifier 
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.type: 'CodeableConcept' = type 
        self.subject: 'Reference' = subject 
        self.created: str = created 
        self.author: list['Reference'] = author or []
        self.recipient: list['Reference'] = recipient or []
        self.source: str = source 
        self.description: str = description 
        self.content: list['Reference'] = content or []
        self.related: list['Related'] = related or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentManifest":
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