"""
Generated class for Organization. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Qualification(BaseModel):
    """ The official certifications, accreditations, training, designations and licenses that authorize and/or otherwise endorse the provision of care by the organization.For example, an approval to provide a type of services issued by a certifying body (such as the US Joint Commission) to an organization.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: An identifier for this qualification for the organization
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
    def from_dict(cls, data: dict) -> "Organization":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Organization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Organization(DomainResource):
    """ A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action.  Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifies this organization  across multiple systems
    :param bool active: Whether the organization's record is still in active use
    :param CodeableConcept type: Kind of organization
    :param str name: Name used for the organization
    :param str alias: A list of alternate names that the organization is known as, or was known as in the past
    :param str description: Additional details about the Organization that could be displayed as further information to identify the Organization beyond its name
    :param ExtendedContactDetail contact: Official contact details for the Organization
    :param Reference partOf: The organization of which this organization forms a part
    :param Reference endpoint: Technical endpoints providing access to services operated for the organization
    :param Qualification qualification: Qualifications, certifications, accreditations, licenses, training, etc. pertaining to the provision of care
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "contact": {"class_name": "ExtendedContactDetail", "is_contained": False},
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        "endpoint": {"class_name": "Reference", "is_contained": False},
        
        
        "qualification": {"class_name": "Qualification", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  active:  'bool'  = None,  type:  list['CodeableConcept']  = None,  name:  'str'  = None,  alias:  list['str']  = None,  description:  'str'  = None,  contact:  list['ExtendedContactDetail']  = None,  partOf:  'Reference'  = None,  endpoint:  list['Reference']  = None,  qualification:  list['Qualification']  = None, ):
        self.resourceType = resourceType or "Organization"
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
        self.type = type or []
        self.name = name 
        self.alias = alias or []
        self.description = description 
        self.contact = contact or []
        self.partOf = partOf 
        self.endpoint = endpoint or []
        self.qualification = qualification or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Organization":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Organization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()