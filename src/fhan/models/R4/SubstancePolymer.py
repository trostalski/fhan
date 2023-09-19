"""
Generated class for SubstancePolymer. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.SubstanceAmount import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *


@dataclass
class SubstancePolymer:
    """
    Todo.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    class: "CodeableConcept" = None
    
    geometry: "CodeableConcept" = None
    
    copolymerConnectivity: "CodeableConcept" = None
    
    modification: str = None
    
    monomerSet: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    ratioType: "CodeableConcept" = None
    
    startingMaterial: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    material: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    isDefining: bool = None
    
    amount: "SubstanceAmount" = None
    
    repeat: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    numberOfUnits: int = None
    
    averageMolecularFormula: str = None
    
    repeatUnitAmountType: "CodeableConcept" = None
    
    repeatUnit: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    orientationOfPolymerisation: "CodeableConcept" = None
    
    repeatUnit: str = None
    
    amount: "SubstanceAmount" = None
    
    degreeOfPolymerisation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    degree: "CodeableConcept" = None
    
    amount: "SubstanceAmount" = None
    
    structuralRepresentation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    representation: str = None
    
    attachment: "Attachment" = None
    