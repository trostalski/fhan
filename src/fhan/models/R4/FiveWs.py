"""
Generated class for FiveWs. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import BaseModel


class FiveWs(BaseModel):
    """Logical Model: Who What When Where Why - Common pattern for all resources that deals with attribution.
    :param Identifier identifier: Business Identifier
    :param str version: Identifier for this version
    :param str status: Status Field
    :param CodeableConcept _class: Classifier Field
    :param CodeableConcept grade: A field that indicates the potential impact of the content of the resource
    :param CodeableConcept whatCodeableConcept: What this resource is about
    :param Reference whatReference: What this resource is about
    :param Reference subject: Who this resource is about
    :param Reference context: Context for the work described in this resource
    :param str init: When the work described in this resource was started (or will be)
    :param Timing planned: When this resource is planned to occur
    :param str doneDateTime: When the work described in this resource was completed (or will be)
    :param Period donePeriod: When the work described in this resource was completed (or will be)
    :param str recorded: When this resource itself was created
    :param Reference author: Who authored the content of the resource
    :param Reference source: Who provided the information in this resource
    :param Reference actor: Who did the work described the resource (or will do)
    :param Reference cause: Who prompted the work described in the resource
    :param Reference witness: Who attests to the content of the resource (individual or org)
    :param Reference who: An actor involved in the work described by this resource
    :param CodeableConcept whereCodeableConcept: The location of the work described
    :param Reference whereReference: The location of the work described
    :param CodeableConcept whyCodeableConcept: Why this work was done
    :param Reference whyReference: Why this work was done
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "_class": {"class_name": "CodeableConcept", "is_contained": False},
        "grade": {"class_name": "CodeableConcept", "is_contained": False},
        "whatCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        "whatReference": {"class_name": "Reference", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "context": {"class_name": "Reference", "is_contained": False},
        "planned": {"class_name": "Timing", "is_contained": False},
        "donePeriod": {"class_name": "Period", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
        "cause": {"class_name": "Reference", "is_contained": False},
        "witness": {"class_name": "Reference", "is_contained": False},
        "who": {"class_name": "Reference", "is_contained": False},
        "whereCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "whereReference": {"class_name": "Reference", "is_contained": False},
        "whyCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        "whyReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        identifier: list["Identifier"] = None,
        version: "str" = None,
        status: "str" = None,
        _class: list["CodeableConcept"] = None,
        grade: "CodeableConcept" = None,
        whatCodeableConcept: "CodeableConcept" = None,
        whatReference: "Reference" = None,
        subject: list["Reference"] = None,
        context: "Reference" = None,
        init: "str" = None,
        planned: list["Timing"] = None,
        doneDateTime: "str" = None,
        donePeriod: "Period" = None,
        recorded: "str" = None,
        author: list["Reference"] = None,
        source: list["Reference"] = None,
        actor: list["Reference"] = None,
        cause: list["Reference"] = None,
        witness: list["Reference"] = None,
        who: list["Reference"] = None,
        whereCodeableConcept: list["CodeableConcept"] = None,
        whereReference: list["Reference"] = None,
        whyCodeableConcept: list["CodeableConcept"] = None,
        whyReference: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "FiveWs"
        self.identifier = identifier or []
        self.version = version
        self.status = status
        self._class = _class or []
        self.grade = grade
        self.whatCodeableConcept = whatCodeableConcept
        self.whatReference = whatReference
        self.subject = subject or []
        self.context = context
        self.init = init
        self.planned = planned or []
        self.doneDateTime = doneDateTime
        self.donePeriod = donePeriod
        self.recorded = recorded
        self.author = author or []
        self.source = source or []
        self.actor = actor or []
        self.cause = cause or []
        self.witness = witness or []
        self.who = who or []
        self.whereCodeableConcept = whereCodeableConcept or []
        self.whereReference = whereReference or []
        self.whyCodeableConcept = whyCodeableConcept or []
        self.whyReference = whyReference or []

    @classmethod
    def from_dict(cls, data: dict) -> "FiveWs":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "FiveWs":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
