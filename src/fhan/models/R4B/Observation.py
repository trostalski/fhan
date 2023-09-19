"""
Generated class for Observation. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.SampledData import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Ratio import *
from fhan.models.R4B.Reference import *


@dataclass
class Observation:
    """
    FHIR Oxygen Saturation Profile
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
    
    partOf: "Reference" = None
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    category:VSCat: "CodeableConcept" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    coding: "Coding" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    system: str = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    
    userSelected: bool = None
    
    text: str = None
    
    code: "CodeableConcept" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    coding: "Coding" = None
    
    coding:OxygenSatCode: "Coding" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    system: str = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    
    userSelected: bool = None
    
    text: str = None
    
    subject: "Reference" = None
    
    focus: "Reference" = None
    
    encounter: "Reference" = None
    
    effectivedateTime: str = None
    
    effectivedateTime: "Period" = None
    
    issued: str = None
    
    performer: "Reference" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity:valueQuantity: "Quantity" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    value: float = None
    
    comparator: str = None
    
    unit: str = None
    
    system: str = None
    
    code: str = None
    
    dataAbsentReason: "CodeableConcept" = None
    
    interpretation: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    bodySite: "CodeableConcept" = None
    
    method: "CodeableConcept" = None
    
    specimen: "Reference" = None
    
    device: "Reference" = None
    
    referenceRange: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    low: "Quantity" = None
    
    high: "Quantity" = None
    
    type: "CodeableConcept" = None
    
    appliesTo: "CodeableConcept" = None
    
    age: "Range" = None
    
    text: str = None
    
    hasMember: "Reference" = None
    
    derivedFrom: "Reference" = None
    
    component: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "CodeableConcept" = None
    
    valueQuantity: str = None
    
    valueQuantity: bool = None
    
    valueQuantity: int = None
    
    valueQuantity: "Range" = None
    
    valueQuantity: "Ratio" = None
    
    valueQuantity: "SampledData" = None
    
    valueQuantity: str = None
    
    valueQuantity: str = None
    
    valueQuantity: "Period" = None
    
    dataAbsentReason: "CodeableConcept" = None
    
    interpretation: "CodeableConcept" = None
    
    referenceRange: "BackboneElement" = None
    