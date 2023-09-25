"""
Generated class for Parameters. 
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
from fhan.models.R4.Resource import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.DomainResource import *


    
    

class Parameter(ModelBase):
    """ A parameter passed to or received from the operation.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name from the definition
    :param str valueBase64Binary: If parameter is a data type
    :param bool valueBoolean: If parameter is a data type
    :param str valueCanonical: If parameter is a data type
    :param str valueCode: If parameter is a data type
    :param str valueDate: If parameter is a data type
    :param str valueDateTime: If parameter is a data type
    :param float valueDecimal: If parameter is a data type
    :param str valueId: If parameter is a data type
    :param str valueInstant: If parameter is a data type
    :param int valueInteger: If parameter is a data type
    :param str valueMarkdown: If parameter is a data type
    :param str valueOid: If parameter is a data type
    :param int valuePositiveInt: If parameter is a data type
    :param str valueString: If parameter is a data type
    :param str valueTime: If parameter is a data type
    :param int valueUnsignedInt: If parameter is a data type
    :param str valueUri: If parameter is a data type
    :param str valueUrl: If parameter is a data type
    :param str valueUuid: If parameter is a data type
    :param 'Address' valueAddress: If parameter is a data type
    :param 'Age' valueAge: If parameter is a data type
    :param 'Annotation' valueAnnotation: If parameter is a data type
    :param 'Attachment' valueAttachment: If parameter is a data type
    :param 'CodeableConcept' valueCodeableConcept: If parameter is a data type
    :param 'Coding' valueCoding: If parameter is a data type
    :param 'ContactPoint' valueContactPoint: If parameter is a data type
    :param 'Count' valueCount: If parameter is a data type
    :param 'Distance' valueDistance: If parameter is a data type
    :param 'Duration' valueDuration: If parameter is a data type
    :param 'HumanName' valueHumanName: If parameter is a data type
    :param 'Identifier' valueIdentifier: If parameter is a data type
    :param 'Money' valueMoney: If parameter is a data type
    :param 'Period' valuePeriod: If parameter is a data type
    :param 'Quantity' valueQuantity: If parameter is a data type
    :param 'Range' valueRange: If parameter is a data type
    :param 'Ratio' valueRatio: If parameter is a data type
    :param 'Reference' valueReference: If parameter is a data type
    :param 'SampledData' valueSampledData: If parameter is a data type
    :param 'Signature' valueSignature: If parameter is a data type
    :param 'Timing' valueTiming: If parameter is a data type
    :param 'ContactDetail' valueContactDetail: If parameter is a data type
    :param 'Contributor' valueContributor: If parameter is a data type
    :param 'DataRequirement' valueDataRequirement: If parameter is a data type
    :param 'Expression' valueExpression: If parameter is a data type
    :param 'ParameterDefinition' valueParameterDefinition: If parameter is a data type
    :param 'RelatedArtifact' valueRelatedArtifact: If parameter is a data type
    :param 'TriggerDefinition' valueTriggerDefinition: If parameter is a data type
    :param 'UsageContext' valueUsageContext: If parameter is a data type
    :param 'Dosage' valueDosage: If parameter is a data type
    :param 'Meta' valueMeta: If parameter is a data type
    :param 'Resource' resource: If parameter is a whole resource
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  valueBase64Binary: str = None,  valueBoolean: bool = None,  valueCanonical: str = None,  valueCode: str = None,  valueDate: str = None,  valueDateTime: str = None,  valueDecimal: float = None,  valueId: str = None,  valueInstant: str = None,  valueInteger: int = None,  valueMarkdown: str = None,  valueOid: str = None,  valuePositiveInt: int = None,  valueString: str = None,  valueTime: str = None,  valueUnsignedInt: int = None,  valueUri: str = None,  valueUrl: str = None,  valueUuid: str = None,  valueAddress: 'Address' = None,  valueAge: 'Age' = None,  valueAnnotation: 'Annotation' = None,  valueAttachment: 'Attachment' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueCoding: 'Coding' = None,  valueContactPoint: 'ContactPoint' = None,  valueCount: 'Count' = None,  valueDistance: 'Distance' = None,  valueDuration: 'Duration' = None,  valueHumanName: 'HumanName' = None,  valueIdentifier: 'Identifier' = None,  valueMoney: 'Money' = None,  valuePeriod: 'Period' = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueRatio: 'Ratio' = None,  valueReference: 'Reference' = None,  valueSampledData: 'SampledData' = None,  valueSignature: 'Signature' = None,  valueTiming: 'Timing' = None,  valueContactDetail: 'ContactDetail' = None,  valueContributor: 'Contributor' = None,  valueDataRequirement: 'DataRequirement' = None,  valueExpression: 'Expression' = None,  valueParameterDefinition: 'ParameterDefinition' = None,  valueRelatedArtifact: 'RelatedArtifact' = None,  valueTriggerDefinition: 'TriggerDefinition' = None,  valueUsageContext: 'UsageContext' = None,  valueDosage: 'Dosage' = None,  valueMeta: 'Meta' = None,  resource: 'Resource' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
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
        self.resource: 'Resource' = resource 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Parameter":
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


    
    

