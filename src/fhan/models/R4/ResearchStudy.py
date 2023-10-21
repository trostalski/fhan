"""
Generated class for ResearchStudy. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Period import *
from fhan.models.R4.Meta import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Arm(BaseModel):
    """Describes an expected sequence of events for one of the participants of a study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out, follow-up.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for study arm
    :param CodeableConcept type: Categorization of study arm
    :param str description: Short explanation of study path
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        type: "CodeableConcept" = None,
        description: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.type = type
        self.description = description

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Objective(BaseModel):
    """A goal that the study is aiming to achieve in terms of a scientific question to be answered by the analysis of data collected during the study.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for the objective
    :param CodeableConcept type: primary | secondary | exploratory
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        type: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.type = type

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ResearchStudy(DomainResource):
    """A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge.  This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional and investigative techniques.  A ResearchStudy involves the gathering of information about human or animal subjects.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for study
    :param str title: Name for this study
    :param Reference protocol: Steps followed in executing study
    :param Reference partOf: Part of larger study
    :param str status: active | administratively-completed | approved | closed-to-accrual | closed-to-accrual-and-intervention | completed | disapproved | in-review | temporarily-closed-to-accrual | temporarily-closed-to-accrual-and-intervention | withdrawn
    :param CodeableConcept primaryPurposeType: treatment | prevention | diagnostic | supportive-care | screening | health-services-research | basic-science | device-feasibility
    :param CodeableConcept phase: n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | phase-2-phase-3 | phase-3 | phase-4
    :param CodeableConcept category: Classifications for the study
    :param CodeableConcept focus: Drugs, devices, etc. under study
    :param CodeableConcept condition: Condition being studied
    :param ContactDetail contact: Contact details for the study
    :param RelatedArtifact relatedArtifact: References and dependencies
    :param CodeableConcept keyword: Used to search for the study
    :param CodeableConcept location: Geographic region(s) for study
    :param str description: What this is study doing
    :param Reference enrollment: Inclusion & exclusion criteria
    :param Period period: When the study began and ended
    :param Reference sponsor: Organization that initiates and is legally responsible for the study
    :param Reference principalInvestigator: Researcher who oversees multiple aspects of the study
    :param Reference site: Facility where study activities are conducted
    :param CodeableConcept reasonStopped: accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-study-progress | temporarily-closed-per-study-design
    :param Annotation note: Comments made about the study
    :param Arm arm: Defined path through the study for a subject
    :param Objective objective: A goal for the study
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "protocol": {"class_name": "Reference", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "primaryPurposeType": {"class_name": "CodeableConcept", "is_contained": False},
        "phase": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "focus": {"class_name": "CodeableConcept", "is_contained": False},
        "condition": {"class_name": "CodeableConcept", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        "keyword": {"class_name": "CodeableConcept", "is_contained": False},
        "location": {"class_name": "CodeableConcept", "is_contained": False},
        "enrollment": {"class_name": "Reference", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "sponsor": {"class_name": "Reference", "is_contained": False},
        "principalInvestigator": {"class_name": "Reference", "is_contained": False},
        "site": {"class_name": "Reference", "is_contained": False},
        "reasonStopped": {"class_name": "CodeableConcept", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "arm": {"class_name": "Arm", "is_contained": True},
        "objective": {"class_name": "Objective", "is_contained": True},
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
        title: "str" = None,
        protocol: list["Reference"] = None,
        partOf: list["Reference"] = None,
        status: "str" = None,
        primaryPurposeType: "CodeableConcept" = None,
        phase: "CodeableConcept" = None,
        category: list["CodeableConcept"] = None,
        focus: list["CodeableConcept"] = None,
        condition: list["CodeableConcept"] = None,
        contact: list["ContactDetail"] = None,
        relatedArtifact: list["RelatedArtifact"] = None,
        keyword: list["CodeableConcept"] = None,
        location: list["CodeableConcept"] = None,
        description: "str" = None,
        enrollment: list["Reference"] = None,
        period: "Period" = None,
        sponsor: "Reference" = None,
        principalInvestigator: "Reference" = None,
        site: list["Reference"] = None,
        reasonStopped: "CodeableConcept" = None,
        note: list["Annotation"] = None,
        arm: list["Arm"] = None,
        objective: list["Objective"] = None,
    ):
        self.resourceType = resourceType or "ResearchStudy"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.title = title
        self.protocol = protocol or []
        self.partOf = partOf or []
        self.status = status
        self.primaryPurposeType = primaryPurposeType
        self.phase = phase
        self.category = category or []
        self.focus = focus or []
        self.condition = condition or []
        self.contact = contact or []
        self.relatedArtifact = relatedArtifact or []
        self.keyword = keyword or []
        self.location = location or []
        self.description = description
        self.enrollment = enrollment or []
        self.period = period
        self.sponsor = sponsor
        self.principalInvestigator = principalInvestigator
        self.site = site or []
        self.reasonStopped = reasonStopped
        self.note = note or []
        self.arm = arm or []
        self.objective = objective or []

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
