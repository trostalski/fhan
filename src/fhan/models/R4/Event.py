"""
Generated class for Event. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Element import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import BaseModel


class Performer(BaseModel):
    """Indicates who or what performed the {{title}} and how they were involved.:param CodeableConcept function: Type of performance
    :param Reference actor: Who performed {{title}}
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        function: "CodeableConcept" = None,
        actor: "Reference" = None,
    ):
        self.function = function
        self.actor = actor

    @classmethod
    def from_dict(cls, data: dict) -> "Event":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Event":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Event(BaseModel):
    """Logical Model: A pattern to be followed by resources that represent the performance of some activity, possibly in accordance with a request or service definition.
    :param Identifier identifier: Business Identifier for {{title}}
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param Reference researchStudy: Associated research study
    :param str status: preparation | in-progress | not-done | suspended | aborted | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept code: What was done
    :param Reference subject: Individual service was done for/to
    :param Reference encounter: Encounter created as part of
    :param str occurrenceDateTime: When {{title}} occurred/is occurring
    :param Period occurrencePeriod: When {{title}} occurred/is occurring
    :param Timing occurrenceTiming: When {{title}} occurred/is occurring
    :param str recorded: When {{title}} was first captured in the subject's record
    :param bool reportedBoolean: Reported rather than primary record
    :param Reference reportedReference: Reported rather than primary record
    :param Performer performer: Who performed {{title}} and what they did
    :param Reference location: Where {{title}} occurred
    :param CodeableConcept reasonCode: Why was {{title}} performed?
    :param Reference reasonReference: Why was {{title}} performed?
    :param Annotation note: Comments made about the event
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "researchStudy": {"class_name": "Reference", "is_contained": False},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        "reportedReference": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Performer", "is_contained": True},
        "location": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        identifier: list["Identifier"] = None,
        instantiatesCanonical: list["str"] = None,
        instantiatesUri: list["str"] = None,
        basedOn: list["Reference"] = None,
        partOf: list["Reference"] = None,
        researchStudy: list["Reference"] = None,
        status: "str" = None,
        statusReason: "CodeableConcept" = None,
        code: "CodeableConcept" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        occurrenceDateTime: "str" = None,
        occurrencePeriod: "Period" = None,
        occurrenceTiming: "Timing" = None,
        recorded: "str" = None,
        reportedBoolean: "bool" = None,
        reportedReference: "Reference" = None,
        performer: list["Performer"] = None,
        location: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        note: list["Annotation"] = None,
    ):
        self.resourceType = resourceType or "Event"
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.researchStudy = researchStudy or []
        self.status = status
        self.statusReason = statusReason
        self.code = code
        self.subject = subject
        self.encounter = encounter
        self.occurrenceDateTime = occurrenceDateTime
        self.occurrencePeriod = occurrencePeriod
        self.occurrenceTiming = occurrenceTiming
        self.recorded = recorded
        self.reportedBoolean = reportedBoolean
        self.reportedReference = reportedReference
        self.performer = performer or []
        self.location = location
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "Event":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Event":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
