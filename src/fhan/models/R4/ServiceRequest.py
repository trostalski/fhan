"""
Generated class for ServiceRequest. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Ratio import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
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


class ServiceRequest(DomainResource):
    """A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers assigned to this order
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: What request fulfills
    :param Reference replaces: What request replaces
    :param Identifier requisition: Composite Request ID
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param CodeableConcept category: Classification of service
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if service/procedure should not be performed
    :param CodeableConcept code: What is being requested/ordered
    :param CodeableConcept orderDetail: Additional order information
    :param Quantity quantityQuantity: Service amount
    :param Ratio quantityRatio: Service amount
    :param Range quantityRange: Service amount
    :param Reference subject: Individual or Entity the service is ordered for
    :param Reference encounter: Encounter in which the request was created
    :param str occurrenceDateTime: When service should occur
    :param Period occurrencePeriod: When service should occur
    :param Timing occurrenceTiming: When service should occur
    :param bool asNeededBoolean: Preconditions for service
    :param CodeableConcept asNeededCodeableConcept: Preconditions for service
    :param str authoredOn: Date request signed
    :param Reference requester: Who/what is requesting service
    :param CodeableConcept performerType: Performer role
    :param Reference performer: Requested performer
    :param CodeableConcept locationCode: Requested location
    :param Reference locationReference: Requested location
    :param CodeableConcept reasonCode: Explanation/Justification for procedure or service
    :param Reference reasonReference: Explanation/Justification for service or service
    :param Reference insurance: Associated insurance coverage
    :param Reference supportingInfo: Additional clinical information
    :param Reference specimen: Procedure Samples
    :param CodeableConcept bodySite: Location on Body
    :param Annotation note: Comments
    :param str patientInstruction: Patient or consumer-oriented instructions
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
        "replaces": {"class_name": "Reference", "is_contained": False},
        "requisition": {"class_name": "Identifier", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "orderDetail": {"class_name": "CodeableConcept", "is_contained": False},
        "quantityQuantity": {"class_name": "Quantity", "is_contained": False},
        "quantityRatio": {"class_name": "Ratio", "is_contained": False},
        "quantityRange": {"class_name": "Range", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        "asNeededCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "requester": {"class_name": "Reference", "is_contained": False},
        "performerType": {"class_name": "CodeableConcept", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "locationCode": {"class_name": "CodeableConcept", "is_contained": False},
        "locationReference": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "insurance": {"class_name": "Reference", "is_contained": False},
        "supportingInfo": {"class_name": "Reference", "is_contained": False},
        "specimen": {"class_name": "Reference", "is_contained": False},
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
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
        replaces: list["Reference"] = None,
        requisition: "Identifier" = None,
        status: "str" = None,
        intent: "str" = None,
        category: list["CodeableConcept"] = None,
        priority: "str" = None,
        doNotPerform: "bool" = None,
        code: "CodeableConcept" = None,
        orderDetail: list["CodeableConcept"] = None,
        quantityQuantity: "Quantity" = None,
        quantityRatio: "Ratio" = None,
        quantityRange: "Range" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        occurrenceDateTime: "str" = None,
        occurrencePeriod: "Period" = None,
        occurrenceTiming: "Timing" = None,
        asNeededBoolean: "bool" = None,
        asNeededCodeableConcept: "CodeableConcept" = None,
        authoredOn: "str" = None,
        requester: "Reference" = None,
        performerType: "CodeableConcept" = None,
        performer: list["Reference"] = None,
        locationCode: list["CodeableConcept"] = None,
        locationReference: list["Reference"] = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        insurance: list["Reference"] = None,
        supportingInfo: list["Reference"] = None,
        specimen: list["Reference"] = None,
        bodySite: list["CodeableConcept"] = None,
        note: list["Annotation"] = None,
        patientInstruction: "str" = None,
        relevantHistory: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "ServiceRequest"
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
        self.requisition = requisition
        self.status = status
        self.intent = intent
        self.category = category or []
        self.priority = priority
        self.doNotPerform = doNotPerform
        self.code = code
        self.orderDetail = orderDetail or []
        self.quantityQuantity = quantityQuantity
        self.quantityRatio = quantityRatio
        self.quantityRange = quantityRange
        self.subject = subject
        self.encounter = encounter
        self.occurrenceDateTime = occurrenceDateTime
        self.occurrencePeriod = occurrencePeriod
        self.occurrenceTiming = occurrenceTiming
        self.asNeededBoolean = asNeededBoolean
        self.asNeededCodeableConcept = asNeededCodeableConcept
        self.authoredOn = authoredOn
        self.requester = requester
        self.performerType = performerType
        self.performer = performer or []
        self.locationCode = locationCode or []
        self.locationReference = locationReference or []
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.insurance = insurance or []
        self.supportingInfo = supportingInfo or []
        self.specimen = specimen or []
        self.bodySite = bodySite or []
        self.note = note or []
        self.patientInstruction = patientInstruction
        self.relevantHistory = relevantHistory or []

    @classmethod
    def from_dict(cls, data: dict) -> "ServiceRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ServiceRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
