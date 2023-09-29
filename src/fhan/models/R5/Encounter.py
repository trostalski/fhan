"""
Generated class for Encounter. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.VirtualServiceDetail import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Participant(BaseModel):
    """ The list of people responsible for providing the service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Role of participant in encounter
    :param Period period: Period of time during the encounter that the participant participated
    :param Reference actor: The individual, device, or service participating in the encounter
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  list['CodeableConcept']  = None,  period:  'Period'  = None,  actor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type or []
        self.period = period 
        self.actor = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Reason(BaseModel):
    """ The list of medical reasons that are expected to be addressed during the episode of care.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept use: What the reason value should be used for/as
    :param CodeableReference value: Reason the encounter takes place (core or reference)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "use": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "value": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  use:  list['CodeableConcept']  = None,  value:  list['CodeableReference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.use = use or []
        self.value = value or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Diagnosis(BaseModel):
    """ The list of diagnosis relevant to this encounter.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference condition: The diagnosis relevant to the encounter
    :param CodeableConcept use: Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "condition": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "use": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  condition:  list['CodeableReference']  = None,  use:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.condition = condition or []
        self.use = use or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Admission(BaseModel):
    """ Details about the stay during which a healthcare service is provided.This does not describe the event of admitting the patient, but rather any information that is relevant from the time of admittance until the time of discharge.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier preAdmissionIdentifier: Pre-admission identifier
    :param Reference origin: The location/organization from which the patient came before admission
    :param CodeableConcept admitSource: From where patient was admitted (physician referral, transfer)
    :param CodeableConcept reAdmission: Indicates that the patient is being re-admitted
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
        
        
        "destination": {"class_name": "Reference", "is_contained": False},
        
        
        "dischargeDisposition": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  preAdmissionIdentifier:  'Identifier'  = None,  origin:  'Reference'  = None,  admitSource:  'CodeableConcept'  = None,  reAdmission:  'CodeableConcept'  = None,  destination:  'Reference'  = None,  dischargeDisposition:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.preAdmissionIdentifier = preAdmissionIdentifier 
        self.origin = origin 
        self.admitSource = admitSource 
        self.reAdmission = reAdmission 
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
    """ List of locations where  the patient has been during this encounter.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference location: Location the encounter takes place
    :param str status: planned | active | reserved | completed
    :param CodeableConcept form: The physical type of the location (usually the level in the location hierarchy - bed, room, ward, virtual etc.)
    :param Period period: Time period during which the patient was present at the location
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        
        "form": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  location:  'Reference'  = None,  status:  'str'  = None,  form:  'CodeableConcept'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.location = location 
        self.status = status 
        self.form = form 
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
    :param CodeableConcept _class: Classification of patient encounter context - e.g. Inpatient, outpatient
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
    :param Participant participant: List of participants involved in the encounter
    :param Reference appointment: The appointment that scheduled this encounter
    :param VirtualServiceDetail virtualService: Connection details of a virtual service (e.g. conference call)
    :param Period actualPeriod: The actual start and end time of the encounter
    :param str plannedStartDate: The planned start date/time (or admission date) of the encounter
    :param str plannedEndDate: The planned end date/time (or discharge date) of the encounter
    :param Duration length: Actual quantity of time the encounter lasted (less time absent)
    :param Reason reason: The list of medical reasons that are expected to be addressed during the episode of care
    :param Diagnosis diagnosis: The list of diagnosis relevant to this encounter
    :param Reference account: The set of accounts that may be used for billing for this Encounter
    :param CodeableConcept dietPreference: Diet preferences reported by the patient
    :param CodeableConcept specialArrangement: Wheelchair, translator, stretcher, etc
    :param CodeableConcept specialCourtesy: Special courtesies (VIP, board member)
    :param Admission admission: Details about the admission to a healthcare service
    :param Location location: List of locations where the patient has been
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "_class": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "priority": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "serviceType": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "subjectStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "episodeOfCare": {"class_name": "Reference", "is_contained": False},
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "careTeam": {"class_name": "Reference", "is_contained": False},
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        "serviceProvider": {"class_name": "Reference", "is_contained": False},
        
        
        "participant": {"class_name": "Participant", "is_contained": True},
        
        
        "appointment": {"class_name": "Reference", "is_contained": False},
        
        
        "virtualService": {"class_name": "VirtualServiceDetail", "is_contained": False},
        
        
        "actualPeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        
        "length": {"class_name": "Duration", "is_contained": False},
        
        
        "reason": {"class_name": "Reason", "is_contained": True},
        
        
        "diagnosis": {"class_name": "Diagnosis", "is_contained": True},
        
        
        "account": {"class_name": "Reference", "is_contained": False},
        
        
        "dietPreference": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "specialArrangement": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "specialCourtesy": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "admission": {"class_name": "Admission", "is_contained": True},
        
        
        "location": {"class_name": "Location", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  _class:  list['CodeableConcept']  = None,  priority:  'CodeableConcept'  = None,  type:  list['CodeableConcept']  = None,  serviceType:  list['CodeableReference']  = None,  subject:  'Reference'  = None,  subjectStatus:  'CodeableConcept'  = None,  episodeOfCare:  list['Reference']  = None,  basedOn:  list['Reference']  = None,  careTeam:  list['Reference']  = None,  partOf:  'Reference'  = None,  serviceProvider:  'Reference'  = None,  participant:  list['Participant']  = None,  appointment:  list['Reference']  = None,  virtualService:  list['VirtualServiceDetail']  = None,  actualPeriod:  'Period'  = None,  plannedStartDate:  'str'  = None,  plannedEndDate:  'str'  = None,  length:  'Duration'  = None,  reason:  list['Reason']  = None,  diagnosis:  list['Diagnosis']  = None,  account:  list['Reference']  = None,  dietPreference:  list['CodeableConcept']  = None,  specialArrangement:  list['CodeableConcept']  = None,  specialCourtesy:  list['CodeableConcept']  = None,  admission:  'Admission'  = None,  location:  list['Location']  = None, ):
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
        self._class = _class or []
        self.priority = priority 
        self.type = type or []
        self.serviceType = serviceType or []
        self.subject = subject 
        self.subjectStatus = subjectStatus 
        self.episodeOfCare = episodeOfCare or []
        self.basedOn = basedOn or []
        self.careTeam = careTeam or []
        self.partOf = partOf 
        self.serviceProvider = serviceProvider 
        self.participant = participant or []
        self.appointment = appointment or []
        self.virtualService = virtualService or []
        self.actualPeriod = actualPeriod 
        self.plannedStartDate = plannedStartDate 
        self.plannedEndDate = plannedEndDate 
        self.length = length 
        self.reason = reason or []
        self.diagnosis = diagnosis or []
        self.account = account or []
        self.dietPreference = dietPreference or []
        self.specialArrangement = specialArrangement or []
        self.specialCourtesy = specialCourtesy or []
        self.admission = admission 
        self.location = location or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Encounter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()