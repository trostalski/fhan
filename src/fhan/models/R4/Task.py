"""
Generated class for Task. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Distance import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Duration import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Count import *
from fhan.models.R4.Address import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Age import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.DomainResource import *


    
    

class Restriction(ModelBase):
    """ If the Task.focus is a request resource and the task is seeking fulfillment (i.e. is asking for the request to be actioned), this element identifies any limitations on what parts of the referenced request should be actioned.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int repetitions: How many times to repeat
    :param 'Period' period: When fulfillment sought
    :param list['Reference'] recipient: For whom is fulfillment sought?
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  repetitions: int = None,  period: 'Period' = None,  recipient: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.repetitions: int = repetitions 
        self.period: 'Period' = period 
        self.recipient: list['Reference'] = recipient or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Restriction":
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


    
    

class Input(ModelBase):
    """ Additional information that may be needed in the execution of the task.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Label for the input
    :param str valueBase64Binary: Content to use in performing the task
    :param bool valueBoolean: Content to use in performing the task
    :param str valueCanonical: Content to use in performing the task
    :param str valueCode: Content to use in performing the task
    :param str valueDate: Content to use in performing the task
    :param str valueDateTime: Content to use in performing the task
    :param float valueDecimal: Content to use in performing the task
    :param str valueId: Content to use in performing the task
    :param str valueInstant: Content to use in performing the task
    :param int valueInteger: Content to use in performing the task
    :param str valueMarkdown: Content to use in performing the task
    :param str valueOid: Content to use in performing the task
    :param int valuePositiveInt: Content to use in performing the task
    :param str valueString: Content to use in performing the task
    :param str valueTime: Content to use in performing the task
    :param int valueUnsignedInt: Content to use in performing the task
    :param str valueUri: Content to use in performing the task
    :param str valueUrl: Content to use in performing the task
    :param str valueUuid: Content to use in performing the task
    :param 'Address' valueAddress: Content to use in performing the task
    :param 'Age' valueAge: Content to use in performing the task
    :param 'Annotation' valueAnnotation: Content to use in performing the task
    :param 'Attachment' valueAttachment: Content to use in performing the task
    :param 'CodeableConcept' valueCodeableConcept: Content to use in performing the task
    :param 'Coding' valueCoding: Content to use in performing the task
    :param 'ContactPoint' valueContactPoint: Content to use in performing the task
    :param 'Count' valueCount: Content to use in performing the task
    :param 'Distance' valueDistance: Content to use in performing the task
    :param 'Duration' valueDuration: Content to use in performing the task
    :param 'HumanName' valueHumanName: Content to use in performing the task
    :param 'Identifier' valueIdentifier: Content to use in performing the task
    :param 'Money' valueMoney: Content to use in performing the task
    :param 'Period' valuePeriod: Content to use in performing the task
    :param 'Quantity' valueQuantity: Content to use in performing the task
    :param 'Range' valueRange: Content to use in performing the task
    :param 'Ratio' valueRatio: Content to use in performing the task
    :param 'Reference' valueReference: Content to use in performing the task
    :param 'SampledData' valueSampledData: Content to use in performing the task
    :param 'Signature' valueSignature: Content to use in performing the task
    :param 'Timing' valueTiming: Content to use in performing the task
    :param 'ContactDetail' valueContactDetail: Content to use in performing the task
    :param 'Contributor' valueContributor: Content to use in performing the task
    :param 'DataRequirement' valueDataRequirement: Content to use in performing the task
    :param 'Expression' valueExpression: Content to use in performing the task
    :param 'ParameterDefinition' valueParameterDefinition: Content to use in performing the task
    :param 'RelatedArtifact' valueRelatedArtifact: Content to use in performing the task
    :param 'TriggerDefinition' valueTriggerDefinition: Content to use in performing the task
    :param 'UsageContext' valueUsageContext: Content to use in performing the task
    :param 'Dosage' valueDosage: Content to use in performing the task
    :param 'Meta' valueMeta: Content to use in performing the task
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  valueBase64Binary: str = None,  valueBoolean: bool = None,  valueCanonical: str = None,  valueCode: str = None,  valueDate: str = None,  valueDateTime: str = None,  valueDecimal: float = None,  valueId: str = None,  valueInstant: str = None,  valueInteger: int = None,  valueMarkdown: str = None,  valueOid: str = None,  valuePositiveInt: int = None,  valueString: str = None,  valueTime: str = None,  valueUnsignedInt: int = None,  valueUri: str = None,  valueUrl: str = None,  valueUuid: str = None,  valueAddress: 'Address' = None,  valueAge: 'Age' = None,  valueAnnotation: 'Annotation' = None,  valueAttachment: 'Attachment' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueCoding: 'Coding' = None,  valueContactPoint: 'ContactPoint' = None,  valueCount: 'Count' = None,  valueDistance: 'Distance' = None,  valueDuration: 'Duration' = None,  valueHumanName: 'HumanName' = None,  valueIdentifier: 'Identifier' = None,  valueMoney: 'Money' = None,  valuePeriod: 'Period' = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueRatio: 'Ratio' = None,  valueReference: 'Reference' = None,  valueSampledData: 'SampledData' = None,  valueSignature: 'Signature' = None,  valueTiming: 'Timing' = None,  valueContactDetail: 'ContactDetail' = None,  valueContributor: 'Contributor' = None,  valueDataRequirement: 'DataRequirement' = None,  valueExpression: 'Expression' = None,  valueParameterDefinition: 'ParameterDefinition' = None,  valueRelatedArtifact: 'RelatedArtifact' = None,  valueTriggerDefinition: 'TriggerDefinition' = None,  valueUsageContext: 'UsageContext' = None,  valueDosage: 'Dosage' = None,  valueMeta: 'Meta' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.valueBase64Binary: str = valueBase64Binary 
        self.valueBoolean: bool = valueBoolean 
        self.valueCanonical: str = valueCanonical 
        self.valueCode: str = valueCode 
        self.valueDate: str = valueDate 
        self.valueDateTime: str = valueDateTime 
        self.valueDecimal: float = valueDecimal 
        self.valueId: str = valueId 
        self.valueInstant: str = valueInstant 
        self.valueInteger: int = valueInteger 
        self.valueMarkdown: str = valueMarkdown 
        self.valueOid: str = valueOid 
        self.valuePositiveInt: int = valuePositiveInt 
        self.valueString: str = valueString 
        self.valueTime: str = valueTime 
        self.valueUnsignedInt: int = valueUnsignedInt 
        self.valueUri: str = valueUri 
        self.valueUrl: str = valueUrl 
        self.valueUuid: str = valueUuid 
        self.valueAddress: 'Address' = valueAddress 
        self.valueAge: 'Age' = valueAge 
        self.valueAnnotation: 'Annotation' = valueAnnotation 
        self.valueAttachment: 'Attachment' = valueAttachment 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueCoding: 'Coding' = valueCoding 
        self.valueContactPoint: 'ContactPoint' = valueContactPoint 
        self.valueCount: 'Count' = valueCount 
        self.valueDistance: 'Distance' = valueDistance 
        self.valueDuration: 'Duration' = valueDuration 
        self.valueHumanName: 'HumanName' = valueHumanName 
        self.valueIdentifier: 'Identifier' = valueIdentifier 
        self.valueMoney: 'Money' = valueMoney 
        self.valuePeriod: 'Period' = valuePeriod 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueRange: 'Range' = valueRange 
        self.valueRatio: 'Ratio' = valueRatio 
        self.valueReference: 'Reference' = valueReference 
        self.valueSampledData: 'SampledData' = valueSampledData 
        self.valueSignature: 'Signature' = valueSignature 
        self.valueTiming: 'Timing' = valueTiming 
        self.valueContactDetail: 'ContactDetail' = valueContactDetail 
        self.valueContributor: 'Contributor' = valueContributor 
        self.valueDataRequirement: 'DataRequirement' = valueDataRequirement 
        self.valueExpression: 'Expression' = valueExpression 
        self.valueParameterDefinition: 'ParameterDefinition' = valueParameterDefinition 
        self.valueRelatedArtifact: 'RelatedArtifact' = valueRelatedArtifact 
        self.valueTriggerDefinition: 'TriggerDefinition' = valueTriggerDefinition 
        self.valueUsageContext: 'UsageContext' = valueUsageContext 
        self.valueDosage: 'Dosage' = valueDosage 
        self.valueMeta: 'Meta' = valueMeta 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Input":
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


    
    

class Output(ModelBase):
    """ Outputs produced by the Task.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Label for output
    :param str valueBase64Binary: Result of output
    :param bool valueBoolean: Result of output
    :param str valueCanonical: Result of output
    :param str valueCode: Result of output
    :param str valueDate: Result of output
    :param str valueDateTime: Result of output
    :param float valueDecimal: Result of output
    :param str valueId: Result of output
    :param str valueInstant: Result of output
    :param int valueInteger: Result of output
    :param str valueMarkdown: Result of output
    :param str valueOid: Result of output
    :param int valuePositiveInt: Result of output
    :param str valueString: Result of output
    :param str valueTime: Result of output
    :param int valueUnsignedInt: Result of output
    :param str valueUri: Result of output
    :param str valueUrl: Result of output
    :param str valueUuid: Result of output
    :param 'Address' valueAddress: Result of output
    :param 'Age' valueAge: Result of output
    :param 'Annotation' valueAnnotation: Result of output
    :param 'Attachment' valueAttachment: Result of output
    :param 'CodeableConcept' valueCodeableConcept: Result of output
    :param 'Coding' valueCoding: Result of output
    :param 'ContactPoint' valueContactPoint: Result of output
    :param 'Count' valueCount: Result of output
    :param 'Distance' valueDistance: Result of output
    :param 'Duration' valueDuration: Result of output
    :param 'HumanName' valueHumanName: Result of output
    :param 'Identifier' valueIdentifier: Result of output
    :param 'Money' valueMoney: Result of output
    :param 'Period' valuePeriod: Result of output
    :param 'Quantity' valueQuantity: Result of output
    :param 'Range' valueRange: Result of output
    :param 'Ratio' valueRatio: Result of output
    :param 'Reference' valueReference: Result of output
    :param 'SampledData' valueSampledData: Result of output
    :param 'Signature' valueSignature: Result of output
    :param 'Timing' valueTiming: Result of output
    :param 'ContactDetail' valueContactDetail: Result of output
    :param 'Contributor' valueContributor: Result of output
    :param 'DataRequirement' valueDataRequirement: Result of output
    :param 'Expression' valueExpression: Result of output
    :param 'ParameterDefinition' valueParameterDefinition: Result of output
    :param 'RelatedArtifact' valueRelatedArtifact: Result of output
    :param 'TriggerDefinition' valueTriggerDefinition: Result of output
    :param 'UsageContext' valueUsageContext: Result of output
    :param 'Dosage' valueDosage: Result of output
    :param 'Meta' valueMeta: Result of output
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  valueBase64Binary: str = None,  valueBoolean: bool = None,  valueCanonical: str = None,  valueCode: str = None,  valueDate: str = None,  valueDateTime: str = None,  valueDecimal: float = None,  valueId: str = None,  valueInstant: str = None,  valueInteger: int = None,  valueMarkdown: str = None,  valueOid: str = None,  valuePositiveInt: int = None,  valueString: str = None,  valueTime: str = None,  valueUnsignedInt: int = None,  valueUri: str = None,  valueUrl: str = None,  valueUuid: str = None,  valueAddress: 'Address' = None,  valueAge: 'Age' = None,  valueAnnotation: 'Annotation' = None,  valueAttachment: 'Attachment' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueCoding: 'Coding' = None,  valueContactPoint: 'ContactPoint' = None,  valueCount: 'Count' = None,  valueDistance: 'Distance' = None,  valueDuration: 'Duration' = None,  valueHumanName: 'HumanName' = None,  valueIdentifier: 'Identifier' = None,  valueMoney: 'Money' = None,  valuePeriod: 'Period' = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueRatio: 'Ratio' = None,  valueReference: 'Reference' = None,  valueSampledData: 'SampledData' = None,  valueSignature: 'Signature' = None,  valueTiming: 'Timing' = None,  valueContactDetail: 'ContactDetail' = None,  valueContributor: 'Contributor' = None,  valueDataRequirement: 'DataRequirement' = None,  valueExpression: 'Expression' = None,  valueParameterDefinition: 'ParameterDefinition' = None,  valueRelatedArtifact: 'RelatedArtifact' = None,  valueTriggerDefinition: 'TriggerDefinition' = None,  valueUsageContext: 'UsageContext' = None,  valueDosage: 'Dosage' = None,  valueMeta: 'Meta' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.valueBase64Binary: str = valueBase64Binary 
        self.valueBoolean: bool = valueBoolean 
        self.valueCanonical: str = valueCanonical 
        self.valueCode: str = valueCode 
        self.valueDate: str = valueDate 
        self.valueDateTime: str = valueDateTime 
        self.valueDecimal: float = valueDecimal 
        self.valueId: str = valueId 
        self.valueInstant: str = valueInstant 
        self.valueInteger: int = valueInteger 
        self.valueMarkdown: str = valueMarkdown 
        self.valueOid: str = valueOid 
        self.valuePositiveInt: int = valuePositiveInt 
        self.valueString: str = valueString 
        self.valueTime: str = valueTime 
        self.valueUnsignedInt: int = valueUnsignedInt 
        self.valueUri: str = valueUri 
        self.valueUrl: str = valueUrl 
        self.valueUuid: str = valueUuid 
        self.valueAddress: 'Address' = valueAddress 
        self.valueAge: 'Age' = valueAge 
        self.valueAnnotation: 'Annotation' = valueAnnotation 
        self.valueAttachment: 'Attachment' = valueAttachment 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueCoding: 'Coding' = valueCoding 
        self.valueContactPoint: 'ContactPoint' = valueContactPoint 
        self.valueCount: 'Count' = valueCount 
        self.valueDistance: 'Distance' = valueDistance 
        self.valueDuration: 'Duration' = valueDuration 
        self.valueHumanName: 'HumanName' = valueHumanName 
        self.valueIdentifier: 'Identifier' = valueIdentifier 
        self.valueMoney: 'Money' = valueMoney 
        self.valuePeriod: 'Period' = valuePeriod 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueRange: 'Range' = valueRange 
        self.valueRatio: 'Ratio' = valueRatio 
        self.valueReference: 'Reference' = valueReference 
        self.valueSampledData: 'SampledData' = valueSampledData 
        self.valueSignature: 'Signature' = valueSignature 
        self.valueTiming: 'Timing' = valueTiming 
        self.valueContactDetail: 'ContactDetail' = valueContactDetail 
        self.valueContributor: 'Contributor' = valueContributor 
        self.valueDataRequirement: 'DataRequirement' = valueDataRequirement 
        self.valueExpression: 'Expression' = valueExpression 
        self.valueParameterDefinition: 'ParameterDefinition' = valueParameterDefinition 
        self.valueRelatedArtifact: 'RelatedArtifact' = valueRelatedArtifact 
        self.valueTriggerDefinition: 'TriggerDefinition' = valueTriggerDefinition 
        self.valueUsageContext: 'UsageContext' = valueUsageContext 
        self.valueDosage: 'Dosage' = valueDosage 
        self.valueMeta: 'Meta' = valueMeta 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Output":
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


