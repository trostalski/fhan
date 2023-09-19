"""
Generated class for VirtualServiceDetail. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Extension import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Coding import *


@dataclass
class VirtualServiceDetail:
    """ VirtualServiceDetail Type: Virtual Service Contact Details.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding channelType: Channel Type
    :param str addressurl: Contact address/number
    :param str addressurl: Contact address/number
    :param ContactPoint addressurl: Contact address/number
    :param ExtendedContactDetail addressurl: Contact address/number
    :param str additionalInfo: Address to see alternative connection details
    :param int maxParticipants: Maximum number of participants supported by the virtual service
    :param str sessionKey: Session Key required by the virtual service
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    channelType: "Coding" = None
    
    addressurl: str = None
    
    addressurl: str = None
    
    addressurl: "ContactPoint" = None
    
    addressurl: "ExtendedContactDetail" = None
    
    additionalInfo: str = None
    
    maxParticipants: int = None
    
    sessionKey: str = None
    