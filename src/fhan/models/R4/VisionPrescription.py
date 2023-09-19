"""
Generated class for VisionPrescription. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class VisionPrescription:
    """
    An authorization for the provision of glasses and/or contact lenses to a patient.
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
    
    status: str = None
    
    created: str = None
    
    patient: "Reference" = None
    
    encounter: "Reference" = None
    
    dateWritten: str = None
    
    prescriber: "Reference" = None
    
    lensSpecification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    product: "CodeableConcept" = None
    
    eye: str = None
    
    sphere: float = None
    
    cylinder: float = None
    
    axis: int = None
    
    prism: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    amount: float = None
    
    base: str = None
    
    add: float = None
    
    power: float = None
    
    backCurve: float = None
    
    diameter: float = None
    
    duration: "Quantity" = None
    
    color: str = None
    
    brand: str = None
    
    note: "Annotation" = None
    