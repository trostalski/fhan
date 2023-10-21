"""
Generated class for RiskAssessment. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Prediction(BaseModel):
    """Describes the expected outcome for the subject.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept outcome: Possible outcome for the subject
    :param float probabilityDecimal: Likelihood of specified outcome
    :param Range probabilityRange: Likelihood of specified outcome
    :param CodeableConcept qualitativeRisk: Likelihood of specified outcome as a qualitative value
    :param float relativeRisk: Relative likelihood
    :param Period whenPeriod: Timeframe or age range
    :param Range whenRange: Timeframe or age range
    :param str rationale: Explanation of prediction
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "outcome": {"class_name": "CodeableConcept", "is_contained": False},
        "probabilityRange": {"class_name": "Range", "is_contained": False},
        "qualitativeRisk": {"class_name": "CodeableConcept", "is_contained": False},
        "whenPeriod": {"class_name": "Period", "is_contained": False},
        "whenRange": {"class_name": "Range", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        outcome: "CodeableConcept" = None,
        probabilityDecimal: "float" = None,
        probabilityRange: "Range" = None,
        qualitativeRisk: "CodeableConcept" = None,
        relativeRisk: "float" = None,
        whenPeriod: "Period" = None,
        whenRange: "Range" = None,
        rationale: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.outcome = outcome
        self.probabilityDecimal = probabilityDecimal
        self.probabilityRange = probabilityRange
        self.qualitativeRisk = qualitativeRisk
        self.relativeRisk = relativeRisk
        self.whenPeriod = whenPeriod
        self.whenRange = whenRange
        self.rationale = rationale

    @classmethod
    def from_dict(cls, data: dict) -> "RiskAssessment":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RiskAssessment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RiskAssessment(DomainResource):
    """An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier for the assessment
    :param Reference basedOn: Request fulfilled by this assessment
    :param Reference parent: Part of this occurrence
    :param str status: registered | preliminary | final | amended +
    :param CodeableConcept method: Evaluation mechanism
    :param CodeableConcept code: Type of assessment
    :param Reference subject: Who/what does assessment apply to?
    :param Reference encounter: Where was assessment performed?
    :param str occurrenceDateTime: When was assessment made?
    :param Period occurrencePeriod: When was assessment made?
    :param Reference condition: Condition assessed
    :param Reference performer: Who did assessment?
    :param CodeableConcept reasonCode: Why the assessment was necessary?
    :param Reference reasonReference: Why the assessment was necessary?
    :param Reference basis: Information used in assessment
    :param Prediction prediction: Outcome predicted
    :param str mitigation: How to reduce risk
    :param Annotation note: Comments on the risk assessment
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
        "parent": {"class_name": "Reference", "is_contained": False},
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        "condition": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "basis": {"class_name": "Reference", "is_contained": False},
        "prediction": {"class_name": "Prediction", "is_contained": True},
        "note": {"class_name": "Annotation", "is_contained": False},
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
        basedOn: "Reference" = None,
        parent: "Reference" = None,
        status: "str" = None,
        method: "CodeableConcept" = None,
        code: "CodeableConcept" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        occurrenceDateTime: "str" = None,
        occurrencePeriod: "Period" = None,
        condition: "Reference" = None,
        performer: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        basis: list["Reference"] = None,
        prediction: list["Prediction"] = None,
        mitigation: "str" = None,
        note: list["Annotation"] = None,
    ):
        self.resourceType = resourceType or "RiskAssessment"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.basedOn = basedOn
        self.parent = parent
        self.status = status
        self.method = method
        self.code = code
        self.subject = subject
        self.encounter = encounter
        self.occurrenceDateTime = occurrenceDateTime
        self.occurrencePeriod = occurrencePeriod
        self.condition = condition
        self.performer = performer
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.basis = basis or []
        self.prediction = prediction or []
        self.mitigation = mitigation
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "RiskAssessment":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RiskAssessment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
