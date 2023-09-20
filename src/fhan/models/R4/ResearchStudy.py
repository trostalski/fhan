"""
Generated class for ResearchStudy. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class arm(Element):
    """ Describes an expected sequence of events for one of the participants of a study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out, follow-up.
    :param BackboneElement arm: Defined path through the study for a subject
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for study arm
    :param CodeableConcept type: Categorization of study arm
    :param str description: Short explanation of study path
    """
    arm: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
@dataclass
class objective(Element):
    """ A goal that the study is aiming to achieve in terms of a scientific question to be answered by the analysis of data collected during the study.
    :param BackboneElement objective: A goal for the study
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for the objective
    :param CodeableConcept type: primary | secondary | exploratory
    """
    objective: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    


@dataclass
class ResearchStudy(ModelBase):
    """ A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge.  This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional and investigative techniques.  A ResearchStudy involves the gathering of information about human or animal subjects.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for study
    :param str title: Name for this study
    :param Reference protocol: Steps followed in executing study
    :param Reference partOf: Part of larger study
    :param str status: active | administratively-completed | approved | closed-to-accrual | closed-to-accrual-and-intervention | completed | disapproved | in-review | temporarily-closed-to-accrual | temporarily-closed-to-accrual-and-intervention | withdrawn
    :param CodeableConcept primaryPurposeType: treatment | prevention | diagnostic | supportive-care | screening | health-services-research | basic-science | device-feasibility
    :param CodeableConcept phase: n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | phase-2-phase-3 | phase-3 | phase-4
    :param CodeableConcept category: Classifications for the study
    :param CodeableConcept focus: Drugs, devices, etc. under study
    :param CodeableConcept condition: Condition being studied
    :param ContactDetail contact: Contact details for the study
    :param RelatedArtifact relatedArtifact: References and dependencies
    :param CodeableConcept keyword: Used to search for the study
    :param CodeableConcept location: Geographic region(s) for study
    :param str description: What this is study doing
    :param Reference enrollment: Inclusion & exclusion criteria
    :param Period period: When the study began and ended
    :param Reference sponsor: Organization that initiates and is legally responsible for the study
    :param Reference principalInvestigator: Researcher who oversees multiple aspects of the study
    :param Reference site: Facility where study activities are conducted
    :param CodeableConcept reasonStopped: accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-study-progress | temporarily-closed-per-study-design
    :param Annotation note: Comments made about the study
    :param BackboneElement arm: Defined path through the study for a subject
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for study arm
    :param CodeableConcept type: Categorization of study arm
    :param str description: Short explanation of study path
    :param BackboneElement objective: A goal for the study
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for the objective
    :param CodeableConcept type: primary | secondary | exploratory
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    title: str = None
    
    protocol: list["Reference"] = None
    
    partOf: list["Reference"] = None
    
    status: str = None
    
    primaryPurposeType: "CodeableConcept" = None
    
    phase: "CodeableConcept" = None
    
    category: list["CodeableConcept"] = None
    
    focus: list["CodeableConcept"] = None
    
    condition: list["CodeableConcept"] = None
    
    contact: list["ContactDetail"] = None
    
    relatedArtifact: list["RelatedArtifact"] = None
    
    keyword: list["CodeableConcept"] = None
    
    location: list["CodeableConcept"] = None
    
    description: str = None
    
    enrollment: list["Reference"] = None
    
    period: "Period" = None
    
    sponsor: "Reference" = None
    
    principalInvestigator: "Reference" = None
    
    site: list["Reference"] = None
    
    reasonStopped: "CodeableConcept" = None
    
    note: list["Annotation"] = None
    
    arm: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    objective: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    