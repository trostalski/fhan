"""
Generated class for ParticipantContactable. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Address import *


@dataclass
class ParticipantContactable:
    """ Logical Model: A pattern followed by resources that represent a participant that can be contacted.
    :param ContactPoint telecom: A contact detail for the {{title}}
    :param Address address: An address for the {{title}}
    
    """
    telecom: "ContactPoint" = None
    
    address: "Address" = None
    