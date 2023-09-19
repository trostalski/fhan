"""
Generated class for SampledData. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *


@dataclass
class SampledData:
    """
    Base StructureDefinition for SampledData Type: A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.
    """
    id: str = None
    
    extension: "Extension" = None
    
    origin: "Quantity" = None
    
    period: float = None
    
    factor: float = None
    
    lowerLimit: float = None
    
    upperLimit: float = None
    
    dimensions: int = None
    
    data: str = None
    