"""
Generated class for FiveWs. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Timing import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class FiveWs:
    """
    Logical Model: Who What When Where Why - Common pattern for all resources that deals with attribution.
    """
    identifier: "Identifier" = None
    
    version: str = None
    
    status: str = None
    
    class: "CodeableConcept" = None
    
    grade: "CodeableConcept" = None
    
    whatCodeableConcept: "CodeableConcept" = None
    
    whatCodeableConcept: "Reference" = None
    
    subject: "Reference" = None
    
    context: "Reference" = None
    
    init: str = None
    
    planned: "Timing" = None
    
    donedateTime: str = None
    
    donedateTime: "Period" = None
    
    recorded: str = None
    
    author: "Reference" = None
    
    source: "Reference" = None
    
    actor: "Reference" = None
    
    cause: "Reference" = None
    
    witness: "Reference" = None
    
    who: "Reference" = None
    
    whereCodeableConcept: "CodeableConcept" = None
    
    whereCodeableConcept: "Reference" = None
    
    whyCodeableConcept: "CodeableConcept" = None
    
    whyCodeableConcept: "Reference" = None
    