"""
Generated class for ActivityDefinition. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Quantity import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Age import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Resource import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.DomainResource import *


    
    

class Participant(ModelBase):
    """ Indicates who should participate in performing the action described.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: patient | practitioner | related-person | device
    :param 'CodeableConcept' role: E.g. Nurse, Surgeon, Parent, etc.
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  role: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.role: 'CodeableConcept' = role 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Participant":
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


    
    

class DynamicValue(ModelBase):
    """ Dynamic values that will be evaluated to produce values for elements of the resulting resource. For example, if the dosage of a medication must be computed based on the patient's weight, a dynamic value would be used to specify an expression that calculated the weight, and the path on the request resource that would contain the result.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: The path to the element to be set dynamically
    :param 'Expression' expression: An expression that provides the dynamic value for the customization
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  path: str = None,  expression: 'Expression' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.path: str = path 
        self.expression: 'Expression' = expression 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DynamicValue":
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


class ActivityDefinition(DomainResource):
    """ This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this activity definition, represented as a URI (globally unique)
    :param list['Identifier'] identifier: Additional identifier for the activity definition
    :param str version: Business version of the activity definition
    :param str name: Name for this activity definition (computer friendly)
    :param str title: Name for this activity definition (human friendly)
    :param str subtitle: Subordinate title of the activity definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param 'CodeableConcept' subjectCodeableConcept: Type of individual the activity definition is intended for
    :param 'Reference' subjectReference: Type of individual the activity definition is intended for
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the activity definition
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for activity definition (if applicable)
    :param str purpose: Why this activity definition is defined
    :param str usage: Describes the clinical usage of the activity definition
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the activity definition was approved by publisher
    :param str lastReviewDate: When the activity definition was last reviewed
    :param 'Period' effectivePeriod: When the activity definition is expected to be used
    :param list['CodeableConcept'] topic: E.g. Education, Treatment, Assessment, etc.
    :param list['ContactDetail'] author: Who authored the content
    :param list['ContactDetail'] editor: Who edited the content
    :param list['ContactDetail'] reviewer: Who reviewed the content
    :param list['ContactDetail'] endorser: Who endorsed the content
    :param list['RelatedArtifact'] relatedArtifact: Additional documentation, citations, etc.
    :param str library: Logic used by the activity definition
    :param str kind: Kind of resource
    :param str profile: What profile the resource needs to conform to
    :param 'CodeableConcept' code: Detail type of activity
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if the activity should not be performed
    :param 'Timing' timingTiming: When activity is to occur
    :param str timingDateTime: When activity is to occur
    :param 'Age' timingAge: When activity is to occur
    :param 'Period' timingPeriod: When activity is to occur
    :param 'Range' timingRange: When activity is to occur
    :param 'Duration' timingDuration: When activity is to occur
    :param 'Reference' location: Where it should happen
    :param list['Participant'] participant: Who should participate in the action
    :param 'Reference' productReference: What's administered/supplied
    :param 'CodeableConcept' productCodeableConcept: What's administered/supplied
    :param 'Quantity' quantity: How much is administered/consumed/supplied
    :param list['Dosage'] dosage: Detailed dosage instructions
    :param list['CodeableConcept'] bodySite: What part of body to perform on
    :param list['Reference'] specimenRequirement: What specimens are required to perform this action
    :param list['Reference'] observationRequirement: What observations are required to perform this action
    :param list['Reference'] observationResultRequirement: What observations must be produced by this action
    :param str transform: Transform to apply the template
    :param list['DynamicValue'] dynamicValue: Dynamic aspects of the definition
    """
    def __init__(self, resourceType: str = "ActivityDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  identifier: list['Identifier'] = None,  version: str = None,  name: str = None,  title: str = None,  subtitle: str = None,  status: str = None,  experimental: bool = None,  subjectCodeableConcept: 'CodeableConcept' = None,  subjectReference: 'Reference' = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  purpose: str = None,  usage: str = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  topic: list['CodeableConcept'] = None,  author: list['ContactDetail'] = None,  editor: list['ContactDetail'] = None,  reviewer: list['ContactDetail'] = None,  endorser: list['ContactDetail'] = None,  relatedArtifact: list['RelatedArtifact'] = None,  library: str = None,  kind: str = None,  profile: str = None,  code: 'CodeableConcept' = None,  intent: str = None,  priority: str = None,  doNotPerform: bool = None,  timingTiming: 'Timing' = None,  timingDateTime: str = None,  timingAge: 'Age' = None,  timingPeriod: 'Period' = None,  timingRange: 'Range' = None,  timingDuration: 'Duration' = None,  location: 'Reference' = None,  participant: list['Participant'] = None,  productReference: 'Reference' = None,  productCodeableConcept: 'CodeableConcept' = None,  quantity: 'Quantity' = None,  dosage: list['Dosage'] = None,  bodySite: list['CodeableConcept'] = None,  specimenRequirement: list['Reference'] = None,  observationRequirement: list['Reference'] = None,  observationResultRequirement: list['Reference'] = None,  transform: str = None,  dynamicValue: list['DynamicValue'] = None, ):
        self.resourceType: str = resourceType or "ActivityDefinition"
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
        self.library: str = library or []
        self.kind: str = kind 
        self.profile: str = profile 
        self.code: 'CodeableConcept' = code 
        self.intent: str = intent 
        self.priority: str = priority 
        self.doNotPerform: bool = doNotPerform 
        self.timingTiming: 'Timing' = timingTiming 
        self.timingDateTime: str = timingDateTime 
        self.timingAge: 'Age' = timingAge 
        self.timingPeriod: 'Period' = timingPeriod 
        self.timingRange: 'Range' = timingRange 
        self.timingDuration: 'Duration' = timingDuration 
        self.location: 'Reference' = location 
        self.participant: list['Participant'] = participant or []
        self.productReference: 'Reference' = productReference 
        self.productCodeableConcept: 'CodeableConcept' = productCodeableConcept 
        self.quantity: 'Quantity' = quantity 
        self.dosage: list['Dosage'] = dosage or []
        self.bodySite: list['CodeableConcept'] = bodySite or []
        self.specimenRequirement: list['Reference'] = specimenRequirement or []
        self.observationRequirement: list['Reference'] = observationRequirement or []
        self.observationResultRequirement: list['Reference'] = observationResultRequirement or []
        self.transform: str = transform 
        self.dynamicValue: list['DynamicValue'] = dynamicValue or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ActivityDefinition":
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