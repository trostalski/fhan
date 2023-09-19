"""
Generated class for AllergyIntolerance. 
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
class AllergyIntolerance:
    """
    Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.
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
    
    clinicalStatus: "CodeableConcept" = None
    
    verificationStatus: "CodeableConcept" = None
    
    type: str = None
    
    category: str = None
    
    criticality: str = None
    
    code: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    encounter: "Reference" = None
    
    onsetdateTime: str = None
    
    onsetdateTime: "Age" = None
    
    onsetdateTime: "Period" = None
    
    onsetdateTime: "Range" = None
    
    onsetdateTime: str = None
    
    recordedDate: str = None
    
    recorder: "Reference" = None
    
    asserter: "Reference" = None
    
    lastOccurrence: str = None
    
    note: "Annotation" = None
    
    reaction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substance: "CodeableConcept" = None
    
    manifestation: "CodeableConcept" = None
    
    description: str = None
    
    onset: str = None
    
    severity: str = None
    
    exposureRoute: "CodeableConcept" = None
    
    note: "Annotation" = None
    