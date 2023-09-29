"""
Generated class for Appointment. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.VirtualServiceDetail import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Participant(BaseModel):
    """ List of participants involved in the appointment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Role of participant in the appointment
    :param Period period: Participation period of the actor
    :param Reference actor: The individual, device, location, or service participating in the appointment
    :param bool required: The participant is required to attend (optional when false)
    :param str status: accepted | declined | tentative | needs-action
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  list['CodeableConcept']  = None,  period:  'Period'  = None,  actor:  'Reference'  = None,  required:  'bool'  = None,  status:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type or []
        self.period = period 
        self.actor = actor 
        self.required = required 
        self.status = status 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Appointment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class WeeklyTemplate(BaseModel):
    """ Information about weekly recurring appointments.:param str id: Unique id for inter-element referencing
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
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  monday:  'bool'  = None,  tuesday:  'bool'  = None,  wednesday:  'bool'  = None,  thursday:  'bool'  = None,  friday:  'bool'  = None,  saturday:  'bool'  = None,  sunday:  'bool'  = None,  weekInterval:  'int'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.monday = monday 
        self.tuesday = tuesday 
        self.wednesday = wednesday 
        self.thursday = thursday 
        self.friday = friday 
        self.saturday = saturday 
        self.sunday = sunday 
        self.weekInterval = weekInterval 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Appointment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class MonthlyTemplate(BaseModel):
    """ Information about monthly recurring appointments.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int dayOfMonth: Recurs on a specific day of the month
    :param Coding nthWeekOfMonth: Indicates which week of the month the appointment should occur
    :param Coding dayOfWeek: Indicates which day of the week the appointment should occur
    :param int monthInterval: Recurs every nth month
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "nthWeekOfMonth": {"class_name": "Coding", "is_contained": False},
        
        
        "dayOfWeek": {"class_name": "Coding", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  dayOfMonth:  'int'  = None,  nthWeekOfMonth:  'Coding'  = None,  dayOfWeek:  'Coding'  = None,  monthInterval:  'int'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.dayOfMonth = dayOfMonth 
        self.nthWeekOfMonth = nthWeekOfMonth 
        self.dayOfWeek = dayOfWeek 
        self.monthInterval = monthInterval 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Appointment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class YearlyTemplate(BaseModel):
    """ Information about yearly recurring appointments.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int yearInterval: Recurs every nth year
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  yearInterval:  'int'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.yearInterval = yearInterval 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Appointment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class RecurrenceTemplate(BaseModel):
    """ The details of the recurrence pattern or template that is used to generate recurring appointments.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept timezone: The timezone of the occurrences
    :param CodeableConcept recurrenceType: The frequency of the recurrence
    :param str lastOccurrenceDate: The date when the recurrence should end
    :param int occurrenceCount: The number of planned occurrences
    :param str occurrenceDate: Specific dates for a recurring set of appointments (no template)
    :param WeeklyTemplate weeklyTemplate: Information about weekly recurring appointments
    :param MonthlyTemplate monthlyTemplate: Information about monthly recurring appointments
    :param YearlyTemplate yearlyTemplate: Information about yearly recurring appointments
    :param str excludingDate: Any dates that should be excluded from the series
    :param int excludingRecurrenceId: Any recurrence IDs that should be excluded from the recurrence
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "timezone": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "recurrenceType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "weeklyTemplate": {"class_name": "WeeklyTemplate", "is_contained": True},
        
        
        "monthlyTemplate": {"class_name": "MonthlyTemplate", "is_contained": True},
        
        
        "yearlyTemplate": {"class_name": "YearlyTemplate", "is_contained": True},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  timezone:  'CodeableConcept'  = None,  recurrenceType:  'CodeableConcept'  = None,  lastOccurrenceDate:  'str'  = None,  occurrenceCount:  'int'  = None,  occurrenceDate:  list['str']  = None,  weeklyTemplate:  'WeeklyTemplate'  = None,  monthlyTemplate:  'MonthlyTemplate'  = None,  yearlyTemplate:  'YearlyTemplate'  = None,  excludingDate:  list['str']  = None,  excludingRecurrenceId:  list['int']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.timezone = timezone 
        self.recurrenceType = recurrenceType 
        self.lastOccurrenceDate = lastOccurrenceDate 
        self.occurrenceCount = occurrenceCount 
        self.occurrenceDate = occurrenceDate or []
        self.weeklyTemplate = weeklyTemplate 
        self.monthlyTemplate = monthlyTemplate 
        self.yearlyTemplate = yearlyTemplate 
        self.excludingDate = excludingDate or []
        self.excludingRecurrenceId = excludingRecurrenceId or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Appointment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Appointment(DomainResource):
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
    :param CodeableConcept _class: Classification when becoming an encounter
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
    :param Participant participant: Participants involved in appointment
    :param int recurrenceId: The sequence number in the recurrence
    :param bool occurrenceChanged: Indicates that this appointment varies from a recurrence pattern
    :param RecurrenceTemplate recurrenceTemplate: Details of the recurrence pattern/template used to generate occurrences
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "cancellationReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "_class": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "serviceCategory": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "serviceType": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "appointmentType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "priority": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "replaces": {"class_name": "Reference", "is_contained": False},
        
        
        "virtualService": {"class_name": "VirtualServiceDetail", "is_contained": False},
        
        
        "supportingInformation": {"class_name": "Reference", "is_contained": False},
        
        
        "previousAppointment": {"class_name": "Reference", "is_contained": False},
        
        
        "originatingAppointment": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "requestedPeriod": {"class_name": "Period", "is_contained": False},
        
        
        "slot": {"class_name": "Reference", "is_contained": False},
        
        
        "account": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "patientInstruction": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "participant": {"class_name": "Participant", "is_contained": True},
        
        
        
        
        "recurrenceTemplate": {"class_name": "RecurrenceTemplate", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  cancellationReason:  'CodeableConcept'  = None,  _class:  list['CodeableConcept']  = None,  serviceCategory:  list['CodeableConcept']  = None,  serviceType:  list['CodeableReference']  = None,  specialty:  list['CodeableConcept']  = None,  appointmentType:  'CodeableConcept'  = None,  reason:  list['CodeableReference']  = None,  priority:  'CodeableConcept'  = None,  description:  'str'  = None,  replaces:  list['Reference']  = None,  virtualService:  list['VirtualServiceDetail']  = None,  supportingInformation:  list['Reference']  = None,  previousAppointment:  'Reference'  = None,  originatingAppointment:  'Reference'  = None,  start:  'str'  = None,  end:  'str'  = None,  minutesDuration:  'int'  = None,  requestedPeriod:  list['Period']  = None,  slot:  list['Reference']  = None,  account:  list['Reference']  = None,  created:  'str'  = None,  cancellationDate:  'str'  = None,  note:  list['Annotation']  = None,  patientInstruction:  list['CodeableReference']  = None,  basedOn:  list['Reference']  = None,  subject:  'Reference'  = None,  participant:  list['Participant']  = None,  recurrenceId:  'int'  = None,  occurrenceChanged:  'bool'  = None,  recurrenceTemplate:  list['RecurrenceTemplate']  = None, ):
        self.resourceType = resourceType or "Appointment"
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
        self.cancellationReason = cancellationReason 
        self._class = _class or []
        self.serviceCategory = serviceCategory or []
        self.serviceType = serviceType or []
        self.specialty = specialty or []
        self.appointmentType = appointmentType 
        self.reason = reason or []
        self.priority = priority 
        self.description = description 
        self.replaces = replaces or []
        self.virtualService = virtualService or []
        self.supportingInformation = supportingInformation or []
        self.previousAppointment = previousAppointment 
        self.originatingAppointment = originatingAppointment 
        self.start = start 
        self.end = end 
        self.minutesDuration = minutesDuration 
        self.requestedPeriod = requestedPeriod or []
        self.slot = slot or []
        self.account = account or []
        self.created = created 
        self.cancellationDate = cancellationDate 
        self.note = note or []
        self.patientInstruction = patientInstruction or []
        self.basedOn = basedOn or []
        self.subject = subject 
        self.participant = participant or []
        self.recurrenceId = recurrenceId 
        self.occurrenceChanged = occurrenceChanged 
        self.recurrenceTemplate = recurrenceTemplate or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Appointment":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()