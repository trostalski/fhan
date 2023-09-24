"""
Generated class for AppointmentResponse. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


class AppointmentResponse(DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Ids for this item
    :param 'Reference' appointment: Appointment this response relates to
    :param str start: Time from appointment, or requested new start time
    :param str end: Time from appointment, or requested new end time
    :param list['CodeableConcept'] participantType: Role of participant in the appointment
    :param 'Reference' actor: Person, Location, HealthcareService, or Device
    :param str participantStatus: accepted | declined | tentative | needs-action
    :param str comment: Additional comments
    """
    def __init__(self, resourceType: str = "AppointmentResponse",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  appointment: 'Reference' = None,  start: str = None,  end: str = None,  participantType: list['CodeableConcept'] = None,  actor: 'Reference' = None,  participantStatus: str = None,  comment: str = None, ):
        self.resourceType: str = resourceType or "AppointmentResponse"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.appointment: 'Reference' = appointment 
        self.start: str = start 
        self.end: str = end 
        self.participantType: list['CodeableConcept'] = participantType or []
        self.actor: 'Reference' = actor 
        self.participantStatus: str = participantStatus 
        self.comment: str = comment 
        