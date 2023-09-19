"""
Generated class for Device. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Count import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *


@dataclass
class Device:
    """ This resource describes the properties (regulated, has real time clock, etc.), adminstrative (manufacturer name, model number, serial number, firmware, etc.), and type (knee replacement, blood pressure cuff, MRI, etc.) of a physical unit (these values do not change much within a given module, for example the serail number, manufacturer name, and model number). An actual unit may consist of several modules in a distinct hierarchy and these are represented by multiple Device resources and bound through the 'parent' element.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Instance identifier
    :param str displayName: The name used to display by default when the device is referenced
    :param CodeableReference definition: The reference to the definition for the device
    :param BackboneElement udiCarrier: Unique Device Identifier (UDI) Barcode string
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str deviceIdentifier: Mandatory fixed portion of UDI
    :param str issuer: UDI Issuing Organization
    :param str jurisdiction: Regional UDI authority
    :param str carrierAIDC: UDI Machine Readable Barcode String
    :param str carrierHRF: UDI Human Readable Barcode String
    :param str entryType: barcode | rfid | manual | card | self-reported | electronic-transmission | unknown
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept availabilityStatus: lost | damaged | destroyed | available
    :param Identifier biologicalSourceEvent: An identifier that supports traceability to the event during which material in this product from one or more biological entities was obtained or pooled
    :param str manufacturer: Name of device manufacturer
    :param str manufactureDate: Date when the device was made
    :param str expirationDate: Date and time of expiry of this device (if applicable)
    :param str lotNumber: Lot number of manufacture
    :param str serialNumber: Serial number assigned by the manufacturer
    :param BackboneElement name: The name or names of the device as known to the manufacturer and/or patient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str value: The term that names the device
    :param str type: registered-name | user-friendly-name | patient-reported-name
    :param bool display: The preferred device name
    :param str modelNumber: The manufacturer's model number for the device
    :param str partNumber: The part number or catalog number of the device
    :param CodeableConcept category: Indicates a high-level grouping of the device
    :param CodeableConcept type: The kind or type of device
    :param BackboneElement version: The actual design of the device or software version running on the device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of the device version, e.g. manufacturer, approved, internal
    :param Identifier component: The hardware or software module of the device to which the version applies
    :param str installDate: The date the version was installed on the device
    :param str value: The version text
    :param BackboneElement conformsTo: Identifies the standards, specifications, or formal guidances for the capabilities supported by the device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Describes the common type of the standard, specification, or formal guidance.  communication | performance | measurement
    :param CodeableConcept specification: Identifies the standard, specification, or formal guidance that the device adheres to
    :param str version: Specific form or variant of the standard
    :param BackboneElement property: Inherent, essentially fixed, characteristics of the device.  e.g., time properties, size, material, etc.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code that specifies the property being represented
    :param Quantity valueQuantity: Value of the property
    :param CodeableConcept valueQuantity: Value of the property
    :param str valueQuantity: Value of the property
    :param bool valueQuantity: Value of the property
    :param int valueQuantity: Value of the property
    :param Range valueQuantity: Value of the property
    :param Attachment valueQuantity: Value of the property
    :param CodeableConcept mode: The designated condition for performing a task
    :param Count cycle: The series of occurrences that repeats during the operation of the device
    :param Duration duration: A measurement of time during the device's operation (e.g., days, hours, mins, etc.)
    :param Reference owner: Organization responsible for device
    :param ContactPoint contact: Details for human/organization for support
    :param Reference location: Where the device is found
    :param str url: Network address to contact device
    :param Reference endpoint: Technical endpoints providing access to electronic services provided by the device
    :param CodeableReference gateway: Linked device acting as a communication/data collector, translator or controller
    :param Annotation note: Device notes and comments
    :param CodeableConcept safety: Safety Characteristics of Device
    :param Reference parent: The higher level or encompassing device that this device is a logical part of
    
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
    
    displayName: str = None
    
    definition: "CodeableReference" = None
    
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
    
    availabilityStatus: "CodeableConcept" = None
    
    biologicalSourceEvent: "Identifier" = None
    
    manufacturer: str = None
    
    manufactureDate: str = None
    
    expirationDate: str = None
    
    lotNumber: str = None
    
    serialNumber: str = None
    
    name: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    value: str = None
    
    type: str = None
    
    display: bool = None
    
    modelNumber: str = None
    
    partNumber: str = None
    
    category: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    version: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    component: "Identifier" = None
    
    installDate: str = None
    
    value: str = None
    
    conformsTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    specification: "CodeableConcept" = None
    
    version: str = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "CodeableConcept" = None
    
    valueQuantity: str = None
    
    valueQuantity: bool = None
    
    valueQuantity: int = None
    
    valueQuantity: "Range" = None
    
    valueQuantity: "Attachment" = None
    
    mode: "CodeableConcept" = None
    
    cycle: "Count" = None
    
    duration: "Duration" = None
    
    owner: "Reference" = None
    
    contact: "ContactPoint" = None
    
    location: "Reference" = None
    
    url: str = None
    
    endpoint: "Reference" = None
    
    gateway: "CodeableReference" = None
    
    note: "Annotation" = None
    
    safety: "CodeableConcept" = None
    
    parent: "Reference" = None
    