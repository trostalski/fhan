"""
Generated class for Person. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Address import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Meta import *


@dataclass
class Person:
    """
    Demographics and administrative information about a person independent of a specific health-related context.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    name: "HumanName" = None
    
    telecom: "ContactPoint" = None
    
    gender: str = None
    
    birthDate: str = None
    
    address: "Address" = None
    
    photo: "Attachment" = None
    
    managingOrganization: "Reference" = None
    
    active: bool = None
    
    link: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    target: "Reference" = None
    
    assurance: str = None
    