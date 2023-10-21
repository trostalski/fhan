"""
Generated class for AdverseEvent. 
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


class Causality(BaseModel):
    """Information on the possible cause of the event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept assessment: Assessment of if the entity caused the event
    :param str productRelatedness: AdverseEvent.suspectEntity.causalityProductRelatedness
    :param Reference author: AdverseEvent.suspectEntity.causalityAuthor
    :param CodeableConcept method: ProbabilityScale | Bayesian | Checklist
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "assessment": {"class_name": "CodeableConcept", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "method": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        assessment: "CodeableConcept" = None,
        productRelatedness: "str" = None,
        author: "Reference" = None,
        method: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.assessment = assessment
        self.productRelatedness = productRelatedness
        self.author = author
        self.method = method

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SuspectEntity(BaseModel):
    """Describes the entity that is suspected to have caused the adverse event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference instance: Refers to the specific entity that caused the adverse event
    :param Causality causality: Information on the possible cause of the event
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "instance": {"class_name": "Reference", "is_contained": False},
        "causality": {"class_name": "Causality", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        instance: "Reference" = None,
        causality: list["Causality"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.instance = instance
        self.causality = causality or []

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AdverseEvent(DomainResource):
    """Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the event
    :param str actuality: actual | potential
    :param CodeableConcept category: product-problem | product-quality | product-use-error | wrong-dose | incorrect-prescribing-information | wrong-technique | wrong-route-of-administration | wrong-rate | wrong-duration | wrong-time | expired-drug | medical-device-use-error | problem-different-manufacturer | unsafe-physical-environment
    :param CodeableConcept event: Type of the event itself in relation to the subject
    :param Reference subject: Subject impacted by event
    :param Reference encounter: Encounter created as part of
    :param str date: When the event occurred
    :param str detected: When the event was detected
    :param str recordedDate: When the event was recorded
    :param Reference resultingCondition: Effect on the subject due to this event
    :param Reference location: Location where adverse event occurred
    :param CodeableConcept seriousness: Seriousness of the event
    :param CodeableConcept severity: mild | moderate | severe
    :param CodeableConcept outcome: resolved | recovering | ongoing | resolvedWithSequelae | fatal | unknown
    :param Reference recorder: Who recorded the adverse event
    :param Reference contributor: Who  was involved in the adverse event or the potential adverse event
    :param SuspectEntity suspectEntity: The suspected agent causing the adverse event
    :param Reference subjectMedicalHistory: AdverseEvent.subjectMedicalHistory
    :param Reference referenceDocument: AdverseEvent.referenceDocument
    :param Reference study: AdverseEvent.study
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "event": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "resultingCondition": {"class_name": "Reference", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "seriousness": {"class_name": "CodeableConcept", "is_contained": False},
        "severity": {"class_name": "CodeableConcept", "is_contained": False},
        "outcome": {"class_name": "CodeableConcept", "is_contained": False},
        "recorder": {"class_name": "Reference", "is_contained": False},
        "contributor": {"class_name": "Reference", "is_contained": False},
        "suspectEntity": {"class_name": "SuspectEntity", "is_contained": True},
        "subjectMedicalHistory": {"class_name": "Reference", "is_contained": False},
        "referenceDocument": {"class_name": "Reference", "is_contained": False},
        "study": {"class_name": "Reference", "is_contained": False},
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
        identifier: "Identifier" = None,
        actuality: "str" = None,
        category: list["CodeableConcept"] = None,
        event: "CodeableConcept" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        date: "str" = None,
        detected: "str" = None,
        recordedDate: "str" = None,
        resultingCondition: list["Reference"] = None,
        location: "Reference" = None,
        seriousness: "CodeableConcept" = None,
        severity: "CodeableConcept" = None,
        outcome: "CodeableConcept" = None,
        recorder: "Reference" = None,
        contributor: list["Reference"] = None,
        suspectEntity: list["SuspectEntity"] = None,
        subjectMedicalHistory: list["Reference"] = None,
        referenceDocument: list["Reference"] = None,
        study: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "AdverseEvent"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.actuality = actuality
        self.category = category or []
        self.event = event
        self.subject = subject
        self.encounter = encounter
        self.date = date
        self.detected = detected
        self.recordedDate = recordedDate
        self.resultingCondition = resultingCondition or []
        self.location = location
        self.seriousness = seriousness
        self.severity = severity
        self.outcome = outcome
        self.recorder = recorder
        self.contributor = contributor or []
        self.suspectEntity = suspectEntity or []
        self.subjectMedicalHistory = subjectMedicalHistory or []
        self.referenceDocument = referenceDocument or []
        self.study = study or []

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "AdverseEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
