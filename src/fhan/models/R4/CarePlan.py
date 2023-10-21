"""
Generated class for CarePlan. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
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


class Detail(BaseModel):
    """A simple summary of a planned activity suitable for a general care plan system (e.g. form driven) that doesn't know about specific resources such as procedure etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str kind: Appointment | CommunicationRequest | DeviceRequest | MedicationRequest | NutritionOrder | Task | ServiceRequest | VisionPrescription
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param CodeableConcept code: Detail type of activity
    :param CodeableConcept reasonCode: Why activity should be done or why activity was prohibited
    :param Reference reasonReference: Why activity is needed
    :param Reference goal: Goals this activity relates to
    :param str status: not-started | scheduled | in-progress | on-hold | completed | cancelled | stopped | unknown | entered-in-error
    :param CodeableConcept statusReason: Reason for current status
    :param bool doNotPerform: If true, activity is prohibiting action
    :param Timing scheduledTiming: When activity is to occur
    :param Period scheduledPeriod: When activity is to occur
    :param str scheduledString: When activity is to occur
    :param Reference location: Where it should happen
    :param Reference performer: Who will be responsible?
    :param CodeableConcept productCodeableConcept: What is to be administered/supplied
    :param Reference productReference: What is to be administered/supplied
    :param Quantity dailyAmount: How to consume/day?
    :param Quantity quantity: How much to administer/supply/consume
    :param str description: Extra info describing activity to perform
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "goal": {"class_name": "Reference", "is_contained": False},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "scheduledTiming": {"class_name": "Timing", "is_contained": False},
        "scheduledPeriod": {"class_name": "Period", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "productCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "productReference": {"class_name": "Reference", "is_contained": False},
        "dailyAmount": {"class_name": "Quantity", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        kind: "str" = None,
        instantiatesCanonical: list["str"] = None,
        instantiatesUri: list["str"] = None,
        code: "CodeableConcept" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        goal: list["Reference"] = None,
        status: "str" = None,
        statusReason: "CodeableConcept" = None,
        doNotPerform: "bool" = None,
        scheduledTiming: "Timing" = None,
        scheduledPeriod: "Period" = None,
        scheduledString: "str" = None,
        location: "Reference" = None,
        performer: list["Reference"] = None,
        productCodeableConcept: "CodeableConcept" = None,
        productReference: "Reference" = None,
        dailyAmount: "Quantity" = None,
        quantity: "Quantity" = None,
        description: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.kind = kind
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.code = code
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.goal = goal or []
        self.status = status
        self.statusReason = statusReason
        self.doNotPerform = doNotPerform
        self.scheduledTiming = scheduledTiming
        self.scheduledPeriod = scheduledPeriod
        self.scheduledString = scheduledString
        self.location = location
        self.performer = performer or []
        self.productCodeableConcept = productCodeableConcept
        self.productReference = productReference
        self.dailyAmount = dailyAmount
        self.quantity = quantity
        self.description = description

    @classmethod
    def from_dict(cls, data: dict) -> "CarePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CarePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Activity(BaseModel):
    """Identifies a planned action to occur as part of the plan.  For example, a medication to be used, lab tests to perform, self-monitoring, education, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept outcomeCodeableConcept: Results of the activity
    :param Reference outcomeReference: Appointment, Encounter, Procedure, etc.
    :param Annotation progress: Comments about the activity status/progress
    :param Reference reference: Activity details defined in specific resource
    :param Detail detail: In-line definition of activity
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "outcomeCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "outcomeReference": {"class_name": "Reference", "is_contained": False},
        "progress": {"class_name": "Annotation", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
        "detail": {"class_name": "Detail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        outcomeCodeableConcept: list["CodeableConcept"] = None,
        outcomeReference: list["Reference"] = None,
        progress: list["Annotation"] = None,
        reference: "Reference" = None,
        detail: "Detail" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.outcomeCodeableConcept = outcomeCodeableConcept or []
        self.outcomeReference = outcomeReference or []
        self.progress = progress or []
        self.reference = reference
        self.detail = detail

    @classmethod
    def from_dict(cls, data: dict) -> "CarePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CarePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CarePlan(DomainResource):
    """Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this plan
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfills CarePlan
    :param Reference replaces: CarePlan replaced by this CarePlan
    :param Reference partOf: Part of referenced CarePlan
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | order | option
    :param CodeableConcept category: Type of plan
    :param str title: Human-friendly name for the care plan
    :param str description: Summary of nature of plan
    :param Reference subject: Who the care plan is for
    :param Reference encounter: Encounter created as part of
    :param Period period: Time period plan covers
    :param str created: Date record was first recorded
    :param Reference author: Who is the designated responsible party
    :param Reference contributor: Who provided the content of the care plan
    :param Reference careTeam: Who's involved in plan?
    :param Reference addresses: Health issues this plan addresses
    :param Reference supportingInfo: Information considered as part of plan
    :param Reference goal: Desired outcome of plan
    :param Activity activity: Action to occur as part of plan
    :param Annotation note: Comments about the plan
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
        "replaces": {"class_name": "Reference", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "contributor": {"class_name": "Reference", "is_contained": False},
        "careTeam": {"class_name": "Reference", "is_contained": False},
        "addresses": {"class_name": "Reference", "is_contained": False},
        "supportingInfo": {"class_name": "Reference", "is_contained": False},
        "goal": {"class_name": "Reference", "is_contained": False},
        "activity": {"class_name": "Activity", "is_contained": True},
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
        instantiatesCanonical: list["str"] = None,
        instantiatesUri: list["str"] = None,
        basedOn: list["Reference"] = None,
        replaces: list["Reference"] = None,
        partOf: list["Reference"] = None,
        status: "str" = None,
        intent: "str" = None,
        category: list["CodeableConcept"] = None,
        title: "str" = None,
        description: "str" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        period: "Period" = None,
        created: "str" = None,
        author: "Reference" = None,
        contributor: list["Reference"] = None,
        careTeam: list["Reference"] = None,
        addresses: list["Reference"] = None,
        supportingInfo: list["Reference"] = None,
        goal: list["Reference"] = None,
        activity: list["Activity"] = None,
        note: list["Annotation"] = None,
    ):
        self.resourceType = resourceType or "CarePlan"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.basedOn = basedOn or []
        self.replaces = replaces or []
        self.partOf = partOf or []
        self.status = status
        self.intent = intent
        self.category = category or []
        self.title = title
        self.description = description
        self.subject = subject
        self.encounter = encounter
        self.period = period
        self.created = created
        self.author = author
        self.contributor = contributor or []
        self.careTeam = careTeam or []
        self.addresses = addresses or []
        self.supportingInfo = supportingInfo or []
        self.goal = goal or []
        self.activity = activity or []
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "CarePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CarePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
