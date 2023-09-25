"""
Generated class for ResearchElementDefinition. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Expression import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Characteristic(ModelBase):
    """ A characteristic that defines the members of the research element. Multiple characteristics are applied with "and" semantics.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' definitionCodeableConcept: What code or expression defines members?
    :param str definitionCanonical: What code or expression defines members?
    :param 'Expression' definitionExpression: What code or expression defines members?
    :param 'DataRequirement' definitionDataRequirement: What code or expression defines members?
    :param list['UsageContext'] usageContext: What code/value pairs define members?
    :param bool exclude: Whether the characteristic includes or excludes members
    :param 'CodeableConcept' unitOfMeasure: What unit is the outcome described in?
    :param str studyEffectiveDescription: What time period does the study cover
    :param str studyEffectiveDateTime: What time period does the study cover
    :param 'Period' studyEffectivePeriod: What time period does the study cover
    :param 'Duration' studyEffectiveDuration: What time period does the study cover
    :param 'Timing' studyEffectiveTiming: What time period does the study cover
    :param 'Duration' studyEffectiveTimeFromStart: Observation time from study start
    :param str studyEffectiveGroupMeasure: mean | median | mean-of-mean | mean-of-median | median-of-mean | median-of-median
    :param str participantEffectiveDescription: What time period do participants cover
    :param str participantEffectiveDateTime: What time period do participants cover
    :param 'Period' participantEffectivePeriod: What time period do participants cover
    :param 'Duration' participantEffectiveDuration: What time period do participants cover
    :param 'Timing' participantEffectiveTiming: What time period do participants cover
    :param 'Duration' participantEffectiveTimeFromStart: Observation time from study start
    :param str participantEffectiveGroupMeasure: mean | median | mean-of-mean | mean-of-median | median-of-mean | median-of-median
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  definitionCodeableConcept: 'CodeableConcept' = None,  definitionCanonical: str = None,  definitionExpression: 'Expression' = None,  definitionDataRequirement: 'DataRequirement' = None,  usageContext: list['UsageContext'] = None,  exclude: bool = None,  unitOfMeasure: 'CodeableConcept' = None,  studyEffectiveDescription: str = None,  studyEffectiveDateTime: str = None,  studyEffectivePeriod: 'Period' = None,  studyEffectiveDuration: 'Duration' = None,  studyEffectiveTiming: 'Timing' = None,  studyEffectiveTimeFromStart: 'Duration' = None,  studyEffectiveGroupMeasure: str = None,  participantEffectiveDescription: str = None,  participantEffectiveDateTime: str = None,  participantEffectivePeriod: 'Period' = None,  participantEffectiveDuration: 'Duration' = None,  participantEffectiveTiming: 'Timing' = None,  participantEffectiveTimeFromStart: 'Duration' = None,  participantEffectiveGroupMeasure: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.definitionCodeableConcept: 'CodeableConcept' = definitionCodeableConcept 
        self.definitionCanonical: str = definitionCanonical 
        self.definitionExpression: 'Expression' = definitionExpression 
        self.definitionDataRequirement: 'DataRequirement' = definitionDataRequirement 
        self.usageContext: list['UsageContext'] = usageContext or []
        self.exclude: bool = exclude 
        self.unitOfMeasure: 'CodeableConcept' = unitOfMeasure 
        self.studyEffectiveDescription: str = studyEffectiveDescription 
        self.studyEffectiveDateTime: str = studyEffectiveDateTime 
        self.studyEffectivePeriod: 'Period' = studyEffectivePeriod 
        self.studyEffectiveDuration: 'Duration' = studyEffectiveDuration 
        self.studyEffectiveTiming: 'Timing' = studyEffectiveTiming 
        self.studyEffectiveTimeFromStart: 'Duration' = studyEffectiveTimeFromStart 
        self.studyEffectiveGroupMeasure: str = studyEffectiveGroupMeasure 
        self.participantEffectiveDescription: str = participantEffectiveDescription 
        self.participantEffectiveDateTime: str = participantEffectiveDateTime 
        self.participantEffectivePeriod: 'Period' = participantEffectivePeriod 
        self.participantEffectiveDuration: 'Duration' = participantEffectiveDuration 
        self.participantEffectiveTiming: 'Timing' = participantEffectiveTiming 
        self.participantEffectiveTimeFromStart: 'Duration' = participantEffectiveTimeFromStart 
        self.participantEffectiveGroupMeasure: str = participantEffectiveGroupMeasure 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Characteristic":
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


class ResearchElementDefinition(DomainResource):
    """ The ResearchElementDefinition resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this research element definition, represented as a URI (globally unique)
    :param list['Identifier'] identifier: Additional identifier for the research element definition
    :param str version: Business version of the research element definition
    :param str name: Name for this research element definition (computer friendly)
    :param str title: Name for this research element definition (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the ResearchElementDefinition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param 'CodeableConcept' subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param 'Reference' subjectReference: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the research element definition
    :param str comment: Used for footnotes or explanatory notes
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for research element definition (if applicable)
    :param str purpose: Why this research element definition is defined
    :param str usage: Describes the clinical usage of the ResearchElementDefinition
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the research element definition was approved by publisher
    :param str lastReviewDate: When the research element definition was last reviewed
    :param 'Period' effectivePeriod: When the research element definition is expected to be used
    :param list['CodeableConcept'] topic: The category of the ResearchElementDefinition, such as Education, Treatment, Assessment, etc.
    :param list['ContactDetail'] author: Who authored the content
    :param list['ContactDetail'] editor: Who edited the content
    :param list['ContactDetail'] reviewer: Who reviewed the content
    :param list['ContactDetail'] endorser: Who endorsed the content
    :param list['RelatedArtifact'] relatedArtifact: Additional documentation, citations, etc.
    :param str library: Logic used by the ResearchElementDefinition
    :param str type: population | exposure | outcome
    :param str variableType: dichotomous | continuous | descriptive
    :param list['Characteristic'] characteristic: What defines the members of the research element
    """
    def __init__(self, resourceType: str = "ResearchElementDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  identifier: list['Identifier'] = None,  version: str = None,  name: str = None,  title: str = None,  shortTitle: str = None,  subtitle: str = None,  status: str = None,  experimental: bool = None,  subjectCodeableConcept: 'CodeableConcept' = None,  subjectReference: 'Reference' = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  comment: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  purpose: str = None,  usage: str = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  topic: list['CodeableConcept'] = None,  author: list['ContactDetail'] = None,  editor: list['ContactDetail'] = None,  reviewer: list['ContactDetail'] = None,  endorser: list['ContactDetail'] = None,  relatedArtifact: list['RelatedArtifact'] = None,  library: str = None,  type: str = None,  variableType: str = None,  characteristic: list['Characteristic'] = None, ):
        self.resourceType: str = resourceType or "ResearchElementDefinition"
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
        self.comment: str = comment or []
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
        self.library: str = library or []
        self.type: str = type 
        self.variableType: str = variableType 
        self.characteristic: list['Characteristic'] = characteristic or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchElementDefinition":
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