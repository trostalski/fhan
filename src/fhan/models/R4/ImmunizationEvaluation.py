"""
Generated class for ImmunizationEvaluation. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class ImmunizationEvaluation(DomainResource):
    """Describes a comparison of an immunization event against published recommendations to determine if the administration is "valid" in relation to those  recommendations.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str status: completed | entered-in-error
    :param Reference patient: Who this evaluation is for
    :param str date: Date evaluation was performed
    :param Reference authority: Who is responsible for publishing the recommendations
    :param CodeableConcept targetDisease: Evaluation target disease
    :param Reference immunizationEvent: Immunization being evaluated
    :param CodeableConcept doseStatus: Status of the dose relative to published recommendations
    :param CodeableConcept doseStatusReason: Reason for the dose status
    :param str description: Evaluation notes
    :param str series: Name of vaccine series
    :param int doseNumberPositiveInt: Dose number within series
    :param str doseNumberString: Dose number within series
    :param int seriesDosesPositiveInt: Recommended number of doses for immunity
    :param str seriesDosesString: Recommended number of doses for immunity
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
        "targetDisease": {"class_name": "CodeableConcept", "is_contained": False},
        "immunizationEvent": {"class_name": "Reference", "is_contained": False},
        "doseStatus": {"class_name": "CodeableConcept", "is_contained": False},
        "doseStatusReason": {"class_name": "CodeableConcept", "is_contained": False},
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
        status: "str" = None,
        patient: "Reference" = None,
        date: "str" = None,
        authority: "Reference" = None,
        targetDisease: "CodeableConcept" = None,
        immunizationEvent: "Reference" = None,
        doseStatus: "CodeableConcept" = None,
        doseStatusReason: list["CodeableConcept"] = None,
        description: "str" = None,
        series: "str" = None,
        doseNumberPositiveInt: "int" = None,
        doseNumberString: "str" = None,
        seriesDosesPositiveInt: "int" = None,
        seriesDosesString: "str" = None,
    ):
        self.resourceType = resourceType or "ImmunizationEvaluation"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status
        self.patient = patient
        self.date = date
        self.authority = authority
        self.targetDisease = targetDisease
        self.immunizationEvent = immunizationEvent
        self.doseStatus = doseStatus
        self.doseStatusReason = doseStatusReason or []
        self.description = description
        self.series = series
        self.doseNumberPositiveInt = doseNumberPositiveInt
        self.doseNumberString = doseNumberString
        self.seriesDosesPositiveInt = seriesDosesPositiveInt
        self.seriesDosesString = seriesDosesString

    @classmethod
    def from_dict(cls, data: dict) -> "ImmunizationEvaluation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImmunizationEvaluation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
