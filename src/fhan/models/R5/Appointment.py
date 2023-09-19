"""
Generated class for Appointment. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *
from fhan.models.R5.VirtualServiceDetail import *


@dataclass
class Appointment:
    """ A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this item
    :param str status: proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist
    :param CodeableConcept cancellationReason: The coded reason for the appointment being cancelled
    :param CodeableConcept class: Classification when becoming an encounter
    :param CodeableConcept serviceCategory: A broad categorization of the service that is to be performed during this appointment
    :param CodeableReference serviceType: The specific service that is to be performed during this appointment
    :param CodeableConcept specialty: The specialty of a practitioner that would be required to perform the service requested in this appointment
    :param CodeableConcept appointmentType: The style of appointment or patient that has been booked in the slot (not service type)
    :param CodeableReference reason: Reason this appointment is scheduled
    :param CodeableConcept priority: Used to make informed decisions if needing to re-prioritize
    :param str description: Shown on a subject line in a meeting request, or appointment list
    :param Reference replaces: Appointment replaced by this Appointment
    :param VirtualServiceDetail virtualService: Connection details of a virtual service (e.g. conference call)
    :param Reference supportingInformation: Additional information to support the appointment
    :param Reference previousAppointment: The previous appointment in a series
    :param Reference originatingAppointment: The originating appointment in a recurring set of appointments
    :param str start: When appointment is to take place
    :param str end: When appointment is to conclude
    :param int minutesDuration: Can be less than start/end (e.g. estimate)
    :param Period requestedPeriod: Potential date/time interval(s) requested to allocate the appointment within
    :param Reference slot: The slots that this appointment is filling
    :param Reference account: The set of accounts that may be used for billing for this Appointment
    :param str created: The date that this appointment was initially created
    :param str cancellationDate: When the appointment was cancelled
    :param Annotation note: Additional comments
    :param CodeableReference patientInstruction: Detailed information and instructions for the patient
    :param Reference basedOn: The request this appointment is allocated to assess
    :param Reference subject: The patient or group associated with the appointment
    :param BackboneElement participant: Participants involved in appointment
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Role of participant in the appointment
    :param Period period: Participation period of the actor
    :param Reference actor: The individual, device, location, or service participating in the appointment
    :param bool required: The participant is required to attend (optional when false)
    :param str status: accepted | declined | tentative | needs-action
    :param int recurrenceId: The sequence number in the recurrence
    :param bool occurrenceChanged: Indicates that this appointment varies from a recurrence pattern
    :param BackboneElement recurrenceTemplate: Details of the recurrence pattern/template used to generate occurrences
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept timezone: The timezone of the occurrences
    :param CodeableConcept recurrenceType: The frequency of the recurrence
    :param str lastOccurrenceDate: The date when the recurrence should end
    :param int occurrenceCount: The number of planned occurrences
    :param str occurrenceDate: Specific dates for a recurring set of appointments (no template)
    :param BackboneElement weeklyTemplate: Information about weekly recurring appointments
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool monday: Recurs on Mondays
    :param bool tuesday: Recurs on Tuesday
    :param bool wednesday: Recurs on Wednesday
    :param bool thursday: Recurs on Thursday
    :param bool friday: Recurs on Friday
    :param bool saturday: Recurs on Saturday
    :param bool sunday: Recurs on Sunday
    :param int weekInterval: Recurs every nth week
    :param BackboneElement monthlyTemplate: Information about monthly recurring appointments
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int dayOfMonth: Recurs on a specific day of the month
    :param Coding nthWeekOfMonth: Indicates which week of the month the appointment should occur
    :param Coding dayOfWeek: Indicates which day of the week the appointment should occur
    :param int monthInterval: Recurs every nth month
    :param BackboneElement yearlyTemplate: Information about yearly recurring appointments
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int yearInterval: Recurs every nth year
    :param str excludingDate: Any dates that should be excluded from the series
    :param int excludingRecurrenceId: Any recurrence IDs that should be excluded from the recurrence
    
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
    
    cancellationReason: "CodeableConcept" = None
    
    class: "CodeableConcept" = None
    
    serviceCategory: "CodeableConcept" = None
    
    serviceType: "CodeableReference" = None
    
    specialty: "CodeableConcept" = None
    
    appointmentType: "CodeableConcept" = None
    
    reason: "CodeableReference" = None
    
    priority: "CodeableConcept" = None
    
    description: str = None
    
    replaces: "Reference" = None
    
    virtualService: "VirtualServiceDetail" = None
    
    supportingInformation: "Reference" = None
    
    previousAppointment: "Reference" = None
    
    originatingAppointment: "Reference" = None
    
    start: str = None
    
    end: str = None
    
    minutesDuration: int = None
    
    requestedPeriod: "Period" = None
    
    slot: "Reference" = None
    
    account: "Reference" = None
    
    created: str = None
    
    cancellationDate: str = None
    
    note: "Annotation" = None
    
    patientInstruction: "CodeableReference" = None
    
    basedOn: "Reference" = None
    
    subject: "Reference" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    period: "Period" = None
    
    actor: "Reference" = None
    
    required: bool = None
    
    status: str = None
    
    recurrenceId: int = None
    
    occurrenceChanged: bool = None
    
    recurrenceTemplate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    timezone: "CodeableConcept" = None
    
    recurrenceType: "CodeableConcept" = None
    
    lastOccurrenceDate: str = None
    
    occurrenceCount: int = None
    
    occurrenceDate: str = None
    
    weeklyTemplate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    monday: bool = None
    
    tuesday: bool = None
    
    wednesday: bool = None
    
    thursday: bool = None
    
    friday: bool = None
    
    saturday: bool = None
    
    sunday: bool = None
    
    weekInterval: int = None
    
    monthlyTemplate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    dayOfMonth: int = None
    
    nthWeekOfMonth: "Coding" = None
    
    dayOfWeek: "Coding" = None
    
    monthInterval: int = None
    
    yearlyTemplate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    yearInterval: int = None
    
    excludingDate: str = None
    
    excludingRecurrenceId: int = None
    