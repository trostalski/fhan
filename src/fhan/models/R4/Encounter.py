"""
Generated class for Encounter. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Duration import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Coding import *
from fhan.models.generator_models import ModelBase

@dataclass
class statusHistory(Element):
    """ The status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store them.
    :param BackboneElement statusHistory: List of past encounter statuses
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    :param Period period: The time that the episode was in the specified status
    """
    statusHistory: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    status: str = None
    
    period: "Period" = None
    
@dataclass
class classHistory(Element):
    """ The class history permits the tracking of the encounters transitions without needing to go  through the resource history.  This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatient.
    :param BackboneElement classHistory: List of past encounter classes
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding _class: inpatient | outpatient | ambulatory | emergency +
    :param Period period: The time that the episode was in the specified class
    """
    classHistory: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    _class: "Coding" = None
    
    period: "Period" = None
    
@dataclass
class participant(Element):
    """ The list of people responsible for providing the service.
    :param BackboneElement participant: List of participants involved in the encounter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Role of participant in encounter
    :param Period period: Period of time during the encounter that the participant participated
    :param Reference individual: Persons involved in the encounter other than the patient
    """
    participant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: list["CodeableConcept"] = None
    
    period: "Period" = None
    
    individual: "Reference" = None
    
@dataclass
class diagnosis(Element):
    """ The list of diagnosis relevant to this encounter.
    :param BackboneElement diagnosis: The list of diagnosis relevant to this encounter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference condition: The diagnosis or procedure relevant to the encounter
    :param CodeableConcept use: Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)
    :param int rank: Ranking of the diagnosis (for each role type)
    """
    diagnosis: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    condition: "Reference" = None
    
    use: "CodeableConcept" = None
    
    rank: int = None
    
@dataclass
class hospitalization(Element):
    """ Details about the admission to a healthcare service.
    :param BackboneElement hospitalization: Details about the admission to a healthcare service
    :param str id: Unique id for inter-element referencing
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
    hospitalization: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    preAdmissionIdentifier: "Identifier" = None
    
    origin: "Reference" = None
    
    admitSource: "CodeableConcept" = None
    
    reAdmission: "CodeableConcept" = None
    
    dietPreference: list["CodeableConcept"] = None
    
    specialCourtesy: list["CodeableConcept"] = None
    
    specialArrangement: list["CodeableConcept"] = None
    
    destination: "Reference" = None
    
    dischargeDisposition: "CodeableConcept" = None
    
@dataclass
class location(Element):
    """ List of locations where  the patient has been during this encounter.
    :param BackboneElement location: List of locations where the patient has been
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference location: Location the encounter takes place
    :param str status: planned | active | reserved | completed
    :param CodeableConcept physicalType: The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
    :param Period period: Time period during which the patient was present at the location
    """
    location: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    location: "Reference" = None
    
    status: str = None
    
    physicalType: "CodeableConcept" = None
    
    period: "Period" = None
    


@dataclass
class Encounter(ModelBase):
    """ An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.
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
    :param BackboneElement statusHistory: List of past encounter statuses
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    :param Period period: The time that the episode was in the specified status
    :param Coding _class: Classification of patient encounter
    :param BackboneElement classHistory: List of past encounter classes
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding _class: inpatient | outpatient | ambulatory | emergency +
    :param Period period: The time that the episode was in the specified class
    :param CodeableConcept type: Specific type of encounter
    :param CodeableConcept serviceType: Specific type of service
    :param CodeableConcept priority: Indicates the urgency of the encounter
    :param Reference subject: The patient or group present at the encounter
    :param Reference episodeOfCare: Episode(s) of care that this encounter should be recorded against
    :param Reference basedOn: The ServiceRequest that initiated this encounter
    :param BackboneElement participant: List of participants involved in the encounter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Role of participant in encounter
    :param Period period: Period of time during the encounter that the participant participated
    :param Reference individual: Persons involved in the encounter other than the patient
    :param Reference appointment: The appointment that scheduled this encounter
    :param Period period: The start and end time of the encounter
    :param Duration length: Quantity of time the encounter lasted (less time absent)
    :param CodeableConcept reasonCode: Coded reason the encounter takes place
    :param Reference reasonReference: Reason the encounter takes place (reference)
    :param BackboneElement diagnosis: The list of diagnosis relevant to this encounter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference condition: The diagnosis or procedure relevant to the encounter
    :param CodeableConcept use: Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)
    :param int rank: Ranking of the diagnosis (for each role type)
    :param Reference account: The set of accounts that may be used for billing for this Encounter
    :param BackboneElement hospitalization: Details about the admission to a healthcare service
    :param str id: Unique id for inter-element referencing
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
    :param BackboneElement location: List of locations where the patient has been
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference location: Location the encounter takes place
    :param str status: planned | active | reserved | completed
    :param CodeableConcept physicalType: The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
    :param Period period: Time period during which the patient was present at the location
    :param Reference serviceProvider: The organization (facility) responsible for this encounter
    :param Reference partOf: Another Encounter this encounter is part of
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    status: str = None
    
    statusHistory: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    status: str = None
    
    period: "Period" = None
    
    _class: "Coding" = None
    
    classHistory: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    _class: "Coding" = None
    
    period: "Period" = None
    
    type: list["CodeableConcept"] = None
    
    serviceType: "CodeableConcept" = None
    
    priority: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    episodeOfCare: list["Reference"] = None
    
    basedOn: list["Reference"] = None
    
    participant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: list["CodeableConcept"] = None
    
    period: "Period" = None
    
    individual: "Reference" = None
    
    appointment: list["Reference"] = None
    
    period: "Period" = None
    
    length: "Duration" = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    diagnosis: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    condition: "Reference" = None
    
    use: "CodeableConcept" = None
    
    rank: int = None
    
    account: list["Reference"] = None
    
    hospitalization: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    preAdmissionIdentifier: "Identifier" = None
    
    origin: "Reference" = None
    
    admitSource: "CodeableConcept" = None
    
    reAdmission: "CodeableConcept" = None
    
    dietPreference: list["CodeableConcept"] = None
    
    specialCourtesy: list["CodeableConcept"] = None
    
    specialArrangement: list["CodeableConcept"] = None
    
    destination: "Reference" = None
    
    dischargeDisposition: "CodeableConcept" = None
    
    location: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    location: "Reference" = None
    
    status: str = None
    
    physicalType: "CodeableConcept" = None
    
    period: "Period" = None
    
    serviceProvider: "Reference" = None
    
    partOf: "Reference" = None
    