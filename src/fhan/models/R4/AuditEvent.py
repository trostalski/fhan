"""
Generated class for AuditEvent. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Network(ModelBase):
    """ Logical network location for application activity, if the activity has a network location.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str address: Identifier for the network access point of the user device
    :param str type: The type of network access point
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  address: str = None,  type: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.address: str = address 
        self.type: str = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Network":
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


  
    
    

class Agent(ModelBase):
    """ An actor taking an active role in the event or activity that is logged.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: How agent participated
    :param list['CodeableConcept'] role: Agent role in the event
    :param 'Reference' who: Identifier of who
    :param str altId: Alternative User identity
    :param str name: Human friendly name for the agent
    :param bool requestor: Whether user is initiator
    :param 'Reference' location: Where
    :param str policy: Policy that authorized event
    :param 'Coding' media: Type of media
    :param 'Network' network: Logical network location for application activity
    :param list['CodeableConcept'] purposeOfUse: Reason given for this user
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  role: list['CodeableConcept'] = None,  who: 'Reference' = None,  altId: str = None,  name: str = None,  requestor: bool = None,  location: 'Reference' = None,  policy: str = None,  media: 'Coding' = None,  network: 'Network' = None,  purposeOfUse: list['CodeableConcept'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.role: list['CodeableConcept'] = role or []
        self.who: 'Reference' = who 
        self.altId: str = altId 
        self.name: str = name 
        self.requestor: bool = requestor 
        self.location: 'Reference' = location 
        self.policy: str = policy or []
        self.media: 'Coding' = media 
        self.network: 'Network' = network 
        self.purposeOfUse: list['CodeableConcept'] = purposeOfUse or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Agent":
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


    
    

class Source(ModelBase):
    """ The system that is reporting the event.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str site: Logical source location within the enterprise
    :param 'Reference' observer: The identity of source detecting the event
    :param list['Coding'] type: The type of source where event originated
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  site: str = None,  observer: 'Reference' = None,  type: list['Coding'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.site: str = site 
        self.observer: 'Reference' = observer 
        self.type: list['Coding'] = type or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Source":
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
    """ Tagged value pairs for conveying additional information about the entity.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: Name of the property
    :param str valueString: Property value
    :param str valueBase64Binary: Property value
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  valueString: str = None,  valueBase64Binary: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.valueString: str = valueString 
        self.valueBase64Binary: str = valueBase64Binary 
        

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


  
    
    

class Entity(ModelBase):
    """ Specific instances of data or objects that have been accessed.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' what: Specific instance of resource
    :param 'Coding' type: Type of entity involved
    :param 'Coding' role: What role the entity played
    :param 'Coding' lifecycle: Life-cycle stage for the entity
    :param list['Coding'] securityLabel: Security labels on the entity
    :param str name: Descriptor for entity
    :param str description: Descriptive text
    :param str query: Query parameters
    :param list['Detail'] detail: Additional Information about the entity
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  what: 'Reference' = None,  type: 'Coding' = None,  role: 'Coding' = None,  lifecycle: 'Coding' = None,  securityLabel: list['Coding'] = None,  name: str = None,  description: str = None,  query: str = None,  detail: list['Detail'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.what: 'Reference' = what 
        self.type: 'Coding' = type 
        self.role: 'Coding' = role 
        self.lifecycle: 'Coding' = lifecycle 
        self.securityLabel: list['Coding'] = securityLabel or []
        self.name: str = name 
        self.description: str = description 
        self.query: str = query 
        self.detail: list['Detail'] = detail or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Entity":
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


class AuditEvent(DomainResource):
    """ A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Coding' type: Type/identifier of event
    :param list['Coding'] subtype: More specific type/id for the event
    :param str action: Type of action performed during the event
    :param 'Period' period: When the activity occurred
    :param str recorded: Time when the event was recorded
    :param str outcome: Whether the event succeeded or failed
    :param str outcomeDesc: Description of the event outcome
    :param list['CodeableConcept'] purposeOfEvent: The purposeOfUse of the event
    :param list['Agent'] agent: Actor involved in the event
    :param 'Source' source: Audit Event Reporter
    :param list['Entity'] entity: Data or objects used
    """
    def __init__(self, resourceType: str = "AuditEvent",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'Coding' = None,  subtype: list['Coding'] = None,  action: str = None,  period: 'Period' = None,  recorded: str = None,  outcome: str = None,  outcomeDesc: str = None,  purposeOfEvent: list['CodeableConcept'] = None,  agent: list['Agent'] = None,  source: 'Source' = None,  entity: list['Entity'] = None, ):
        self.resourceType: str = resourceType or "AuditEvent"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'Coding' = type 
        self.subtype: list['Coding'] = subtype or []
        self.action: str = action 
        self.period: 'Period' = period 
        self.recorded: str = recorded 
        self.outcome: str = outcome 
        self.outcomeDesc: str = outcomeDesc 
        self.purposeOfEvent: list['CodeableConcept'] = purposeOfEvent or []
        self.agent: list['Agent'] = agent or []
        self.source: 'Source' = source 
        self.entity: list['Entity'] = entity or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
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