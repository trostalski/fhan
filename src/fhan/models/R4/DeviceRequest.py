"""
Generated class for DeviceRequest. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
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


class Parameter(BaseModel):
    """Specific parameters for the ordered item.  For example, the prism value for lenses.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Device detail
    :param CodeableConcept valueCodeableConcept: Value of detail
    :param Quantity valueQuantity: Value of detail
    :param Range valueRange: Value of detail
    :param bool valueBoolean: Value of detail
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "valueCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueRange": {"class_name": "Range", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        valueCodeableConcept: "CodeableConcept" = None,
        valueQuantity: "Quantity" = None,
        valueRange: "Range" = None,
        valueBoolean: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.valueCodeableConcept = valueCodeableConcept
        self.valueQuantity = valueQuantity
        self.valueRange = valueRange
        self.valueBoolean = valueBoolean

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DeviceRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DeviceRequest(DomainResource):
    """Represents a request for a patient to employ a medical device. The device may be an implantable device, or an external assistive device, such as a walker.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Request identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: What request fulfills
    :param Reference priorRequest: What request replaces
    :param Identifier groupIdentifier: Identifier of composite request
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param Reference codeReference: Device requested
    :param CodeableConcept codeCodeableConcept: Device requested
    :param Parameter parameter: Device details
    :param Reference subject: Focus of request
    :param Reference encounter: Encounter motivating request
    :param str occurrenceDateTime: Desired time or schedule for use
    :param Period occurrencePeriod: Desired time or schedule for use
    :param Timing occurrenceTiming: Desired time or schedule for use
    :param str authoredOn: When recorded
    :param Reference requester: Who/what is requesting diagnostics
    :param CodeableConcept performerType: Filler role
    :param Reference performer: Requested Filler
    :param CodeableConcept reasonCode: Coded Reason for request
    :param Reference reasonReference: Linked Reason for request
    :param Reference insurance: Associated insurance coverage
    :param Reference supportingInfo: Additional clinical information
    :param Annotation note: Notes or comments
    :param Reference relevantHistory: Request provenance
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
        "priorRequest": {"class_name": "Reference", "is_contained": False},
        "groupIdentifier": {"class_name": "Identifier", "is_contained": False},
        "codeReference": {"class_name": "Reference", "is_contained": False},
        "codeCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        "parameter": {"class_name": "Parameter", "is_contained": True},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        "requester": {"class_name": "Reference", "is_contained": False},
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
        priorRequest: list["Reference"] = None,
        groupIdentifier: "Identifier" = None,
        status: "str" = None,
        intent: "str" = None,
        priority: "str" = None,
        codeReference: "Reference" = None,
        codeCodeableConcept: "CodeableConcept" = None,
        parameter: list["Parameter"] = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        occurrenceDateTime: "str" = None,
        occurrencePeriod: "Period" = None,
        occurrenceTiming: "Timing" = None,
        authoredOn: "str" = None,
        requester: "Reference" = None,
        performerType: "CodeableConcept" = None,
        performer: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        insurance: list["Reference"] = None,
        supportingInfo: list["Reference"] = None,
        note: list["Annotation"] = None,
        relevantHistory: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "DeviceRequest"
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
        self.priorRequest = priorRequest or []
        self.groupIdentifier = groupIdentifier
        self.status = status
        self.intent = intent
        self.priority = priority
        self.codeReference = codeReference
        self.codeCodeableConcept = codeCodeableConcept
        self.parameter = parameter or []
        self.subject = subject
        self.encounter = encounter
        self.occurrenceDateTime = occurrenceDateTime
        self.occurrencePeriod = occurrencePeriod
        self.occurrenceTiming = occurrenceTiming
        self.authoredOn = authoredOn
        self.requester = requester
        self.performerType = performerType
        self.performer = performer
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.insurance = insurance or []
        self.supportingInfo = supportingInfo or []
        self.note = note or []
        self.relevantHistory = relevantHistory or []

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DeviceRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
