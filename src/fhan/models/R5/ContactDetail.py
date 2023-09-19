"""
Generated class for ContactDetail. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Extension import *
from fhan.models.R5.ContactPoint import *


@dataclass
class ContactDetail:
    """ ContactDetail Type: Specifies contact information for a person or organization.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str name: Name of an individual to contact
    :param ContactPoint telecom: Contact details for individual or organization
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    name: str = None
    
    telecom: "ContactPoint" = None
    