class Part(ModelBase):
    """ A parameter passed to or received from the operation.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name from the definition
    :param str valueBase64Binary: If parameter is a data type
    :param bool valueBoolean: If parameter is a data type
    :param str valueCanonical: If parameter is a data type
    :param str valueCode: If parameter is a data type
    :param str valueDate: If parameter is a data type
    :param str valueDateTime: If parameter is a data type
    :param float valueDecimal: If parameter is a data type
    :param str valueId: If parameter is a data type
    :param str valueInstant: If parameter is a data type
    :param int valueInteger: If parameter is a data type
    :param str valueMarkdown: If parameter is a data type
    :param str valueOid: If parameter is a data type
    :param int valuePositiveInt: If parameter is a data type
    :param str valueString: If parameter is a data type
    :param str valueTime: If parameter is a data type
    :param int valueUnsignedInt: If parameter is a data type
    :param str valueUri: If parameter is a data type
    :param str valueUrl: If parameter is a data type
    :param str valueUuid: If parameter is a data type
    :param 'Address' valueAddress: If parameter is a data type
    :param 'Age' valueAge: If parameter is a data type
    :param 'Annotation' valueAnnotation: If parameter is a data type
    :param 'Attachment' valueAttachment: If parameter is a data type
    :param 'CodeableConcept' valueCodeableConcept: If parameter is a data type
    :param 'Coding' valueCoding: If parameter is a data type
    :param 'ContactPoint' valueContactPoint: If parameter is a data type
    :param 'Count' valueCount: If parameter is a data type
    :param 'Distance' valueDistance: If parameter is a data type
    :param 'Duration' valueDuration: If parameter is a data type
    :param 'HumanName' valueHumanName: If parameter is a data type
    :param 'Identifier' valueIdentifier: If parameter is a data type
    :param 'Money' valueMoney: If parameter is a data type
    :param 'Period' valuePeriod: If parameter is a data type
    :param 'Quantity' valueQuantity: If parameter is a data type
    :param 'Range' valueRange: If parameter is a data type
    :param 'Ratio' valueRatio: If parameter is a data type
    :param 'Reference' valueReference: If parameter is a data type
    :param 'SampledData' valueSampledData: If parameter is a data type
    :param 'Signature' valueSignature: If parameter is a data type
    :param 'Timing' valueTiming: If parameter is a data type
    :param 'ContactDetail' valueContactDetail: If parameter is a data type
    :param 'Contributor' valueContributor: If parameter is a data type
    :param 'DataRequirement' valueDataRequirement: If parameter is a data type
    :param 'Expression' valueExpression: If parameter is a data type
    :param 'ParameterDefinition' valueParameterDefinition: If parameter is a data type
    :param 'RelatedArtifact' valueRelatedArtifact: If parameter is a data type
    :param 'TriggerDefinition' valueTriggerDefinition: If parameter is a data type
    :param 'UsageContext' valueUsageContext: If parameter is a data type
    :param 'Dosage' valueDosage: If parameter is a data type
    :param 'Meta' valueMeta: If parameter is a data type
    :param 'Resource' resource: If parameter is a whole resource
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  valueBase64Binary: str = None,  valueBoolean: bool = None,  valueCanonical: str = None,  valueCode: str = None,  valueDate: str = None,  valueDateTime: str = None,  valueDecimal: float = None,  valueId: str = None,  valueInstant: str = None,  valueInteger: int = None,  valueMarkdown: str = None,  valueOid: str = None,  valuePositiveInt: int = None,  valueString: str = None,  valueTime: str = None,  valueUnsignedInt: int = None,  valueUri: str = None,  valueUrl: str = None,  valueUuid: str = None,  valueAddress: 'Address' = None,  valueAge: 'Age' = None,  valueAnnotation: 'Annotation' = None,  valueAttachment: 'Attachment' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueCoding: 'Coding' = None,  valueContactPoint: 'ContactPoint' = None,  valueCount: 'Count' = None,  valueDistance: 'Distance' = None,  valueDuration: 'Duration' = None,  valueHumanName: 'HumanName' = None,  valueIdentifier: 'Identifier' = None,  valueMoney: 'Money' = None,  valuePeriod: 'Period' = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueRatio: 'Ratio' = None,  valueReference: 'Reference' = None,  valueSampledData: 'SampledData' = None,  valueSignature: 'Signature' = None,  valueTiming: 'Timing' = None,  valueContactDetail: 'ContactDetail' = None,  valueContributor: 'Contributor' = None,  valueDataRequirement: 'DataRequirement' = None,  valueExpression: 'Expression' = None,  valueParameterDefinition: 'ParameterDefinition' = None,  valueRelatedArtifact: 'RelatedArtifact' = None,  valueTriggerDefinition: 'TriggerDefinition' = None,  valueUsageContext: 'UsageContext' = None,  valueDosage: 'Dosage' = None,  valueMeta: 'Meta' = None,  resource: 'Resource' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
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
        self.resource: 'Resource' = resource 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Part":
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


class Parameters(DomainResource):
    """ This resource is a non-persisted resource used to pass information into and back from an [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param list['Parameter'] parameter: Operation Parameter
    :param list['Part'] part: Operation Parameter
    """
    def __init__(self, resourceType: str = "Parameters",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  parameter: list['Parameter'] = None,  part: list['Part'] = None, ):
        self.resourceType: str = resourceType or "Parameters"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.parameter: list['Parameter'] = parameter or []
        self.part: list['Part'] = part or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Parameters":
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