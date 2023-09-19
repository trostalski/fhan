"""
Generated class for AppointmentResponse. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class AppointmentResponse:
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
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    appointment: "Reference" = None
    
    proposedNewTime: bool = None
    
    start: str = None
    
    end: str = None
    
    participantType: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    participantStatus: str = None
    
    comment: str = None
    
    recurring: bool = None
    
    occurrenceDate: str = None
    
    recurrenceId: int = None
    