"""
Generated class for Encounter. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *
from fhan.models.R5.VirtualServiceDetail import *


@dataclass
class Encounter:
    """ An interaction between healthcare provider(s), and/or patient(s) for the purpose of providing healthcare service(s) or assessing the health status of patient(s).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier(s) by which this encounter is known
    :param str status: planned | in-progress | on-hold | discharged | completed | cancelled | discontinued | entered-in-error | unknown
    :param CodeableConcept class: Classification of patient encounter context - e.g. Inpatient, outpatient
    :param CodeableConcept priority: Indicates the urgency of the encounter
    :param CodeableConcept type: Specific type of encounter (e.g. e-mail consultation, surgical day-care, ...)
    :param CodeableReference serviceType: Specific type of service
    :param Reference subject: The patient or group related to this encounter
    :param CodeableConcept subjectStatus: The current status of the subject in relation to the Encounter
    :param Reference episodeOfCare: Episode(s) of care that this encounter should be recorded against
    :param Reference basedOn: The request that initiated this encounter
    :param Reference careTeam: The group(s) that are allocated to participate in this encounter
    :param Reference partOf: Another Encounter this encounter is part of
    :param Reference serviceProvider: The organization (facility) responsible for this encounter
    :param BackboneElement participant: List of participants involved in the encounter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Role of participant in encounter
    :param Period period: Period of time during the encounter that the participant participated
    :param Reference actor: The individual, device, or service participating in the encounter
    :param Reference appointment: The appointment that scheduled this encounter
    :param VirtualServiceDetail virtualService: Connection details of a virtual service (e.g. conference call)
    :param Period actualPeriod: The actual start and end time of the encounter
    :param str plannedStartDate: The planned start date/time (or admission date) of the encounter
    :param str plannedEndDate: The planned end date/time (or discharge date) of the encounter
    :param Duration length: Actual quantity of time the encounter lasted (less time absent)
    :param BackboneElement reason: The list of medical reasons that are expected to be addressed during the episode of care
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept use: What the reason value should be used for/as
    :param CodeableReference value: Reason the encounter takes place (core or reference)
    :param BackboneElement diagnosis: The list of diagnosis relevant to this encounter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference condition: The diagnosis relevant to the encounter
    :param CodeableConcept use: Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)
    :param Reference account: The set of accounts that may be used for billing for this Encounter
    :param CodeableConcept dietPreference: Diet preferences reported by the patient
    :param CodeableConcept specialArrangement: Wheelchair, translator, stretcher, etc
    :param CodeableConcept specialCourtesy: Special courtesies (VIP, board member)
    :param BackboneElement admission: Details about the admission to a healthcare service
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier preAdmissionIdentifier: Pre-admission identifier
    :param Reference origin: The location/organization from which the patient came before admission
    :param CodeableConcept admitSource: From where patient was admitted (physician referral, transfer)
    :param CodeableConcept reAdmission: Indicates that the patient is being re-admitted
    :param Reference destination: Location/organization to which the patient is discharged
    :param CodeableConcept dischargeDisposition: Category or kind of location after discharge
    :param BackboneElement location: List of locations where the patient has been
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference location: Location the encounter takes place
    :param str status: planned | active | reserved | completed
    :param CodeableConcept form: The physical type of the location (usually the level in the location hierarchy - bed, room, ward, virtual etc.)
    :param Period period: Time period during which the patient was present at the location
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    class: "CodeableConcept" = None
    
    priority: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    serviceType: "CodeableReference" = None
    
    subject: "Reference" = None
    
    subjectStatus: "CodeableConcept" = None
    
    episodeOfCare: "Reference" = None
    
    basedOn: "Reference" = None
    
    careTeam: "Reference" = None
    
    partOf: "Reference" = None
    
    serviceProvider: "Reference" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    period: "Period" = None
    
    actor: "Reference" = None
    
    appointment: "Reference" = None
    
    virtualService: "VirtualServiceDetail" = None
    
    actualPeriod: "Period" = None
    
    plannedStartDate: str = None
    
    plannedEndDate: str = None
    
    length: "Duration" = None
    
    reason: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    use: "CodeableConcept" = None
    
    value: "CodeableReference" = None
    
    diagnosis: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    condition: "CodeableReference" = None
    
    use: "CodeableConcept" = None
    
    account: "Reference" = None
    
    dietPreference: "CodeableConcept" = None
    
    specialArrangement: "CodeableConcept" = None
    
    specialCourtesy: "CodeableConcept" = None
    
    admission: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    preAdmissionIdentifier: "Identifier" = None
    
    origin: "Reference" = None
    
    admitSource: "CodeableConcept" = None
    
    reAdmission: "CodeableConcept" = None
    
    destination: "Reference" = None
    
    dischargeDisposition: "CodeableConcept" = None
    
    location: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    location: "Reference" = None
    
    status: str = None
    
    form: "CodeableConcept" = None
    
    period: "Period" = None
    