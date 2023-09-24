"""
Generated class for Condition. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Age import *
from fhan.models.R4.Range import *
from fhan.models.R4.Element import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Stage(Element):
    """ Clinical stage or grade of a condition. May include formal severity assessments.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept summary: Simple summary (disease specific)
    :param Reference assessment: Formal record of assessment
    :param CodeableConcept type: Kind of staging
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    summary:  "CodeableConcept" = CodeableConcept()
    
    assessment:  list["Reference"] = [Reference()]
    
    type:  "CodeableConcept" = CodeableConcept()
    

    
    
@dataclass
class Evidence(Element):
    """ Supporting evidence / manifestations that are the basis of the Condition's verification status, such as evidence that confirmed or refuted the condition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Manifestation/symptom
    :param Reference detail: Supporting information found elsewhere
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    code:  list["CodeableConcept"] = [CodeableConcept()]
    
    detail:  list["Reference"] = [Reference()]
    

@dataclass
class Condition(ModelBase):
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
    :param CodeableConcept clinicalStatus: active | recurrence | relapse | inactive | remission | resolved
    :param CodeableConcept verificationStatus: unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
    :param CodeableConcept category: problem-list-item | encounter-diagnosis
    :param CodeableConcept severity: Subjective severity of condition
    :param CodeableConcept code: Identification of the condition, problem or diagnosis
    :param CodeableConcept bodySite: Anatomical location, if relevant
    :param Reference subject: Who has the condition?
    :param Reference encounter: Encounter created as part of
    :param str onsetDateTime: Estimated or actual date,  date-time, or age
    :param str abatementDateTime: When in resolution/remission
    :param str recordedDate: Date record was first recorded
    :param Reference recorder: Who recorded the condition
    :param Reference asserter: Person who asserts this condition
    :param Stage stage: Stage/grade, usually assessed formally
    :param Evidence evidence: Supporting evidence
    :param Annotation note: Additional information about the Condition
    """

    resourceType: str = "Condition"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    clinicalStatus: "CodeableConcept" = None
    
    verificationStatus: "CodeableConcept" = None
    
    category: list["CodeableConcept"] = None
    
    severity: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    bodySite: list["CodeableConcept"] = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    onsetDateTime: str = None
    
    abatementDateTime: str = None
    
    recordedDate: str = None
    
    recorder: "Reference" = None
    
    asserter: "Reference" = None
    
    stage: list["Stage"] = None
    
    evidence: list["Evidence"] = None
    
    note: list["Annotation"] = None
    