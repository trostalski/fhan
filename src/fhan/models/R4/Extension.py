"""
Generated class for Extension. 
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
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.Money import *
from fhan.models.R4.Dosage import *
from fhan.models.generator_models import ModelBase

class Extension(ModelBase):
    """ Base StructureDefinition for Extension Type: Optional Extension Element - found in all resources.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str url: identifies the meaning of the extension
    :param str valueBase64Binary: Value of extension
    :param bool valueBoolean: Value of extension
    :param str valueCanonical: Value of extension
    :param str valueCode: Value of extension
    :param str valueDate: Value of extension
    :param str valueDateTime: Value of extension
    :param float valueDecimal: Value of extension
    :param str valueId: Value of extension
    :param str valueInstant: Value of extension
    :param int valueInteger: Value of extension
    :param str valueMarkdown: Value of extension
    :param str valueOid: Value of extension
    :param int valuePositiveInt: Value of extension
    :param str valueString: Value of extension
    :param str valueTime: Value of extension
    :param int valueUnsignedInt: Value of extension
    :param str valueUri: Value of extension
    :param str valueUrl: Value of extension
    :param str valueUuid: Value of extension
    :param 'Address' valueAddress: Value of extension
    :param 'Age' valueAge: Value of extension
    :param 'Annotation' valueAnnotation: Value of extension
    :param 'Attachment' valueAttachment: Value of extension
    :param 'CodeableConcept' valueCodeableConcept: Value of extension
    :param 'Coding' valueCoding: Value of extension
    :param 'ContactPoint' valueContactPoint: Value of extension
    :param 'Count' valueCount: Value of extension
    :param 'Distance' valueDistance: Value of extension
    :param 'Duration' valueDuration: Value of extension
    :param 'HumanName' valueHumanName: Value of extension
    :param 'Identifier' valueIdentifier: Value of extension
    :param 'Money' valueMoney: Value of extension
    :param 'Period' valuePeriod: Value of extension
    :param 'Quantity' valueQuantity: Value of extension
    :param 'Range' valueRange: Value of extension
    :param 'Ratio' valueRatio: Value of extension
    :param 'Reference' valueReference: Value of extension
    :param 'SampledData' valueSampledData: Value of extension
    :param 'Signature' valueSignature: Value of extension
    :param 'Timing' valueTiming: Value of extension
    :param 'ContactDetail' valueContactDetail: Value of extension
    :param 'Contributor' valueContributor: Value of extension
    :param 'DataRequirement' valueDataRequirement: Value of extension
    :param 'Expression' valueExpression: Value of extension
    :param 'ParameterDefinition' valueParameterDefinition: Value of extension
    :param 'RelatedArtifact' valueRelatedArtifact: Value of extension
    :param 'TriggerDefinition' valueTriggerDefinition: Value of extension
    :param 'UsageContext' valueUsageContext: Value of extension
    :param 'Dosage' valueDosage: Value of extension
    :param 'Meta' valueMeta: Value of extension
    """
    def __init__(self, resourceType: str = "Extension",  id: str = None,  extension: list['Extension'] = None,  url: str = None,  valueBase64Binary: str = None,  valueBoolean: bool = None,  valueCanonical: str = None,  valueCode: str = None,  valueDate: str = None,  valueDateTime: str = None,  valueDecimal: float = None,  valueId: str = None,  valueInstant: str = None,  valueInteger: int = None,  valueMarkdown: str = None,  valueOid: str = None,  valuePositiveInt: int = None,  valueString: str = None,  valueTime: str = None,  valueUnsignedInt: int = None,  valueUri: str = None,  valueUrl: str = None,  valueUuid: str = None,  valueAddress: 'Address' = None,  valueAge: 'Age' = None,  valueAnnotation: 'Annotation' = None,  valueAttachment: 'Attachment' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueCoding: 'Coding' = None,  valueContactPoint: 'ContactPoint' = None,  valueCount: 'Count' = None,  valueDistance: 'Distance' = None,  valueDuration: 'Duration' = None,  valueHumanName: 'HumanName' = None,  valueIdentifier: 'Identifier' = None,  valueMoney: 'Money' = None,  valuePeriod: 'Period' = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueRatio: 'Ratio' = None,  valueReference: 'Reference' = None,  valueSampledData: 'SampledData' = None,  valueSignature: 'Signature' = None,  valueTiming: 'Timing' = None,  valueContactDetail: 'ContactDetail' = None,  valueContributor: 'Contributor' = None,  valueDataRequirement: 'DataRequirement' = None,  valueExpression: 'Expression' = None,  valueParameterDefinition: 'ParameterDefinition' = None,  valueRelatedArtifact: 'RelatedArtifact' = None,  valueTriggerDefinition: 'TriggerDefinition' = None,  valueUsageContext: 'UsageContext' = None,  valueDosage: 'Dosage' = None,  valueMeta: 'Meta' = None, ):
        self.resourceType: str = resourceType or "Extension"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.url: str = url 
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
    def from_dict(cls, data: dict) -> "Extension":
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