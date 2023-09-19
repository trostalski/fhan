"""
Generated class for EnrollmentResponse. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Reference import *


@dataclass
class EnrollmentResponse:
    """
    This resource provides enrollment and plan details from the processing of an EnrollmentRequest resource.
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
    
    request: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    created: str = None
    
    organization: "Reference" = None
    
    requestProvider: "Reference" = None
    