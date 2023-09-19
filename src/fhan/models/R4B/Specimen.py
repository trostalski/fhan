"""
Generated class for Specimen. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Duration import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Specimen:
    """
    A sample to be used for analysis.
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
    
    accessionIdentifier: "Identifier" = None
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    receivedTime: str = None
    
    parent: "Reference" = None
    
    request: "Reference" = None
    
    collection: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    collector: "Reference" = None
    
    collecteddateTime: str = None
    
    collecteddateTime: "Period" = None
    
    duration: "Duration" = None
    
    quantity: "Quantity" = None
    
    method: "CodeableConcept" = None
    
    bodySite: "CodeableConcept" = None
    
    fastingStatusCodeableConcept: "CodeableConcept" = None
    
    fastingStatusCodeableConcept: "Duration" = None
    
    processing: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    procedure: "CodeableConcept" = None
    
    additive: "Reference" = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
    container: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    description: str = None
    
    type: "CodeableConcept" = None
    
    capacity: "Quantity" = None
    
    specimenQuantity: "Quantity" = None
    
    additiveCodeableConcept: "CodeableConcept" = None
    
    additiveCodeableConcept: "Reference" = None
    
    condition: "CodeableConcept" = None
    
    note: "Annotation" = None
    