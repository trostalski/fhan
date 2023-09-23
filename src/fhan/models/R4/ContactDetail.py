"""
Generated class for ContactDetail. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Element import *


@dataclass
class ContactDetail(Element):
    """ Base StructureDefinition for ContactDetail Type: Specifies contact information for a person or organization.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str name: Name of an individual to contact
    :param ContactPoint telecom: Contact details for individual or organization
    """

    resourceType: str = "ContactDetail"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    name: str = None
    
    telecom: list[ContactPoint] = ContactPoint() 
    