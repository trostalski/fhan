"""
Generated class for Device. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class Device(ModelBase):
    """ A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Instance identifier
    :param Reference definition: The reference to the definition for the device
    :param BackboneElement udiCarrier: Unique Device Identifier (UDI) Barcode string
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str deviceIdentifier: Mandatory fixed portion of UDI
    :param str issuer: UDI Issuing Organization
    :param str jurisdiction: Regional UDI authority
    :param str carrierAIDC: UDI Machine Readable Barcode String
    :param str carrierHRF: UDI Human Readable Barcode String
    :param str entryType: barcode | rfid | manual +
    :param str status: active | inactive | entered-in-error | unknown
    :param CodeableConcept statusReason: online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off
    :param str distinctIdentifier: The distinct identification string
    :param str manufacturer: Name of device manufacturer
    :param str manufactureDate: Date when the device was made
    :param str expirationDate: Date and time of expiry of this device (if applicable)
    :param str lotNumber: Lot number of manufacture
    :param str serialNumber: Serial number assigned by the manufacturer
    :param BackboneElement deviceName: The name of the device as given by the manufacturer
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The name of the device
    :param str type: udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
    :param str modelNumber: The model number for the device
    :param str partNumber: The part number of the device
    :param CodeableConcept type: The kind or type of device
    :param BackboneElement specialization: The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept systemType: The standard that is used to operate and communicate
    :param str version: The version of the standard that is used to operate and communicate
    :param BackboneElement version: The actual design of the device or software version running on the device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of the device version
    :param Identifier component: A single component of the device version
    :param str value: The version text
    :param BackboneElement property: The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    :param Quantity valueQuantity: Property value as a quantity
    :param CodeableConcept valueCode: Property value as a code, e.g., NTP4 (synced to NTP)
    :param Reference patient: Patient to whom Device is affixed
    :param Reference owner: Organization responsible for device
    :param ContactPoint contact: Details for human/organization for support
    :param Reference location: Where the device is found
    :param str url: Network address to contact device
    :param Annotation note: Device notes and comments
    :param CodeableConcept safety: Safety Characteristics of Device
    :param Reference parent: The parent device
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
    