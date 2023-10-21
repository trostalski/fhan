"""
Generated class for Observation. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Ratio import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class ReferenceRange(BaseModel):
    """Guidance on how to interpret the value by comparison to a normal or recommended range.  Multiple reference ranges are interpreted as an "OR".   In other words, to represent two distinct target populations, two `referenceRange` elements would be used.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity low: Low Range, if relevant
    :param Quantity high: High Range, if relevant
    :param CodeableConcept type: Reference range qualifier
    :param CodeableConcept appliesTo: Reference range population
    :param Range age: Applicable age range, if relevant
    :param str text: Text based reference range in an observation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "low": {"class_name": "Quantity", "is_contained": False},
        "high": {"class_name": "Quantity", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "appliesTo": {"class_name": "CodeableConcept", "is_contained": False},
        "age": {"class_name": "Range", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        low: "Quantity" = None,
        high: "Quantity" = None,
        type: "CodeableConcept" = None,
        appliesTo: list["CodeableConcept"] = None,
        age: "Range" = None,
        text: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.low = low
        self.high = high
        self.type = type
        self.appliesTo = appliesTo or []
        self.age = age
        self.text = text

    @classmethod
    def from_dict(cls, data: dict) -> "Observation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Observation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Component(BaseModel):
    """Some observations have multiple component observations.  These component observations are expressed as separate code value pairs that share the same attributes.  Examples include systolic and diastolic component observations for blood pressure measurement and multiple component observations for genetics observations.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of component observation (code / type)
    :param Quantity valueQuantity: Actual component result
    :param CodeableConcept valueCodeableConcept: Actual component result
    :param str valueString: Actual component result
    :param bool valueBoolean: Actual component result
    :param int valueInteger: Actual component result
    :param Range valueRange: Actual component result
    :param Ratio valueRatio: Actual component result
    :param SampledData valueSampledData: Actual component result
    :param str valueTime: Actual component result
    :param str valueDateTime: Actual component result
    :param Period valuePeriod: Actual component result
    :param CodeableConcept dataAbsentReason: Why the component result is missing
    :param CodeableConcept interpretation: High, low, normal, etc.
    :param ReferenceRange referenceRange: Provides guide for interpretation of component result
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "valueRange": {"class_name": "Range", "is_contained": False},
        "valueRatio": {"class_name": "Ratio", "is_contained": False},
        "valueSampledData": {"class_name": "SampledData", "is_contained": False},
        "valuePeriod": {"class_name": "Period", "is_contained": False},
        "dataAbsentReason": {"class_name": "CodeableConcept", "is_contained": False},
        "interpretation": {"class_name": "CodeableConcept", "is_contained": False},
        "referenceRange": {"class_name": "ReferenceRange", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        valueQuantity: "Quantity" = None,
        valueCodeableConcept: "CodeableConcept" = None,
        valueString: "str" = None,
        valueBoolean: "bool" = None,
        valueInteger: "int" = None,
        valueRange: "Range" = None,
        valueRatio: "Ratio" = None,
        valueSampledData: "SampledData" = None,
        valueTime: "str" = None,
        valueDateTime: "str" = None,
        valuePeriod: "Period" = None,
        dataAbsentReason: "CodeableConcept" = None,
        interpretation: list["CodeableConcept"] = None,
        referenceRange: list["ReferenceRange"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.valueQuantity = valueQuantity
        self.valueCodeableConcept = valueCodeableConcept
        self.valueString = valueString
        self.valueBoolean = valueBoolean
        self.valueInteger = valueInteger
        self.valueRange = valueRange
        self.valueRatio = valueRatio
        self.valueSampledData = valueSampledData
        self.valueTime = valueTime
        self.valueDateTime = valueDateTime
        self.valuePeriod = valuePeriod
        self.dataAbsentReason = dataAbsentReason
        self.interpretation = interpretation or []
        self.referenceRange = referenceRange or []

    @classmethod
    def from_dict(cls, data: dict) -> "Observation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Observation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Observation(DomainResource):
    """Measurements and simple assertions made about a patient, device or other subject.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for observation
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param str status: registered | preliminary | final | amended +
    :param CodeableConcept category: Classification of  type of observation
    :param CodeableConcept code: Type of observation (code / type)
    :param Reference subject: Who and/or what the observation is about
    :param Reference focus: What the observation is about, when it is not about the subject of record
    :param Reference encounter: Healthcare event during which this observation is made
    :param str effectiveDateTime: Clinically relevant time/time-period for observation
    :param Period effectivePeriod: Clinically relevant time/time-period for observation
    :param Timing effectiveTiming: Clinically relevant time/time-period for observation
    :param str effectiveInstant: Clinically relevant time/time-period for observation
    :param str issued: Date/Time this version was made available
    :param Reference performer: Who is responsible for the observation
    :param Quantity valueQuantity: Actual result
    :param CodeableConcept valueCodeableConcept: Actual result
    :param str valueString: Actual result
    :param bool valueBoolean: Actual result
    :param int valueInteger: Actual result
    :param Range valueRange: Actual result
    :param Ratio valueRatio: Actual result
    :param SampledData valueSampledData: Actual result
    :param str valueTime: Actual result
    :param str valueDateTime: Actual result
    :param Period valuePeriod: Actual result
    :param CodeableConcept dataAbsentReason: Why the result is missing
    :param CodeableConcept interpretation: High, low, normal, etc.
    :param Annotation note: Comments about the observation
    :param CodeableConcept bodySite: Observed body part
    :param CodeableConcept method: How it was done
    :param Reference specimen: Specimen used for this observation
    :param Reference device: (Measurement) Device
    :param ReferenceRange referenceRange: Provides guide for interpretation
    :param Reference hasMember: Related resource that belongs to the Observation group
    :param Reference derivedFrom: Related measurements the observation is made from
    :param Component component: Component results
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
        "partOf": {"class_name": "Reference", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "focus": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        "effectiveTiming": {"class_name": "Timing", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "valueRange": {"class_name": "Range", "is_contained": False},
        "valueRatio": {"class_name": "Ratio", "is_contained": False},
        "valueSampledData": {"class_name": "SampledData", "is_contained": False},
        "valuePeriod": {"class_name": "Period", "is_contained": False},
        "dataAbsentReason": {"class_name": "CodeableConcept", "is_contained": False},
        "interpretation": {"class_name": "CodeableConcept", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        "specimen": {"class_name": "Reference", "is_contained": False},
        "device": {"class_name": "Reference", "is_contained": False},
        "referenceRange": {"class_name": "ReferenceRange", "is_contained": True},
        "hasMember": {"class_name": "Reference", "is_contained": False},
        "derivedFrom": {"class_name": "Reference", "is_contained": False},
        "component": {"class_name": "Component", "is_contained": True},
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
        basedOn: list["Reference"] = None,
        partOf: list["Reference"] = None,
        status: "str" = None,
        category: list["CodeableConcept"] = None,
        code: "CodeableConcept" = None,
        subject: "Reference" = None,
        focus: list["Reference"] = None,
        encounter: "Reference" = None,
        effectiveDateTime: "str" = None,
        effectivePeriod: "Period" = None,
        effectiveTiming: "Timing" = None,
        effectiveInstant: "str" = None,
        issued: "str" = None,
        performer: list["Reference"] = None,
        valueQuantity: "Quantity" = None,
        valueCodeableConcept: "CodeableConcept" = None,
        valueString: "str" = None,
        valueBoolean: "bool" = None,
        valueInteger: "int" = None,
        valueRange: "Range" = None,
        valueRatio: "Ratio" = None,
        valueSampledData: "SampledData" = None,
        valueTime: "str" = None,
        valueDateTime: "str" = None,
        valuePeriod: "Period" = None,
        dataAbsentReason: "CodeableConcept" = None,
        interpretation: list["CodeableConcept"] = None,
        note: list["Annotation"] = None,
        bodySite: "CodeableConcept" = None,
        method: "CodeableConcept" = None,
        specimen: "Reference" = None,
        device: "Reference" = None,
        referenceRange: list["ReferenceRange"] = None,
        hasMember: list["Reference"] = None,
        derivedFrom: list["Reference"] = None,
        component: list["Component"] = None,
    ):
        self.resourceType = resourceType or "Observation"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.status = status
        self.category = category or []
        self.code = code
        self.subject = subject
        self.focus = focus or []
        self.encounter = encounter
        self.effectiveDateTime = effectiveDateTime
        self.effectivePeriod = effectivePeriod
        self.effectiveTiming = effectiveTiming
        self.effectiveInstant = effectiveInstant
        self.issued = issued
        self.performer = performer or []
        self.valueQuantity = valueQuantity
        self.valueCodeableConcept = valueCodeableConcept
        self.valueString = valueString
        self.valueBoolean = valueBoolean
        self.valueInteger = valueInteger
        self.valueRange = valueRange
        self.valueRatio = valueRatio
        self.valueSampledData = valueSampledData
        self.valueTime = valueTime
        self.valueDateTime = valueDateTime
        self.valuePeriod = valuePeriod
        self.dataAbsentReason = dataAbsentReason
        self.interpretation = interpretation or []
        self.note = note or []
        self.bodySite = bodySite
        self.method = method
        self.specimen = specimen
        self.device = device
        self.referenceRange = referenceRange or []
        self.hasMember = hasMember or []
        self.derivedFrom = derivedFrom or []
        self.component = component or []

    @classmethod
    def from_dict(cls, data: dict) -> "Observation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Observation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
