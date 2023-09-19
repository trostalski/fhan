"""
Generated class for Patient. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.HumanName import *
from fhan.models.R4B.ContactPoint import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Address import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Patient:
    """
    Demographics and other administrative information about an individual or animal receiving care or other health-related services.
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
    
    active: bool = None
    
    name: "HumanName" = None
    
    telecom: "ContactPoint" = None
    
    gender: str = None
    
    birthDate: str = None
    
    deceasedboolean: bool = None
    
    deceasedboolean: str = None
    
    address: "Address" = None
    
    maritalStatus: "CodeableConcept" = None
    
    multipleBirthboolean: bool = None
    
    multipleBirthboolean: int = None
    
    photo: "Attachment" = None
    
    contact: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relationship: "CodeableConcept" = None
    
    name: "HumanName" = None
    
    telecom: "ContactPoint" = None
    
    address: "Address" = None
    
    gender: str = None
    
    organization: "Reference" = None
    
    period: "Period" = None
    
    communication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    language: "CodeableConcept" = None
    
    preferred: bool = None
    
    generalPractitioner: "Reference" = None
    
    managingOrganization: "Reference" = None
    
    link: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    other: "Reference" = None
    
    type: str = None
    