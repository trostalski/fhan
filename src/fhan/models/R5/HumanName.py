"""
Generated class for HumanName. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Period import *
from fhan.models.R5.Extension import *


@dataclass
class HumanName:
    """ HumanName Type: A name, normally of a human, that can be used for other living entities (e.g. animals but not organizations) that have been assigned names by a human and may need the use of name parts or the need for usage information.
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
    
    extension: "Extension" = None
    
    use: str = None
    
    text: str = None
    
    family: str = None
    
    given: str = None
    
    prefix: str = None
    
    suffix: str = None
    
    period: "Period" = None
    