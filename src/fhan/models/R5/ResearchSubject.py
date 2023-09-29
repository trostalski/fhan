"""
Generated class for ResearchSubject. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Progress(BaseModel):
    """ The current state (status) of the subject and resons for status change where appropriate.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: state | milestone
    :param CodeableConcept subjectState: candidate | eligible | follow-up | ineligible | not-registered | off-study | on-study | on-study-intervention | on-study-observation | pending-on-study | potential-candidate | screening | withdrawn
    :param CodeableConcept milestone: SignedUp | Screened | Randomized
    :param CodeableConcept reason: State change reason
    :param str startDate: State change date
    :param str endDate: State change date
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subjectState": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "milestone": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  subjectState:  'CodeableConcept'  = None,  milestone:  'CodeableConcept'  = None,  reason:  'CodeableConcept'  = None,  startDate:  'str'  = None,  endDate:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.subjectState = subjectState 
        self.milestone = milestone 
        self.reason = reason 
        self.startDate = startDate 
        self.endDate = endDate 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchSubject":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchSubject":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ResearchSubject(DomainResource):
    """ A ResearchSubject is a participant or object which is the recipient of investigative activities in a research study.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for research subject in a study
    :param str status: draft | active | retired | unknown
    :param Progress progress: Subject status
    :param Period period: Start and end of participation
    :param Reference study: Study subject is part of
    :param Reference subject: Who or what is part of study
    :param str assignedComparisonGroup: What path should be followed
    :param str actualComparisonGroup: What path was followed
    :param Reference consent: Agreement to participate in study
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "progress": {"class_name": "Progress", "is_contained": True},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "study": {"class_name": "Reference", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        "consent": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  progress:  list['Progress']  = None,  period:  'Period'  = None,  study:  'Reference'  = None,  subject:  'Reference'  = None,  assignedComparisonGroup:  'str'  = None,  actualComparisonGroup:  'str'  = None,  consent:  list['Reference']  = None, ):
        self.resourceType = resourceType or "ResearchSubject"
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
        self.progress = progress or []
        self.period = period 
        self.study = study 
        self.subject = subject 
        self.assignedComparisonGroup = assignedComparisonGroup 
        self.actualComparisonGroup = actualComparisonGroup 
        self.consent = consent or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchSubject":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchSubject":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()