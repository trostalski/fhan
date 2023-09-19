"""
Generated class for Device. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.ContactPoint import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Device:
    """
    A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.
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
    
    definition: "Reference" = None
    
    udiCarrier: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    deviceIdentifier: str = None
    
    issuer: str = None
    
    jurisdiction: str = None
    
    carrierAIDC: str = None
    
    carrierHRF: str = None
    
    entryType: str = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    distinctIdentifier: str = None
    
    manufacturer: str = None
    
    manufactureDate: str = None
    
    expirationDate: str = None
    
    lotNumber: str = None
    
    serialNumber: str = None
    
    deviceName: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: str = None
    
    modelNumber: str = None
    
    partNumber: str = None
    
    type: "CodeableConcept" = None
    
    specialization: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    systemType: "CodeableConcept" = None
    
    version: str = None
    
    version: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    component: "Identifier" = None
    
    value: str = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueCode: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    owner: "Reference" = None
    
    contact: "ContactPoint" = None
    
    location: "Reference" = None
    
    url: str = None
    
    note: "Annotation" = None
    
    safety: "CodeableConcept" = None
    
    parent: "Reference" = None
    