"""
Generated class for PlanDefinition. 
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
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Age import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Target(ModelBase):
    """ Indicates what should be done and within what timeframe.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' measure: The parameter whose value is to be tracked
    :param 'Quantity' detailQuantity: The target value to be achieved
    :param 'Range' detailRange: The target value to be achieved
    :param 'CodeableConcept' detailCodeableConcept: The target value to be achieved
    :param 'Duration' due: Reach goal within
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  measure: 'CodeableConcept' = None,  detailQuantity: 'Quantity' = None,  detailRange: 'Range' = None,  detailCodeableConcept: 'CodeableConcept' = None,  due: 'Duration' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.measure: 'CodeableConcept' = measure 
        self.detailQuantity: 'Quantity' = detailQuantity 
        self.detailRange: 'Range' = detailRange 
        self.detailCodeableConcept: 'CodeableConcept' = detailCodeableConcept 
        self.due: 'Duration' = due 
        

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


  
    
    

class Goal(ModelBase):
    """ Goals that describe what the activities within the plan are intended to achieve. For example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' category: E.g. Treatment, dietary, behavioral
    :param 'CodeableConcept' description: Code or text describing the goal
    :param 'CodeableConcept' priority: high-priority | medium-priority | low-priority
    :param 'CodeableConcept' start: When goal pursuit begins
    :param list['CodeableConcept'] addresses: What does the goal address
    :param list['RelatedArtifact'] documentation: Supporting documentation for the goal
    :param list['Target'] target: Target outcome for the goal
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  category: 'CodeableConcept' = None,  description: 'CodeableConcept' = None,  priority: 'CodeableConcept' = None,  start: 'CodeableConcept' = None,  addresses: list['CodeableConcept'] = None,  documentation: list['RelatedArtifact'] = None,  target: list['Target'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.category: 'CodeableConcept' = category 
        self.description: 'CodeableConcept' = description 
        self.priority: 'CodeableConcept' = priority 
        self.start: 'CodeableConcept' = start 
        self.addresses: list['CodeableConcept'] = addresses or []
        self.documentation: list['RelatedArtifact'] = documentation or []
        self.target: list['Target'] = target or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Goal":
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


    
        
    
    

class Condition(ModelBase):
    """ An expression that describes applicability criteria or start/stop conditions for the action.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str kind: applicability | start | stop
    :param 'Expression' expression: Boolean-valued expression
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  kind: str = None,  expression: 'Expression' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.kind: str = kind 
        self.expression: 'Expression' = expression 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Condition":
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


    
    

