"""
Generated class for Bundle. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.DomainResource import *


    
    

class Link(ModelBase):
    """ A series of links that provide context to this bundle.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str relation: See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1
    :param str url: Reference details for the link
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  relation: str = None,  url: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.relation: str = relation 
        self.url: str = url 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Link":
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


    
        
    
    

class Search(ModelBase):
    """ Information about the search process that lead to the creation of this entry.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include | outcome - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  mode: str = None,  score: float = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.mode: str = mode 
        self.score: float = score 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Search":
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


    
    

class Request(ModelBase):
    """ Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache currency
    :param str ifModifiedSince: For managing cache currency
    :param str ifMatch: For managing update contention
    :param str ifNoneExist: For conditional creates
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  method: str = None,  url: str = None,  ifNoneMatch: str = None,  ifModifiedSince: str = None,  ifMatch: str = None,  ifNoneExist: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.method: str = method 
        self.url: str = url 
        self.ifNoneMatch: str = ifNoneMatch 
        self.ifModifiedSince: str = ifModifiedSince 
        self.ifMatch: str = ifMatch 
        self.ifNoneExist: str = ifNoneExist 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Request":
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


    
    

class Response(ModelBase):
    """ Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: Status response code (text optional)
    :param str location: The location (if the operation returns a location)
    :param str etag: The Etag for the resource (if relevant)
    :param str lastModified: Server's date time modified
    :param 'Resource' outcome: OperationOutcome with hints and warnings (for batch/transaction)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  status: str = None,  location: str = None,  etag: str = None,  lastModified: str = None,  outcome: 'Resource' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.status: str = status 
        self.location: str = location 
        self.etag: str = etag 
        self.lastModified: str = lastModified 
        self.outcome: 'Resource' = outcome 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Response":
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


  
    
    

class Entry(ModelBase):
    """ An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str fullUrl: URI for resource (Absolute URL server address or URI for UUID/OID)
    :param 'Resource' resource: A resource in the bundle
    :param 'Search' search: Search related information
    :param 'Request' request: Additional execution information (transaction/batch/history)
    :param 'Response' response: Results of execution (transaction/batch/history)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  fullUrl: str = None,  resource: 'Resource' = None,  search: 'Search' = None,  request: 'Request' = None,  response: 'Response' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.fullUrl: str = fullUrl 
        self.resource: 'Resource' = resource 
        self.search: 'Search' = search 
        self.request: 'Request' = request 
        self.response: 'Response' = response 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Entry":
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


class Bundle(DomainResource):
    """ A container for a collection of resources.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Identifier' identifier: Persistent identifier for the bundle
    :param str type: document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection
    :param str timestamp: When the bundle was assembled
    :param int total: If search, the total number of matches
    :param list['Link'] link: Links related to this Bundle
    :param list['Entry'] entry: Entry in the bundle - will have a resource or information
    :param 'Signature' signature: Digital Signature
    """
    def __init__(self, resourceType: str = "Bundle",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  identifier: 'Identifier' = None,  type: str = None,  timestamp: str = None,  total: int = None,  link: list['Link'] = None,  entry: list['Entry'] = None,  signature: 'Signature' = None, ):
        self.resourceType: str = resourceType or "Bundle"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.identifier: 'Identifier' = identifier 
        self.type: str = type 
        self.timestamp: str = timestamp 
        self.total: int = total 
        self.link: list['Link'] = link or []
        self.entry: list['Entry'] = entry or []
        self.signature: 'Signature' = signature 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Bundle":
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