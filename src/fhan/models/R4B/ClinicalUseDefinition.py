"""
Generated class for ClinicalUseDefinition. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.CodeableReference import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class ClinicalUseDefinition:
    """
    A single issue - either an indication, contraindication, interaction or an undesirable effect for a medicinal product, medication, device or procedure.
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
    
    type: str = None
    
    category: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    status: "CodeableConcept" = None
    
    contraindication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    diseaseSymptomProcedure: "CodeableReference" = None
    
    diseaseStatus: "CodeableReference" = None
    
    comorbidity: "CodeableReference" = None
    
    indication: "Reference" = None
    
    otherTherapy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relationshipType: "CodeableConcept" = None
    
    therapy: "CodeableReference" = None
    
    indication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    diseaseSymptomProcedure: "CodeableReference" = None
    
    diseaseStatus: "CodeableReference" = None
    
    comorbidity: "CodeableReference" = None
    
    intendedEffect: "CodeableReference" = None
    
    durationRange: "Range" = None
    
    durationRange: str = None
    
    undesirableEffect: "Reference" = None
    
    otherTherapy: "BackboneElement" = None
    
    interaction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    interactant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemReference: "Reference" = None
    
    itemReference: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    effect: "CodeableReference" = None
    
    incidence: "CodeableConcept" = None
    
    management: "CodeableConcept" = None
    
    population: "Reference" = None
    
    undesirableEffect: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    symptomConditionEffect: "CodeableReference" = None
    
    classification: "CodeableConcept" = None
    
    frequencyOfOccurrence: "CodeableConcept" = None
    
    warning: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    code: "CodeableConcept" = None
    