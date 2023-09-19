"""
Generated class for EnrollmentRequest. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class EnrollmentRequest:
    """
    This resource provides the insurance enrollment details to the insurer regarding a specified coverage.
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
    
    created: str = None
    
    insurer: "Reference" = None
    
    provider: "Reference" = None
    
    candidate: "Reference" = None
    
    coverage: "Reference" = None
    