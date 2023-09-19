"""
Generated class for Quantity. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *


@dataclass
class Quantity:
    """
    An amount of money. With regard to precision, see [Decimal Precision](datatypes.html#precision)
    """
    id: str = None
    
    extension: "Extension" = None
    
    value: float = None
    
    comparator: str = None
    
    unit: str = None
    
    system: str = None
    
    code: str = None
    