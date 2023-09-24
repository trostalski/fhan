"""
Generated class for ClinicalImpression. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Investigation(ModelBase):
    """ One or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomes.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: A name/code for the set
    :param list['Reference'] item: Record of a specific investigation
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  item: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.item: list['Reference'] = item or []
        

    
    

class Finding(ModelBase):
    """ Specific findings or diagnoses that were considered likely or relevant to ongoing treatment.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' itemCodeableConcept: What was found
    :param 'Reference' itemReference: What was found
    :param str basis: Which investigations support finding
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  itemCodeableConcept: 'CodeableConcept' = None,  itemReference: 'Reference' = None,  basis: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemCodeableConcept: 'CodeableConcept' = itemCodeableConcept 
        self.itemReference: 'Reference' = itemReference 
        self.basis: str = basis 
        

class ClinicalImpression(DomainResource):
    """ A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient's condition. Assessments are often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the recording of assessment tools such as Apgar score.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier
    :param str status: in-progress | completed | entered-in-error
    :param 'CodeableConcept' statusReason: Reason for current status
    :param 'CodeableConcept' code: Kind of assessment performed
    :param str description: Why/how the assessment was performed
    :param 'Reference' subject: Patient or group assessed
    :param 'Reference' encounter: Encounter created as part of
    :param str effectiveDateTime: Time of assessment
    :param str date: When the assessment was documented
    :param 'Reference' assessor: The clinician performing the assessment
    :param 'Reference' previous: Reference to last assessment
    :param list['Reference'] problem: Relevant impressions of patient state
    :param list['Investigation'] investigation: One or more sets of investigations (signs, symptoms, etc.)
    :param str protocol: Clinical Protocol followed
    :param str summary: Summary of the assessment
    :param list['Finding'] finding: Possible or likely findings and diagnoses
    :param list['CodeableConcept'] prognosisCodeableConcept: Estimate of likely outcome
    :param list['Reference'] prognosisReference: RiskAssessment expressing likely outcome
    :param list['Reference'] supportingInfo: Information supporting the clinical impression
    :param list['Annotation'] note: Comments made about the ClinicalImpression
    """
    def __init__(self, resourceType: str = "ClinicalImpression",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  description: str = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  effectiveDateTime: str = None,  date: str = None,  assessor: 'Reference' = None,  previous: 'Reference' = None,  problem: list['Reference'] = None,  investigation: list['Investigation'] = None,  protocol: str = None,  summary: str = None,  finding: list['Finding'] = None,  prognosisCodeableConcept: list['CodeableConcept'] = None,  prognosisReference: list['Reference'] = None,  supportingInfo: list['Reference'] = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "ClinicalImpression"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.code: 'CodeableConcept' = code 
        self.description: str = description 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.effectiveDateTime: str = effectiveDateTime 
        self.date: str = date 
        self.assessor: 'Reference' = assessor 
        self.previous: 'Reference' = previous 
        self.problem: list['Reference'] = problem or []
        self.investigation: list['Investigation'] = investigation or []
        self.protocol: str = protocol or []
        self.summary: str = summary 
        self.finding: list['Finding'] = finding or []
        self.prognosisCodeableConcept: list['CodeableConcept'] = prognosisCodeableConcept or []
        self.prognosisReference: list['Reference'] = prognosisReference or []
        self.supportingInfo: list['Reference'] = supportingInfo or []
        self.note: list['Annotation'] = note or []
        