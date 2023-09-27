"""
Generated class for EventDefinition. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class EventDefinition(DomainResource):
    """ The EventDefinition resource provides a reusable description of when a particular event can occur.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this event definition, represented as a URI (globally unique)
    :param 'Identifier' identifier: Additional identifier for the event definition
    :param str version: Business version of the event definition
    :param str name: Name for this event definition (computer friendly)
    :param str title: Name for this event definition (human friendly)
    :param str subtitle: Subordinate title of the event definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param 'CodeableConcept' subjectCodeableConcept: Type of individual the event definition is focused on
    :param 'Reference' subjectReference: Type of individual the event definition is focused on
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param 'ContactDetail' contact: Contact details for the publisher
    :param str description: Natural language description of the event definition
    :param 'UsageContext' useContext: The context that the content is intended to support
    :param 'CodeableConcept' jurisdiction: Intended jurisdiction for event definition (if applicable)
    :param str purpose: Why this event definition is defined
    :param str usage: Describes the clinical usage of the event definition
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the event definition was approved by publisher
    :param str lastReviewDate: When the event definition was last reviewed
    :param 'Period' effectivePeriod: When the event definition is expected to be used
    :param 'CodeableConcept' topic: E.g. Education, Treatment, Assessment, etc.
    :param 'ContactDetail' author: Who authored the content
    :param 'ContactDetail' editor: Who edited the content
    :param 'ContactDetail' reviewer: Who reviewed the content
    :param 'ContactDetail' endorser: Who endorsed the content
    :param 'RelatedArtifact' relatedArtifact: Additional documentation, citations, etc.
    :param 'TriggerDefinition' trigger: "when" the event occurs (multiple = 'or')
    """
    def __init__(self, resourceType: str = "EventDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  url: str = None,  identifier: 'Identifier' = None,  version: str = None,  name: str = None,  title: str = None,  subtitle: str = None,  status: str = None,  experimental: bool = None,  subjectCodeableConcept: 'CodeableConcept' = None,  subjectReference: 'Reference' = None,  date: str = None,  publisher: str = None,  contact: 'ContactDetail' = None,  description: str = None,  useContext: 'UsageContext' = None,  jurisdiction: 'CodeableConcept' = None,  purpose: str = None,  usage: str = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  topic: 'CodeableConcept' = None,  author: 'ContactDetail' = None,  editor: 'ContactDetail' = None,  reviewer: 'ContactDetail' = None,  endorser: 'ContactDetail' = None,  relatedArtifact: 'RelatedArtifact' = None,  trigger: 'TriggerDefinition' = None, ):
        self.resourceType: str = resourceType or "EventDefinition"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.url: str = url 
        self.identifier: list['Identifier'] = identifier or []
        self.version: str = version 
        self.name: str = name 
        self.title: str = title 
        self.subtitle: str = subtitle 
        self.status: str = status 
        self.experimental: bool = experimental 
        self.subjectCodeableConcept: 'CodeableConcept' = subjectCodeableConcept 
        self.subjectReference: 'Reference' = subjectReference 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.purpose: str = purpose 
        self.usage: str = usage 
        self.copyright: str = copyright 
        self.approvalDate: str = approvalDate 
        self.lastReviewDate: str = lastReviewDate 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.topic: list['CodeableConcept'] = topic or []
        self.author: list['ContactDetail'] = author or []
        self.editor: list['ContactDetail'] = editor or []
        self.reviewer: list['ContactDetail'] = reviewer or []
        self.endorser: list['ContactDetail'] = endorser or []
        self.relatedArtifact: list['RelatedArtifact'] = relatedArtifact or []
        self.trigger: list['TriggerDefinition'] = trigger or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EventDefinition":
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