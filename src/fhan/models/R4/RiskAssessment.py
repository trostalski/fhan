"""
Generated class for RiskAssessment. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Range import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class prediction(Element):
    """ Describes the expected outcome for the subject.
    :param BackboneElement prediction: Outcome predicted
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept outcome: Possible outcome for the subject
    :param float probabilitydecimal: Likelihood of specified outcome
    :param Range probabilitydecimal: Likelihood of specified outcome
    :param CodeableConcept qualitativeRisk: Likelihood of specified outcome as a qualitative value
    :param float relativeRisk: Relative likelihood
    :param Period whenPeriod: Timeframe or age range
    :param Range whenPeriod: Timeframe or age range
    :param str rationale: Explanation of prediction
    """
    prediction: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    outcome: "CodeableConcept" = None
    
    probabilitydecimal: float = None
    
    probabilitydecimal: "Range" = None
    
    qualitativeRisk: "CodeableConcept" = None
    
    relativeRisk: float = None
    
    whenPeriod: "Period" = None
    
    whenPeriod: "Range" = None
    
    rationale: str = None
    


@dataclass
class RiskAssessment(ModelBase):
    """ An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier for the assessment
    :param Reference basedOn: Request fulfilled by this assessment
    :param Reference parent: Part of this occurrence
    :param str status: registered | preliminary | final | amended +
    :param CodeableConcept method: Evaluation mechanism
    :param CodeableConcept code: Type of assessment
    :param Reference subject: Who/what does assessment apply to?
    :param Reference encounter: Where was assessment performed?
    :param str occurrencedateTime: When was assessment made?
    :param Period occurrencedateTime: When was assessment made?
    :param Reference condition: Condition assessed
    :param Reference performer: Who did assessment?
    :param CodeableConcept reasonCode: Why the assessment was necessary?
    :param Reference reasonReference: Why the assessment was necessary?
    :param Reference basis: Information used in assessment
    :param BackboneElement prediction: Outcome predicted
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept outcome: Possible outcome for the subject
    :param float probabilitydecimal: Likelihood of specified outcome
    :param Range probabilitydecimal: Likelihood of specified outcome
    :param CodeableConcept qualitativeRisk: Likelihood of specified outcome as a qualitative value
    :param float relativeRisk: Relative likelihood
    :param Period whenPeriod: Timeframe or age range
    :param Range whenPeriod: Timeframe or age range
    :param str rationale: Explanation of prediction
    :param str mitigation: How to reduce risk
    :param Annotation note: Comments on the risk assessment
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
    
    basedOn: "Reference" = None
    
    parent: "Reference" = None
    
    status: str = None
    
    method: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    condition: "Reference" = None
    
    performer: "Reference" = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    basis: list["Reference"] = None
    
    prediction: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    outcome: "CodeableConcept" = None
    
    probabilitydecimal: float = None
    
    probabilitydecimal: "Range" = None
    
    qualitativeRisk: "CodeableConcept" = None
    
    relativeRisk: float = None
    
    whenPeriod: "Period" = None
    
    whenPeriod: "Range" = None
    
    rationale: str = None
    
    mitigation: str = None
    
    note: list["Annotation"] = None
    