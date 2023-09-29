"""
Generated class for HealthcareService. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Availability import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Eligibility(BaseModel):
    """ Does this service have specific eligibility requirements that need to be met in order to use the service?:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded value for the eligibility
    :param str comment: Describes the eligibility conditions for the service
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  comment:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.comment = comment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "HealthcareService":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "HealthcareService":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class HealthcareService(DomainResource):
    """ The details of a healthcare service available at a location or in a catalog.  In the case where there is a hierarchy of services (for example, Lab -> Pathology -> Wound Cultures), this can be represented using a set of linked HealthcareServices.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifiers for this item
    :param bool active: Whether this HealthcareService record is in active use
    :param Reference providedBy: Organization that provides this service
    :param Reference offeredIn: The service within which this service is offered
    :param CodeableConcept category: Broad category of service being performed or delivered
    :param CodeableConcept type: Type of service that may be delivered or performed
    :param CodeableConcept specialty: Specialties handled by the HealthcareService
    :param Reference location: Location(s) where service may be provided
    :param str name: Description of service as presented to a consumer while searching
    :param str comment: Additional description and/or any specific issues not covered elsewhere
    :param str extraDetails: Extra details about the service that can't be placed in the other fields
    :param Attachment photo: Facilitates quick identification of the service
    :param ExtendedContactDetail contact: Official contact details for the HealthcareService
    :param Reference coverageArea: Location(s) service is intended for/available to
    :param CodeableConcept serviceProvisionCode: Conditions under which service is available/offered
    :param Eligibility eligibility: Specific eligibility requirements required to use the service
    :param CodeableConcept program: Programs that this service is applicable to
    :param CodeableConcept characteristic: Collection of characteristics (attributes)
    :param CodeableConcept communication: The language that this service is offered in
    :param CodeableConcept referralMethod: Ways that the service accepts referrals
    :param bool appointmentRequired: If an appointment is required for access to this service
    :param Availability availability: Times the healthcare service is available (including exceptions)
    :param Reference endpoint: Technical endpoints providing access to electronic services operated for the healthcare service
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "providedBy": {"class_name": "Reference", "is_contained": False},
        
        
        "offeredIn": {"class_name": "Reference", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "photo": {"class_name": "Attachment", "is_contained": False},
        
        
        "contact": {"class_name": "ExtendedContactDetail", "is_contained": False},
        
        
        "coverageArea": {"class_name": "Reference", "is_contained": False},
        
        
        "serviceProvisionCode": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "eligibility": {"class_name": "Eligibility", "is_contained": True},
        
        
        "program": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "characteristic": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "communication": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "referralMethod": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "availability": {"class_name": "Availability", "is_contained": False},
        
        
        "endpoint": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  active:  'bool'  = None,  providedBy:  'Reference'  = None,  offeredIn:  list['Reference']  = None,  category:  list['CodeableConcept']  = None,  type:  list['CodeableConcept']  = None,  specialty:  list['CodeableConcept']  = None,  location:  list['Reference']  = None,  name:  'str'  = None,  comment:  'str'  = None,  extraDetails:  'str'  = None,  photo:  'Attachment'  = None,  contact:  list['ExtendedContactDetail']  = None,  coverageArea:  list['Reference']  = None,  serviceProvisionCode:  list['CodeableConcept']  = None,  eligibility:  list['Eligibility']  = None,  program:  list['CodeableConcept']  = None,  characteristic:  list['CodeableConcept']  = None,  communication:  list['CodeableConcept']  = None,  referralMethod:  list['CodeableConcept']  = None,  appointmentRequired:  'bool'  = None,  availability:  list['Availability']  = None,  endpoint:  list['Reference']  = None, ):
        self.resourceType = resourceType or "HealthcareService"
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
        self.providedBy = providedBy 
        self.offeredIn = offeredIn or []
        self.category = category or []
        self.type = type or []
        self.specialty = specialty or []
        self.location = location or []
        self.name = name 
        self.comment = comment 
        self.extraDetails = extraDetails 
        self.photo = photo 
        self.contact = contact or []
        self.coverageArea = coverageArea or []
        self.serviceProvisionCode = serviceProvisionCode or []
        self.eligibility = eligibility or []
        self.program = program or []
        self.characteristic = characteristic or []
        self.communication = communication or []
        self.referralMethod = referralMethod or []
        self.appointmentRequired = appointmentRequired 
        self.availability = availability or []
        self.endpoint = endpoint or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "HealthcareService":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "HealthcareService":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()