"""
Generated class for AdverseEvent. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class AdverseEvent:
    """
    Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death.
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
    
    actuality: str = None
    
    category: "CodeableConcept" = None
    
    event: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    date: str = None
    
    detected: str = None
    
    recordedDate: str = None
    
    resultingCondition: "Reference" = None
    
    location: "Reference" = None
    
    seriousness: "CodeableConcept" = None
    
    severity: "CodeableConcept" = None
    
    outcome: "CodeableConcept" = None
    
    recorder: "Reference" = None
    
    contributor: "Reference" = None
    
    suspectEntity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    instance: "Reference" = None
    
    causality: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    assessment: "CodeableConcept" = None
    
    productRelatedness: str = None
    
    author: "Reference" = None
    
    method: "CodeableConcept" = None
    
    subjectMedicalHistory: "Reference" = None
    
    referenceDocument: "Reference" = None
    
    study: "Reference" = None
    