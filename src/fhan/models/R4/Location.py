"""
Generated class for Location. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Address import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Location:
    """
    Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.
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
    
    status: str = None
    
    operationalStatus: "Coding" = None
    
    name: str = None
    
    alias: str = None
    
    description: str = None
    
    mode: str = None
    
    type: "CodeableConcept" = None
    
    telecom: "ContactPoint" = None
    
    address: "Address" = None
    
    physicalType: "CodeableConcept" = None
    
    position: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    longitude: float = None
    
    latitude: float = None
    
    altitude: float = None
    
    managingOrganization: "Reference" = None
    
    partOf: "Reference" = None
    
    hoursOfOperation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    daysOfWeek: str = None
    
    allDay: bool = None
    
    openingTime: str = None
    
    closingTime: str = None
    
    availabilityExceptions: str = None
    
    endpoint: "Reference" = None
    