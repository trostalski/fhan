"""
Generated class for Task. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.SampledData import *
from fhan.models.R4.Money import *
from fhan.models.R4.Range import *
from fhan.models.R4.Count import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Distance import *
from fhan.models.R4.Duration import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Address import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Signature import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Period import *
from fhan.models.R4.Age import *
from fhan.models.R4.DomainResource import *


class Restriction(BaseModel):
    """If the Task.focus is a request resource and the task is seeking fulfillment (i.e. is asking for the request to be actioned), this element identifies any limitations on what parts of the referenced request should be actioned.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int repetitions: How many times to repeat
    :param Period period: When fulfillment sought
    :param Reference recipient: For whom is fulfillment sought?
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "recipient": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        repetitions: "int" = None,
        period: "Period" = None,
        recipient: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.repetitions = repetitions
        self.period = period
        self.recipient = recipient or []

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Task":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Input(BaseModel):
    """Additional information that may be needed in the execution of the task.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Label for the input
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
    :param Address valueAddress: Content to use in performing the task
    :param Age valueAge: Content to use in performing the task
    :param Annotation valueAnnotation: Content to use in performing the task
    :param Attachment valueAttachment: Content to use in performing the task
    :param CodeableConcept valueCodeableConcept: Content to use in performing the task
    :param Coding valueCoding: Content to use in performing the task
    :param ContactPoint valueContactPoint: Content to use in performing the task
    :param Count valueCount: Content to use in performing the task
    :param Distance valueDistance: Content to use in performing the task
    :param Duration valueDuration: Content to use in performing the task
    :param HumanName valueHumanName: Content to use in performing the task
    :param Identifier valueIdentifier: Content to use in performing the task
    :param Money valueMoney: Content to use in performing the task
    :param Period valuePeriod: Content to use in performing the task
    :param Quantity valueQuantity: Content to use in performing the task
    :param Range valueRange: Content to use in performing the task
    :param Ratio valueRatio: Content to use in performing the task
    :param Reference valueReference: Content to use in performing the task
    :param SampledData valueSampledData: Content to use in performing the task
    :param Signature valueSignature: Content to use in performing the task
    :param Timing valueTiming: Content to use in performing the task
    :param ContactDetail valueContactDetail: Content to use in performing the task
    :param Contributor valueContributor: Content to use in performing the task
    :param DataRequirement valueDataRequirement: Content to use in performing the task
    :param Expression valueExpression: Content to use in performing the task
    :param ParameterDefinition valueParameterDefinition: Content to use in performing the task
    :param RelatedArtifact valueRelatedArtifact: Content to use in performing the task
    :param TriggerDefinition valueTriggerDefinition: Content to use in performing the task
    :param UsageContext valueUsageContext: Content to use in performing the task
    :param Dosage valueDosage: Content to use in performing the task
    :param Meta valueMeta: Content to use in performing the task
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
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
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
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
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
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
    def from_dict(cls, data: dict) -> "Task":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Task":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Output(BaseModel):
    """Outputs produced by the Task.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Label for output
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
    :param Address valueAddress: Result of output
    :param Age valueAge: Result of output
    :param Annotation valueAnnotation: Result of output
    :param Attachment valueAttachment: Result of output
    :param CodeableConcept valueCodeableConcept: Result of output
    :param Coding valueCoding: Result of output
    :param ContactPoint valueContactPoint: Result of output
    :param Count valueCount: Result of output
    :param Distance valueDistance: Result of output
    :param Duration valueDuration: Result of output
    :param HumanName valueHumanName: Result of output
    :param Identifier valueIdentifier: Result of output
    :param Money valueMoney: Result of output
    :param Period valuePeriod: Result of output
    :param Quantity valueQuantity: Result of output
    :param Range valueRange: Result of output
    :param Ratio valueRatio: Result of output
    :param Reference valueReference: Result of output
    :param SampledData valueSampledData: Result of output
    :param Signature valueSignature: Result of output
    :param Timing valueTiming: Result of output
    :param ContactDetail valueContactDetail: Result of output
    :param Contributor valueContributor: Result of output
    :param DataRequirement valueDataRequirement: Result of output
    :param Expression valueExpression: Result of output
    :param ParameterDefinition valueParameterDefinition: Result of output
    :param RelatedArtifact valueRelatedArtifact: Result of output
    :param TriggerDefinition valueTriggerDefinition: Result of output
    :param UsageContext valueUsageContext: Result of output
    :param Dosage valueDosage: Result of output
    :param Meta valueMeta: Result of output
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
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
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
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
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
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
    def from_dict(cls, data: dict) -> "Task":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Task":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Task(DomainResource):
    """A task to be performed.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Task Instance Identifier
    :param str instantiatesCanonical: Formal definition of task
    :param str instantiatesUri: Formal definition of task
    :param Reference basedOn: Request fulfilled by this task
    :param Identifier groupIdentifier: Requisition or grouper id
    :param Reference partOf: Composite task
    :param str status: draft | requested | received | accepted | +
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept businessStatus: E.g. "Specimen collected", "IV prepped"
    :param str intent: unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept code: Task Type
    :param str description: Human-readable explanation of task
    :param Reference focus: What task is acting on
    :param Reference _for: Beneficiary of the Task
    :param Reference encounter: Healthcare event during which this task originated
    :param Period executionPeriod: Start and end time of execution
    :param str authoredOn: Task Creation Date
    :param str lastModified: Task Last Modified Date
    :param Reference requester: Who is asking for task to be done
    :param CodeableConcept performerType: Requested performer
    :param Reference owner: Responsible individual
    :param Reference location: Where task occurs
    :param CodeableConcept reasonCode: Why task is needed
    :param Reference reasonReference: Why task is needed
    :param Reference insurance: Associated insurance coverage
    :param Annotation note: Comments made about the task
    :param Reference relevantHistory: Key events in history of the Task
    :param Restriction restriction: Constraints on fulfillment tasks
    :param Input input: Information used to perform task
    :param Output output: Information produced as part of task
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "groupIdentifier": {"class_name": "Identifier", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "businessStatus": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "focus": {"class_name": "Reference", "is_contained": False},
        "_for": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "executionPeriod": {"class_name": "Period", "is_contained": False},
        "requester": {"class_name": "Reference", "is_contained": False},
        "performerType": {"class_name": "CodeableConcept", "is_contained": False},
        "owner": {"class_name": "Reference", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "insurance": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "relevantHistory": {"class_name": "Reference", "is_contained": False},
        "restriction": {"class_name": "Restriction", "is_contained": True},
        "input": {"class_name": "Input", "is_contained": True},
        "output": {"class_name": "Output", "is_contained": True},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        instantiatesCanonical: "str" = None,
        instantiatesUri: "str" = None,
        basedOn: list["Reference"] = None,
        groupIdentifier: "Identifier" = None,
        partOf: list["Reference"] = None,
        status: "str" = None,
        statusReason: "CodeableConcept" = None,
        businessStatus: "CodeableConcept" = None,
        intent: "str" = None,
        priority: "str" = None,
        code: "CodeableConcept" = None,
        description: "str" = None,
        focus: "Reference" = None,
        _for: "Reference" = None,
        encounter: "Reference" = None,
        executionPeriod: "Period" = None,
        authoredOn: "str" = None,
        lastModified: "str" = None,
        requester: "Reference" = None,
        performerType: list["CodeableConcept"] = None,
        owner: "Reference" = None,
        location: "Reference" = None,
        reasonCode: "CodeableConcept" = None,
        reasonReference: "Reference" = None,
        insurance: list["Reference"] = None,
        note: list["Annotation"] = None,
        relevantHistory: list["Reference"] = None,
        restriction: "Restriction" = None,
        input: list["Input"] = None,
        output: list["Output"] = None,
    ):
        self.resourceType = resourceType or "Task"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical
        self.instantiatesUri = instantiatesUri
        self.basedOn = basedOn or []
        self.groupIdentifier = groupIdentifier
        self.partOf = partOf or []
        self.status = status
        self.statusReason = statusReason
        self.businessStatus = businessStatus
        self.intent = intent
        self.priority = priority
        self.code = code
        self.description = description
        self.focus = focus
        self._for = _for
        self.encounter = encounter
        self.executionPeriod = executionPeriod
        self.authoredOn = authoredOn
        self.lastModified = lastModified
        self.requester = requester
        self.performerType = performerType or []
        self.owner = owner
        self.location = location
        self.reasonCode = reasonCode
        self.reasonReference = reasonReference
        self.insurance = insurance or []
        self.note = note or []
        self.relevantHistory = relevantHistory or []
        self.restriction = restriction
        self.input = input or []
        self.output = output or []

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Task":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
