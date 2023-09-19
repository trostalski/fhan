"""
Generated class for RiskAssessment. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *


@dataclass
class RiskAssessment:
    """
    An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
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
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    basis: "Reference" = None
    
    prediction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    outcome: "CodeableConcept" = None
    
    probabilitydecimal: float = None
    
    probabilitydecimal: "Range" = None
    
    qualitativeRisk: "CodeableConcept" = None
    
    relativeRisk: float = None
    
    whenPeriod: "Period" = None
    
    whenPeriod: "Range" = None
    
    rationale: str = None
    
    mitigation: str = None
    
    note: "Annotation" = None
    