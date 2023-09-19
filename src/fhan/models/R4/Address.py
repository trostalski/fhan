"""
Generated class for Address. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *


@dataclass
class Address:
    """
    Base StructureDefinition for Address Type: An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.
    """
    id: str = None
    
    extension: "Extension" = None
    
    use: str = None
    
    type: str = None
    
    text: str = None
    
    line: str = None
    
    city: str = None
    
    district: str = None
    
    state: str = None
    
    postalCode: str = None
    
    country: str = None
    
    period: "Period" = None
    