"""
Generated class for Appointment. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Participant(Element):
    """ List of participants involved in the appointment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Role of participant in the appointment
    :param Reference actor: Person, Location/HealthcareService or Device
    :param str required: required | optional | information-only
    :param str status: accepted | declined | tentative | needs-action
    :param Period period: Participation period of the actor
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    type: list[CodeableConcept] = CodeableConcept() 
    actor: "Reference" = Reference()
    
    required: str = None
    
    status: str = None
    period: "Period" = Period()
    

@dataclass
class Appointment(ModelBase):
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
    :param CodeableConcept cancelationReason: The coded reason for the appointment being cancelled
    :param CodeableConcept serviceCategory: A broad categorization of the service that is to be performed during this appointment
    :param CodeableConcept serviceType: The specific service that is to be performed during this appointment
    :param CodeableConcept specialty: The specialty of a practitioner that would be required to perform the service requested in this appointment
    :param CodeableConcept appointmentType: The style of appointment or patient that has been booked in the slot (not service type)
    :param CodeableConcept reasonCode: Coded reason this appointment is scheduled
    :param Reference reasonReference: Reason the appointment is to take place (resource)
    :param int priority: Used to make informed decisions if needing to re-prioritize
    :param str description: Shown on a subject line in a meeting request, or appointment list
    :param Reference supportingInformation: Additional information to support the appointment
    :param str start: When appointment is to take place
    :param str end: When appointment is to conclude
    :param int minutesDuration: Can be less than start/end (e.g. estimate)
    :param Reference slot: The slots that this appointment is filling
    :param str created: The date that this appointment was initially created
    :param str comment: Additional comments
    :param str patientInstruction: Detailed information and instructions for the patient
    :param Reference basedOn: The service request this appointment is allocated to assess
    :param Participant participant: Participants involved in appointment
    :param Period requestedPeriod: Potential date/time interval(s) requested to allocate the appointment within
    """

    resourceType: str = "Appointment"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    cancelationReason: "CodeableConcept" = CodeableConcept()
    
    serviceCategory: list[CodeableConcept] = CodeableConcept() 
    
    serviceType: list[CodeableConcept] = CodeableConcept() 
    
    specialty: list[CodeableConcept] = CodeableConcept() 
    
    appointmentType: "CodeableConcept" = CodeableConcept()
    
    reasonCode: list[CodeableConcept] = CodeableConcept() 
    
    reasonReference: list[Reference] = Reference() 
    
    priority: int = None
    
    description: str = None
    
    supportingInformation: list[Reference] = Reference() 
    
    start: str = None
    
    end: str = None
    
    minutesDuration: int = None
    
    slot: list[Reference] = Reference() 
    
    created: str = None
    
    comment: str = None
    
    patientInstruction: str = None
    
    basedOn: list[Reference] = Reference() 
    
    participant: list[Participant] = Participant() 
    
    requestedPeriod: list[Period] = Period() 
    