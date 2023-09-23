"""
Generated class for Slot. 
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
class Slot(ModelBase):
    """ A slot of time on a schedule that may be available for booking appointments.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this item
    :param CodeableConcept serviceCategory: A broad categorization of the service that is to be performed during this appointment
    :param CodeableConcept serviceType: The type of appointments that can be booked into this slot (ideally this would be an identifiable service - which is at a location, rather than the location itself). If provided then this overrides the value provided on the availability resource
    :param CodeableConcept specialty: The specialty of a practitioner that would be required to perform the service requested in this appointment
    :param CodeableConcept appointmentType: The style of appointment or patient that may be booked in the slot (not service type)
    :param Reference schedule: The schedule resource that this slot defines an interval of status information
    :param str status: busy | free | busy-unavailable | busy-tentative | entered-in-error
    :param str start: Date/Time that the slot is to begin
    :param str end: Date/Time that the slot is to conclude
    :param bool overbooked: This slot has already been overbooked, appointments are unlikely to be accepted for this time
    :param str comment: Comments on the slot to describe any extended information. Such as custom constraints on the slot
    """

    resourceType: str = "Slot"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    serviceCategory: list[CodeableConcept] = CodeableConcept() 
    
    serviceType: list[CodeableConcept] = CodeableConcept() 
    
    specialty: list[CodeableConcept] = CodeableConcept() 
    
    appointmentType: "CodeableConcept" = CodeableConcept()
    
    schedule: "Reference" = Reference()
    
    status: str = None
    
    start: str = None
    
    end: str = None
    
    overbooked: bool = None
    
    comment: str = None
    