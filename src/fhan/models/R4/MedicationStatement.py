"""
Generated class for MedicationStatement. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class MedicationStatement(DomainResource):
    """A record of a medication that is being consumed by a patient.   A MedicationStatement may indicate that the patient may be taking the medication now or has taken the medication in the past or will be taking the medication in the future.  The source of this information can be the patient, significant other (such as a family member or spouse), or a clinician.  A common scenario where this information is captured is during the history taking process during a patient visit or stay.   The medication information may come from sources such as the patient's memory, from a prescription bottle,  or from a list of medications the patient, clinician or other party maintains.

    The primary difference between a medication statement and a medication administration is that the medication administration has complete administration information and is based on actual administration information from the person who administered the medication.  A medication statement is often, if not always, less specific.  There is no required date/time when the medication was administered, in fact we only know that a source has reported the patient is taking this medication, where details such as time, quantity, or rate or even medication product may be incomplete or missing or less precise.  As stated earlier, the medication statement information may come from the patient's memory, from a prescription bottle or from a list of medications the patient, clinician or other party maintains.  Medication administration is more formal and is not missing detailed information.
        :param str id: Logical id of this artifact
        :param Meta meta: Metadata about the resource
        :param str implicitRules: A set of rules under which this content was created
        :param str language: Language of the resource content
        :param Narrative text: Text summary of the resource, for human interpretation
        :param Resource contained: Contained, inline Resources
        :param Extension extension: Additional content defined by implementations
        :param Extension modifierExtension: Extensions that cannot be ignored
        :param Identifier identifier: External identifier
        :param Reference basedOn: Fulfils plan, proposal or order
        :param Reference partOf: Part of referenced event
        :param str status: active | completed | entered-in-error | intended | stopped | on-hold | unknown | not-taken
        :param CodeableConcept statusReason: Reason for current status
        :param CodeableConcept category: Type of medication usage
        :param CodeableConcept medicationCodeableConcept: What medication was taken
        :param Reference medicationReference: What medication was taken
        :param Reference subject: Who is/was taking  the medication
        :param Reference context: Encounter / Episode associated with MedicationStatement
        :param str effectiveDateTime: The date/time or interval when the medication is/was/will be taken
        :param Period effectivePeriod: The date/time or interval when the medication is/was/will be taken
        :param str dateAsserted: When the statement was asserted?
        :param Reference informationSource: Person or organization that provided the information about the taking of this medication
        :param Reference derivedFrom: Additional supporting information
        :param CodeableConcept reasonCode: Reason for why the medication is being/was taken
        :param Reference reasonReference: Condition or observation that supports why the medication is being/was taken
        :param Annotation note: Further information about the statement
        :param Dosage dosage: Details of how medication is/was taken or should be taken
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
        "medicationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "medicationReference": {"class_name": "Reference", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "context": {"class_name": "Reference", "is_contained": False},
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        "informationSource": {"class_name": "Reference", "is_contained": False},
        "derivedFrom": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "dosage": {"class_name": "Dosage", "is_contained": False},
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
        partOf: list["Reference"] = None,
        status: "str" = None,
        statusReason: list["CodeableConcept"] = None,
        category: "CodeableConcept" = None,
        medicationCodeableConcept: "CodeableConcept" = None,
        medicationReference: "Reference" = None,
        subject: "Reference" = None,
        context: "Reference" = None,
        effectiveDateTime: "str" = None,
        effectivePeriod: "Period" = None,
        dateAsserted: "str" = None,
        informationSource: "Reference" = None,
        derivedFrom: list["Reference"] = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        note: list["Annotation"] = None,
        dosage: list["Dosage"] = None,
    ):
        self.resourceType = resourceType or "MedicationStatement"
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
        self.partOf = partOf or []
        self.status = status
        self.statusReason = statusReason or []
        self.category = category
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference
        self.subject = subject
        self.context = context
        self.effectiveDateTime = effectiveDateTime
        self.effectivePeriod = effectivePeriod
        self.dateAsserted = dateAsserted
        self.informationSource = informationSource
        self.derivedFrom = derivedFrom or []
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.note = note or []
        self.dosage = dosage or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationStatement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
