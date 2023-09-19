"""
Generated class for ExtendedContactDetail. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Address import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Period import *
from fhan.models.R5.HumanName import *
from fhan.models.R5.Reference import *


@dataclass
class ExtendedContactDetail:
    """ ExtendedContactDetail Type: Specifies contact information for a specific purpose over a period of time, might be handled/monitored by a specific named person or organization.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param CodeableConcept purpose: The type of contact
    :param HumanName name: Name of an individual to contact
    :param ContactPoint telecom: Contact details (e.g.phone/fax/url)
    :param Address address: Address for the contact
    :param Reference organization: This contact detail is handled/monitored by a specific organization
    :param Period period: Period that this contact was valid for usage
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    purpose: "CodeableConcept" = None
    
    name: "HumanName" = None
    
    telecom: "ContactPoint" = None
    
    address: "Address" = None
    
    organization: "Reference" = None
    
    period: "Period" = None
    