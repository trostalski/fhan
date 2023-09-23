"""
Generated class for AppointmentResponse. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

@dataclass
class AppointmentResponse(ModelBase):
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
    :param str start: Time from appointment, or requested new start time
    :param str end: Time from appointment, or requested new end time
    :param CodeableConcept participantType: Role of participant in the appointment
    :param Reference actor: Person, Location, HealthcareService, or Device
    :param str participantStatus: accepted | declined | tentative | needs-action
    :param str comment: Additional comments
    """

    resourceType: str = "AppointmentResponse"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    appointment: "Reference" = Reference()
    
    start: str = None
    
    end: str = None
    
    participantType: list[CodeableConcept] = CodeableConcept() 
    
    actor: "Reference" = Reference()
    
    participantStatus: str = None
    
    comment: str = None
    