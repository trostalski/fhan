"""
Generated class for Condition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Age import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class Condition:
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
    :param str onsetdateTime: Estimated or actual date,  date-time, or age
    :param Age onsetdateTime: Estimated or actual date,  date-time, or age
    :param Period onsetdateTime: Estimated or actual date,  date-time, or age
    :param Range onsetdateTime: Estimated or actual date,  date-time, or age
    :param str onsetdateTime: Estimated or actual date,  date-time, or age
    :param str abatementdateTime: When in resolution/remission
    :param Age abatementdateTime: When in resolution/remission
    :param Period abatementdateTime: When in resolution/remission
    :param Range abatementdateTime: When in resolution/remission
    :param str abatementdateTime: When in resolution/remission
    :param str recordedDate: Date condition was first recorded
    :param BackboneElement participant: Who or what participated in the activities related to the condition and how they were involved
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of involvement
    :param Reference actor: Who or what participated in the activities related to the condition
    :param BackboneElement stage: Stage/grade, usually assessed formally
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept summary: Simple summary (disease specific)
    :param Reference assessment: Formal record of assessment
    :param CodeableConcept type: Kind of staging
    :param CodeableReference evidence: Supporting evidence for the verification status
    :param Annotation note: Additional information about the Condition
    
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
    
    clinicalStatus: "CodeableConcept" = None
    
    verificationStatus: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    severity: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    bodySite: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    onsetdateTime: str = None
    
    onsetdateTime: "Age" = None
    
    onsetdateTime: "Period" = None
    
    onsetdateTime: "Range" = None
    
    onsetdateTime: str = None
    
    abatementdateTime: str = None
    
    abatementdateTime: "Age" = None
    
    abatementdateTime: "Period" = None
    
    abatementdateTime: "Range" = None
    
    abatementdateTime: str = None
    
    recordedDate: str = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    stage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    summary: "CodeableConcept" = None
    
    assessment: "Reference" = None
    
    type: "CodeableConcept" = None
    
    evidence: "CodeableReference" = None
    
    note: "Annotation" = None
    