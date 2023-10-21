"""
Generated class for ElementDefinition. 
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
from fhan.models.R4.Element import *
from fhan.models.R4.Duration import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Address import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.Extension import *
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


class Discriminator(BaseModel):
    """Designates which child elements are used to discriminate between the slices when processing an instance. If one or more discriminators are provided, the value of the child elements in the instance data SHALL completely distinguish which slice the element in the resource matches based on the allowed values for those elements in each of the slices.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: value | exists | pattern | type | profile
    :param str path: Path to element value
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        type: "str" = None,
        path: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.type = type
        self.path = path

    @classmethod
    def from_dict(cls, data: dict) -> "ElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Slicing(BaseModel):
    """Indicates that the element is sliced into a set of alternative definitions (i.e. in a structure definition, there are multiple different constraints on a single element in the base resource). Slicing can be used in any resource that has cardinality ..* on the base resource, or any resource with a choice of types. The set of slices is any elements that come after this in the element sequence that have the same path, until a shorter path occurs (the shorter path terminates the set).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Discriminator discriminator: Element values that are used to distinguish the slices
    :param str description: Text description of how slicing works (or not)
    :param bool ordered: If elements must be in same order as slices
    :param str rules: closed | open | openAtEnd
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "discriminator": {"class_name": "Discriminator", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        discriminator: list["Discriminator"] = None,
        description: "str" = None,
        ordered: "bool" = None,
        rules: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.discriminator = discriminator or []
        self.description = description
        self.ordered = ordered
        self.rules = rules

    @classmethod
    def from_dict(cls, data: dict) -> "ElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Base(BaseModel):
    """Information about the base definition of the element, provided to make it unnecessary for tools to trace the deviation of the element through the derived and related profiles. When the element definition is not the original definition of an element - i.g. either in a constraint on another type, or for elements from a super type in a snap shot - then the information in provided in the element definition may be different to the base definition. On the original definition of the element, it will be same.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str path: Path that identifies the base element
    :param int min: Min cardinality of the base element
    :param str max: Max cardinality of the base element
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        path: "str" = None,
        min: "int" = None,
        max: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.path = path
        self.min = min
        self.max = max

    @classmethod
    def from_dict(cls, data: dict) -> "ElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Type(BaseModel):
    """The data type or resource that the value of this element is permitted to be.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str code: Data type or Resource (reference to definition)
    :param str profile: Profiles (StructureDefinition or IG) - one must apply
    :param str targetProfile: Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply
    :param str aggregation: contained | referenced | bundled - how aggregated
    :param str versioning: either | independent | specific
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        code: "str" = None,
        profile: list["str"] = None,
        targetProfile: list["str"] = None,
        aggregation: list["str"] = None,
        versioning: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.code = code
        self.profile = profile or []
        self.targetProfile = targetProfile or []
        self.aggregation = aggregation or []
        self.versioning = versioning

    @classmethod
    def from_dict(cls, data: dict) -> "ElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Example(BaseModel):
    """A sample value for this element demonstrating the type of information that would typically be found in the element.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str label: Describes the purpose of this example
    :param str valueBase64Binary: Value of Example (one of allowed types)
    :param bool valueBoolean: Value of Example (one of allowed types)
    :param str valueCanonical: Value of Example (one of allowed types)
    :param str valueCode: Value of Example (one of allowed types)
    :param str valueDate: Value of Example (one of allowed types)
    :param str valueDateTime: Value of Example (one of allowed types)
    :param float valueDecimal: Value of Example (one of allowed types)
    :param str valueId: Value of Example (one of allowed types)
    :param str valueInstant: Value of Example (one of allowed types)
    :param int valueInteger: Value of Example (one of allowed types)
    :param str valueMarkdown: Value of Example (one of allowed types)
    :param str valueOid: Value of Example (one of allowed types)
    :param int valuePositiveInt: Value of Example (one of allowed types)
    :param str valueString: Value of Example (one of allowed types)
    :param str valueTime: Value of Example (one of allowed types)
    :param int valueUnsignedInt: Value of Example (one of allowed types)
    :param str valueUri: Value of Example (one of allowed types)
    :param str valueUrl: Value of Example (one of allowed types)
    :param str valueUuid: Value of Example (one of allowed types)
    :param Address valueAddress: Value of Example (one of allowed types)
    :param Age valueAge: Value of Example (one of allowed types)
    :param Annotation valueAnnotation: Value of Example (one of allowed types)
    :param Attachment valueAttachment: Value of Example (one of allowed types)
    :param CodeableConcept valueCodeableConcept: Value of Example (one of allowed types)
    :param Coding valueCoding: Value of Example (one of allowed types)
    :param ContactPoint valueContactPoint: Value of Example (one of allowed types)
    :param Count valueCount: Value of Example (one of allowed types)
    :param Distance valueDistance: Value of Example (one of allowed types)
    :param Duration valueDuration: Value of Example (one of allowed types)
    :param HumanName valueHumanName: Value of Example (one of allowed types)
    :param Identifier valueIdentifier: Value of Example (one of allowed types)
    :param Money valueMoney: Value of Example (one of allowed types)
    :param Period valuePeriod: Value of Example (one of allowed types)
    :param Quantity valueQuantity: Value of Example (one of allowed types)
    :param Range valueRange: Value of Example (one of allowed types)
    :param Ratio valueRatio: Value of Example (one of allowed types)
    :param Reference valueReference: Value of Example (one of allowed types)
    :param SampledData valueSampledData: Value of Example (one of allowed types)
    :param Signature valueSignature: Value of Example (one of allowed types)
    :param Timing valueTiming: Value of Example (one of allowed types)
    :param ContactDetail valueContactDetail: Value of Example (one of allowed types)
    :param Contributor valueContributor: Value of Example (one of allowed types)
    :param DataRequirement valueDataRequirement: Value of Example (one of allowed types)
    :param Expression valueExpression: Value of Example (one of allowed types)
    :param ParameterDefinition valueParameterDefinition: Value of Example (one of allowed types)
    :param RelatedArtifact valueRelatedArtifact: Value of Example (one of allowed types)
    :param TriggerDefinition valueTriggerDefinition: Value of Example (one of allowed types)
    :param UsageContext valueUsageContext: Value of Example (one of allowed types)
    :param Dosage valueDosage: Value of Example (one of allowed types)
    :param Meta valueMeta: Value of Example (one of allowed types)
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
        id: "str" = None,
        extension: list["Extension"] = None,
        label: "str" = None,
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
        self.label = label
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
    def from_dict(cls, data: dict) -> "ElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Constraint(BaseModel):
    """Formal constraints such as co-occurrence and other constraints that can be computationally evaluated within the context of the instance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str key: Target of 'condition' reference above
    :param str requirements: Why this constraint is necessary or appropriate
    :param str severity: error | warning
    :param str human: Human description of constraint
    :param str expression: FHIRPath expression of constraint
    :param str xpath: XPath expression of constraint
    :param str source: Reference to original source of constraint
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        key: "str" = None,
        requirements: "str" = None,
        severity: "str" = None,
        human: "str" = None,
        expression: "str" = None,
        xpath: "str" = None,
        source: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.key = key
        self.requirements = requirements
        self.severity = severity
        self.human = human
        self.expression = expression
        self.xpath = xpath
        self.source = source

    @classmethod
    def from_dict(cls, data: dict) -> "ElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Binding(BaseModel):
    """Binds to a value set if this element is coded (code, Coding, CodeableConcept, Quantity), or the data types (string, uri).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str strength: required | extensible | preferred | example
    :param str description: Human explanation of the value set
    :param str valueSet: Source of value set
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        strength: "str" = None,
        description: "str" = None,
        valueSet: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.strength = strength
        self.description = description
        self.valueSet = valueSet

    @classmethod
    def from_dict(cls, data: dict) -> "ElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Mapping(BaseModel):
    """Identifies a concept from an external specification that roughly corresponds to this element.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str identity: Reference to mapping declaration
    :param str language: Computable language of mapping
    :param str map: Details of the mapping
    :param str comment: Comments about the mapping or its use
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        identity: "str" = None,
        language: "str" = None,
        map: "str" = None,
        comment: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.identity = identity
        self.language = language
        self.map = map
        self.comment = comment

    @classmethod
    def from_dict(cls, data: dict) -> "ElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ElementDefinition(BaseModel):
    """Base StructureDefinition for ElementDefinition Type: Captures constraints on each element within the resource, profile, or extension.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: Path of the element in the hierarchy of elements
    :param str representation: xmlAttr | xmlText | typeAttr | cdaText | xhtml
    :param str sliceName: Name for this particular element (in a set of slices)
    :param bool sliceIsConstraining: If this slice definition constrains an inherited slice definition (or not)
    :param str label: Name for element to display with or prompt for element
    :param Coding code: Corresponding codes in terminologies
    :param Slicing slicing: This element is sliced - slices follow
    :param str short: Concise definition for space-constrained presentation
    :param str definition: Full formal definition as narrative text
    :param str comment: Comments about the use of this element
    :param str requirements: Why this resource has been created
    :param str alias: Other names
    :param int min: Minimum Cardinality
    :param str max: Maximum Cardinality (a number or *)
    :param Base base: Base definition information for tools
    :param str contentReference: Reference to definition of content for the element
    :param Type type: Data type and Profile for this element
    :param str defaultValueBase64Binary: Specified value if missing from instance
    :param bool defaultValueBoolean: Specified value if missing from instance
    :param str defaultValueCanonical: Specified value if missing from instance
    :param str defaultValueCode: Specified value if missing from instance
    :param str defaultValueDate: Specified value if missing from instance
    :param str defaultValueDateTime: Specified value if missing from instance
    :param float defaultValueDecimal: Specified value if missing from instance
    :param str defaultValueId: Specified value if missing from instance
    :param str defaultValueInstant: Specified value if missing from instance
    :param int defaultValueInteger: Specified value if missing from instance
    :param str defaultValueMarkdown: Specified value if missing from instance
    :param str defaultValueOid: Specified value if missing from instance
    :param int defaultValuePositiveInt: Specified value if missing from instance
    :param str defaultValueString: Specified value if missing from instance
    :param str defaultValueTime: Specified value if missing from instance
    :param int defaultValueUnsignedInt: Specified value if missing from instance
    :param str defaultValueUri: Specified value if missing from instance
    :param str defaultValueUrl: Specified value if missing from instance
    :param str defaultValueUuid: Specified value if missing from instance
    :param Address defaultValueAddress: Specified value if missing from instance
    :param Age defaultValueAge: Specified value if missing from instance
    :param Annotation defaultValueAnnotation: Specified value if missing from instance
    :param Attachment defaultValueAttachment: Specified value if missing from instance
    :param CodeableConcept defaultValueCodeableConcept: Specified value if missing from instance
    :param Coding defaultValueCoding: Specified value if missing from instance
    :param ContactPoint defaultValueContactPoint: Specified value if missing from instance
    :param Count defaultValueCount: Specified value if missing from instance
    :param Distance defaultValueDistance: Specified value if missing from instance
    :param Duration defaultValueDuration: Specified value if missing from instance
    :param HumanName defaultValueHumanName: Specified value if missing from instance
    :param Identifier defaultValueIdentifier: Specified value if missing from instance
    :param Money defaultValueMoney: Specified value if missing from instance
    :param Period defaultValuePeriod: Specified value if missing from instance
    :param Quantity defaultValueQuantity: Specified value if missing from instance
    :param Range defaultValueRange: Specified value if missing from instance
    :param Ratio defaultValueRatio: Specified value if missing from instance
    :param Reference defaultValueReference: Specified value if missing from instance
    :param SampledData defaultValueSampledData: Specified value if missing from instance
    :param Signature defaultValueSignature: Specified value if missing from instance
    :param Timing defaultValueTiming: Specified value if missing from instance
    :param ContactDetail defaultValueContactDetail: Specified value if missing from instance
    :param Contributor defaultValueContributor: Specified value if missing from instance
    :param DataRequirement defaultValueDataRequirement: Specified value if missing from instance
    :param Expression defaultValueExpression: Specified value if missing from instance
    :param ParameterDefinition defaultValueParameterDefinition: Specified value if missing from instance
    :param RelatedArtifact defaultValueRelatedArtifact: Specified value if missing from instance
    :param TriggerDefinition defaultValueTriggerDefinition: Specified value if missing from instance
    :param UsageContext defaultValueUsageContext: Specified value if missing from instance
    :param Dosage defaultValueDosage: Specified value if missing from instance
    :param Meta defaultValueMeta: Specified value if missing from instance
    :param str meaningWhenMissing: Implicit meaning when this element is missing
    :param str orderMeaning: What the order of the elements means
    :param str fixedBase64Binary: Value must be exactly this
    :param bool fixedBoolean: Value must be exactly this
    :param str fixedCanonical: Value must be exactly this
    :param str fixedCode: Value must be exactly this
    :param str fixedDate: Value must be exactly this
    :param str fixedDateTime: Value must be exactly this
    :param float fixedDecimal: Value must be exactly this
    :param str fixedId: Value must be exactly this
    :param str fixedInstant: Value must be exactly this
    :param int fixedInteger: Value must be exactly this
    :param str fixedMarkdown: Value must be exactly this
    :param str fixedOid: Value must be exactly this
    :param int fixedPositiveInt: Value must be exactly this
    :param str fixedString: Value must be exactly this
    :param str fixedTime: Value must be exactly this
    :param int fixedUnsignedInt: Value must be exactly this
    :param str fixedUri: Value must be exactly this
    :param str fixedUrl: Value must be exactly this
    :param str fixedUuid: Value must be exactly this
    :param Address fixedAddress: Value must be exactly this
    :param Age fixedAge: Value must be exactly this
    :param Annotation fixedAnnotation: Value must be exactly this
    :param Attachment fixedAttachment: Value must be exactly this
    :param CodeableConcept fixedCodeableConcept: Value must be exactly this
    :param Coding fixedCoding: Value must be exactly this
    :param ContactPoint fixedContactPoint: Value must be exactly this
    :param Count fixedCount: Value must be exactly this
    :param Distance fixedDistance: Value must be exactly this
    :param Duration fixedDuration: Value must be exactly this
    :param HumanName fixedHumanName: Value must be exactly this
    :param Identifier fixedIdentifier: Value must be exactly this
    :param Money fixedMoney: Value must be exactly this
    :param Period fixedPeriod: Value must be exactly this
    :param Quantity fixedQuantity: Value must be exactly this
    :param Range fixedRange: Value must be exactly this
    :param Ratio fixedRatio: Value must be exactly this
    :param Reference fixedReference: Value must be exactly this
    :param SampledData fixedSampledData: Value must be exactly this
    :param Signature fixedSignature: Value must be exactly this
    :param Timing fixedTiming: Value must be exactly this
    :param ContactDetail fixedContactDetail: Value must be exactly this
    :param Contributor fixedContributor: Value must be exactly this
    :param DataRequirement fixedDataRequirement: Value must be exactly this
    :param Expression fixedExpression: Value must be exactly this
    :param ParameterDefinition fixedParameterDefinition: Value must be exactly this
    :param RelatedArtifact fixedRelatedArtifact: Value must be exactly this
    :param TriggerDefinition fixedTriggerDefinition: Value must be exactly this
    :param UsageContext fixedUsageContext: Value must be exactly this
    :param Dosage fixedDosage: Value must be exactly this
    :param Meta fixedMeta: Value must be exactly this
    :param str patternBase64Binary: Value must have at least these property values
    :param bool patternBoolean: Value must have at least these property values
    :param str patternCanonical: Value must have at least these property values
    :param str patternCode: Value must have at least these property values
    :param str patternDate: Value must have at least these property values
    :param str patternDateTime: Value must have at least these property values
    :param float patternDecimal: Value must have at least these property values
    :param str patternId: Value must have at least these property values
    :param str patternInstant: Value must have at least these property values
    :param int patternInteger: Value must have at least these property values
    :param str patternMarkdown: Value must have at least these property values
    :param str patternOid: Value must have at least these property values
    :param int patternPositiveInt: Value must have at least these property values
    :param str patternString: Value must have at least these property values
    :param str patternTime: Value must have at least these property values
    :param int patternUnsignedInt: Value must have at least these property values
    :param str patternUri: Value must have at least these property values
    :param str patternUrl: Value must have at least these property values
    :param str patternUuid: Value must have at least these property values
    :param Address patternAddress: Value must have at least these property values
    :param Age patternAge: Value must have at least these property values
    :param Annotation patternAnnotation: Value must have at least these property values
    :param Attachment patternAttachment: Value must have at least these property values
    :param CodeableConcept patternCodeableConcept: Value must have at least these property values
    :param Coding patternCoding: Value must have at least these property values
    :param ContactPoint patternContactPoint: Value must have at least these property values
    :param Count patternCount: Value must have at least these property values
    :param Distance patternDistance: Value must have at least these property values
    :param Duration patternDuration: Value must have at least these property values
    :param HumanName patternHumanName: Value must have at least these property values
    :param Identifier patternIdentifier: Value must have at least these property values
    :param Money patternMoney: Value must have at least these property values
    :param Period patternPeriod: Value must have at least these property values
    :param Quantity patternQuantity: Value must have at least these property values
    :param Range patternRange: Value must have at least these property values
    :param Ratio patternRatio: Value must have at least these property values
    :param Reference patternReference: Value must have at least these property values
    :param SampledData patternSampledData: Value must have at least these property values
    :param Signature patternSignature: Value must have at least these property values
    :param Timing patternTiming: Value must have at least these property values
    :param ContactDetail patternContactDetail: Value must have at least these property values
    :param Contributor patternContributor: Value must have at least these property values
    :param DataRequirement patternDataRequirement: Value must have at least these property values
    :param Expression patternExpression: Value must have at least these property values
    :param ParameterDefinition patternParameterDefinition: Value must have at least these property values
    :param RelatedArtifact patternRelatedArtifact: Value must have at least these property values
    :param TriggerDefinition patternTriggerDefinition: Value must have at least these property values
    :param UsageContext patternUsageContext: Value must have at least these property values
    :param Dosage patternDosage: Value must have at least these property values
    :param Meta patternMeta: Value must have at least these property values
    :param Example example: Example value (as defined for type)
    :param str minValueDate: Minimum Allowed Value (for some types)
    :param str minValueDateTime: Minimum Allowed Value (for some types)
    :param str minValueInstant: Minimum Allowed Value (for some types)
    :param str minValueTime: Minimum Allowed Value (for some types)
    :param float minValueDecimal: Minimum Allowed Value (for some types)
    :param int minValueInteger: Minimum Allowed Value (for some types)
    :param int minValuePositiveInt: Minimum Allowed Value (for some types)
    :param int minValueUnsignedInt: Minimum Allowed Value (for some types)
    :param Quantity minValueQuantity: Minimum Allowed Value (for some types)
    :param str maxValueDate: Maximum Allowed Value (for some types)
    :param str maxValueDateTime: Maximum Allowed Value (for some types)
    :param str maxValueInstant: Maximum Allowed Value (for some types)
    :param str maxValueTime: Maximum Allowed Value (for some types)
    :param float maxValueDecimal: Maximum Allowed Value (for some types)
    :param int maxValueInteger: Maximum Allowed Value (for some types)
    :param int maxValuePositiveInt: Maximum Allowed Value (for some types)
    :param int maxValueUnsignedInt: Maximum Allowed Value (for some types)
    :param Quantity maxValueQuantity: Maximum Allowed Value (for some types)
    :param int maxLength: Max length for strings
    :param str condition: Reference to invariant about presence
    :param Constraint constraint: Condition that must evaluate to true
    :param bool mustSupport: If the element must be supported
    :param bool isModifier: If this modifies the meaning of other elements
    :param str isModifierReason: Reason that this element is marked as a modifier
    :param bool isSummary: Include when _summary = true?
    :param Binding binding: ValueSet details if this is coded
    :param Mapping mapping: Map element to another set of definitions
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "Coding", "is_contained": False},
        "slicing": {"class_name": "Slicing", "is_contained": True},
        "base": {"class_name": "Base", "is_contained": True},
        "type": {"class_name": "Type", "is_contained": True},
        "defaultValueAddress": {"class_name": "Address", "is_contained": False},
        "defaultValueAge": {"class_name": "Age", "is_contained": False},
        "defaultValueAnnotation": {"class_name": "Annotation", "is_contained": False},
        "defaultValueAttachment": {"class_name": "Attachment", "is_contained": False},
        "defaultValueCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "defaultValueCoding": {"class_name": "Coding", "is_contained": False},
        "defaultValueContactPoint": {
            "class_name": "ContactPoint",
            "is_contained": False,
        },
        "defaultValueCount": {"class_name": "Count", "is_contained": False},
        "defaultValueDistance": {"class_name": "Distance", "is_contained": False},
        "defaultValueDuration": {"class_name": "Duration", "is_contained": False},
        "defaultValueHumanName": {"class_name": "HumanName", "is_contained": False},
        "defaultValueIdentifier": {"class_name": "Identifier", "is_contained": False},
        "defaultValueMoney": {"class_name": "Money", "is_contained": False},
        "defaultValuePeriod": {"class_name": "Period", "is_contained": False},
        "defaultValueQuantity": {"class_name": "Quantity", "is_contained": False},
        "defaultValueRange": {"class_name": "Range", "is_contained": False},
        "defaultValueRatio": {"class_name": "Ratio", "is_contained": False},
        "defaultValueReference": {"class_name": "Reference", "is_contained": False},
        "defaultValueSampledData": {"class_name": "SampledData", "is_contained": False},
        "defaultValueSignature": {"class_name": "Signature", "is_contained": False},
        "defaultValueTiming": {"class_name": "Timing", "is_contained": False},
        "defaultValueContactDetail": {
            "class_name": "ContactDetail",
            "is_contained": False,
        },
        "defaultValueContributor": {"class_name": "Contributor", "is_contained": False},
        "defaultValueDataRequirement": {
            "class_name": "DataRequirement",
            "is_contained": False,
        },
        "defaultValueExpression": {"class_name": "Expression", "is_contained": False},
        "defaultValueParameterDefinition": {
            "class_name": "ParameterDefinition",
            "is_contained": False,
        },
        "defaultValueRelatedArtifact": {
            "class_name": "RelatedArtifact",
            "is_contained": False,
        },
        "defaultValueTriggerDefinition": {
            "class_name": "TriggerDefinition",
            "is_contained": False,
        },
        "defaultValueUsageContext": {
            "class_name": "UsageContext",
            "is_contained": False,
        },
        "defaultValueDosage": {"class_name": "Dosage", "is_contained": False},
        "defaultValueMeta": {"class_name": "Meta", "is_contained": False},
        "fixedAddress": {"class_name": "Address", "is_contained": False},
        "fixedAge": {"class_name": "Age", "is_contained": False},
        "fixedAnnotation": {"class_name": "Annotation", "is_contained": False},
        "fixedAttachment": {"class_name": "Attachment", "is_contained": False},
        "fixedCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "fixedCoding": {"class_name": "Coding", "is_contained": False},
        "fixedContactPoint": {"class_name": "ContactPoint", "is_contained": False},
        "fixedCount": {"class_name": "Count", "is_contained": False},
        "fixedDistance": {"class_name": "Distance", "is_contained": False},
        "fixedDuration": {"class_name": "Duration", "is_contained": False},
        "fixedHumanName": {"class_name": "HumanName", "is_contained": False},
        "fixedIdentifier": {"class_name": "Identifier", "is_contained": False},
        "fixedMoney": {"class_name": "Money", "is_contained": False},
        "fixedPeriod": {"class_name": "Period", "is_contained": False},
        "fixedQuantity": {"class_name": "Quantity", "is_contained": False},
        "fixedRange": {"class_name": "Range", "is_contained": False},
        "fixedRatio": {"class_name": "Ratio", "is_contained": False},
        "fixedReference": {"class_name": "Reference", "is_contained": False},
        "fixedSampledData": {"class_name": "SampledData", "is_contained": False},
        "fixedSignature": {"class_name": "Signature", "is_contained": False},
        "fixedTiming": {"class_name": "Timing", "is_contained": False},
        "fixedContactDetail": {"class_name": "ContactDetail", "is_contained": False},
        "fixedContributor": {"class_name": "Contributor", "is_contained": False},
        "fixedDataRequirement": {
            "class_name": "DataRequirement",
            "is_contained": False,
        },
        "fixedExpression": {"class_name": "Expression", "is_contained": False},
        "fixedParameterDefinition": {
            "class_name": "ParameterDefinition",
            "is_contained": False,
        },
        "fixedRelatedArtifact": {
            "class_name": "RelatedArtifact",
            "is_contained": False,
        },
        "fixedTriggerDefinition": {
            "class_name": "TriggerDefinition",
            "is_contained": False,
        },
        "fixedUsageContext": {"class_name": "UsageContext", "is_contained": False},
        "fixedDosage": {"class_name": "Dosage", "is_contained": False},
        "fixedMeta": {"class_name": "Meta", "is_contained": False},
        "patternAddress": {"class_name": "Address", "is_contained": False},
        "patternAge": {"class_name": "Age", "is_contained": False},
        "patternAnnotation": {"class_name": "Annotation", "is_contained": False},
        "patternAttachment": {"class_name": "Attachment", "is_contained": False},
        "patternCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "patternCoding": {"class_name": "Coding", "is_contained": False},
        "patternContactPoint": {"class_name": "ContactPoint", "is_contained": False},
        "patternCount": {"class_name": "Count", "is_contained": False},
        "patternDistance": {"class_name": "Distance", "is_contained": False},
        "patternDuration": {"class_name": "Duration", "is_contained": False},
        "patternHumanName": {"class_name": "HumanName", "is_contained": False},
        "patternIdentifier": {"class_name": "Identifier", "is_contained": False},
        "patternMoney": {"class_name": "Money", "is_contained": False},
        "patternPeriod": {"class_name": "Period", "is_contained": False},
        "patternQuantity": {"class_name": "Quantity", "is_contained": False},
        "patternRange": {"class_name": "Range", "is_contained": False},
        "patternRatio": {"class_name": "Ratio", "is_contained": False},
        "patternReference": {"class_name": "Reference", "is_contained": False},
        "patternSampledData": {"class_name": "SampledData", "is_contained": False},
        "patternSignature": {"class_name": "Signature", "is_contained": False},
        "patternTiming": {"class_name": "Timing", "is_contained": False},
        "patternContactDetail": {"class_name": "ContactDetail", "is_contained": False},
        "patternContributor": {"class_name": "Contributor", "is_contained": False},
        "patternDataRequirement": {
            "class_name": "DataRequirement",
            "is_contained": False,
        },
        "patternExpression": {"class_name": "Expression", "is_contained": False},
        "patternParameterDefinition": {
            "class_name": "ParameterDefinition",
            "is_contained": False,
        },
        "patternRelatedArtifact": {
            "class_name": "RelatedArtifact",
            "is_contained": False,
        },
        "patternTriggerDefinition": {
            "class_name": "TriggerDefinition",
            "is_contained": False,
        },
        "patternUsageContext": {"class_name": "UsageContext", "is_contained": False},
        "patternDosage": {"class_name": "Dosage", "is_contained": False},
        "patternMeta": {"class_name": "Meta", "is_contained": False},
        "example": {"class_name": "Example", "is_contained": True},
        "minValueQuantity": {"class_name": "Quantity", "is_contained": False},
        "maxValueQuantity": {"class_name": "Quantity", "is_contained": False},
        "constraint": {"class_name": "Constraint", "is_contained": True},
        "binding": {"class_name": "Binding", "is_contained": True},
        "mapping": {"class_name": "Mapping", "is_contained": True},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        path: "str" = None,
        representation: list["str"] = None,
        sliceName: "str" = None,
        sliceIsConstraining: "bool" = None,
        label: "str" = None,
        code: list["Coding"] = None,
        slicing: "Slicing" = None,
        short: "str" = None,
        definition: "str" = None,
        comment: "str" = None,
        requirements: "str" = None,
        alias: list["str"] = None,
        min: "int" = None,
        max: "str" = None,
        base: "Base" = None,
        contentReference: "str" = None,
        type: list["Type"] = None,
        defaultValueBase64Binary: "str" = None,
        defaultValueBoolean: "bool" = None,
        defaultValueCanonical: "str" = None,
        defaultValueCode: "str" = None,
        defaultValueDate: "str" = None,
        defaultValueDateTime: "str" = None,
        defaultValueDecimal: "float" = None,
        defaultValueId: "str" = None,
        defaultValueInstant: "str" = None,
        defaultValueInteger: "int" = None,
        defaultValueMarkdown: "str" = None,
        defaultValueOid: "str" = None,
        defaultValuePositiveInt: "int" = None,
        defaultValueString: "str" = None,
        defaultValueTime: "str" = None,
        defaultValueUnsignedInt: "int" = None,
        defaultValueUri: "str" = None,
        defaultValueUrl: "str" = None,
        defaultValueUuid: "str" = None,
        defaultValueAddress: "Address" = None,
        defaultValueAge: "Age" = None,
        defaultValueAnnotation: "Annotation" = None,
        defaultValueAttachment: "Attachment" = None,
        defaultValueCodeableConcept: "CodeableConcept" = None,
        defaultValueCoding: "Coding" = None,
        defaultValueContactPoint: "ContactPoint" = None,
        defaultValueCount: "Count" = None,
        defaultValueDistance: "Distance" = None,
        defaultValueDuration: "Duration" = None,
        defaultValueHumanName: "HumanName" = None,
        defaultValueIdentifier: "Identifier" = None,
        defaultValueMoney: "Money" = None,
        defaultValuePeriod: "Period" = None,
        defaultValueQuantity: "Quantity" = None,
        defaultValueRange: "Range" = None,
        defaultValueRatio: "Ratio" = None,
        defaultValueReference: "Reference" = None,
        defaultValueSampledData: "SampledData" = None,
        defaultValueSignature: "Signature" = None,
        defaultValueTiming: "Timing" = None,
        defaultValueContactDetail: "ContactDetail" = None,
        defaultValueContributor: "Contributor" = None,
        defaultValueDataRequirement: "DataRequirement" = None,
        defaultValueExpression: "Expression" = None,
        defaultValueParameterDefinition: "ParameterDefinition" = None,
        defaultValueRelatedArtifact: "RelatedArtifact" = None,
        defaultValueTriggerDefinition: "TriggerDefinition" = None,
        defaultValueUsageContext: "UsageContext" = None,
        defaultValueDosage: "Dosage" = None,
        defaultValueMeta: "Meta" = None,
        meaningWhenMissing: "str" = None,
        orderMeaning: "str" = None,
        fixedBase64Binary: "str" = None,
        fixedBoolean: "bool" = None,
        fixedCanonical: "str" = None,
        fixedCode: "str" = None,
        fixedDate: "str" = None,
        fixedDateTime: "str" = None,
        fixedDecimal: "float" = None,
        fixedId: "str" = None,
        fixedInstant: "str" = None,
        fixedInteger: "int" = None,
        fixedMarkdown: "str" = None,
        fixedOid: "str" = None,
        fixedPositiveInt: "int" = None,
        fixedString: "str" = None,
        fixedTime: "str" = None,
        fixedUnsignedInt: "int" = None,
        fixedUri: "str" = None,
        fixedUrl: "str" = None,
        fixedUuid: "str" = None,
        fixedAddress: "Address" = None,
        fixedAge: "Age" = None,
        fixedAnnotation: "Annotation" = None,
        fixedAttachment: "Attachment" = None,
        fixedCodeableConcept: "CodeableConcept" = None,
        fixedCoding: "Coding" = None,
        fixedContactPoint: "ContactPoint" = None,
        fixedCount: "Count" = None,
        fixedDistance: "Distance" = None,
        fixedDuration: "Duration" = None,
        fixedHumanName: "HumanName" = None,
        fixedIdentifier: "Identifier" = None,
        fixedMoney: "Money" = None,
        fixedPeriod: "Period" = None,
        fixedQuantity: "Quantity" = None,
        fixedRange: "Range" = None,
        fixedRatio: "Ratio" = None,
        fixedReference: "Reference" = None,
        fixedSampledData: "SampledData" = None,
        fixedSignature: "Signature" = None,
        fixedTiming: "Timing" = None,
        fixedContactDetail: "ContactDetail" = None,
        fixedContributor: "Contributor" = None,
        fixedDataRequirement: "DataRequirement" = None,
        fixedExpression: "Expression" = None,
        fixedParameterDefinition: "ParameterDefinition" = None,
        fixedRelatedArtifact: "RelatedArtifact" = None,
        fixedTriggerDefinition: "TriggerDefinition" = None,
        fixedUsageContext: "UsageContext" = None,
        fixedDosage: "Dosage" = None,
        fixedMeta: "Meta" = None,
        patternBase64Binary: "str" = None,
        patternBoolean: "bool" = None,
        patternCanonical: "str" = None,
        patternCode: "str" = None,
        patternDate: "str" = None,
        patternDateTime: "str" = None,
        patternDecimal: "float" = None,
        patternId: "str" = None,
        patternInstant: "str" = None,
        patternInteger: "int" = None,
        patternMarkdown: "str" = None,
        patternOid: "str" = None,
        patternPositiveInt: "int" = None,
        patternString: "str" = None,
        patternTime: "str" = None,
        patternUnsignedInt: "int" = None,
        patternUri: "str" = None,
        patternUrl: "str" = None,
        patternUuid: "str" = None,
        patternAddress: "Address" = None,
        patternAge: "Age" = None,
        patternAnnotation: "Annotation" = None,
        patternAttachment: "Attachment" = None,
        patternCodeableConcept: "CodeableConcept" = None,
        patternCoding: "Coding" = None,
        patternContactPoint: "ContactPoint" = None,
        patternCount: "Count" = None,
        patternDistance: "Distance" = None,
        patternDuration: "Duration" = None,
        patternHumanName: "HumanName" = None,
        patternIdentifier: "Identifier" = None,
        patternMoney: "Money" = None,
        patternPeriod: "Period" = None,
        patternQuantity: "Quantity" = None,
        patternRange: "Range" = None,
        patternRatio: "Ratio" = None,
        patternReference: "Reference" = None,
        patternSampledData: "SampledData" = None,
        patternSignature: "Signature" = None,
        patternTiming: "Timing" = None,
        patternContactDetail: "ContactDetail" = None,
        patternContributor: "Contributor" = None,
        patternDataRequirement: "DataRequirement" = None,
        patternExpression: "Expression" = None,
        patternParameterDefinition: "ParameterDefinition" = None,
        patternRelatedArtifact: "RelatedArtifact" = None,
        patternTriggerDefinition: "TriggerDefinition" = None,
        patternUsageContext: "UsageContext" = None,
        patternDosage: "Dosage" = None,
        patternMeta: "Meta" = None,
        example: list["Example"] = None,
        minValueDate: "str" = None,
        minValueDateTime: "str" = None,
        minValueInstant: "str" = None,
        minValueTime: "str" = None,
        minValueDecimal: "float" = None,
        minValueInteger: "int" = None,
        minValuePositiveInt: "int" = None,
        minValueUnsignedInt: "int" = None,
        minValueQuantity: "Quantity" = None,
        maxValueDate: "str" = None,
        maxValueDateTime: "str" = None,
        maxValueInstant: "str" = None,
        maxValueTime: "str" = None,
        maxValueDecimal: "float" = None,
        maxValueInteger: "int" = None,
        maxValuePositiveInt: "int" = None,
        maxValueUnsignedInt: "int" = None,
        maxValueQuantity: "Quantity" = None,
        maxLength: "int" = None,
        condition: list["str"] = None,
        constraint: list["Constraint"] = None,
        mustSupport: "bool" = None,
        isModifier: "bool" = None,
        isModifierReason: "str" = None,
        isSummary: "bool" = None,
        binding: "Binding" = None,
        mapping: list["Mapping"] = None,
    ):
        self.resourceType = resourceType or "ElementDefinition"
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.path = path
        self.representation = representation or []
        self.sliceName = sliceName
        self.sliceIsConstraining = sliceIsConstraining
        self.label = label
        self.code = code or []
        self.slicing = slicing
        self.short = short
        self.definition = definition
        self.comment = comment
        self.requirements = requirements
        self.alias = alias or []
        self.min = min
        self.max = max
        self.base = base
        self.contentReference = contentReference
        self.type = type or []
        self.defaultValueBase64Binary = defaultValueBase64Binary
        self.defaultValueBoolean = defaultValueBoolean
        self.defaultValueCanonical = defaultValueCanonical
        self.defaultValueCode = defaultValueCode
        self.defaultValueDate = defaultValueDate
        self.defaultValueDateTime = defaultValueDateTime
        self.defaultValueDecimal = defaultValueDecimal
        self.defaultValueId = defaultValueId
        self.defaultValueInstant = defaultValueInstant
        self.defaultValueInteger = defaultValueInteger
        self.defaultValueMarkdown = defaultValueMarkdown
        self.defaultValueOid = defaultValueOid
        self.defaultValuePositiveInt = defaultValuePositiveInt
        self.defaultValueString = defaultValueString
        self.defaultValueTime = defaultValueTime
        self.defaultValueUnsignedInt = defaultValueUnsignedInt
        self.defaultValueUri = defaultValueUri
        self.defaultValueUrl = defaultValueUrl
        self.defaultValueUuid = defaultValueUuid
        self.defaultValueAddress = defaultValueAddress
        self.defaultValueAge = defaultValueAge
        self.defaultValueAnnotation = defaultValueAnnotation
        self.defaultValueAttachment = defaultValueAttachment
        self.defaultValueCodeableConcept = defaultValueCodeableConcept
        self.defaultValueCoding = defaultValueCoding
        self.defaultValueContactPoint = defaultValueContactPoint
        self.defaultValueCount = defaultValueCount
        self.defaultValueDistance = defaultValueDistance
        self.defaultValueDuration = defaultValueDuration
        self.defaultValueHumanName = defaultValueHumanName
        self.defaultValueIdentifier = defaultValueIdentifier
        self.defaultValueMoney = defaultValueMoney
        self.defaultValuePeriod = defaultValuePeriod
        self.defaultValueQuantity = defaultValueQuantity
        self.defaultValueRange = defaultValueRange
        self.defaultValueRatio = defaultValueRatio
        self.defaultValueReference = defaultValueReference
        self.defaultValueSampledData = defaultValueSampledData
        self.defaultValueSignature = defaultValueSignature
        self.defaultValueTiming = defaultValueTiming
        self.defaultValueContactDetail = defaultValueContactDetail
        self.defaultValueContributor = defaultValueContributor
        self.defaultValueDataRequirement = defaultValueDataRequirement
        self.defaultValueExpression = defaultValueExpression
        self.defaultValueParameterDefinition = defaultValueParameterDefinition
        self.defaultValueRelatedArtifact = defaultValueRelatedArtifact
        self.defaultValueTriggerDefinition = defaultValueTriggerDefinition
        self.defaultValueUsageContext = defaultValueUsageContext
        self.defaultValueDosage = defaultValueDosage
        self.defaultValueMeta = defaultValueMeta
        self.meaningWhenMissing = meaningWhenMissing
        self.orderMeaning = orderMeaning
        self.fixedBase64Binary = fixedBase64Binary
        self.fixedBoolean = fixedBoolean
        self.fixedCanonical = fixedCanonical
        self.fixedCode = fixedCode
        self.fixedDate = fixedDate
        self.fixedDateTime = fixedDateTime
        self.fixedDecimal = fixedDecimal
        self.fixedId = fixedId
        self.fixedInstant = fixedInstant
        self.fixedInteger = fixedInteger
        self.fixedMarkdown = fixedMarkdown
        self.fixedOid = fixedOid
        self.fixedPositiveInt = fixedPositiveInt
        self.fixedString = fixedString
        self.fixedTime = fixedTime
        self.fixedUnsignedInt = fixedUnsignedInt
        self.fixedUri = fixedUri
        self.fixedUrl = fixedUrl
        self.fixedUuid = fixedUuid
        self.fixedAddress = fixedAddress
        self.fixedAge = fixedAge
        self.fixedAnnotation = fixedAnnotation
        self.fixedAttachment = fixedAttachment
        self.fixedCodeableConcept = fixedCodeableConcept
        self.fixedCoding = fixedCoding
        self.fixedContactPoint = fixedContactPoint
        self.fixedCount = fixedCount
        self.fixedDistance = fixedDistance
        self.fixedDuration = fixedDuration
        self.fixedHumanName = fixedHumanName
        self.fixedIdentifier = fixedIdentifier
        self.fixedMoney = fixedMoney
        self.fixedPeriod = fixedPeriod
        self.fixedQuantity = fixedQuantity
        self.fixedRange = fixedRange
        self.fixedRatio = fixedRatio
        self.fixedReference = fixedReference
        self.fixedSampledData = fixedSampledData
        self.fixedSignature = fixedSignature
        self.fixedTiming = fixedTiming
        self.fixedContactDetail = fixedContactDetail
        self.fixedContributor = fixedContributor
        self.fixedDataRequirement = fixedDataRequirement
        self.fixedExpression = fixedExpression
        self.fixedParameterDefinition = fixedParameterDefinition
        self.fixedRelatedArtifact = fixedRelatedArtifact
        self.fixedTriggerDefinition = fixedTriggerDefinition
        self.fixedUsageContext = fixedUsageContext
        self.fixedDosage = fixedDosage
        self.fixedMeta = fixedMeta
        self.patternBase64Binary = patternBase64Binary
        self.patternBoolean = patternBoolean
        self.patternCanonical = patternCanonical
        self.patternCode = patternCode
        self.patternDate = patternDate
        self.patternDateTime = patternDateTime
        self.patternDecimal = patternDecimal
        self.patternId = patternId
        self.patternInstant = patternInstant
        self.patternInteger = patternInteger
        self.patternMarkdown = patternMarkdown
        self.patternOid = patternOid
        self.patternPositiveInt = patternPositiveInt
        self.patternString = patternString
        self.patternTime = patternTime
        self.patternUnsignedInt = patternUnsignedInt
        self.patternUri = patternUri
        self.patternUrl = patternUrl
        self.patternUuid = patternUuid
        self.patternAddress = patternAddress
        self.patternAge = patternAge
        self.patternAnnotation = patternAnnotation
        self.patternAttachment = patternAttachment
        self.patternCodeableConcept = patternCodeableConcept
        self.patternCoding = patternCoding
        self.patternContactPoint = patternContactPoint
        self.patternCount = patternCount
        self.patternDistance = patternDistance
        self.patternDuration = patternDuration
        self.patternHumanName = patternHumanName
        self.patternIdentifier = patternIdentifier
        self.patternMoney = patternMoney
        self.patternPeriod = patternPeriod
        self.patternQuantity = patternQuantity
        self.patternRange = patternRange
        self.patternRatio = patternRatio
        self.patternReference = patternReference
        self.patternSampledData = patternSampledData
        self.patternSignature = patternSignature
        self.patternTiming = patternTiming
        self.patternContactDetail = patternContactDetail
        self.patternContributor = patternContributor
        self.patternDataRequirement = patternDataRequirement
        self.patternExpression = patternExpression
        self.patternParameterDefinition = patternParameterDefinition
        self.patternRelatedArtifact = patternRelatedArtifact
        self.patternTriggerDefinition = patternTriggerDefinition
        self.patternUsageContext = patternUsageContext
        self.patternDosage = patternDosage
        self.patternMeta = patternMeta
        self.example = example or []
        self.minValueDate = minValueDate
        self.minValueDateTime = minValueDateTime
        self.minValueInstant = minValueInstant
        self.minValueTime = minValueTime
        self.minValueDecimal = minValueDecimal
        self.minValueInteger = minValueInteger
        self.minValuePositiveInt = minValuePositiveInt
        self.minValueUnsignedInt = minValueUnsignedInt
        self.minValueQuantity = minValueQuantity
        self.maxValueDate = maxValueDate
        self.maxValueDateTime = maxValueDateTime
        self.maxValueInstant = maxValueInstant
        self.maxValueTime = maxValueTime
        self.maxValueDecimal = maxValueDecimal
        self.maxValueInteger = maxValueInteger
        self.maxValuePositiveInt = maxValuePositiveInt
        self.maxValueUnsignedInt = maxValueUnsignedInt
        self.maxValueQuantity = maxValueQuantity
        self.maxLength = maxLength
        self.condition = condition or []
        self.constraint = constraint or []
        self.mustSupport = mustSupport
        self.isModifier = isModifier
        self.isModifierReason = isModifierReason
        self.isSummary = isSummary
        self.binding = binding
        self.mapping = mapping or []

    @classmethod
    def from_dict(cls, data: dict) -> "ElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
