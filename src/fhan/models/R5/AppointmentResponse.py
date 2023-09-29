"""
Generated class for AppointmentResponse. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


class AppointmentResponse(DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this item
    :param Reference appointment: Appointment this response relates to
    :param bool proposedNewTime: Indicator for a counter proposal
    :param str start: Time from appointment, or requested new start time
    :param str end: Time from appointment, or requested new end time
    :param CodeableConcept participantType: Role of participant in the appointment
    :param Reference actor: Person(s), Location, HealthcareService, or Device
    :param str participantStatus: accepted | declined | tentative | needs-action | entered-in-error
    :param str comment: Additional comments
    :param bool recurring: This response is for all occurrences in a recurring request
    :param str occurrenceDate: Original date within a recurring request
    :param int recurrenceId: The recurrence ID of the specific recurring request
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "appointment": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "participantType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  appointment:  'Reference'  = None,  proposedNewTime:  'bool'  = None,  start:  'str'  = None,  end:  'str'  = None,  participantType:  list['CodeableConcept']  = None,  actor:  'Reference'  = None,  participantStatus:  'str'  = None,  comment:  'str'  = None,  recurring:  'bool'  = None,  occurrenceDate:  'str'  = None,  recurrenceId:  'int'  = None, ):
        self.resourceType = resourceType or "AppointmentResponse"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.appointment = appointment 
        self.proposedNewTime = proposedNewTime 
        self.start = start 
        self.end = end 
        self.participantType = participantType or []
        self.actor = actor 
        self.participantStatus = participantStatus 
        self.comment = comment 
        self.recurring = recurring 
        self.occurrenceDate = occurrenceDate 
        self.recurrenceId = recurrenceId 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AppointmentResponse":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AppointmentResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()