"""
Generated class for CarePlan. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class CarePlan:
    """
    Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.
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
    
    basedOn: "Reference" = None
    
    replaces: "Reference" = None
    
    partOf: "Reference" = None
    
    status: str = None
    
    intent: str = None
    
    category: "CodeableConcept" = None
    
    title: str = None
    
    description: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    period: "Period" = None
    
    created: str = None
    
    author: "Reference" = None
    
    contributor: "Reference" = None
    
    careTeam: "Reference" = None
    
    addresses: "Reference" = None
    
    supportingInfo: "Reference" = None
    
    goal: "Reference" = None
    
    activity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    outcomeCodeableConcept: "CodeableConcept" = None
    
    outcomeReference: "Reference" = None
    
    progress: "Annotation" = None
    
    reference: "Reference" = None
    
    detail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    kind: str = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    code: "CodeableConcept" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    goal: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    doNotPerform: bool = None
    
    scheduledTiming: "Timing" = None
    
    scheduledTiming: "Period" = None
    
    scheduledTiming: str = None
    
    location: "Reference" = None
    
    performer: "Reference" = None
    
    productCodeableConcept: "CodeableConcept" = None
    
    productCodeableConcept: "Reference" = None
    
    dailyAmount: "Quantity" = None
    
    quantity: "Quantity" = None
    
    description: str = None
    
    note: "Annotation" = None
    