"""
Generated class for ClinicalImpression. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Investigation(Element):
    """ One or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomes.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: A name/code for the set
    :param Reference item: Record of a specific investigation
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    code: "CodeableConcept" = CodeableConcept()
    item: list[Reference] = Reference() 
    

    
    
@dataclass
class Finding(Element):
    """ Specific findings or diagnoses that were considered likely or relevant to ongoing treatment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept itemCodeableConcept: What was found
    :param Reference itemReference: What was found
    :param str basis: Which investigations support finding
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    itemCodeableConcept: "CodeableConcept" = CodeableConcept()
    itemReference: "Reference" = Reference()
    
    basis: str = None
    

@dataclass
class ClinicalImpression(ModelBase):
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
    :param str status: in-progress | completed | entered-in-error
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept code: Kind of assessment performed
    :param str description: Why/how the assessment was performed
    :param Reference subject: Patient or group assessed
    :param Reference encounter: Encounter created as part of
    :param str effectiveDateTime: Time of assessment
    :param str date: When the assessment was documented
    :param Reference assessor: The clinician performing the assessment
    :param Reference previous: Reference to last assessment
    :param Reference problem: Relevant impressions of patient state
    :param Investigation investigation: One or more sets of investigations (signs, symptoms, etc.)
    :param str protocol: Clinical Protocol followed
    :param str summary: Summary of the assessment
    :param Finding finding: Possible or likely findings and diagnoses
    :param CodeableConcept prognosisCodeableConcept: Estimate of likely outcome
    :param Reference prognosisReference: RiskAssessment expressing likely outcome
    :param Reference supportingInfo: Information supporting the clinical impression
    :param Annotation note: Comments made about the ClinicalImpression
    """

    resourceType: str = "ClinicalImpression"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    statusReason: "CodeableConcept" = CodeableConcept()
    
    code: "CodeableConcept" = CodeableConcept()
    
    description: str = None
    
    subject: "Reference" = Reference()
    
    encounter: "Reference" = Reference()
    
    effectiveDateTime: str = None
    
    date: str = None
    
    assessor: "Reference" = Reference()
    
    previous: "Reference" = Reference()
    
    problem: list[Reference] = Reference() 
    
    investigation: list[Investigation] = Investigation() 
    
    protocol: str = None
    
    summary: str = None
    
    finding: list[Finding] = Finding() 
    
    prognosisCodeableConcept: list[CodeableConcept] = CodeableConcept() 
    
    prognosisReference: list[Reference] = Reference() 
    
    supportingInfo: list[Reference] = Reference() 
    
    note: list[Annotation] = Annotation() 
    