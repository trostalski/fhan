"""
Generated class for CarePlan. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Activity(BaseModel):
    """ Identifies an action that has occurred or is a planned action to occur as part of the plan. For example, a medication to be used, lab tests to perform, self-monitoring that has occurred, education etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference performedActivity: Results of the activity (concept, or Appointment, Encounter, Procedure, etc.)
    :param Annotation progress: Comments about the activity status/progress
    :param Reference plannedActivityReference: Activity that is intended to be part of the care plan
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "performedActivity": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "progress": {"class_name": "Annotation", "is_contained": False},
        
        
        "plannedActivityReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  performedActivity:  list['CodeableReference']  = None,  progress:  list['Annotation']  = None,  plannedActivityReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.performedActivity = performedActivity or []
        self.progress = progress or []
        self.plannedActivityReference = plannedActivityReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "CarePlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "CarePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CarePlan(DomainResource):
    """ Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this plan
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference replaces: CarePlan replaced by this CarePlan
    :param Reference partOf: Part of referenced CarePlan
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | order | option | directive
    :param CodeableConcept category: Type of plan
    :param str title: Human-friendly name for the care plan
    :param str description: Summary of nature of plan
    :param Reference subject: Who the care plan is for
    :param Reference encounter: The Encounter during which this CarePlan was created
    :param Period period: Time period plan covers
    :param str created: Date record was first recorded
    :param Reference custodian: Who is the designated responsible party
    :param Reference contributor: Who provided the content of the care plan
    :param Reference careTeam: Who's involved in plan?
    :param CodeableReference addresses: Health issues this plan addresses
    :param Reference supportingInfo: Information considered as part of plan
    :param Reference goal: Desired outcome of plan
    :param Activity activity: Action to occur or has occurred as part of plan
    :param Annotation note: Comments about the plan
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "replaces": {"class_name": "Reference", "is_contained": False},
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        
        "custodian": {"class_name": "Reference", "is_contained": False},
        
        
        "contributor": {"class_name": "Reference", "is_contained": False},
        
        
        "careTeam": {"class_name": "Reference", "is_contained": False},
        
        
        "addresses": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "supportingInfo": {"class_name": "Reference", "is_contained": False},
        
        
        "goal": {"class_name": "Reference", "is_contained": False},
        
        
        "activity": {"class_name": "Activity", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instantiatesCanonical:  list['str']  = None,  instantiatesUri:  list['str']  = None,  basedOn:  list['Reference']  = None,  replaces:  list['Reference']  = None,  partOf:  list['Reference']  = None,  status:  'str'  = None,  intent:  'str'  = None,  category:  list['CodeableConcept']  = None,  title:  'str'  = None,  description:  'str'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  period:  'Period'  = None,  created:  'str'  = None,  custodian:  'Reference'  = None,  contributor:  list['Reference']  = None,  careTeam:  list['Reference']  = None,  addresses:  list['CodeableReference']  = None,  supportingInfo:  list['Reference']  = None,  goal:  list['Reference']  = None,  activity:  list['Activity']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "CarePlan"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.basedOn = basedOn or []
        self.replaces = replaces or []
        self.partOf = partOf or []
        self.status = status 
        self.intent = intent 
        self.category = category or []
        self.title = title 
        self.description = description 
        self.subject = subject 
        self.encounter = encounter 
        self.period = period 
        self.created = created 
        self.custodian = custodian 
        self.contributor = contributor or []
        self.careTeam = careTeam or []
        self.addresses = addresses or []
        self.supportingInfo = supportingInfo or []
        self.goal = goal or []
        self.activity = activity or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "CarePlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "CarePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()