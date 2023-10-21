"""
Generated class for Encounter. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Coding import *
from fhan.models.R4.DomainResource import *


class StatusHistory(BaseModel):
    """The status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store them.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    :param Period period: The time that the episode was in the specified status
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        status: "str" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.status = status
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ClassHistory(BaseModel):
    """The class history permits the tracking of the encounters transitions without needing to go  through the resource history.  This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatient.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding _class: inpatient | outpatient | ambulatory | emergency +
    :param Period period: The time that the episode was in the specified class
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "_class": {"class_name": "Coding", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        _class: "Coding" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self._class = _class
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Participant(BaseModel):
    """The list of people responsible for providing the service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Role of participant in encounter
    :param Period period: Period of time during the encounter that the participant participated
    :param Reference individual: Persons involved in the encounter other than the patient
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "individual": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: list["CodeableConcept"] = None,
        period: "Period" = None,
        individual: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type or []
        self.period = period
        self.individual = individual

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Diagnosis(BaseModel):
    """The list of diagnosis relevant to this encounter.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference condition: The diagnosis or procedure relevant to the encounter
    :param CodeableConcept use: Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)
    :param int rank: Ranking of the diagnosis (for each role type)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "condition": {"class_name": "Reference", "is_contained": False},
        "use": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        condition: "Reference" = None,
        use: "CodeableConcept" = None,
        rank: "int" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.condition = condition
        self.use = use
        self.rank = rank

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Hospitalization(BaseModel):
    """Details about the admission to a healthcare service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier preAdmissionIdentifier: Pre-admission identifier
    :param Reference origin: The location/organization from which the patient came before admission
    :param CodeableConcept admitSource: From where patient was admitted (physician referral, transfer)
    :param CodeableConcept reAdmission: The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
    :param CodeableConcept dietPreference: Diet preferences reported by the patient
    :param CodeableConcept specialCourtesy: Special courtesies (VIP, board member)
    :param CodeableConcept specialArrangement: Wheelchair, translator, stretcher, etc.
    :param Reference destination: Location/organization to which the patient is discharged
    :param CodeableConcept dischargeDisposition: Category or kind of location after discharge
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "preAdmissionIdentifier": {"class_name": "Identifier", "is_contained": False},
        "origin": {"class_name": "Reference", "is_contained": False},
        "admitSource": {"class_name": "CodeableConcept", "is_contained": False},
        "reAdmission": {"class_name": "CodeableConcept", "is_contained": False},
        "dietPreference": {"class_name": "CodeableConcept", "is_contained": False},
        "specialCourtesy": {"class_name": "CodeableConcept", "is_contained": False},
        "specialArrangement": {"class_name": "CodeableConcept", "is_contained": False},
        "destination": {"class_name": "Reference", "is_contained": False},
        "dischargeDisposition": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        preAdmissionIdentifier: "Identifier" = None,
        origin: "Reference" = None,
        admitSource: "CodeableConcept" = None,
        reAdmission: "CodeableConcept" = None,
        dietPreference: list["CodeableConcept"] = None,
        specialCourtesy: list["CodeableConcept"] = None,
        specialArrangement: list["CodeableConcept"] = None,
        destination: "Reference" = None,
        dischargeDisposition: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.preAdmissionIdentifier = preAdmissionIdentifier
        self.origin = origin
        self.admitSource = admitSource
        self.reAdmission = reAdmission
        self.dietPreference = dietPreference or []
        self.specialCourtesy = specialCourtesy or []
        self.specialArrangement = specialArrangement or []
        self.destination = destination
        self.dischargeDisposition = dischargeDisposition

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Location(BaseModel):
    """List of locations where  the patient has been during this encounter.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference location: Location the encounter takes place
    :param str status: planned | active | reserved | completed
    :param CodeableConcept physicalType: The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
    :param Period period: Time period during which the patient was present at the location
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "physicalType": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        location: "Reference" = None,
        status: "str" = None,
        physicalType: "CodeableConcept" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.location = location
        self.status = status
        self.physicalType = physicalType
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Encounter(DomainResource):
    """An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier(s) by which this encounter is known
    :param str status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    :param StatusHistory statusHistory: List of past encounter statuses
    :param Coding _class: Classification of patient encounter
    :param ClassHistory classHistory: List of past encounter classes
    :param CodeableConcept type: Specific type of encounter
    :param CodeableConcept serviceType: Specific type of service
    :param CodeableConcept priority: Indicates the urgency of the encounter
    :param Reference subject: The patient or group present at the encounter
    :param Reference episodeOfCare: Episode(s) of care that this encounter should be recorded against
    :param Reference basedOn: The ServiceRequest that initiated this encounter
    :param Participant participant: List of participants involved in the encounter
    :param Reference appointment: The appointment that scheduled this encounter
    :param Period period: The start and end time of the encounter
    :param Duration length: Quantity of time the encounter lasted (less time absent)
    :param CodeableConcept reasonCode: Coded reason the encounter takes place
    :param Reference reasonReference: Reason the encounter takes place (reference)
    :param Diagnosis diagnosis: The list of diagnosis relevant to this encounter
    :param Reference account: The set of accounts that may be used for billing for this Encounter
    :param Hospitalization hospitalization: Details about the admission to a healthcare service
    :param Location location: List of locations where the patient has been
    :param Reference serviceProvider: The organization (facility) responsible for this encounter
    :param Reference partOf: Another Encounter this encounter is part of
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "statusHistory": {"class_name": "StatusHistory", "is_contained": True},
        "_class": {"class_name": "Coding", "is_contained": False},
        "classHistory": {"class_name": "ClassHistory", "is_contained": True},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "serviceType": {"class_name": "CodeableConcept", "is_contained": False},
        "priority": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "episodeOfCare": {"class_name": "Reference", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "participant": {"class_name": "Participant", "is_contained": True},
        "appointment": {"class_name": "Reference", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "length": {"class_name": "Duration", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "diagnosis": {"class_name": "Diagnosis", "is_contained": True},
        "account": {"class_name": "Reference", "is_contained": False},
        "hospitalization": {"class_name": "Hospitalization", "is_contained": True},
        "location": {"class_name": "Location", "is_contained": True},
        "serviceProvider": {"class_name": "Reference", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
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
        status: "str" = None,
        statusHistory: list["StatusHistory"] = None,
        _class: "Coding" = None,
        classHistory: list["ClassHistory"] = None,
        type: list["CodeableConcept"] = None,
        serviceType: "CodeableConcept" = None,
        priority: "CodeableConcept" = None,
        subject: "Reference" = None,
        episodeOfCare: list["Reference"] = None,
        basedOn: list["Reference"] = None,
        participant: list["Participant"] = None,
        appointment: list["Reference"] = None,
        period: "Period" = None,
        length: "Duration" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        diagnosis: list["Diagnosis"] = None,
        account: list["Reference"] = None,
        hospitalization: "Hospitalization" = None,
        location: list["Location"] = None,
        serviceProvider: "Reference" = None,
        partOf: "Reference" = None,
    ):
        self.resourceType = resourceType or "Encounter"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status
        self.statusHistory = statusHistory or []
        self._class = _class
        self.classHistory = classHistory or []
        self.type = type or []
        self.serviceType = serviceType
        self.priority = priority
        self.subject = subject
        self.episodeOfCare = episodeOfCare or []
        self.basedOn = basedOn or []
        self.participant = participant or []
        self.appointment = appointment or []
        self.period = period
        self.length = length
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.diagnosis = diagnosis or []
        self.account = account or []
        self.hospitalization = hospitalization
        self.location = location or []
        self.serviceProvider = serviceProvider
        self.partOf = partOf

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
