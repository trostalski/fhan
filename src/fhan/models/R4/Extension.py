"""
Generated class for Extension. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.SampledData import *
from fhan.models.R4.Money import *
from fhan.models.R4.Range import *
from fhan.models.R4.Count import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Distance import *
from fhan.models.R4.Duration import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Address import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.Age import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Signature import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Period import *
from fhan.models.R4.Ratio import *
from fhan.models.generator_models import BaseModel


class Extension(BaseModel):
    """Base StructureDefinition for Extension Type: Optional Extension Element - found in all resources.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
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
    :param Address valueAddress: Value of extension
    :param Age valueAge: Value of extension
    :param Annotation valueAnnotation: Value of extension
    :param Attachment valueAttachment: Value of extension
    :param CodeableConcept valueCodeableConcept: Value of extension
    :param Coding valueCoding: Value of extension
    :param ContactPoint valueContactPoint: Value of extension
    :param Count valueCount: Value of extension
    :param Distance valueDistance: Value of extension
    :param Duration valueDuration: Value of extension
    :param HumanName valueHumanName: Value of extension
    :param Identifier valueIdentifier: Value of extension
    :param Money valueMoney: Value of extension
    :param Period valuePeriod: Value of extension
    :param Quantity valueQuantity: Value of extension
    :param Range valueRange: Value of extension
    :param Ratio valueRatio: Value of extension
    :param Reference valueReference: Value of extension
    :param SampledData valueSampledData: Value of extension
    :param Signature valueSignature: Value of extension
    :param Timing valueTiming: Value of extension
    :param ContactDetail valueContactDetail: Value of extension
    :param Contributor valueContributor: Value of extension
    :param DataRequirement valueDataRequirement: Value of extension
    :param Expression valueExpression: Value of extension
    :param ParameterDefinition valueParameterDefinition: Value of extension
    :param RelatedArtifact valueRelatedArtifact: Value of extension
    :param TriggerDefinition valueTriggerDefinition: Value of extension
    :param UsageContext valueUsageContext: Value of extension
    :param Dosage valueDosage: Value of extension
    :param Meta valueMeta: Value of extension
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "valueAddress": {"class_name": "Address", "is_contained": False},
        "valueAge": {"class_name": "Age", "is_contained": False},
        "valueAnnotation": {"class_name": "Annotation", "is_contained": False},
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        "valueCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "valueCoding": {"class_name": "Coding", "is_contained": False},
        "valueContactPoint": {"class_name": "ContactPoint", "is_contained": False},
        "valueCount": {"class_name": "Count", "is_contained": False},
        "valueDistance": {"class_name": "Distance", "is_contained": False},
        "valueDuration": {"class_name": "Duration", "is_contained": False},
        "valueHumanName": {"class_name": "HumanName", "is_contained": False},
        "valueIdentifier": {"class_name": "Identifier", "is_contained": False},
        "valueMoney": {"class_name": "Money", "is_contained": False},
        "valuePeriod": {"class_name": "Period", "is_contained": False},
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueRange": {"class_name": "Range", "is_contained": False},
        "valueRatio": {"class_name": "Ratio", "is_contained": False},
        "valueReference": {"class_name": "Reference", "is_contained": False},
        "valueSampledData": {"class_name": "SampledData", "is_contained": False},
        "valueSignature": {"class_name": "Signature", "is_contained": False},
        "valueTiming": {"class_name": "Timing", "is_contained": False},
        "valueContactDetail": {"class_name": "ContactDetail", "is_contained": False},
        "valueContributor": {"class_name": "Contributor", "is_contained": False},
        "valueDataRequirement": {
            "class_name": "DataRequirement",
            "is_contained": False,
        },
        "valueExpression": {"class_name": "Expression", "is_contained": False},
        "valueParameterDefinition": {
            "class_name": "ParameterDefinition",
            "is_contained": False,
        },
        "valueRelatedArtifact": {
            "class_name": "RelatedArtifact",
            "is_contained": False,
        },
        "valueTriggerDefinition": {
            "class_name": "TriggerDefinition",
            "is_contained": False,
        },
        "valueUsageContext": {"class_name": "UsageContext", "is_contained": False},
        "valueDosage": {"class_name": "Dosage", "is_contained": False},
        "valueMeta": {"class_name": "Meta", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        url: "str" = None,
        valueBase64Binary: "str" = None,
        valueBoolean: "bool" = None,
        valueCanonical: "str" = None,
        valueCode: "str" = None,
        valueDate: "str" = None,
        valueDateTime: "str" = None,
        valueDecimal: "float" = None,
        valueId: "str" = None,
        valueInstant: "str" = None,
        valueInteger: "int" = None,
        valueMarkdown: "str" = None,
        valueOid: "str" = None,
        valuePositiveInt: "int" = None,
        valueString: "str" = None,
        valueTime: "str" = None,
        valueUnsignedInt: "int" = None,
        valueUri: "str" = None,
        valueUrl: "str" = None,
        valueUuid: "str" = None,
        valueAddress: "Address" = None,
        valueAge: "Age" = None,
        valueAnnotation: "Annotation" = None,
        valueAttachment: "Attachment" = None,
        valueCodeableConcept: "CodeableConcept" = None,
        valueCoding: "Coding" = None,
        valueContactPoint: "ContactPoint" = None,
        valueCount: "Count" = None,
        valueDistance: "Distance" = None,
        valueDuration: "Duration" = None,
        valueHumanName: "HumanName" = None,
        valueIdentifier: "Identifier" = None,
        valueMoney: "Money" = None,
        valuePeriod: "Period" = None,
        valueQuantity: "Quantity" = None,
        valueRange: "Range" = None,
        valueRatio: "Ratio" = None,
        valueReference: "Reference" = None,
        valueSampledData: "SampledData" = None,
        valueSignature: "Signature" = None,
        valueTiming: "Timing" = None,
        valueContactDetail: "ContactDetail" = None,
        valueContributor: "Contributor" = None,
        valueDataRequirement: "DataRequirement" = None,
        valueExpression: "Expression" = None,
        valueParameterDefinition: "ParameterDefinition" = None,
        valueRelatedArtifact: "RelatedArtifact" = None,
        valueTriggerDefinition: "TriggerDefinition" = None,
        valueUsageContext: "UsageContext" = None,
        valueDosage: "Dosage" = None,
        valueMeta: "Meta" = None,
    ):
        self.resourceType = resourceType or "Extension"
        self.id = id
        self.extension = extension or []
        self.url = url
        self.valueBase64Binary = valueBase64Binary
        self.valueBoolean = valueBoolean
        self.valueCanonical = valueCanonical
        self.valueCode = valueCode
        self.valueDate = valueDate
        self.valueDateTime = valueDateTime
        self.valueDecimal = valueDecimal
        self.valueId = valueId
        self.valueInstant = valueInstant
        self.valueInteger = valueInteger
        self.valueMarkdown = valueMarkdown
        self.valueOid = valueOid
        self.valuePositiveInt = valuePositiveInt
        self.valueString = valueString
        self.valueTime = valueTime
        self.valueUnsignedInt = valueUnsignedInt
        self.valueUri = valueUri
        self.valueUrl = valueUrl
        self.valueUuid = valueUuid
        self.valueAddress = valueAddress
        self.valueAge = valueAge
        self.valueAnnotation = valueAnnotation
        self.valueAttachment = valueAttachment
        self.valueCodeableConcept = valueCodeableConcept
        self.valueCoding = valueCoding
        self.valueContactPoint = valueContactPoint
        self.valueCount = valueCount
        self.valueDistance = valueDistance
        self.valueDuration = valueDuration
        self.valueHumanName = valueHumanName
        self.valueIdentifier = valueIdentifier
        self.valueMoney = valueMoney
        self.valuePeriod = valuePeriod
        self.valueQuantity = valueQuantity
        self.valueRange = valueRange
        self.valueRatio = valueRatio
        self.valueReference = valueReference
        self.valueSampledData = valueSampledData
        self.valueSignature = valueSignature
        self.valueTiming = valueTiming
        self.valueContactDetail = valueContactDetail
        self.valueContributor = valueContributor
        self.valueDataRequirement = valueDataRequirement
        self.valueExpression = valueExpression
        self.valueParameterDefinition = valueParameterDefinition
        self.valueRelatedArtifact = valueRelatedArtifact
        self.valueTriggerDefinition = valueTriggerDefinition
        self.valueUsageContext = valueUsageContext
        self.valueDosage = valueDosage
        self.valueMeta = valueMeta

    @classmethod
    def from_dict(cls, data: dict) -> "Extension":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Extension":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
