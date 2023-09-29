"""
Generated class for PractitionerRole. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Availability import *
from fhan.models.R5.Meta import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


class PractitionerRole(DomainResource):
    """ A specific set of Roles/Locations/specialties/services that a practitioner may perform, or has performed at an organization during a period of time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers for a role/location
    :param bool active: Whether this practitioner role record is in active use
    :param Period period: The period during which the practitioner is authorized to perform in these role(s)
    :param Reference practitioner: Practitioner that provides services for the organization
    :param Reference organization: Organization where the roles are available
    :param CodeableConcept code: Roles which this practitioner may perform
    :param CodeableConcept specialty: Specific specialty of the practitioner
    :param Reference location: Location(s) where the practitioner provides care
    :param Reference healthcareService: Healthcare services provided for this role's Organization/Location(s)
    :param ExtendedContactDetail contact: Official contact details relating to this PractitionerRole
    :param CodeableConcept characteristic: Collection of characteristics (attributes)
    :param CodeableConcept communication: A language the practitioner (in this role) can use in patient communication
    :param Availability availability: Times the Practitioner is available at this location and/or healthcare service (including exceptions)
    :param Reference endpoint: Endpoints for interacting with the practitioner in this role
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "practitioner": {"class_name": "Reference", "is_contained": False},
        
        
        "organization": {"class_name": "Reference", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "healthcareService": {"class_name": "Reference", "is_contained": False},
        
        
        "contact": {"class_name": "ExtendedContactDetail", "is_contained": False},
        
        
        "characteristic": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "communication": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "availability": {"class_name": "Availability", "is_contained": False},
        
        
        "endpoint": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  active:  'bool'  = None,  period:  'Period'  = None,  practitioner:  'Reference'  = None,  organization:  'Reference'  = None,  code:  list['CodeableConcept']  = None,  specialty:  list['CodeableConcept']  = None,  location:  list['Reference']  = None,  healthcareService:  list['Reference']  = None,  contact:  list['ExtendedContactDetail']  = None,  characteristic:  list['CodeableConcept']  = None,  communication:  list['CodeableConcept']  = None,  availability:  list['Availability']  = None,  endpoint:  list['Reference']  = None, ):
        self.resourceType = resourceType or "PractitionerRole"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.active = active 
        self.period = period 
        self.practitioner = practitioner 
        self.organization = organization 
        self.code = code or []
        self.specialty = specialty or []
        self.location = location or []
        self.healthcareService = healthcareService or []
        self.contact = contact or []
        self.characteristic = characteristic or []
        self.communication = communication or []
        self.availability = availability or []
        self.endpoint = endpoint or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PractitionerRole":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PractitionerRole":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()