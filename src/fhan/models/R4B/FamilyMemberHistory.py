"""
Generated class for FamilyMemberHistory. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Age import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class FamilyMemberHistory:
    """
    Significant health conditions for a person related to the patient relevant in the context of care for the patient.
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
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    status: str = None
    
    dataAbsentReason: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    date: str = None
    
    name: str = None
    
    relationship: "CodeableConcept" = None
    
    sex: "CodeableConcept" = None
    
    bornPeriod: "Period" = None
    
    bornPeriod: str = None
    
    bornPeriod: str = None
    
    ageAge: "Age" = None
    
    ageAge: "Range" = None
    
    ageAge: str = None
    
    estimatedAge: bool = None
    
    deceasedboolean: bool = None
    
    deceasedboolean: "Age" = None
    
    deceasedboolean: "Range" = None
    
    deceasedboolean: str = None
    
    deceasedboolean: str = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    note: "Annotation" = None
    
    condition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    outcome: "CodeableConcept" = None
    
    contributedToDeath: bool = None
    
    onsetAge: "Age" = None
    
    onsetAge: "Range" = None
    
    onsetAge: "Period" = None
    
    onsetAge: str = None
    
    note: "Annotation" = None
    