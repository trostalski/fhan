"""
Generated class for ClinicalImpression. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Investigation(BaseModel):
    """One or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomes.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: A name/code for the set
    :param Reference item: Record of a specific investigation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "item": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        item: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.item = item or []

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalImpression":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClinicalImpression":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Finding(BaseModel):
    """Specific findings or diagnoses that were considered likely or relevant to ongoing treatment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept itemCodeableConcept: What was found
    :param Reference itemReference: What was found
    :param str basis: Which investigations support finding
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "itemCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        "itemReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        itemCodeableConcept: "CodeableConcept" = None,
        itemReference: "Reference" = None,
        basis: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemCodeableConcept = itemCodeableConcept
        self.itemReference = itemReference
        self.basis = basis

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalImpression":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClinicalImpression":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ClinicalImpression(DomainResource):
    """A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient's condition. Assessments are often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the recording of assessment tools such as Apgar score.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str status: in-progress | completed | entered-in-error
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept code: Kind of assessment performed
    :param str description: Why/how the assessment was performed
    :param Reference subject: Patient or group assessed
    :param Reference encounter: Encounter created as part of
    :param str effectiveDateTime: Time of assessment
    :param Period effectivePeriod: Time of assessment
    :param str date: When the assessment was documented
    :param Reference assessor: The clinician performing the assessment
    :param Reference previous: Reference to last assessment
    :param Reference problem: Relevant impressions of patient state
    :param Investigation investigation: One or more sets of investigations (signs, symptoms, etc.)
    :param str protocol: Clinical Protocol followed
    :param str summary: Summary of the assessment
    :param Finding finding: Possible or likely findings and diagnoses
    :param CodeableConcept prognosisCodeableConcept: Estimate of likely outcome
    :param Reference prognosisReference: RiskAssessment expressing likely outcome
    :param Reference supportingInfo: Information supporting the clinical impression
    :param Annotation note: Comments made about the ClinicalImpression
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        "assessor": {"class_name": "Reference", "is_contained": False},
        "previous": {"class_name": "Reference", "is_contained": False},
        "problem": {"class_name": "Reference", "is_contained": False},
        "investigation": {"class_name": "Investigation", "is_contained": True},
        "finding": {"class_name": "Finding", "is_contained": True},
        "prognosisCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "prognosisReference": {"class_name": "Reference", "is_contained": False},
        "supportingInfo": {"class_name": "Reference", "is_contained": False},
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
        status: "str" = None,
        statusReason: "CodeableConcept" = None,
        code: "CodeableConcept" = None,
        description: "str" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        effectiveDateTime: "str" = None,
        effectivePeriod: "Period" = None,
        date: "str" = None,
        assessor: "Reference" = None,
        previous: "Reference" = None,
        problem: list["Reference"] = None,
        investigation: list["Investigation"] = None,
        protocol: list["str"] = None,
        summary: "str" = None,
        finding: list["Finding"] = None,
        prognosisCodeableConcept: list["CodeableConcept"] = None,
        prognosisReference: list["Reference"] = None,
        supportingInfo: list["Reference"] = None,
        note: list["Annotation"] = None,
    ):
        self.resourceType = resourceType or "ClinicalImpression"
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
        self.statusReason = statusReason
        self.code = code
        self.description = description
        self.subject = subject
        self.encounter = encounter
        self.effectiveDateTime = effectiveDateTime
        self.effectivePeriod = effectivePeriod
        self.date = date
        self.assessor = assessor
        self.previous = previous
        self.problem = problem or []
        self.investigation = investigation or []
        self.protocol = protocol or []
        self.summary = summary
        self.finding = finding or []
        self.prognosisCodeableConcept = prognosisCodeableConcept or []
        self.prognosisReference = prognosisReference or []
        self.supportingInfo = supportingInfo or []
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalImpression":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClinicalImpression":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
