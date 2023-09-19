"""
Generated class for HumanName. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Period import *


@dataclass
class HumanName:
    """
    Base StructureDefinition for HumanName Type: A human's name with the ability to identify parts and usage.
    """
    id: str = None
    
    extension: "Extension" = None
    
    use: str = None
    
    text: str = None
    
    family: str = None
    
    given: str = None
    
    prefix: str = None
    
    suffix: str = None
    
    period: "Period" = None
    