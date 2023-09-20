"""
Generated class for ContactPoint. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *


@dataclass
class ContactPoint(Element):
    """ Base StructureDefinition for ContactPoint Type: Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str system: phone | fax | email | pager | url | sms | other
    :param str value: The actual contact point details
    :param str use: home | work | temp | old | mobile - purpose of this contact point
    :param int rank: Specify preferred order of use (1 = highest)
    :param Period period: Time period when the contact point was/is in use
    """

    resourceType: str = "ContactPoint"
    id: str = None
    
    extension: list["Extension"] = None
    
    system: str = None
    
    value: str = None
    
    use: str = None
    
    rank: int = None
    
    period: "Period" = None
    