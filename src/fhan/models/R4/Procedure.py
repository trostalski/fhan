"""
Generated class for Procedure. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Age import *
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


class Performer(BaseModel):
    """Limited to "real" people rather than equipment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: The reference to the practitioner
    :param Reference onBehalfOf: Organization the device or practitioner was acting for
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
        "onBehalfOf": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        function: "CodeableConcept" = None,
        actor: "Reference" = None,
        onBehalfOf: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function
        self.actor = actor
        self.onBehalfOf = onBehalfOf

    @classmethod
    def from_dict(cls, data: dict) -> "Procedure":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Procedure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class FocalDevice(BaseModel):
    """A device that is implanted, removed or otherwise manipulated (calibration, battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a focal portion of the Procedure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept action: Kind of change to device
    :param Reference manipulated: Device that was changed
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "action": {"class_name": "CodeableConcept", "is_contained": False},
        "manipulated": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        action: "CodeableConcept" = None,
        manipulated: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.action = action
        self.manipulated = manipulated

    @classmethod
    def from_dict(cls, data: dict) -> "Procedure":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Procedure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Procedure(DomainResource):
    """An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Identifiers for this procedure
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: A request for this procedure
    :param Reference partOf: Part of referenced event
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept category: Classification of the procedure
    :param CodeableConcept code: Identification of the procedure
    :param Reference subject: Who the procedure was performed on
    :param Reference encounter: Encounter created as part of
    :param str performedDateTime: When the procedure was performed
    :param Period performedPeriod: When the procedure was performed
    :param str performedString: When the procedure was performed
    :param Age performedAge: When the procedure was performed
    :param Range performedRange: When the procedure was performed
    :param Reference recorder: Who recorded the procedure
    :param Reference asserter: Person who asserts this procedure
    :param Performer performer: The people who performed the procedure
    :param Reference location: Where the procedure happened
    :param CodeableConcept reasonCode: Coded reason procedure performed
    :param Reference reasonReference: The justification that the procedure was performed
    :param CodeableConcept bodySite: Target body sites
    :param CodeableConcept outcome: The result of procedure
    :param Reference report: Any report resulting from the procedure
    :param CodeableConcept complication: Complication following the procedure
    :param Reference complicationDetail: A condition that is a result of the procedure
    :param CodeableConcept followUp: Instructions for follow up
    :param Annotation note: Additional information about the procedure
    :param FocalDevice focalDevice: Manipulated, implanted, or removed device
    :param Reference usedReference: Items used during procedure
    :param CodeableConcept usedCode: Coded items used during the procedure
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
        "partOf": {"class_name": "Reference", "is_contained": False},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "performedPeriod": {"class_name": "Period", "is_contained": False},
        "performedAge": {"class_name": "Age", "is_contained": False},
        "performedRange": {"class_name": "Range", "is_contained": False},
        "recorder": {"class_name": "Reference", "is_contained": False},
        "asserter": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Performer", "is_contained": True},
        "location": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        "outcome": {"class_name": "CodeableConcept", "is_contained": False},
        "report": {"class_name": "Reference", "is_contained": False},
        "complication": {"class_name": "CodeableConcept", "is_contained": False},
        "complicationDetail": {"class_name": "Reference", "is_contained": False},
        "followUp": {"class_name": "CodeableConcept", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "focalDevice": {"class_name": "FocalDevice", "is_contained": True},
        "usedReference": {"class_name": "Reference", "is_contained": False},
        "usedCode": {"class_name": "CodeableConcept", "is_contained": False},
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
        partOf: list["Reference"] = None,
        status: "str" = None,
        statusReason: "CodeableConcept" = None,
        category: "CodeableConcept" = None,
        code: "CodeableConcept" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        performedDateTime: "str" = None,
        performedPeriod: "Period" = None,
        performedString: "str" = None,
        performedAge: "Age" = None,
        performedRange: "Range" = None,
        recorder: "Reference" = None,
        asserter: "Reference" = None,
        performer: list["Performer"] = None,
        location: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        bodySite: list["CodeableConcept"] = None,
        outcome: "CodeableConcept" = None,
        report: list["Reference"] = None,
        complication: list["CodeableConcept"] = None,
        complicationDetail: list["Reference"] = None,
        followUp: list["CodeableConcept"] = None,
        note: list["Annotation"] = None,
        focalDevice: list["FocalDevice"] = None,
        usedReference: list["Reference"] = None,
        usedCode: list["CodeableConcept"] = None,
    ):
        self.resourceType = resourceType or "Procedure"
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
        self.partOf = partOf or []
        self.status = status
        self.statusReason = statusReason
        self.category = category
        self.code = code
        self.subject = subject
        self.encounter = encounter
        self.performedDateTime = performedDateTime
        self.performedPeriod = performedPeriod
        self.performedString = performedString
        self.performedAge = performedAge
        self.performedRange = performedRange
        self.recorder = recorder
        self.asserter = asserter
        self.performer = performer or []
        self.location = location
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.bodySite = bodySite or []
        self.outcome = outcome
        self.report = report or []
        self.complication = complication or []
        self.complicationDetail = complicationDetail or []
        self.followUp = followUp or []
        self.note = note or []
        self.focalDevice = focalDevice or []
        self.usedReference = usedReference or []
        self.usedCode = usedCode or []

    @classmethod
    def from_dict(cls, data: dict) -> "Procedure":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Procedure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
