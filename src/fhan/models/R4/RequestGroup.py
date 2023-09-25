"""
Generated class for RequestGroup. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Age import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Condition(ModelBase):
    """ An expression that describes applicability criteria, or start/stop conditions for the action.:param str id: Unique id for inter-element referencing
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
    :param str actionId: What action this is related to
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


  
    
    

class Action(ModelBase):
    """ The actions, if any, produced by the evaluation of the artifact.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str prefix: User-visible prefix for the action (e.g. 1. or A.)
    :param str title: User-visible title
    :param str description: Short description of the action
    :param str textEquivalent: Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system
    :param str priority: routine | urgent | asap | stat
    :param list['CodeableConcept'] code: Code representing the meaning of the action or sub-actions
    :param list['RelatedArtifact'] documentation: Supporting documentation for the intended performer of the action
    :param list['Condition'] condition: Whether or not the action is applicable
    :param list['RelatedAction'] relatedAction: Relationship to another action
    :param str timingDateTime: When the action should take place
    :param 'Age' timingAge: When the action should take place
    :param 'Period' timingPeriod: When the action should take place
    :param 'Duration' timingDuration: When the action should take place
    :param 'Range' timingRange: When the action should take place
    :param 'Timing' timingTiming: When the action should take place
    :param list['Reference'] participant: Who should perform the action
    :param 'CodeableConcept' type: create | update | remove | fire-event
    :param str groupingBehavior: visual-group | logical-group | sentence-group
    :param str selectionBehavior: any | all | all-or-none | exactly-one | at-most-one | one-or-more
    :param str requiredBehavior: must | could | must-unless-documented
    :param str precheckBehavior: yes | no
    :param str cardinalityBehavior: single | multiple
    :param 'Reference' resource: The target of the action
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  prefix: str = None,  title: str = None,  description: str = None,  textEquivalent: str = None,  priority: str = None,  code: list['CodeableConcept'] = None,  documentation: list['RelatedArtifact'] = None,  condition: list['Condition'] = None,  relatedAction: list['RelatedAction'] = None,  timingDateTime: str = None,  timingAge: 'Age' = None,  timingPeriod: 'Period' = None,  timingDuration: 'Duration' = None,  timingRange: 'Range' = None,  timingTiming: 'Timing' = None,  participant: list['Reference'] = None,  type: 'CodeableConcept' = None,  groupingBehavior: str = None,  selectionBehavior: str = None,  requiredBehavior: str = None,  precheckBehavior: str = None,  cardinalityBehavior: str = None,  resource: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.prefix: str = prefix 
        self.title: str = title 
        self.description: str = description 
        self.textEquivalent: str = textEquivalent 
        self.priority: str = priority 
        self.code: list['CodeableConcept'] = code or []
        self.documentation: list['RelatedArtifact'] = documentation or []
        self.condition: list['Condition'] = condition or []
        self.relatedAction: list['RelatedAction'] = relatedAction or []
        self.timingDateTime: str = timingDateTime 
        self.timingAge: 'Age' = timingAge 
        self.timingPeriod: 'Period' = timingPeriod 
        self.timingDuration: 'Duration' = timingDuration 
        self.timingRange: 'Range' = timingRange 
        self.timingTiming: 'Timing' = timingTiming 
        self.participant: list['Reference'] = participant or []
        self.type: 'CodeableConcept' = type 
        self.groupingBehavior: str = groupingBehavior 
        self.selectionBehavior: str = selectionBehavior 
        self.requiredBehavior: str = requiredBehavior 
        self.precheckBehavior: str = precheckBehavior 
        self.cardinalityBehavior: str = cardinalityBehavior 
        self.resource: 'Reference' = resource 
        

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


class RequestGroup(DomainResource):
    """ A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param list['Reference'] basedOn: Fulfills plan, proposal, or order
    :param list['Reference'] replaces: Request(s) replaced by this request
    :param 'Identifier' groupIdentifier: Composite request this is part of
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param 'CodeableConcept' code: What's being requested/ordered
    :param 'Reference' subject: Who the request group is about
    :param 'Reference' encounter: Created as part of
    :param str authoredOn: When the request group was authored
    :param 'Reference' author: Device or practitioner that authored the request group
    :param list['CodeableConcept'] reasonCode: Why the request group is needed
    :param list['Reference'] reasonReference: Why the request group is needed
    :param list['Annotation'] note: Additional notes about the response
    :param list['Action'] action: Proposed actions, if any
    """
    def __init__(self, resourceType: str = "RequestGroup",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  replaces: list['Reference'] = None,  groupIdentifier: 'Identifier' = None,  status: str = None,  intent: str = None,  priority: str = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  authoredOn: str = None,  author: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  note: list['Annotation'] = None,  action: list['Action'] = None, ):
        self.resourceType: str = resourceType or "RequestGroup"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.basedOn: list['Reference'] = basedOn or []
        self.replaces: list['Reference'] = replaces or []
        self.groupIdentifier: 'Identifier' = groupIdentifier 
        self.status: str = status 
        self.intent: str = intent 
        self.priority: str = priority 
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.authoredOn: str = authoredOn 
        self.author: 'Reference' = author 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.note: list['Annotation'] = note or []
        self.action: list['Action'] = action or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RequestGroup":
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