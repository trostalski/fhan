"""
Generated class for ImmunizationRecommendation. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class DateCriterion(BaseModel):
    """Vaccine date recommendations.  For example, earliest date to administer, latest date to administer, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of date
    :param str value: Recommended date
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        value: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "ImmunizationRecommendation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImmunizationRecommendation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Recommendation(BaseModel):
    """Vaccine administration recommendations.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept vaccineCode: Vaccine  or vaccine group recommendation applies to
    :param CodeableConcept targetDisease: Disease to be immunized against
    :param CodeableConcept contraindicatedVaccineCode: Vaccine which is contraindicated to fulfill the recommendation
    :param CodeableConcept forecastStatus: Vaccine recommendation status
    :param CodeableConcept forecastReason: Vaccine administration status reason
    :param DateCriterion dateCriterion: Dates governing proposed immunization
    :param str description: Protocol details
    :param str series: Name of vaccination series
    :param int doseNumberPositiveInt: Recommended dose number within series
    :param str doseNumberString: Recommended dose number within series
    :param int seriesDosesPositiveInt: Recommended number of doses for immunity
    :param str seriesDosesString: Recommended number of doses for immunity
    :param Reference supportingImmunization: Past immunizations supporting recommendation
    :param Reference supportingPatientInformation: Patient observations supporting recommendation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "vaccineCode": {"class_name": "CodeableConcept", "is_contained": False},
        "targetDisease": {"class_name": "CodeableConcept", "is_contained": False},
        "contraindicatedVaccineCode": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "forecastStatus": {"class_name": "CodeableConcept", "is_contained": False},
        "forecastReason": {"class_name": "CodeableConcept", "is_contained": False},
        "dateCriterion": {"class_name": "DateCriterion", "is_contained": True},
        "supportingImmunization": {"class_name": "Reference", "is_contained": False},
        "supportingPatientInformation": {
            "class_name": "Reference",
            "is_contained": False,
        },
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        vaccineCode: list["CodeableConcept"] = None,
        targetDisease: "CodeableConcept" = None,
        contraindicatedVaccineCode: list["CodeableConcept"] = None,
        forecastStatus: "CodeableConcept" = None,
        forecastReason: list["CodeableConcept"] = None,
        dateCriterion: list["DateCriterion"] = None,
        description: "str" = None,
        series: "str" = None,
        doseNumberPositiveInt: "int" = None,
        doseNumberString: "str" = None,
        seriesDosesPositiveInt: "int" = None,
        seriesDosesString: "str" = None,
        supportingImmunization: list["Reference"] = None,
        supportingPatientInformation: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.vaccineCode = vaccineCode or []
        self.targetDisease = targetDisease
        self.contraindicatedVaccineCode = contraindicatedVaccineCode or []
        self.forecastStatus = forecastStatus
        self.forecastReason = forecastReason or []
        self.dateCriterion = dateCriterion or []
        self.description = description
        self.series = series
        self.doseNumberPositiveInt = doseNumberPositiveInt
        self.doseNumberString = doseNumberString
        self.seriesDosesPositiveInt = seriesDosesPositiveInt
        self.seriesDosesString = seriesDosesString
        self.supportingImmunization = supportingImmunization or []
        self.supportingPatientInformation = supportingPatientInformation or []

    @classmethod
    def from_dict(cls, data: dict) -> "ImmunizationRecommendation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImmunizationRecommendation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ImmunizationRecommendation(DomainResource):
    """A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with optional supporting justification.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param Reference patient: Who this profile is for
    :param str date: Date recommendation(s) created
    :param Reference authority: Who is responsible for protocol
    :param Recommendation recommendation: Vaccine administration recommendations
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "authority": {"class_name": "Reference", "is_contained": False},
        "recommendation": {"class_name": "Recommendation", "is_contained": True},
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
        patient: "Reference" = None,
        date: "str" = None,
        authority: "Reference" = None,
        recommendation: list["Recommendation"] = None,
    ):
        self.resourceType = resourceType or "ImmunizationRecommendation"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.patient = patient
        self.date = date
        self.authority = authority
        self.recommendation = recommendation or []

    @classmethod
    def from_dict(cls, data: dict) -> "ImmunizationRecommendation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImmunizationRecommendation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
