"""
Generated class for HumanName. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.Element import *

@dataclass
class HumanName(Element):
    """ Base StructureDefinition for HumanName Type: A human's name with the ability to identify parts and usage.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str use: usual | official | temp | nickname | anonymous | old | maiden
    :param str text: Text representation of the full name
    :param str family: Family name (often called 'Surname')
    :param str given: Given names (not always 'first'). Includes middle names
    :param str prefix: Parts that come before the name
    :param str suffix: Parts that come after the name
    :param Period period: Time period when name was/is in use
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    use: str = None
    
    text: str = None
    
    family: str = None
    
    given: str = None
    
    prefix: str = None
    
    suffix: str = None
    
    period: "Period" = None
    