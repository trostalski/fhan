"""
Generated class for Condition. 
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
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Age import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Participant(BaseModel):
    """ Indicates who or what participated in the activities related to the condition and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of involvement
    :param Reference actor: Who or what participated in the activities related to the condition
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  function:  'CodeableConcept'  = None,  actor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function 
        self.actor = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Condition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Condition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Stage(BaseModel):
    """ A simple summary of the stage such as "Stage 3" or "Early Onset". The determination of the stage is disease-specific, such as cancer, retinopathy of prematurity, kidney diseases, Alzheimer's, or Parkinson disease.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept summary: Simple summary (disease specific)
    :param Reference assessment: Formal record of assessment
    :param CodeableConcept type: Kind of staging
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "summary": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "assessment": {"class_name": "Reference", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  summary:  'CodeableConcept'  = None,  assessment:  list['Reference']  = None,  type:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.summary = summary 
        self.assessment = assessment or []
        self.type = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Condition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Condition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Condition(DomainResource):
    """ A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this condition
    :param CodeableConcept clinicalStatus: active | recurrence | relapse | inactive | remission | resolved | unknown
    :param CodeableConcept verificationStatus: unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
    :param CodeableConcept category: problem-list-item | encounter-diagnosis
    :param CodeableConcept severity: Subjective severity of condition
    :param CodeableConcept code: Identification of the condition, problem or diagnosis
    :param CodeableConcept bodySite: Anatomical location, if relevant
    :param Reference subject: Who has the condition?
    :param Reference encounter: The Encounter during which this Condition was created
    :param str onsetDateTime: Estimated or actual date,  date-time, or age
    :param Age onsetAge: Estimated or actual date,  date-time, or age
    :param Period onsetPeriod: Estimated or actual date,  date-time, or age
    :param Range onsetRange: Estimated or actual date,  date-time, or age
    :param str onsetString: Estimated or actual date,  date-time, or age
    :param str abatementDateTime: When in resolution/remission
    :param Age abatementAge: When in resolution/remission
    :param Period abatementPeriod: When in resolution/remission
    :param Range abatementRange: When in resolution/remission
    :param str abatementString: When in resolution/remission
    :param str recordedDate: Date condition was first recorded
    :param Participant participant: Who or what participated in the activities related to the condition and how they were involved
    :param Stage stage: Stage/grade, usually assessed formally
    :param CodeableReference evidence: Supporting evidence for the verification status
    :param Annotation note: Additional information about the Condition
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "clinicalStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "verificationStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "severity": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "onsetAge": {"class_name": "Age", "is_contained": False},
        
        
        "onsetPeriod": {"class_name": "Period", "is_contained": False},
        
        
        "onsetRange": {"class_name": "Range", "is_contained": False},
        
        
        
        
        "abatementAge": {"class_name": "Age", "is_contained": False},
        
        
        "abatementPeriod": {"class_name": "Period", "is_contained": False},
        
        
        "abatementRange": {"class_name": "Range", "is_contained": False},
        
        
        
        
        "participant": {"class_name": "Participant", "is_contained": True},
        
        
        "stage": {"class_name": "Stage", "is_contained": True},
        
        
        "evidence": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  clinicalStatus:  'CodeableConcept'  = None,  verificationStatus:  'CodeableConcept'  = None,  category:  list['CodeableConcept']  = None,  severity:  'CodeableConcept'  = None,  code:  'CodeableConcept'  = None,  bodySite:  list['CodeableConcept']  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  onsetDateTime:  'str'  = None,  onsetAge:  'Age'  = None,  onsetPeriod:  'Period'  = None,  onsetRange:  'Range'  = None,  onsetString:  'str'  = None,  abatementDateTime:  'str'  = None,  abatementAge:  'Age'  = None,  abatementPeriod:  'Period'  = None,  abatementRange:  'Range'  = None,  abatementString:  'str'  = None,  recordedDate:  'str'  = None,  participant:  list['Participant']  = None,  stage:  list['Stage']  = None,  evidence:  list['CodeableReference']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "Condition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.clinicalStatus = clinicalStatus 
        self.verificationStatus = verificationStatus 
        self.category = category or []
        self.severity = severity 
        self.code = code 
        self.bodySite = bodySite or []
        self.subject = subject 
        self.encounter = encounter 
        self.onsetDateTime = onsetDateTime 
        self.onsetAge = onsetAge 
        self.onsetPeriod = onsetPeriod 
        self.onsetRange = onsetRange 
        self.onsetString = onsetString 
        self.abatementDateTime = abatementDateTime 
        self.abatementAge = abatementAge 
        self.abatementPeriod = abatementPeriod 
        self.abatementRange = abatementRange 
        self.abatementString = abatementString 
        self.recordedDate = recordedDate 
        self.participant = participant or []
        self.stage = stage or []
        self.evidence = evidence or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Condition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Condition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()