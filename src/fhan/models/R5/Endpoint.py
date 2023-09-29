"""
Generated class for Endpoint. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Payload(BaseModel):
    """ The set of payloads that are provided/available at this endpoint.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
    :param str mimeType: Mimetype to send. If not specified, the content could be anything (including no payload, if the connectionType defined this)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  list['CodeableConcept']  = None,  mimeType:  list['str']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type or []
        self.mimeType = mimeType or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Endpoint":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Endpoint":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Endpoint(DomainResource):
    """ The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b, a REST endpoint for another FHIR server, or a s/Mime email address. This may include any security context information.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifies this endpoint across multiple systems
    :param str status: active | suspended | error | off | entered-in-error | test
    :param CodeableConcept connectionType: Protocol/Profile/Standard to be used with this endpoint connection
    :param str name: A name that this endpoint can be identified by
    :param str description: Additional details about the endpoint that could be displayed as further information to identify the description beyond its name
    :param CodeableConcept environmentType: The type of environment(s) exposed at this endpoint
    :param Reference managingOrganization: Organization that manages this endpoint (might not be the organization that exposes the endpoint)
    :param ContactPoint contact: Contact details for source (e.g. troubleshooting)
    :param Period period: Interval the endpoint is expected to be operational
    :param Payload payload: Set of payloads that are provided by this endpoint
    :param str address: The technical base address for connecting to this endpoint
    :param str header: Usage depends on the channel type
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "connectionType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "environmentType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "managingOrganization": {"class_name": "Reference", "is_contained": False},
        
        
        "contact": {"class_name": "ContactPoint", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "payload": {"class_name": "Payload", "is_contained": True},
        
        
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  connectionType:  list['CodeableConcept']  = None,  name:  'str'  = None,  description:  'str'  = None,  environmentType:  list['CodeableConcept']  = None,  managingOrganization:  'Reference'  = None,  contact:  list['ContactPoint']  = None,  period:  'Period'  = None,  payload:  list['Payload']  = None,  address:  'str'  = None,  header:  list['str']  = None, ):
        self.resourceType = resourceType or "Endpoint"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status 
        self.connectionType = connectionType or []
        self.name = name 
        self.description = description 
        self.environmentType = environmentType or []
        self.managingOrganization = managingOrganization 
        self.contact = contact or []
        self.period = period 
        self.payload = payload or []
        self.address = address 
        self.header = header or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Endpoint":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Endpoint":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()