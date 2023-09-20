"""
Generated class for DeviceDefinition. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ProductShelfLife import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class UdiDeviceIdentifier(Element):
    """ Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str deviceIdentifier: The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier
    :param str issuer: The organization that assigns the identifier algorithm
    :param str jurisdiction: The jurisdiction to which the deviceIdentifier applies
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    deviceIdentifier: str = None
    
    issuer: str = None
    
    jurisdiction: str = None
    

    
    
@dataclass
class DeviceName(Element):
    """ A name given to the device to identify it.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The name of the device
    :param str type: udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    name: str = None
    
    type: str = None
    

    
    
@dataclass
class Specialization(Element):
    """ The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str systemType: The standard that is used to operate and communicate
    :param str version: The version of the standard that is used to operate and communicate
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    systemType: str = None
    
    version: str = None
    

    
    
@dataclass
class Capability(Element):
    """ Device capabilities.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of capability
    :param CodeableConcept description: Description of capability
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    description: list[CodeableConcept] = None
    

    
    
@dataclass
class Property(Element):
    """ The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    :param Quantity valueQuantity: Property value as a quantity
    :param CodeableConcept valueCode: Property value as a code, e.g., NTP4 (synced to NTP)
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    valueQuantity: list[Quantity] = None
    valueCode: list[CodeableConcept] = None
    

    
    
@dataclass
class Material(Element):
    """ A substance used to create the material(s) of which the device is made.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept substance: The substance
    :param bool alternate: Indicates an alternative material of the device
    :param bool allergenicIndicator: Whether the substance is a known or suspected allergen
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    substance: "CodeableConcept" = None
    
    alternate: bool = None
    
    allergenicIndicator: bool = None
    
@dataclass
class DeviceDefinition(ModelBase):
    """ The characteristics, operational status and capabilities of a medical-related component of a medical device.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Instance identifier
    :param UdiDeviceIdentifier udiDeviceIdentifier: Unique Device Identifier (UDI) Barcode string
    :param str manufacturerString: Name of device manufacturer
    :param DeviceName deviceName: A name given to the device to identify it
    :param str modelNumber: The model number for the device
    :param CodeableConcept type: What kind of device or device system this is
    :param Specialization specialization: The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    :param str version: Available versions
    :param CodeableConcept safety: Safety characteristics of the device
    :param ProductShelfLife shelfLifeStorage: Shelf Life and storage information
    :param ProdCharacteristic physicalCharacteristics: Dimensions, color etc.
    :param CodeableConcept languageCode: Language code for the human-readable text strings produced by the device (all supported)
    :param Capability capability: Device capabilities
    :param Property property: The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    :param Reference owner: Organization responsible for device
    :param ContactPoint contact: Details for human/organization for support
    :param str url: Network address to contact device
    :param str onlineInformation: Access to on-line information
    :param Annotation note: Device notes and comments
    :param Quantity quantity: The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product)
    :param Reference parentDevice: The parent device it can be part of
    :param Material material: A substance used to create the material(s) of which the device is made
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    udiDeviceIdentifier: list["UdiDeviceIdentifier"] = None
    
    manufacturerString: str = None
    
    deviceName: list["DeviceName"] = None
    
    modelNumber: str = None
    
    type: "CodeableConcept" = None
    
    specialization: list["Specialization"] = None
    
    version: str = None
    
    safety: list["CodeableConcept"] = None
    
    shelfLifeStorage: list["ProductShelfLife"] = None
    
    physicalCharacteristics: "ProdCharacteristic" = None
    
    languageCode: list["CodeableConcept"] = None
    
    capability: list["Capability"] = None
    
    property: list["Property"] = None
    
    owner: "Reference" = None
    
    contact: list["ContactPoint"] = None
    
    url: str = None
    
    onlineInformation: str = None
    
    note: list["Annotation"] = None
    
    quantity: "Quantity" = None
    
    parentDevice: "Reference" = None
    
    material: list["Material"] = None
    