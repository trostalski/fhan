"""
Generated class for ObservationDefinition. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class QuantitativeDetails(BaseModel):
    """Characteristics for quantitative results of this observation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept customaryUnit: Customary unit for quantitative results
    :param CodeableConcept unit: SI unit for quantitative results
    :param float conversionFactor: SI to Customary unit conversion factor
    :param int decimalPrecision: Decimal precision of observation quantitative results
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "customaryUnit": {"class_name": "CodeableConcept", "is_contained": False},
        "unit": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        customaryUnit: "CodeableConcept" = None,
        unit: "CodeableConcept" = None,
        conversionFactor: "float" = None,
        decimalPrecision: "int" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.customaryUnit = customaryUnit
        self.unit = unit
        self.conversionFactor = conversionFactor
        self.decimalPrecision = decimalPrecision

    @classmethod
    def from_dict(cls, data: dict) -> "ObservationDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ObservationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class QualifiedInterval(BaseModel):
    """Multiple  ranges of results qualified by different contexts for ordinal or continuous observations conforming to this ObservationDefinition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str category: reference | critical | absolute
    :param Range range: The interval itself, for continuous or ordinal observations
    :param CodeableConcept context: Range context qualifier
    :param CodeableConcept appliesTo: Targetted population of the range
    :param str gender: male | female | other | unknown
    :param Range age: Applicable age range, if relevant
    :param Range gestationalAge: Applicable gestational age range, if relevant
    :param str condition: Condition associated with the reference range
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "range": {"class_name": "Range", "is_contained": False},
        "context": {"class_name": "CodeableConcept", "is_contained": False},
        "appliesTo": {"class_name": "CodeableConcept", "is_contained": False},
        "age": {"class_name": "Range", "is_contained": False},
        "gestationalAge": {"class_name": "Range", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        category: "str" = None,
        range: "Range" = None,
        context: "CodeableConcept" = None,
        appliesTo: list["CodeableConcept"] = None,
        gender: "str" = None,
        age: "Range" = None,
        gestationalAge: "Range" = None,
        condition: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category
        self.range = range
        self.context = context
        self.appliesTo = appliesTo or []
        self.gender = gender
        self.age = age
        self.gestationalAge = gestationalAge
        self.condition = condition

    @classmethod
    def from_dict(cls, data: dict) -> "ObservationDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ObservationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ObservationDefinition(DomainResource):
    """Set of definitional characteristics for a kind of observation or measurement produced or consumed by an orderable health care service.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept category: Category of observation
    :param CodeableConcept code: Type of observation (code / type)
    :param Identifier identifier: Business identifier for this ObservationDefinition instance
    :param str permittedDataType: Quantity | CodeableConcept | string | boolean | integer | Range | Ratio | SampledData | time | dateTime | Period
    :param bool multipleResultsAllowed: Multiple results allowed
    :param CodeableConcept method: Method used to produce the observation
    :param str preferredReportName: Preferred report name
    :param QuantitativeDetails quantitativeDetails: Characteristics of quantitative results
    :param QualifiedInterval qualifiedInterval: Qualified range for continuous and ordinal observation results
    :param Reference validCodedValueSet: Value set of valid coded values for the observations conforming to this ObservationDefinition
    :param Reference normalCodedValueSet: Value set of normal coded values for the observations conforming to this ObservationDefinition
    :param Reference abnormalCodedValueSet: Value set of abnormal coded values for the observations conforming to this ObservationDefinition
    :param Reference criticalCodedValueSet: Value set of critical coded values for the observations conforming to this ObservationDefinition
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        "quantitativeDetails": {
            "class_name": "QuantitativeDetails",
            "is_contained": True,
        },
        "qualifiedInterval": {"class_name": "QualifiedInterval", "is_contained": True},
        "validCodedValueSet": {"class_name": "Reference", "is_contained": False},
        "normalCodedValueSet": {"class_name": "Reference", "is_contained": False},
        "abnormalCodedValueSet": {"class_name": "Reference", "is_contained": False},
        "criticalCodedValueSet": {"class_name": "Reference", "is_contained": False},
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
        category: list["CodeableConcept"] = None,
        code: "CodeableConcept" = None,
        identifier: list["Identifier"] = None,
        permittedDataType: list["str"] = None,
        multipleResultsAllowed: "bool" = None,
        method: "CodeableConcept" = None,
        preferredReportName: "str" = None,
        quantitativeDetails: "QuantitativeDetails" = None,
        qualifiedInterval: list["QualifiedInterval"] = None,
        validCodedValueSet: "Reference" = None,
        normalCodedValueSet: "Reference" = None,
        abnormalCodedValueSet: "Reference" = None,
        criticalCodedValueSet: "Reference" = None,
    ):
        self.resourceType = resourceType or "ObservationDefinition"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category or []
        self.code = code
        self.identifier = identifier or []
        self.permittedDataType = permittedDataType or []
        self.multipleResultsAllowed = multipleResultsAllowed
        self.method = method
        self.preferredReportName = preferredReportName
        self.quantitativeDetails = quantitativeDetails
        self.qualifiedInterval = qualifiedInterval or []
        self.validCodedValueSet = validCodedValueSet
        self.normalCodedValueSet = normalCodedValueSet
        self.abnormalCodedValueSet = abnormalCodedValueSet
        self.criticalCodedValueSet = criticalCodedValueSet

    @classmethod
    def from_dict(cls, data: dict) -> "ObservationDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ObservationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