class Task(DomainResource):
    """ A task to be performed.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Task Instance Identifier
    :param str instantiatesCanonical: Formal definition of task
    :param str instantiatesUri: Formal definition of task
    :param list['Reference'] basedOn: Request fulfilled by this task
    :param 'Identifier' groupIdentifier: Requisition or grouper id
    :param list['Reference'] partOf: Composite task
    :param str status: draft | requested | received | accepted | +
    :param 'CodeableConcept' statusReason: Reason for current status
    :param 'CodeableConcept' businessStatus: E.g. "Specimen collected", "IV prepped"
    :param str intent: unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param 'CodeableConcept' code: Task Type
    :param str description: Human-readable explanation of task
    :param 'Reference' focus: What task is acting on
    :param 'Reference' _for: Beneficiary of the Task
    :param 'Reference' encounter: Healthcare event during which this task originated
    :param 'Period' executionPeriod: Start and end time of execution
    :param str authoredOn: Task Creation Date
    :param str lastModified: Task Last Modified Date
    :param 'Reference' requester: Who is asking for task to be done
    :param list['CodeableConcept'] performerType: Requested performer
    :param 'Reference' owner: Responsible individual
    :param 'Reference' location: Where task occurs
    :param 'CodeableConcept' reasonCode: Why task is needed
    :param 'Reference' reasonReference: Why task is needed
    :param list['Reference'] insurance: Associated insurance coverage
    :param list['Annotation'] note: Comments made about the task
    :param list['Reference'] relevantHistory: Key events in history of the Task
    :param 'Restriction' restriction: Constraints on fulfillment tasks
    :param list['Input'] input: Information used to perform task
    :param list['Output'] output: Information produced as part of task
    """
    def __init__(self, resourceType: str = "Task",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  groupIdentifier: 'Identifier' = None,  partOf: list['Reference'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  businessStatus: 'CodeableConcept' = None,  intent: str = None,  priority: str = None,  code: 'CodeableConcept' = None,  description: str = None,  focus: 'Reference' = None,  _for: 'Reference' = None,  encounter: 'Reference' = None,  executionPeriod: 'Period' = None,  authoredOn: str = None,  lastModified: str = None,  requester: 'Reference' = None,  performerType: list['CodeableConcept'] = None,  owner: 'Reference' = None,  location: 'Reference' = None,  reasonCode: 'CodeableConcept' = None,  reasonReference: 'Reference' = None,  insurance: list['Reference'] = None,  note: list['Annotation'] = None,  relevantHistory: list['Reference'] = None,  restriction: 'Restriction' = None,  input: list['Input'] = None,  output: list['Output'] = None, ):
        self.resourceType: str = resourceType or "Task"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical 
        self.instantiatesUri: str = instantiatesUri 
        self.basedOn: list['Reference'] = basedOn or []
        self.groupIdentifier: 'Identifier' = groupIdentifier 
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.businessStatus: 'CodeableConcept' = businessStatus 
        self.intent: str = intent 
        self.priority: str = priority 
        self.code: 'CodeableConcept' = code 
        self.description: str = description 
        self.focus: 'Reference' = focus 
        self._for: 'Reference' = _for 
        self.encounter: 'Reference' = encounter 
        self.executionPeriod: 'Period' = executionPeriod 
        self.authoredOn: str = authoredOn 
        self.lastModified: str = lastModified 
        self.requester: 'Reference' = requester 
        self.performerType: list['CodeableConcept'] = performerType or []
        self.owner: 'Reference' = owner 
        self.location: 'Reference' = location 
        self.reasonCode: 'CodeableConcept' = reasonCode 
        self.reasonReference: 'Reference' = reasonReference 
        self.insurance: list['Reference'] = insurance or []
        self.note: list['Annotation'] = note or []
        self.relevantHistory: list['Reference'] = relevantHistory or []
        self.restriction: 'Restriction' = restriction 
        self.input: list['Input'] = input or []
        self.output: list['Output'] = output or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
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