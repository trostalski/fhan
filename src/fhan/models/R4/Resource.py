"""
Generated class for Resource. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Meta import *


@dataclass
class Resource:
    """
    This is the base resource type for everything.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    