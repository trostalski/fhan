"""
Generated class for DeviceUseStatement. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class DeviceUseStatement(DomainResource):
    """A record of a device being used by a patient where the record is the result of a report from the patient or another clinician.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier for this record
    :param Reference basedOn: Fulfills plan, proposal or order
    :param str status: active | completed | entered-in-error +
    :param Reference subject: Patient using device
    :param Reference derivedFrom: Supporting information
    :param Timing timingTiming: How often  the device was used
    :param Period timingPeriod: How often  the device was used
    :param str timingDateTime: How often  the device was used
    :param str recordedOn: When statement was recorded
    :param Reference source: Who made the statement
    :param Reference device: Reference to device used
    :param CodeableConcept reasonCode: Why device was used
    :param Reference reasonReference: Why was DeviceUseStatement performed?
    :param CodeableConcept bodySite: Target body site
    :param Annotation note: Addition details (comments, instructions)
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
        "subject": {"class_name": "Reference", "is_contained": False},
        "derivedFrom": {"class_name": "Reference", "is_contained": False},
        "timingTiming": {"class_name": "Timing", "is_contained": False},
        "timingPeriod": {"class_name": "Period", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
        "device": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
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
        basedOn: list["Reference"] = None,
        status: "str" = None,
        subject: "Reference" = None,
        derivedFrom: list["Reference"] = None,
        timingTiming: "Timing" = None,
        timingPeriod: "Period" = None,
        timingDateTime: "str" = None,
        recordedOn: "str" = None,
        source: "Reference" = None,
        device: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        bodySite: "CodeableConcept" = None,
        note: list["Annotation"] = None,
    ):
        self.resourceType = resourceType or "DeviceUseStatement"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.basedOn = basedOn or []
        self.status = status
        self.subject = subject
        self.derivedFrom = derivedFrom or []
        self.timingTiming = timingTiming
        self.timingPeriod = timingPeriod
        self.timingDateTime = timingDateTime
        self.recordedOn = recordedOn
        self.source = source
        self.device = device
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.bodySite = bodySite
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceUseStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DeviceUseStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
