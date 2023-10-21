"""
Generated class for StructureMap. 
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
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Signature import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Period import *
from fhan.models.R4.Age import *
from fhan.models.R4.DomainResource import *


class Structure(BaseModel):
    """A structure definition used by this map. The structure definition may describe instances that are converted, or the instances that are produced.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: Canonical reference to structure definition
    :param str mode: source | queried | target | produced
    :param str alias: Name for type in this map
    :param str documentation: Documentation on use of structure
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        url: "str" = None,
        mode: "str" = None,
        alias: "str" = None,
        documentation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.mode = mode
        self.alias = alias
        self.documentation = documentation

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Input(BaseModel):
    """A name assigned to an instance of data. The instance must be provided when the mapping is invoked.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name for this instance of data
    :param str type: Type for this instance of data
    :param str mode: source | target
    :param str documentation: Documentation for this instance of data
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        type: "str" = None,
        mode: "str" = None,
        documentation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.type = type
        self.mode = mode
        self.documentation = documentation

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Source(BaseModel):
    """Source inputs to the mapping.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param int min: Specified minimum cardinality
    :param str max: Specified maximum cardinality (number or *)
    :param str type: Rule only applies if source has this type
    :param str defaultValueBase64Binary: Default value if no value exists
    :param bool defaultValueBoolean: Default value if no value exists
    :param str defaultValueCanonical: Default value if no value exists
    :param str defaultValueCode: Default value if no value exists
    :param str defaultValueDate: Default value if no value exists
    :param str defaultValueDateTime: Default value if no value exists
    :param float defaultValueDecimal: Default value if no value exists
    :param str defaultValueId: Default value if no value exists
    :param str defaultValueInstant: Default value if no value exists
    :param int defaultValueInteger: Default value if no value exists
    :param str defaultValueMarkdown: Default value if no value exists
    :param str defaultValueOid: Default value if no value exists
    :param int defaultValuePositiveInt: Default value if no value exists
    :param str defaultValueString: Default value if no value exists
    :param str defaultValueTime: Default value if no value exists
    :param int defaultValueUnsignedInt: Default value if no value exists
    :param str defaultValueUri: Default value if no value exists
    :param str defaultValueUrl: Default value if no value exists
    :param str defaultValueUuid: Default value if no value exists
    :param Address defaultValueAddress: Default value if no value exists
    :param Age defaultValueAge: Default value if no value exists
    :param Annotation defaultValueAnnotation: Default value if no value exists
    :param Attachment defaultValueAttachment: Default value if no value exists
    :param CodeableConcept defaultValueCodeableConcept: Default value if no value exists
    :param Coding defaultValueCoding: Default value if no value exists
    :param ContactPoint defaultValueContactPoint: Default value if no value exists
    :param Count defaultValueCount: Default value if no value exists
    :param Distance defaultValueDistance: Default value if no value exists
    :param Duration defaultValueDuration: Default value if no value exists
    :param HumanName defaultValueHumanName: Default value if no value exists
    :param Identifier defaultValueIdentifier: Default value if no value exists
    :param Money defaultValueMoney: Default value if no value exists
    :param Period defaultValuePeriod: Default value if no value exists
    :param Quantity defaultValueQuantity: Default value if no value exists
    :param Range defaultValueRange: Default value if no value exists
    :param Ratio defaultValueRatio: Default value if no value exists
    :param Reference defaultValueReference: Default value if no value exists
    :param SampledData defaultValueSampledData: Default value if no value exists
    :param Signature defaultValueSignature: Default value if no value exists
    :param Timing defaultValueTiming: Default value if no value exists
    :param ContactDetail defaultValueContactDetail: Default value if no value exists
    :param Contributor defaultValueContributor: Default value if no value exists
    :param DataRequirement defaultValueDataRequirement: Default value if no value exists
    :param Expression defaultValueExpression: Default value if no value exists
    :param ParameterDefinition defaultValueParameterDefinition: Default value if no value exists
    :param RelatedArtifact defaultValueRelatedArtifact: Default value if no value exists
    :param TriggerDefinition defaultValueTriggerDefinition: Default value if no value exists
    :param UsageContext defaultValueUsageContext: Default value if no value exists
    :param Dosage defaultValueDosage: Default value if no value exists
    :param Meta defaultValueMeta: Default value if no value exists
    :param str element: Optional field for this source
    :param str listMode: first | not_first | last | not_last | only_one
    :param str variable: Named context for field, if a field is specified
    :param str condition: FHIRPath expression  - must be true or the rule does not apply
    :param str check: FHIRPath expression  - must be true or the mapping engine throws an error instead of completing
    :param str logMessage: Message to put in log if source exists (FHIRPath)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
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
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        context: "str" = None,
        min: "int" = None,
        max: "str" = None,
        type: "str" = None,
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
        element: "str" = None,
        listMode: "str" = None,
        variable: "str" = None,
        condition: "str" = None,
        check: "str" = None,
        logMessage: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.context = context
        self.min = min
        self.max = max
        self.type = type
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
        self.element = element
        self.listMode = listMode
        self.variable = variable
        self.condition = condition
        self.check = check
        self.logMessage = logMessage

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Parameter(BaseModel):
    """Parameters to the transform.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str valueId: Parameter value - variable or literal
    :param str valueString: Parameter value - variable or literal
    :param bool valueBoolean: Parameter value - variable or literal
    :param int valueInteger: Parameter value - variable or literal
    :param float valueDecimal: Parameter value - variable or literal
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        valueId: "str" = None,
        valueString: "str" = None,
        valueBoolean: "bool" = None,
        valueInteger: "int" = None,
        valueDecimal: "float" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.valueId = valueId
        self.valueString = valueString
        self.valueBoolean = valueBoolean
        self.valueInteger = valueInteger
        self.valueDecimal = valueDecimal

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Target(BaseModel):
    """Content to create because of this mapping rule.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param str contextType: type | variable
    :param str element: Field to create in the context
    :param str variable: Named context for field, if desired, and a field is specified
    :param str listMode: first | share | last | collate
    :param str listRuleId: Internal rule reference for shared list items
    :param str transform: create | copy +
    :param Parameter parameter: Parameters to the transform
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "parameter": {"class_name": "Parameter", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        context: "str" = None,
        contextType: "str" = None,
        element: "str" = None,
        variable: "str" = None,
        listMode: list["str"] = None,
        listRuleId: "str" = None,
        transform: "str" = None,
        parameter: list["Parameter"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.context = context
        self.contextType = contextType
        self.element = element
        self.variable = variable
        self.listMode = listMode or []
        self.listRuleId = listRuleId
        self.transform = transform
        self.parameter = parameter or []

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Dependent(BaseModel):
    """Which other rules to apply in the context of this rule.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of a rule or group to apply
    :param str variable: Variable to pass to the rule or group
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        variable: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.variable = variable or []

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Rule(BaseModel):
    """Transform Rule from source to target.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of the rule for internal references
    :param Source source: Source inputs to the mapping
    :param Target target: Content to create because of this mapping rule
    :param Rule rule: Rules contained in this rule
    :param Dependent dependent: Which other rules to apply in the context of this rule
    :param str documentation: Documentation for this instance of data
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "source": {"class_name": "Source", "is_contained": True},
        "target": {"class_name": "Target", "is_contained": True},
        "rule": {"class_name": "Rule", "is_contained": True},
        "dependent": {"class_name": "Dependent", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        source: list["Source"] = None,
        target: list["Target"] = None,
        rule: list["Rule"] = None,
        dependent: list["Dependent"] = None,
        documentation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.source = source or []
        self.target = target or []
        self.rule = rule or []
        self.dependent = dependent or []
        self.documentation = documentation

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Group(BaseModel):
    """Organizes the mapping into manageable chunks for human review/ease of maintenance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Human-readable label
    :param str extends: Another group that this group adds rules to
    :param str typeMode: none | types | type-and-types
    :param str documentation: Additional description/explanation for group
    :param Input input: Named instance provided when invoking the map
    :param Rule rule: Transform Rule from source to target
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "input": {"class_name": "Input", "is_contained": True},
        "rule": {"class_name": "Rule", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        extends: "str" = None,
        typeMode: "str" = None,
        documentation: "str" = None,
        input: list["Input"] = None,
        rule: list["Rule"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.extends = extends
        self.typeMode = typeMode
        self.documentation = documentation
        self.input = input or []
        self.rule = rule or []

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class StructureMap(DomainResource):
    """A Map of relationships between 2 structures that can be used to transform data.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this structure map, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the structure map
    :param str version: Business version of the structure map
    :param str name: Name for this structure map (computer friendly)
    :param str title: Name for this structure map (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the structure map
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for structure map (if applicable)
    :param str purpose: Why this structure map is defined
    :param str copyright: Use and/or publishing restrictions
    :param Structure structure: Structure Definition used by this map
    :param str _import: Other maps used by this map (canonical URLs)
    :param Group group: Named sections for reader convenience
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "structure": {"class_name": "Structure", "is_contained": True},
        "group": {"class_name": "Group", "is_contained": True},
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
        url: "str" = None,
        identifier: list["Identifier"] = None,
        version: "str" = None,
        name: "str" = None,
        title: "str" = None,
        status: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        copyright: "str" = None,
        structure: list["Structure"] = None,
        _import: list["str"] = None,
        group: list["Group"] = None,
    ):
        self.resourceType = resourceType or "StructureMap"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.identifier = identifier or []
        self.version = version
        self.name = name
        self.title = title
        self.status = status
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.copyright = copyright
        self.structure = structure or []
        self._import = _import or []
        self.group = group or []

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
