"""
Generated class for Goal. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Target(BaseModel):
    """ Indicates what should be done by when.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept measure: The parameter whose value is being tracked
    :param Quantity detailQuantity: The target value to be achieved
    :param Range detailRange: The target value to be achieved
    :param CodeableConcept detailCodeableConcept: The target value to be achieved
    :param str detailString: The target value to be achieved
    :param bool detailBoolean: The target value to be achieved
    :param int detailInteger: The target value to be achieved
    :param Ratio detailRatio: The target value to be achieved
    :param str dueDate: Reach goal on or before
    :param Duration dueDuration: Reach goal on or before
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "measure": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "detailQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "detailRange": {"class_name": "Range", "is_contained": False},
        
        
        "detailCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "detailRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        
        "dueDuration": {"class_name": "Duration", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  measure:  'CodeableConcept'  = None,  detailQuantity:  'Quantity'  = None,  detailRange:  'Range'  = None,  detailCodeableConcept:  'CodeableConcept'  = None,  detailString:  'str'  = None,  detailBoolean:  'bool'  = None,  detailInteger:  'int'  = None,  detailRatio:  'Ratio'  = None,  dueDate:  'str'  = None,  dueDuration:  'Duration'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.measure = measure 
        self.detailQuantity = detailQuantity 
        self.detailRange = detailRange 
        self.detailCodeableConcept = detailCodeableConcept 
        self.detailString = detailString 
        self.detailBoolean = detailBoolean 
        self.detailInteger = detailInteger 
        self.detailRatio = detailRatio 
        self.dueDate = dueDate 
        self.dueDuration = dueDuration 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Goal":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Goal":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Goal(DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this goal
    :param str lifecycleStatus: proposed | planned | accepted | active | on-hold | completed | cancelled | entered-in-error | rejected
    :param CodeableConcept achievementStatus: in-progress | improving | worsening | no-change | achieved | sustaining | not-achieved | no-progress | not-attainable
    :param CodeableConcept category: E.g. Treatment, dietary, behavioral, etc
    :param bool continuous: After meeting the goal, ongoing activity is needed to sustain the goal objective
    :param CodeableConcept priority: high-priority | medium-priority | low-priority
    :param CodeableConcept description: Code or text describing goal
    :param Reference subject: Who this goal is intended for
    :param str startDate: When goal pursuit begins
    :param CodeableConcept startCodeableConcept: When goal pursuit begins
    :param Target target: Target outcome for the goal
    :param str statusDate: When goal status took effect
    :param str statusReason: Reason for current status
    :param Reference source: Who's responsible for creating Goal?
    :param Reference addresses: Issues addressed by this goal
    :param Annotation note: Comments about the goal
    :param CodeableReference outcome: What result was achieved regarding the goal?
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "achievementStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "priority": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "description": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        
        "startCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "target": {"class_name": "Target", "is_contained": True},
        
        
        
        
        "source": {"class_name": "Reference", "is_contained": False},
        
        
        "addresses": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "outcome": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  lifecycleStatus:  'str'  = None,  achievementStatus:  'CodeableConcept'  = None,  category:  list['CodeableConcept']  = None,  continuous:  'bool'  = None,  priority:  'CodeableConcept'  = None,  description:  'CodeableConcept'  = None,  subject:  'Reference'  = None,  startDate:  'str'  = None,  startCodeableConcept:  'CodeableConcept'  = None,  target:  list['Target']  = None,  statusDate:  'str'  = None,  statusReason:  'str'  = None,  source:  'Reference'  = None,  addresses:  list['Reference']  = None,  note:  list['Annotation']  = None,  outcome:  list['CodeableReference']  = None, ):
        self.resourceType = resourceType or "Goal"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.lifecycleStatus = lifecycleStatus 
        self.achievementStatus = achievementStatus 
        self.category = category or []
        self.continuous = continuous 
        self.priority = priority 
        self.description = description 
        self.subject = subject 
        self.startDate = startDate 
        self.startCodeableConcept = startCodeableConcept 
        self.target = target or []
        self.statusDate = statusDate 
        self.statusReason = statusReason 
        self.source = source 
        self.addresses = addresses or []
        self.note = note or []
        self.outcome = outcome or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Goal":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Goal":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()