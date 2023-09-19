"""
Generated class for Request. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Timing import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Request:
    """
    Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    """
    identifier: "Identifier" = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    replaces: "Reference" = None
    
    groupIdentifier: "Identifier" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    intent: str = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: "Timing" = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    reportedboolean: bool = None
    
    reportedboolean: "Reference" = None
    
    performerType: "CodeableConcept" = None
    
    performer: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    insurance: "Reference" = None
    
    supportingInfo: "Reference" = None
    
    note: "Annotation" = None
    
    relevantHistory: "Reference" = None
    