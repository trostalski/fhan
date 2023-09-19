"""
Generated class for HumanName. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *


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
    