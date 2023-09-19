"""
Generated class for ResearchSubject. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Reference import *


@dataclass
class ResearchSubject:
    """
    A physical entity which is the primary unit of operational and/or administrative interest in a study.
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
    
    period: "Period" = None
    
    study: "Reference" = None
    
    individual: "Reference" = None
    
    assignedArm: str = None
    
    actualArm: str = None
    
    consent: "Reference" = None
    