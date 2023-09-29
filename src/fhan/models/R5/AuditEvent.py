"""
Generated class for AuditEvent. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Outcome(BaseModel):
    """ Indicates whether the event succeeded or failed. A free text descripiton can be given in outcome.text.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding code: Whether the event succeeded or failed
    :param CodeableConcept detail: Additional outcome detail
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "Coding", "is_contained": False},
        
        
        "detail": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'Coding'  = None,  detail:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.detail = detail or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Agent(BaseModel):
    """ An actor taking an active role in the event or activity that is logged.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: How agent participated
    :param CodeableConcept role: Agent role in the event
    :param Reference who: Identifier of who
    :param bool requestor: Whether user is initiator
    :param Reference location: The agent location when the event occurred
    :param str policy: Policy that authorized the agent participation in the event
    :param Reference networkReference: This agent network location for the activity
    :param str networkUri: This agent network location for the activity
    :param str networkString: This agent network location for the activity
    :param CodeableConcept authorization: Allowable authorization for this agent
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "who": {"class_name": "Reference", "is_contained": False},
        
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        
        "networkReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        "authorization": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  role:  list['CodeableConcept']  = None,  who:  'Reference'  = None,  requestor:  'bool'  = None,  location:  'Reference'  = None,  policy:  list['str']  = None,  networkReference:  'Reference'  = None,  networkUri:  'str'  = None,  networkString:  'str'  = None,  authorization:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.role = role or []
        self.who = who 
        self.requestor = requestor 
        self.location = location 
        self.policy = policy or []
        self.networkReference = networkReference 
        self.networkUri = networkUri 
        self.networkString = networkString 
        self.authorization = authorization or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Source(BaseModel):
    """ The actor that is reporting the event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference site: Logical source location within the enterprise
    :param Reference observer: The identity of source detecting the event
    :param CodeableConcept type: The type of source where event originated
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "site": {"class_name": "Reference", "is_contained": False},
        
        
        "observer": {"class_name": "Reference", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  site:  'Reference'  = None,  observer:  'Reference'  = None,  type:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.site = site 
        self.observer = observer 
        self.type = type or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Detail(BaseModel):
    """ Tagged value pairs for conveying additional information about the entity.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Name of the property
    :param Quantity valueQuantity: Property value
    :param CodeableConcept valueCodeableConcept: Property value
    :param str valueString: Property value
    :param bool valueBoolean: Property value
    :param int valueInteger: Property value
    :param Range valueRange: Property value
    :param Ratio valueRatio: Property value
    :param str valueTime: Property value
    :param str valueDateTime: Property value
    :param Period valuePeriod: Property value
    :param str valueBase64Binary: Property value
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        "valueRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        
        
        "valuePeriod": {"class_name": "Period", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueString:  'str'  = None,  valueBoolean:  'bool'  = None,  valueInteger:  'int'  = None,  valueRange:  'Range'  = None,  valueRatio:  'Ratio'  = None,  valueTime:  'str'  = None,  valueDateTime:  'str'  = None,  valuePeriod:  'Period'  = None,  valueBase64Binary:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueQuantity = valueQuantity 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueString = valueString 
        self.valueBoolean = valueBoolean 
        self.valueInteger = valueInteger 
        self.valueRange = valueRange 
        self.valueRatio = valueRatio 
        self.valueTime = valueTime 
        self.valueDateTime = valueDateTime 
        self.valuePeriod = valuePeriod 
        self.valueBase64Binary = valueBase64Binary 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Entity(BaseModel):
    """ Specific instances of data or objects that have been accessed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference what: Specific instance of resource
    :param CodeableConcept role: What role the entity played
    :param CodeableConcept securityLabel: Security labels on the entity
    :param str query: Query parameters
    :param Detail detail: Additional Information about the entity
    :param Agent agent: Entity is attributed to this agent
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "what": {"class_name": "Reference", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "securityLabel": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "detail": {"class_name": "Detail", "is_contained": True},
        
        
        "agent": {"class_name": "Agent", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  what:  'Reference'  = None,  role:  'CodeableConcept'  = None,  securityLabel:  list['CodeableConcept']  = None,  query:  'str'  = None,  detail:  list['Detail']  = None,  agent:  list['Agent']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.what = what 
        self.role = role 
        self.securityLabel = securityLabel or []
        self.query = query 
        self.detail = detail or []
        self.agent = agent or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AuditEvent(DomainResource):
    """ A record of an event relevant for purposes such as operations, privacy, security, maintenance, and performance analysis.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept category: Type/identifier of event
    :param CodeableConcept code: Specific type of event
    :param str action: Type of action performed during the event
    :param str severity: emergency | alert | critical | error | warning | notice | informational | debug
    :param Period occurredPeriod: When the activity occurred
    :param str occurredDateTime: When the activity occurred
    :param str recorded: Time when the event was recorded
    :param Outcome outcome: Whether the event succeeded or failed
    :param CodeableConcept authorization: Authorization related to the event
    :param Reference basedOn: Workflow authorization within which this event occurred
    :param Reference patient: The patient is the subject of the data used/created/updated/deleted during the activity
    :param Reference encounter: Encounter within which this event occurred or which the event is tightly associated
    :param Agent agent: Actor involved in the event
    :param Source source: Audit Event Reporter
    :param Entity entity: Data or objects used
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "occurredPeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        
        "outcome": {"class_name": "Outcome", "is_contained": True},
        
        
        "authorization": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "patient": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        "agent": {"class_name": "Agent", "is_contained": True},
        
        
        "source": {"class_name": "Source", "is_contained": True},
        
        
        "entity": {"class_name": "Entity", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  category:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  action:  'str'  = None,  severity:  'str'  = None,  occurredPeriod:  'Period'  = None,  occurredDateTime:  'str'  = None,  recorded:  'str'  = None,  outcome:  'Outcome'  = None,  authorization:  list['CodeableConcept']  = None,  basedOn:  list['Reference']  = None,  patient:  'Reference'  = None,  encounter:  'Reference'  = None,  agent:  list['Agent']  = None,  source:  'Source'  = None,  entity:  list['Entity']  = None, ):
        self.resourceType = resourceType or "AuditEvent"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category or []
        self.code = code 
        self.action = action 
        self.severity = severity 
        self.occurredPeriod = occurredPeriod 
        self.occurredDateTime = occurredDateTime 
        self.recorded = recorded 
        self.outcome = outcome 
        self.authorization = authorization or []
        self.basedOn = basedOn or []
        self.patient = patient 
        self.encounter = encounter 
        self.agent = agent or []
        self.source = source 
        self.entity = entity or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AuditEvent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AuditEvent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()