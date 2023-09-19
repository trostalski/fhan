"""
Generated class for MedicinalProductInteraction. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *


@dataclass
class MedicinalProductInteraction:
    """
    The interactions of the medicinal product with other medicinal products, or other forms of interactions.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    subject: "Reference" = None
    
    description: str = None
    
    interactant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemReference: "Reference" = None
    
    itemReference: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    effect: "CodeableConcept" = None
    
    incidence: "CodeableConcept" = None
    
    management: "CodeableConcept" = None
    