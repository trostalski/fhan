"""
Generated class for SpecimenDefinition. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *


@dataclass
class SpecimenDefinition:
    """
    A kind of specimen with associated set of requirements.
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
    
    typeCollected: "CodeableConcept" = None
    
    patientPreparation: "CodeableConcept" = None
    
    timeAspect: str = None
    
    collection: "CodeableConcept" = None
    
    typeTested: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    isDerived: bool = None
    
    type: "CodeableConcept" = None
    
    preference: str = None
    
    container: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    material: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    cap: "CodeableConcept" = None
    
    description: str = None
    
    capacity: "Quantity" = None
    
    minimumVolumeQuantity: "Quantity" = None
    
    minimumVolumeQuantity: str = None
    
    additive: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    additiveCodeableConcept: "CodeableConcept" = None
    
    additiveCodeableConcept: "Reference" = None
    
    preparation: str = None
    
    requirement: str = None
    
    retentionTime: "Duration" = None
    
    rejectionCriterion: "CodeableConcept" = None
    
    handling: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    temperatureQualifier: "CodeableConcept" = None
    
    temperatureRange: "Range" = None
    
    maxDuration: "Duration" = None
    
    instruction: str = None
    