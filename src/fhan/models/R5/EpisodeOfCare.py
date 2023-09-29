"""
Generated class for EpisodeOfCare. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class StatusHistory(BaseModel):
    """ The history of statuses that the EpisodeOfCare has been through (without requiring processing the history of the resource).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: planned | waitlist | active | onhold | finished | cancelled | entered-in-error
    :param Period period: Duration the EpisodeOfCare was in the specified status
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  status:  'str'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.status = status 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EpisodeOfCare":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EpisodeOfCare":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Reason(BaseModel):
    """ The list of medical reasons that are expected to be addressed during the episode of care.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept use: What the reason value should be used for/as
    :param CodeableReference value: Medical reason to be addressed
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "use": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "value": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  use:  'CodeableConcept'  = None,  value:  list['CodeableReference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.use = use 
        self.value = value or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EpisodeOfCare":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EpisodeOfCare":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Diagnosis(BaseModel):
    """ The list of medical conditions that were addressed during the episode of care.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference condition: The medical condition that was addressed during the episode of care
    :param CodeableConcept use: Role that this diagnosis has within the episode of care (e.g. admission, billing, discharge …)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "condition": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "use": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  condition:  list['CodeableReference']  = None,  use:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.condition = condition or []
        self.use = use 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EpisodeOfCare":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EpisodeOfCare":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class EpisodeOfCare(DomainResource):
    """ An association between a patient and an organization / healthcare provider(s) during which time encounters may occur. The managing organization assumes a level of responsibility for the patient during this time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier(s) relevant for this EpisodeOfCare
    :param str status: planned | waitlist | active | onhold | finished | cancelled | entered-in-error
    :param StatusHistory statusHistory: Past list of status codes (the current status may be included to cover the start date of the status)
    :param CodeableConcept type: Type/class  - e.g. specialist referral, disease management
    :param Reason reason: The list of medical reasons that are expected to be addressed during the episode of care
    :param Diagnosis diagnosis: The list of medical conditions that were addressed during the episode of care
    :param Reference patient: The patient who is the focus of this episode of care
    :param Reference managingOrganization: Organization that assumes responsibility for care coordination
    :param Period period: Interval during responsibility is assumed
    :param Reference referralRequest: Originating Referral Request(s)
    :param Reference careManager: Care manager/care coordinator for the patient
    :param Reference careTeam: Other practitioners facilitating this episode of care
    :param Reference account: The set of accounts that may be used for billing for this EpisodeOfCare
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "statusHistory": {"class_name": "StatusHistory", "is_contained": True},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reason": {"class_name": "Reason", "is_contained": True},
        
        
        "diagnosis": {"class_name": "Diagnosis", "is_contained": True},
        
        
        "patient": {"class_name": "Reference", "is_contained": False},
        
        
        "managingOrganization": {"class_name": "Reference", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "referralRequest": {"class_name": "Reference", "is_contained": False},
        
        
        "careManager": {"class_name": "Reference", "is_contained": False},
        
        
        "careTeam": {"class_name": "Reference", "is_contained": False},
        
        
        "account": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  statusHistory:  list['StatusHistory']  = None,  type:  list['CodeableConcept']  = None,  reason:  list['Reason']  = None,  diagnosis:  list['Diagnosis']  = None,  patient:  'Reference'  = None,  managingOrganization:  'Reference'  = None,  period:  'Period'  = None,  referralRequest:  list['Reference']  = None,  careManager:  'Reference'  = None,  careTeam:  list['Reference']  = None,  account:  list['Reference']  = None, ):
        self.resourceType = resourceType or "EpisodeOfCare"
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
        self.statusHistory = statusHistory or []
        self.type = type or []
        self.reason = reason or []
        self.diagnosis = diagnosis or []
        self.patient = patient 
        self.managingOrganization = managingOrganization 
        self.period = period 
        self.referralRequest = referralRequest or []
        self.careManager = careManager 
        self.careTeam = careTeam or []
        self.account = account or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EpisodeOfCare":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EpisodeOfCare":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()