class RelatedAction(ModelBase):
    """ A relationship to another action such as "before" or "30-60 minutes after start of".:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str actionId: What action is this related to
    :param str relationship: before-start | before | before-end | concurrent-with-start | concurrent | concurrent-with-end | after-start | after | after-end
    :param 'Duration' offsetDuration: Time offset for the relationship
    :param 'Range' offsetRange: Time offset for the relationship
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  actionId: str = None,  relationship: str = None,  offsetDuration: 'Duration' = None,  offsetRange: 'Range' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.actionId: str = actionId 
        self.relationship: str = relationship 
        self.offsetDuration: 'Duration' = offsetDuration 
        self.offsetRange: 'Range' = offsetRange 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RelatedAction":
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


    
    

class Participant(ModelBase):
    """ Indicates who should participate in performing the action described.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: patient | practitioner | related-person | device
    :param 'CodeableConcept' role: E.g. Nurse, Surgeon, Parent
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
    """ Customizations that should be applied to the statically defined resource. For example, if the dosage of a medication must be computed based on the patient's weight, a customization would be used to specify an expression that calculated the weight, and the path on the resource that would contain the result.:param str id: Unique id for inter-element referencing
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


  
    
    

class Action(ModelBase):
    """ An action or group of actions to be taken as part of the plan.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str prefix: User-visible prefix for the action (e.g. 1. or A.)
    :param str title: User-visible title
    :param str description: Brief description of the action
    :param str textEquivalent: Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system
    :param str priority: routine | urgent | asap | stat
    :param list['CodeableConcept'] code: Code representing the meaning of the action or sub-actions
    :param list['CodeableConcept'] reason: Why the action should be performed
    :param list['RelatedArtifact'] documentation: Supporting documentation for the intended performer of the action
    :param str goalId: What goals this action supports
    :param 'CodeableConcept' subjectCodeableConcept: Type of individual the action is focused on
    :param 'Reference' subjectReference: Type of individual the action is focused on
    :param list['TriggerDefinition'] trigger: When the action should be triggered
    :param list['Condition'] condition: Whether or not the action is applicable
    :param list['DataRequirement'] input: Input data requirements
    :param list['DataRequirement'] output: Output data definition
    :param list['RelatedAction'] relatedAction: Relationship to another action
    :param str timingDateTime: When the action should take place
    :param 'Age' timingAge: When the action should take place
    :param 'Period' timingPeriod: When the action should take place
    :param 'Duration' timingDuration: When the action should take place
    :param 'Range' timingRange: When the action should take place
    :param 'Timing' timingTiming: When the action should take place
    :param list['Participant'] participant: Who should participate in the action
    :param 'CodeableConcept' type: create | update | remove | fire-event
    :param str groupingBehavior: visual-group | logical-group | sentence-group
    :param str selectionBehavior: any | all | all-or-none | exactly-one | at-most-one | one-or-more
    :param str requiredBehavior: must | could | must-unless-documented
    :param str precheckBehavior: yes | no
    :param str cardinalityBehavior: single | multiple
    :param str definitionCanonical: Description of the activity to be performed
    :param str definitionUri: Description of the activity to be performed
    :param str transform: Transform to apply the template
    :param list['DynamicValue'] dynamicValue: Dynamic aspects of the definition
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  prefix: str = None,  title: str = None,  description: str = None,  textEquivalent: str = None,  priority: str = None,  code: list['CodeableConcept'] = None,  reason: list['CodeableConcept'] = None,  documentation: list['RelatedArtifact'] = None,  goalId: str = None,  subjectCodeableConcept: 'CodeableConcept' = None,  subjectReference: 'Reference' = None,  trigger: list['TriggerDefinition'] = None,  condition: list['Condition'] = None,  input: list['DataRequirement'] = None,  output: list['DataRequirement'] = None,  relatedAction: list['RelatedAction'] = None,  timingDateTime: str = None,  timingAge: 'Age' = None,  timingPeriod: 'Period' = None,  timingDuration: 'Duration' = None,  timingRange: 'Range' = None,  timingTiming: 'Timing' = None,  participant: list['Participant'] = None,  type: 'CodeableConcept' = None,  groupingBehavior: str = None,  selectionBehavior: str = None,  requiredBehavior: str = None,  precheckBehavior: str = None,  cardinalityBehavior: str = None,  definitionCanonical: str = None,  definitionUri: str = None,  transform: str = None,  dynamicValue: list['DynamicValue'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.prefix: str = prefix 
        self.title: str = title 
        self.description: str = description 
        self.textEquivalent: str = textEquivalent 
        self.priority: str = priority 
        self.code: list['CodeableConcept'] = code or []
        self.reason: list['CodeableConcept'] = reason or []
        self.documentation: list['RelatedArtifact'] = documentation or []
        self.goalId: str = goalId or []
        self.subjectCodeableConcept: 'CodeableConcept' = subjectCodeableConcept 
        self.subjectReference: 'Reference' = subjectReference 
        self.trigger: list['TriggerDefinition'] = trigger or []
        self.condition: list['Condition'] = condition or []
        self.input: list['DataRequirement'] = input or []
        self.output: list['DataRequirement'] = output or []
        self.relatedAction: list['RelatedAction'] = relatedAction or []
        self.timingDateTime: str = timingDateTime 
        self.timingAge: 'Age' = timingAge 
        self.timingPeriod: 'Period' = timingPeriod 
        self.timingDuration: 'Duration' = timingDuration 
        self.timingRange: 'Range' = timingRange 
        self.timingTiming: 'Timing' = timingTiming 
        self.participant: list['Participant'] = participant or []
        self.type: 'CodeableConcept' = type 
        self.groupingBehavior: str = groupingBehavior 
        self.selectionBehavior: str = selectionBehavior 
        self.requiredBehavior: str = requiredBehavior 
        self.precheckBehavior: str = precheckBehavior 
        self.cardinalityBehavior: str = cardinalityBehavior 
        self.definitionCanonical: str = definitionCanonical 
        self.definitionUri: str = definitionUri 
        self.transform: str = transform 
        self.dynamicValue: list['DynamicValue'] = dynamicValue or []
        

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


class PlanDefinition(DomainResource):
    """ This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. The resource is general enough to support the description of a broad range of clinical artifacts such as clinical decision support rules, order sets and protocols.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this plan definition, represented as a URI (globally unique)
    :param list['Identifier'] identifier: Additional identifier for the plan definition
    :param str version: Business version of the plan definition
    :param str name: Name for this plan definition (computer friendly)
    :param str title: Name for this plan definition (human friendly)
    :param str subtitle: Subordinate title of the plan definition
    :param 'CodeableConcept' type: order-set | clinical-protocol | eca-rule | workflow-definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param 'CodeableConcept' subjectCodeableConcept: Type of individual the plan definition is focused on
    :param 'Reference' subjectReference: Type of individual the plan definition is focused on
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the plan definition
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for plan definition (if applicable)
    :param str purpose: Why this plan definition is defined
    :param str usage: Describes the clinical usage of the plan
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the plan definition was approved by publisher
    :param str lastReviewDate: When the plan definition was last reviewed
    :param 'Period' effectivePeriod: When the plan definition is expected to be used
    :param list['CodeableConcept'] topic: E.g. Education, Treatment, Assessment
    :param list['ContactDetail'] author: Who authored the content
    :param list['ContactDetail'] editor: Who edited the content
    :param list['ContactDetail'] reviewer: Who reviewed the content
    :param list['ContactDetail'] endorser: Who endorsed the content
    :param list['RelatedArtifact'] relatedArtifact: Additional documentation, citations
    :param str library: Logic used by the plan definition
    :param list['Goal'] goal: What the plan is trying to accomplish
    :param list['Action'] action: Action defined by the plan
    """
    def __init__(self, resourceType: str = "PlanDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  identifier: list['Identifier'] = None,  version: str = None,  name: str = None,  title: str = None,  subtitle: str = None,  type: 'CodeableConcept' = None,  status: str = None,  experimental: bool = None,  subjectCodeableConcept: 'CodeableConcept' = None,  subjectReference: 'Reference' = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  purpose: str = None,  usage: str = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  topic: list['CodeableConcept'] = None,  author: list['ContactDetail'] = None,  editor: list['ContactDetail'] = None,  reviewer: list['ContactDetail'] = None,  endorser: list['ContactDetail'] = None,  relatedArtifact: list['RelatedArtifact'] = None,  library: str = None,  goal: list['Goal'] = None,  action: list['Action'] = None, ):
        self.resourceType: str = resourceType or "PlanDefinition"
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
        self.type: 'CodeableConcept' = type 
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
        self.goal: list['Goal'] = goal or []
        self.action: list['Action'] = action or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PlanDefinition":
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