"""
Generated class for PractitionerRole. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class availableTime(Element):
    """ A collection of times the practitioner is available or performing this role at the location and/or healthcareservice.
    :param BackboneElement availableTime: Times the Service Site is available
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: Always available? e.g. 24 hour service
    :param str availableStartTime: Opening time of day (ignored if allDay = true)
    :param str availableEndTime: Closing time of day (ignored if allDay = true)
    """
    availableTime: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    daysOfWeek: str = None
    
    allDay: bool = None
    
    availableStartTime: str = None
    
    availableEndTime: str = None
    
@dataclass
class notAvailable(Element):
    """ The practitioner is not available or performing this role during this period of time due to the provided reason.
    :param BackboneElement notAvailable: Not available during this time due to provided reason
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Reason presented to the user explaining why time not available
    :param Period during: Service not available from this date
    """
    notAvailable: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    during: "Period" = None
    


@dataclass
class PractitionerRole(ModelBase):
    """ A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifiers that are specific to a role/location
    :param bool active: Whether this practitioner role record is in active use
    :param Period period: The period during which the practitioner is authorized to perform in these role(s)
    :param Reference practitioner: Practitioner that is able to provide the defined services for the organization
    :param Reference organization: Organization where the roles are available
    :param CodeableConcept code: Roles which this practitioner may perform
    :param CodeableConcept specialty: Specific specialty of the practitioner
    :param Reference location: The location(s) at which this practitioner provides care
    :param Reference healthcareService: The list of healthcare services that this worker provides for this role's Organization/Location(s)
    :param ContactPoint telecom: Contact details that are specific to the role/location/service
    :param BackboneElement availableTime: Times the Service Site is available
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: Always available? e.g. 24 hour service
    :param str availableStartTime: Opening time of day (ignored if allDay = true)
    :param str availableEndTime: Closing time of day (ignored if allDay = true)
    :param BackboneElement notAvailable: Not available during this time due to provided reason
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Reason presented to the user explaining why time not available
    :param Period during: Service not available from this date
    :param str availabilityExceptions: Description of availability exceptions
    :param Reference endpoint: Technical endpoints providing access to services operated for the practitioner with this role
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    active: bool = None
    
    period: "Period" = None
    
    practitioner: "Reference" = None
    
    organization: "Reference" = None
    
    code: list["CodeableConcept"] = None
    
    specialty: list["CodeableConcept"] = None
    
    location: list["Reference"] = None
    
    healthcareService: list["Reference"] = None
    
    telecom: list["ContactPoint"] = None
    
    availableTime: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    daysOfWeek: str = None
    
    allDay: bool = None
    
    availableStartTime: str = None
    
    availableEndTime: str = None
    
    notAvailable: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    during: "Period" = None
    
    availabilityExceptions: str = None
    
    endpoint: list["Reference"] = None
    