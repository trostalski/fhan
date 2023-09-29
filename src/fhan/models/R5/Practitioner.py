"""
Generated class for Practitioner. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Address import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.HumanName import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Qualification(BaseModel):
    """ The official qualifications, certifications, accreditations, training, licenses (and other types of educations/skills/capabilities) that authorize or otherwise pertain to the provision of care by the practitioner.For example, a medical license issued by a medical board of licensure authorizing the practitioner to practice medicine within a certain locality.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: An identifier for this qualification for the practitioner
    :param CodeableConcept code: Coded representation of the qualification
    :param Period period: Period during which the qualification is valid
    :param Reference issuer: Organization that regulates and issues the qualification
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "issuer": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  code:  'CodeableConcept'  = None,  period:  'Period'  = None,  issuer:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.code = code 
        self.period = period 
        self.issuer = issuer 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Practitioner":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Practitioner":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Communication(BaseModel):
    """ A language which may be used to communicate with the practitioner, often for correspondence/administrative purposes.The `PractitionerRole.communication` property should be used for publishing the languages that a practitioner is able to communicate with patients (on a per Organization/Role basis).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept language: The language code used to communicate with the practitioner
    :param bool preferred: Language preference indicator
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "language": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  language:  'CodeableConcept'  = None,  preferred:  'bool'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.language = language 
        self.preferred = preferred 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Practitioner":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Practitioner":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Practitioner(DomainResource):
    """ A person who is directly or indirectly involved in the provisioning of healthcare or related services.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: An identifier for the person as this agent
    :param bool active: Whether this practitioner's record is in active use
    :param HumanName name: The name(s) associated with the practitioner
    :param ContactPoint telecom: A contact detail for the practitioner (that apply to all roles)
    :param str gender: male | female | other | unknown
    :param str birthDate: The date  on which the practitioner was born
    :param bool deceasedBoolean: Indicates if the practitioner is deceased or not
    :param str deceasedDateTime: Indicates if the practitioner is deceased or not
    :param Address address: Address(es) of the practitioner that are not role specific (typically home address)
    :param Attachment photo: Image of the person
    :param Qualification qualification: Qualifications, certifications, accreditations, licenses, training, etc. pertaining to the provision of care
    :param Communication communication: A language which may be used to communicate with the practitioner
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "name": {"class_name": "HumanName", "is_contained": False},
        
        
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        
        
        
        
        
        
        "address": {"class_name": "Address", "is_contained": False},
        
        
        "photo": {"class_name": "Attachment", "is_contained": False},
        
        
        "qualification": {"class_name": "Qualification", "is_contained": True},
        
        
        "communication": {"class_name": "Communication", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  active:  'bool'  = None,  name:  list['HumanName']  = None,  telecom:  list['ContactPoint']  = None,  gender:  'str'  = None,  birthDate:  'str'  = None,  deceasedBoolean:  'bool'  = None,  deceasedDateTime:  'str'  = None,  address:  list['Address']  = None,  photo:  list['Attachment']  = None,  qualification:  list['Qualification']  = None,  communication:  list['Communication']  = None, ):
        self.resourceType = resourceType or "Practitioner"
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
        self.name = name or []
        self.telecom = telecom or []
        self.gender = gender 
        self.birthDate = birthDate 
        self.deceasedBoolean = deceasedBoolean 
        self.deceasedDateTime = deceasedDateTime 
        self.address = address or []
        self.photo = photo or []
        self.qualification = qualification or []
        self.communication = communication or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Practitioner":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Practitioner":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()