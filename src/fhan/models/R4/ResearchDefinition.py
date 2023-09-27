"""
Generated class for ResearchDefinition. 
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
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class ResearchDefinition(DomainResource):
    """ The ResearchDefinition resource describes the conditional state (population and any exposures being compared within the population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is about.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this research definition, represented as a URI (globally unique)
    :param 'Identifier' identifier: Additional identifier for the research definition
    :param str version: Business version of the research definition
    :param str name: Name for this research definition (computer friendly)
    :param str title: Name for this research definition (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the ResearchDefinition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param 'CodeableConcept' subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param 'Reference' subjectReference: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param 'ContactDetail' contact: Contact details for the publisher
    :param str description: Natural language description of the research definition
    :param str comment: Used for footnotes or explanatory notes
    :param 'UsageContext' useContext: The context that the content is intended to support
    :param 'CodeableConcept' jurisdiction: Intended jurisdiction for research definition (if applicable)
    :param str purpose: Why this research definition is defined
    :param str usage: Describes the clinical usage of the ResearchDefinition
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the research definition was approved by publisher
    :param str lastReviewDate: When the research definition was last reviewed
    :param 'Period' effectivePeriod: When the research definition is expected to be used
    :param 'CodeableConcept' topic: The category of the ResearchDefinition, such as Education, Treatment, Assessment, etc.
    :param 'ContactDetail' author: Who authored the content
    :param 'ContactDetail' editor: Who edited the content
    :param 'ContactDetail' reviewer: Who reviewed the content
    :param 'ContactDetail' endorser: Who endorsed the content
    :param 'RelatedArtifact' relatedArtifact: Additional documentation, citations, etc.
    :param str library: Logic used by the ResearchDefinition
    :param 'Reference' population: What population?
    :param 'Reference' exposure: What exposure?
    :param 'Reference' exposureAlternative: What alternative exposure state?
    :param 'Reference' outcome: What outcome?
    """
    def __init__(self, resourceType: str = "ResearchDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  url: str = None,  identifier: 'Identifier' = None,  version: str = None,  name: str = None,  title: str = None,  shortTitle: str = None,  subtitle: str = None,  status: str = None,  experimental: bool = None,  subjectCodeableConcept: 'CodeableConcept' = None,  subjectReference: 'Reference' = None,  date: str = None,  publisher: str = None,  contact: 'ContactDetail' = None,  description: str = None,  comment: str = None,  useContext: 'UsageContext' = None,  jurisdiction: 'CodeableConcept' = None,  purpose: str = None,  usage: str = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  topic: 'CodeableConcept' = None,  author: 'ContactDetail' = None,  editor: 'ContactDetail' = None,  reviewer: 'ContactDetail' = None,  endorser: 'ContactDetail' = None,  relatedArtifact: 'RelatedArtifact' = None,  library: str = None,  population: 'Reference' = None,  exposure: 'Reference' = None,  exposureAlternative: 'Reference' = None,  outcome: 'Reference' = None, ):
        self.resourceType: str = resourceType or "ResearchDefinition"
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
        self.shortTitle: str = shortTitle 
        self.subtitle: str = subtitle 
        self.status: str = status 
        self.experimental: bool = experimental 
        self.subjectCodeableConcept: 'CodeableConcept' = subjectCodeableConcept 
        self.subjectReference: 'Reference' = subjectReference 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.comment: list[str] = comment or []
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
        self.library: list[str] = library or []
        self.population: 'Reference' = population 
        self.exposure: 'Reference' = exposure 
        self.exposureAlternative: 'Reference' = exposureAlternative 
        self.outcome: 'Reference' = outcome 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchDefinition":
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