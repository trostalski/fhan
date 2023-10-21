"""
Generated class for MedicationAdministration. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Ratio import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Performer(BaseModel):
    """Indicates who or what performed the medication administration and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed the medication administration
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        function: "CodeableConcept" = None,
        actor: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function
        self.actor = actor

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationAdministration":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationAdministration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Dosage(BaseModel):
    """Describes the medication dosage information details e.g. dose, rate, site, route, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str text: Free text dosage instructions e.g. SIG
    :param CodeableConcept site: Body site administered to
    :param CodeableConcept route: Path of substance into body
    :param CodeableConcept method: How drug was administered
    :param Quantity dose: Amount of medication per dose
    :param Ratio rateRatio: Dose quantity per unit of time
    :param Quantity rateQuantity: Dose quantity per unit of time
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "site": {"class_name": "CodeableConcept", "is_contained": False},
        "route": {"class_name": "CodeableConcept", "is_contained": False},
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        "dose": {"class_name": "Quantity", "is_contained": False},
        "rateRatio": {"class_name": "Ratio", "is_contained": False},
        "rateQuantity": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        text: "str" = None,
        site: "CodeableConcept" = None,
        route: "CodeableConcept" = None,
        method: "CodeableConcept" = None,
        dose: "Quantity" = None,
        rateRatio: "Ratio" = None,
        rateQuantity: "Quantity" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.text = text
        self.site = site
        self.route = route
        self.method = method
        self.dose = dose
        self.rateRatio = rateRatio
        self.rateQuantity = rateQuantity

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationAdministration":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationAdministration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicationAdministration(DomainResource):
    """Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple as swallowing a tablet or it may be a long running infusion.  Related resources tie this event to the authorizing prescription, and the specific encounter between patient and health care practitioner.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param str instantiates: Instantiates protocol or definition
    :param Reference partOf: Part of referenced event
    :param str status: in-progress | not-done | on-hold | completed | entered-in-error | stopped | unknown
    :param CodeableConcept statusReason: Reason administration not performed
    :param CodeableConcept category: Type of medication usage
    :param CodeableConcept medicationCodeableConcept: What was administered
    :param Reference medicationReference: What was administered
    :param Reference subject: Who received medication
    :param Reference context: Encounter or Episode of Care administered as part of
    :param Reference supportingInformation: Additional information to support administration
    :param str effectiveDateTime: Start and end time of administration
    :param Period effectivePeriod: Start and end time of administration
    :param Performer performer: Who performed the medication administration and what they did
    :param CodeableConcept reasonCode: Reason administration performed
    :param Reference reasonReference: Condition or observation that supports why the medication was administered
    :param Reference request: Request administration performed against
    :param Reference device: Device used to administer
    :param Annotation note: Information about the administration
    :param Dosage dosage: Details of how medication was taken
    :param Reference eventHistory: A list of events of interest in the lifecycle
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "medicationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "medicationReference": {"class_name": "Reference", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "context": {"class_name": "Reference", "is_contained": False},
        "supportingInformation": {"class_name": "Reference", "is_contained": False},
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        "performer": {"class_name": "Performer", "is_contained": True},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "device": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "dosage": {"class_name": "Dosage", "is_contained": True},
        "eventHistory": {"class_name": "Reference", "is_contained": False},
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
        instantiates: list["str"] = None,
        partOf: list["Reference"] = None,
        status: "str" = None,
        statusReason: list["CodeableConcept"] = None,
        category: "CodeableConcept" = None,
        medicationCodeableConcept: "CodeableConcept" = None,
        medicationReference: "Reference" = None,
        subject: "Reference" = None,
        context: "Reference" = None,
        supportingInformation: list["Reference"] = None,
        effectiveDateTime: "str" = None,
        effectivePeriod: "Period" = None,
        performer: list["Performer"] = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        request: "Reference" = None,
        device: list["Reference"] = None,
        note: list["Annotation"] = None,
        dosage: "Dosage" = None,
        eventHistory: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "MedicationAdministration"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instantiates = instantiates or []
        self.partOf = partOf or []
        self.status = status
        self.statusReason = statusReason or []
        self.category = category
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference
        self.subject = subject
        self.context = context
        self.supportingInformation = supportingInformation or []
        self.effectiveDateTime = effectiveDateTime
        self.effectivePeriod = effectivePeriod
        self.performer = performer or []
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.request = request
        self.device = device or []
        self.note = note or []
        self.dosage = dosage
        self.eventHistory = eventHistory or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationAdministration":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationAdministration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
