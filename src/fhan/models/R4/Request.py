"""
Generated class for Request. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import BaseModel


class Request(BaseModel):
    """Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    :param Identifier identifier: Business Identifier for {{title}}
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference replaces: Request(s) replaced by this {{title}}
    :param Identifier groupIdentifier: Composite request this is part of
    :param str status: draft | active | suspended | cancelled | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param str intent: proposal | plan | order (immutable)
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: true if request is prohibiting action
    :param CodeableConcept code: What's being requested/ordered
    :param Reference subject: Individual the service is ordered/prohibited for
    :param Reference encounter: Encounter created as part of
    :param str occurrenceDateTime: When service should (not) occur
    :param Period occurrencePeriod: When service should (not) occur
    :param Timing occurrenceTiming: When service should (not) occur
    :param str authoredOn: When request was created/transitioned to active
    :param Reference requester: Who/what is requesting service
    :param bool reportedBoolean: Reported rather than primary record
    :param Reference reportedReference: Reported rather than primary record
    :param CodeableConcept performerType: Desired kind of service performer
    :param Reference performer: Specific desired (non)performer
    :param CodeableConcept reasonCode: Why is service (not) needed?
    :param Reference reasonReference: Why is service (not) needed?
    :param Reference insurance: Associated insurance coverage
    :param Reference supportingInfo: Extra information to use in performing request
    :param Annotation note: Comments made about {{title}}
    :param Reference relevantHistory: Key events in history of {{title}}
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "replaces": {"class_name": "Reference", "is_contained": False},
        "groupIdentifier": {"class_name": "Identifier", "is_contained": False},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        "requester": {"class_name": "Reference", "is_contained": False},
        "reportedReference": {"class_name": "Reference", "is_contained": False},
        "performerType": {"class_name": "CodeableConcept", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "insurance": {"class_name": "Reference", "is_contained": False},
        "supportingInfo": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "relevantHistory": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        identifier: list["Identifier"] = None,
        instantiatesCanonical: list["str"] = None,
        instantiatesUri: list["str"] = None,
        basedOn: list["Reference"] = None,
        replaces: list["Reference"] = None,
        groupIdentifier: "Identifier" = None,
        status: "str" = None,
        statusReason: "CodeableConcept" = None,
        intent: "str" = None,
        priority: "str" = None,
        doNotPerform: "bool" = None,
        code: "CodeableConcept" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        occurrenceDateTime: "str" = None,
        occurrencePeriod: "Period" = None,
        occurrenceTiming: "Timing" = None,
        authoredOn: "str" = None,
        requester: "Reference" = None,
        reportedBoolean: "bool" = None,
        reportedReference: "Reference" = None,
        performerType: "CodeableConcept" = None,
        performer: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        insurance: list["Reference"] = None,
        supportingInfo: list["Reference"] = None,
        note: list["Annotation"] = None,
        relevantHistory: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "Request"
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.basedOn = basedOn or []
        self.replaces = replaces or []
        self.groupIdentifier = groupIdentifier
        self.status = status
        self.statusReason = statusReason
        self.intent = intent
        self.priority = priority
        self.doNotPerform = doNotPerform
        self.code = code
        self.subject = subject
        self.encounter = encounter
        self.occurrenceDateTime = occurrenceDateTime
        self.occurrencePeriod = occurrencePeriod
        self.occurrenceTiming = occurrenceTiming
        self.authoredOn = authoredOn
        self.requester = requester
        self.reportedBoolean = reportedBoolean
        self.reportedReference = reportedReference
        self.performerType = performerType
        self.performer = performer
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.insurance = insurance or []
        self.supportingInfo = supportingInfo or []
        self.note = note or []
        self.relevantHistory = relevantHistory or []

    @classmethod
    def from_dict(cls, data: dict) -> "Request":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Request":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
