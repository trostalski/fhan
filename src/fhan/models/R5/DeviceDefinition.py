"""
Generated class for DeviceDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.ProductShelfLife import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Range import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Period import *
from fhan.models.R5.Reference import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *


@dataclass
class DeviceDefinition:
    """ This is a specialized resource that defines the characteristics and capabilities of a device.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str description: Additional information to describe the device
    :param Identifier identifier: Instance identifier
    :param BackboneElement udiDeviceIdentifier: Unique Device Identifier (UDI) Barcode string
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str deviceIdentifier: The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdiction provided in the DeviceDefinition.udiDeviceIdentifier
    :param str issuer: The organization that assigns the identifier algorithm
    :param str jurisdiction: The jurisdiction to which the deviceIdentifier applies
    :param BackboneElement marketDistribution: Indicates whether and when the device is available on the market
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Period marketPeriod: Begin and end dates for the commercial distribution of the device
    :param str subJurisdiction: National state or territory where the device is commercialized
    :param BackboneElement regulatoryIdentifier: Regulatory identifier(s) associated with this device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: basic | master | license
    :param str deviceIdentifier: The identifier itself
    :param str issuer: The organization that issued this identifier
    :param str jurisdiction: The jurisdiction to which the deviceIdentifier applies
    :param str partNumber: The part number or catalog number of the device
    :param Reference manufacturer: Name of device manufacturer
    :param BackboneElement deviceName: The name or names of the device as given by the manufacturer
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: A name that is used to refer to the device
    :param str type: registered-name | user-friendly-name | patient-reported-name
    :param str modelNumber: The catalog or model number for the device for example as defined by the manufacturer
    :param BackboneElement classification: What kind of device or device system this is
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A classification or risk class of the device model
    :param RelatedArtifact justification: Further information qualifying this classification of the device model
    :param BackboneElement conformsTo: Identifies the standards, specifications, or formal guidances for the capabilities supported by the device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Describes the common type of the standard, specification, or formal guidance
    :param CodeableConcept specification: Identifies the standard, specification, or formal guidance that the device adheres to the Device Specification type
    :param str version: The specific form or variant of the standard, specification or formal guidance
    :param RelatedArtifact source: Standard, regulation, certification, or guidance website, document, or other publication, or similar, supporting the conformance
    :param BackboneElement hasPart: A device, part of the current one
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Reference to the part
    :param int count: Number of occurrences of the part
    :param BackboneElement packaging: Information about the packaging of the device, i.e. how the device is packaged
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business identifier of the packaged medication
    :param CodeableConcept type: A code that defines the specific type of packaging
    :param int count: The number of items contained in the package (devices or sub-packages)
    :param BackboneElement distributor: An organization that distributes the packaged device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Distributor's human-readable name
    :param Reference organizationReference: Distributor as an Organization resource
    :param BackboneElement udiDeviceIdentifier: Unique Device Identifier (UDI) Barcode string
    :param BackboneElement packaging: Information about the packaging of the device, i.e. how the device is packaged
    :param BackboneElement version: The version of the device or software
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of the device version, e.g. manufacturer, approved, internal
    :param Identifier component: The hardware or software module of the device to which the version applies
    :param str value: The version text
    :param CodeableConcept safety: Safety characteristics of the device
    :param ProductShelfLife shelfLifeStorage: Shelf Life and storage information
    :param CodeableConcept languageCode: Language code for the human-readable text strings produced by the device (all supported)
    :param BackboneElement property: Inherent, essentially fixed, characteristics of this kind of device, e.g., time properties, size, etc
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
    :param Reference owner: Organization responsible for device
    :param ContactPoint contact: Details for human/organization for support
    :param BackboneElement link: An associated device, attached to, used with, communicating with or linking a previous or new device model to the focal device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding relation: The type indicates the relationship of the related device to the device instance
    :param CodeableReference relatedDevice: A reference to the linked device
    :param Annotation note: Device notes and comments
    :param BackboneElement material: A substance used to create the material(s) of which the device is made
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept substance: A relevant substance that the device contains, may contain, or is made of
    :param bool alternate: Indicates an alternative material of the device
    :param bool allergenicIndicator: Whether the substance is a known or suspected allergen
    :param str productionIdentifierInUDI: lot-number | manufactured-date | serial-number | expiration-date | biological-source | software-version
    :param BackboneElement guideline: Information aimed at providing directions for the usage of this model of device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param UsageContext useContext: The circumstances that form the setting for using the device
    :param str usageInstruction: Detailed written and visual directions for the user on how to use the device
    :param RelatedArtifact relatedArtifact: A source of information or reference for this guideline
    :param CodeableConcept indication: A clinical condition for which the device was designed to be used
    :param CodeableConcept contraindication: A specific situation when a device should not be used because it may cause harm
    :param CodeableConcept warning: Specific hazard alert information that a user needs to know before using the device
    :param str intendedUse: A description of the general purpose or medical use of the device or its function
    :param BackboneElement correctiveAction: Tracking of latest field safety corrective action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool recall: Whether the corrective action was a recall
    :param str scope: model | lot-numbers | serial-numbers
    :param Period period: Start and end dates of the  corrective action
    :param BackboneElement chargeItem: Billing code or reference associated with the device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference chargeItemCode: The code or reference for the charge item
    :param Quantity count: Coefficient applicable to the billing code
    :param Period effectivePeriod: A specific time period in which this charge item applies
    :param UsageContext useContext: The context to which this charge item applies
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    identifier: "Identifier" = None
    
    udiDeviceIdentifier: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    deviceIdentifier: str = None
    
    issuer: str = None
    
    jurisdiction: str = None
    
    marketDistribution: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    marketPeriod: "Period" = None
    
    subJurisdiction: str = None
    
    regulatoryIdentifier: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    deviceIdentifier: str = None
    
    issuer: str = None
    
    jurisdiction: str = None
    
    partNumber: str = None
    
    manufacturer: "Reference" = None
    
    deviceName: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: str = None
    
    modelNumber: str = None
    
    classification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    justification: "RelatedArtifact" = None
    
    conformsTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    specification: "CodeableConcept" = None
    
    version: str = None
    
    source: "RelatedArtifact" = None
    
    hasPart: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    reference: "Reference" = None
    
    count: int = None
    
    packaging: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    count: int = None
    
    distributor: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    organizationReference: "Reference" = None
    
    udiDeviceIdentifier: "BackboneElement" = None
    
    packaging: "BackboneElement" = None
    
    version: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    component: "Identifier" = None
    
    value: str = None
    
    safety: "CodeableConcept" = None
    
    shelfLifeStorage: "ProductShelfLife" = None
    
    languageCode: "CodeableConcept" = None
    
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
    
    owner: "Reference" = None
    
    contact: "ContactPoint" = None
    
    link: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relation: "Coding" = None
    
    relatedDevice: "CodeableReference" = None
    
    note: "Annotation" = None
    
    material: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substance: "CodeableConcept" = None
    
    alternate: bool = None
    
    allergenicIndicator: bool = None
    
    productionIdentifierInUDI: str = None
    
    guideline: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    useContext: "UsageContext" = None
    
    usageInstruction: str = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    indication: "CodeableConcept" = None
    
    contraindication: "CodeableConcept" = None
    
    warning: "CodeableConcept" = None
    
    intendedUse: str = None
    
    correctiveAction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    recall: bool = None
    
    scope: str = None
    
    period: "Period" = None
    
    chargeItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    chargeItemCode: "CodeableReference" = None
    
    count: "Quantity" = None
    
    effectivePeriod: "Period" = None
    
    useContext: "UsageContext" = None
    