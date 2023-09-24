"""
Generated class for PractitionerRole. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class AvailableTime(ModelBase):
    """ A collection of times the practitioner is available or performing this role at the location and/or healthcareservice.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: Always available? e.g. 24 hour service
    :param str availableStartTime: Opening time of day (ignored if allDay = true)
    :param str availableEndTime: Closing time of day (ignored if allDay = true)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  daysOfWeek: str = None,  allDay: bool = None,  availableStartTime: str = None,  availableEndTime: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.daysOfWeek: str = daysOfWeek or []
        self.allDay: bool = allDay 
        self.availableStartTime: str = availableStartTime 
        self.availableEndTime: str = availableEndTime 
        

    
    

class NotAvailable(ModelBase):
    """ The practitioner is not available or performing this role during this period of time due to the provided reason.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Reason presented to the user explaining why time not available
    :param 'Period' during: Service not available from this date
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  description: str = None,  during: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.description: str = description 
        self.during: 'Period' = during 
        

class PractitionerRole(DomainResource):
    """ A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifiers that are specific to a role/location
    :param bool active: Whether this practitioner role record is in active use
    :param 'Period' period: The period during which the practitioner is authorized to perform in these role(s)
    :param 'Reference' practitioner: Practitioner that is able to provide the defined services for the organization
    :param 'Reference' organization: Organization where the roles are available
    :param list['CodeableConcept'] code: Roles which this practitioner may perform
    :param list['CodeableConcept'] specialty: Specific specialty of the practitioner
    :param list['Reference'] location: The location(s) at which this practitioner provides care
    :param list['Reference'] healthcareService: The list of healthcare services that this worker provides for this role's Organization/Location(s)
    :param list['ContactPoint'] telecom: Contact details that are specific to the role/location/service
    :param list['AvailableTime'] availableTime: Times the Service Site is available
    :param list['NotAvailable'] notAvailable: Not available during this time due to provided reason
    :param str availabilityExceptions: Description of availability exceptions
    :param list['Reference'] endpoint: Technical endpoints providing access to services operated for the practitioner with this role
    """
    def __init__(self, resourceType: str = "PractitionerRole",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  active: bool = None,  period: 'Period' = None,  practitioner: 'Reference' = None,  organization: 'Reference' = None,  code: list['CodeableConcept'] = None,  specialty: list['CodeableConcept'] = None,  location: list['Reference'] = None,  healthcareService: list['Reference'] = None,  telecom: list['ContactPoint'] = None,  availableTime: list['AvailableTime'] = None,  notAvailable: list['NotAvailable'] = None,  availabilityExceptions: str = None,  endpoint: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "PractitionerRole"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.active: bool = active 
        self.period: 'Period' = period 
        self.practitioner: 'Reference' = practitioner 
        self.organization: 'Reference' = organization 
        self.code: list['CodeableConcept'] = code or []
        self.specialty: list['CodeableConcept'] = specialty or []
        self.location: list['Reference'] = location or []
        self.healthcareService: list['Reference'] = healthcareService or []
        self.telecom: list['ContactPoint'] = telecom or []
        self.availableTime: list['AvailableTime'] = availableTime or []
        self.notAvailable: list['NotAvailable'] = notAvailable or []
        self.availabilityExceptions: str = availabilityExceptions 
        self.endpoint: list['Reference'] = endpoint or []
        