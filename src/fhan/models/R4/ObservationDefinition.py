"""
Generated class for ObservationDefinition. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *


@dataclass
class ObservationDefinition:
    """
    Set of definitional characteristics for a kind of observation or measurement produced or consumed by an orderable health care service.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    identifier: "Identifier" = None
    
    permittedDataType: str = None
    
    multipleResultsAllowed: bool = None
    
    method: "CodeableConcept" = None
    
    preferredReportName: str = None
    
    quantitativeDetails: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    customaryUnit: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    conversionFactor: float = None
    
    decimalPrecision: int = None
    
    qualifiedInterval: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: str = None
    
    range: "Range" = None
    
    context: "CodeableConcept" = None
    
    appliesTo: "CodeableConcept" = None
    
    gender: str = None
    
    age: "Range" = None
    
    gestationalAge: "Range" = None
    
    condition: str = None
    
    validCodedValueSet: "Reference" = None
    
    normalCodedValueSet: "Reference" = None
    
    abnormalCodedValueSet: "Reference" = None
    
    criticalCodedValueSet: "Reference" = None
    