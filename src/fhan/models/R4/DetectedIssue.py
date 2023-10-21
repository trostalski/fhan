"""
Generated class for DetectedIssue. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Evidence(BaseModel):
    """Supporting evidence or manifestations that provide the basis for identifying the detected issue such as a GuidanceResponse or MeasureReport.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Manifestation
    :param Reference detail: Supporting information
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "detail": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: list["CodeableConcept"] = None,
        detail: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code or []
        self.detail = detail or []

    @classmethod
    def from_dict(cls, data: dict) -> "DetectedIssue":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DetectedIssue":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Mitigation(BaseModel):
    """Indicates an action that has been taken or is committed to reduce or eliminate the likelihood of the risk identified by the detected issue from manifesting.  Can also reflect an observation of known mitigating factors that may reduce/eliminate the need for any action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept action: What mitigation?
    :param str date: Date committed
    :param Reference author: Who is committing?
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "action": {"class_name": "CodeableConcept", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        action: "CodeableConcept" = None,
        date: "str" = None,
        author: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.action = action
        self.date = date
        self.author = author

    @classmethod
    def from_dict(cls, data: dict) -> "DetectedIssue":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DetectedIssue":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DetectedIssue(DomainResource):
    """Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique id for the detected issue
    :param str status: registered | preliminary | final | amended +
    :param CodeableConcept code: Issue Category, e.g. drug-drug, duplicate therapy, etc.
    :param str severity: high | moderate | low
    :param Reference patient: Associated patient
    :param str identifiedDateTime: When identified
    :param Period identifiedPeriod: When identified
    :param Reference author: The provider or device that identified the issue
    :param Reference implicated: Problem resource
    :param Evidence evidence: Supporting evidence
    :param str detail: Description and context
    :param str reference: Authority for issue
    :param Mitigation mitigation: Step taken to address
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "identifiedPeriod": {"class_name": "Period", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "implicated": {"class_name": "Reference", "is_contained": False},
        "evidence": {"class_name": "Evidence", "is_contained": True},
        "mitigation": {"class_name": "Mitigation", "is_contained": True},
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
        code: "CodeableConcept" = None,
        severity: "str" = None,
        patient: "Reference" = None,
        identifiedDateTime: "str" = None,
        identifiedPeriod: "Period" = None,
        author: "Reference" = None,
        implicated: list["Reference"] = None,
        evidence: list["Evidence"] = None,
        detail: "str" = None,
        reference: "str" = None,
        mitigation: list["Mitigation"] = None,
    ):
        self.resourceType = resourceType or "DetectedIssue"
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
        self.code = code
        self.severity = severity
        self.patient = patient
        self.identifiedDateTime = identifiedDateTime
        self.identifiedPeriod = identifiedPeriod
        self.author = author
        self.implicated = implicated or []
        self.evidence = evidence or []
        self.detail = detail
        self.reference = reference
        self.mitigation = mitigation or []

    @classmethod
    def from_dict(cls, data: dict) -> "DetectedIssue":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DetectedIssue":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
