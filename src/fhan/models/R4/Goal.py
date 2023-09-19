"""
Generated class for Goal. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *


@dataclass
class Goal:
    """
    Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.
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
    
    lifecycleStatus: str = None
    
    achievementStatus: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    priority: "CodeableConcept" = None
    
    description: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    startdate: str = None
    
    startdate: "CodeableConcept" = None
    
    target: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    measure: "CodeableConcept" = None
    
    detailQuantity: "Quantity" = None
    
    detailQuantity: "Range" = None
    
    detailQuantity: "CodeableConcept" = None
    
    detailQuantity: str = None
    
    detailQuantity: bool = None
    
    detailQuantity: int = None
    
    detailQuantity: "Ratio" = None
    
    duedate: str = None
    
    duedate: "Duration" = None
    
    statusDate: str = None
    
    statusReason: str = None
    
    expressedBy: "Reference" = None
    
    addresses: "Reference" = None
    
    note: "Annotation" = None
    
    outcomeCode: "CodeableConcept" = None
    
    outcomeReference: "Reference" = None
    