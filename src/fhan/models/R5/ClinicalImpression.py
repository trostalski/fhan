"""
Generated class for ClinicalImpression. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ClinicalImpression:
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
    :param str effectivedateTime: Time of assessment
    :param Period effectivedateTime: Time of assessment
    :param str date: When the assessment was documented
    :param Reference performer: The clinician performing the assessment
    :param Reference previous: Reference to last assessment
    :param Reference problem: Relevant impressions of patient state
    :param CodeableConcept changePattern: Change in the status/pattern of a subject's condition since previously assessed, such as worsening, improving, or no change
    :param str protocol: Clinical Protocol followed
    :param str summary: Summary of the assessment
    :param BackboneElement finding: Possible or likely findings and diagnoses
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: What was found
    :param str basis: Which investigations support finding
    :param CodeableConcept prognosisCodeableConcept: Estimate of likely outcome
    :param Reference prognosisReference: RiskAssessment expressing likely outcome
    :param Reference supportingInfo: Information supporting the clinical impression
    :param Annotation note: Comments made about the ClinicalImpression
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    description: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    effectivedateTime: str = None
    
    effectivedateTime: "Period" = None
    
    date: str = None
    
    performer: "Reference" = None
    
    previous: "Reference" = None
    
    problem: "Reference" = None
    
    changePattern: "CodeableConcept" = None
    
    protocol: str = None
    
    summary: str = None
    
    finding: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    item: "CodeableReference" = None
    
    basis: str = None
    
    prognosisCodeableConcept: "CodeableConcept" = None
    
    prognosisReference: "Reference" = None
    
    supportingInfo: "Reference" = None
    
    note: "Annotation" = None
    