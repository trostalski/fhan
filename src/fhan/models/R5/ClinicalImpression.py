"""
Generated class for ClinicalImpression. 
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


    
    

class Finding(BaseModel):
    """ Specific findings or diagnoses that were considered likely or relevant to ongoing treatment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: What was found
    :param str basis: Which investigations support finding
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "item": {"class_name": "CodeableReference", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  item:  'CodeableReference'  = None,  basis:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.item = item 
        self.basis = basis 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalImpression":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalImpression":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ClinicalImpression(DomainResource):
    """ A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient's condition. Assessments are often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the recording of assessment tools such as Apgar score.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param str description: Why/how the assessment was performed
    :param Reference subject: Patient or group assessed
    :param Reference encounter: The Encounter during which this ClinicalImpression was created
    :param str effectiveDateTime: Time of assessment
    :param Period effectivePeriod: Time of assessment
    :param str date: When the assessment was documented
    :param Reference performer: The clinician performing the assessment
    :param Reference previous: Reference to last assessment
    :param Reference problem: Relevant impressions of patient state
    :param CodeableConcept changePattern: Change in the status/pattern of a subject's condition since previously assessed, such as worsening, improving, or no change
    :param str protocol: Clinical Protocol followed
    :param str summary: Summary of the assessment
    :param Finding finding: Possible or likely findings and diagnoses
    :param CodeableConcept prognosisCodeableConcept: Estimate of likely outcome
    :param Reference prognosisReference: RiskAssessment expressing likely outcome
    :param Reference supportingInfo: Information supporting the clinical impression
    :param Annotation note: Comments made about the ClinicalImpression
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        "performer": {"class_name": "Reference", "is_contained": False},
        
        
        "previous": {"class_name": "Reference", "is_contained": False},
        
        
        "problem": {"class_name": "Reference", "is_contained": False},
        
        
        "changePattern": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "finding": {"class_name": "Finding", "is_contained": True},
        
        
        "prognosisCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "prognosisReference": {"class_name": "Reference", "is_contained": False},
        
        
        "supportingInfo": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  statusReason:  'CodeableConcept'  = None,  description:  'str'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  effectiveDateTime:  'str'  = None,  effectivePeriod:  'Period'  = None,  date:  'str'  = None,  performer:  'Reference'  = None,  previous:  'Reference'  = None,  problem:  list['Reference']  = None,  changePattern:  'CodeableConcept'  = None,  protocol:  list['str']  = None,  summary:  'str'  = None,  finding:  list['Finding']  = None,  prognosisCodeableConcept:  list['CodeableConcept']  = None,  prognosisReference:  list['Reference']  = None,  supportingInfo:  list['Reference']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "ClinicalImpression"
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
        self.statusReason = statusReason 
        self.description = description 
        self.subject = subject 
        self.encounter = encounter 
        self.effectiveDateTime = effectiveDateTime 
        self.effectivePeriod = effectivePeriod 
        self.date = date 
        self.performer = performer 
        self.previous = previous 
        self.problem = problem or []
        self.changePattern = changePattern 
        self.protocol = protocol or []
        self.summary = summary 
        self.finding = finding or []
        self.prognosisCodeableConcept = prognosisCodeableConcept or []
        self.prognosisReference = prognosisReference or []
        self.supportingInfo = supportingInfo or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalImpression":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalImpression":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()