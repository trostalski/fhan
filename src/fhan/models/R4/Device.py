"""
Generated class for Device. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class UdiCarrier(BaseModel):
    """Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str deviceIdentifier: Mandatory fixed portion of UDI
    :param str issuer: UDI Issuing Organization
    :param str jurisdiction: Regional UDI authority
    :param str carrierAIDC: UDI Machine Readable Barcode String
    :param str carrierHRF: UDI Human Readable Barcode String
    :param str entryType: barcode | rfid | manual +
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        deviceIdentifier: "str" = None,
        issuer: "str" = None,
        jurisdiction: "str" = None,
        carrierAIDC: "str" = None,
        carrierHRF: "str" = None,
        entryType: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.deviceIdentifier = deviceIdentifier
        self.issuer = issuer
        self.jurisdiction = jurisdiction
        self.carrierAIDC = carrierAIDC
        self.carrierHRF = carrierHRF
        self.entryType = entryType

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DeviceName(BaseModel):
    """This represents the manufacturer's name of the device as provided by the device, from a UDI label, or by a person describing the Device.  This typically would be used when a person provides the name(s) or when the device represents one of the names available from DeviceDefinition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The name of the device
    :param str type: udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        type: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.type = type

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Specialization(BaseModel):
    """The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept systemType: The standard that is used to operate and communicate
    :param str version: The version of the standard that is used to operate and communicate
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "systemType": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        systemType: "CodeableConcept" = None,
        version: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.systemType = systemType
        self.version = version

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Version(BaseModel):
    """The actual design of the device or software version running on the device.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of the device version
    :param Identifier component: A single component of the device version
    :param str value: The version text
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "component": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        component: "Identifier" = None,
        value: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.component = component
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Property(BaseModel):
    """The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    :param Quantity valueQuantity: Property value as a quantity
    :param CodeableConcept valueCode: Property value as a code, e.g., NTP4 (synced to NTP)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueCode": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        valueQuantity: list["Quantity"] = None,
        valueCode: list["CodeableConcept"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.valueQuantity = valueQuantity or []
        self.valueCode = valueCode or []

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Device(DomainResource):
    """A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.
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
    :param UdiCarrier udiCarrier: Unique Device Identifier (UDI) Barcode string
    :param str status: active | inactive | entered-in-error | unknown
    :param CodeableConcept statusReason: online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off
    :param str distinctIdentifier: The distinct identification string
    :param str manufacturer: Name of device manufacturer
    :param str manufactureDate: Date when the device was made
    :param str expirationDate: Date and time of expiry of this device (if applicable)
    :param str lotNumber: Lot number of manufacture
    :param str serialNumber: Serial number assigned by the manufacturer
    :param DeviceName deviceName: The name of the device as given by the manufacturer
    :param str modelNumber: The model number for the device
    :param str partNumber: The part number of the device
    :param CodeableConcept type: The kind or type of device
    :param Specialization specialization: The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    :param Version version: The actual design of the device or software version running on the device
    :param Property property: The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    :param Reference patient: Patient to whom Device is affixed
    :param Reference owner: Organization responsible for device
    :param ContactPoint contact: Details for human/organization for support
    :param Reference location: Where the device is found
    :param str url: Network address to contact device
    :param Annotation note: Device notes and comments
    :param CodeableConcept safety: Safety Characteristics of Device
    :param Reference parent: The parent device
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "definition": {"class_name": "Reference", "is_contained": False},
        "udiCarrier": {"class_name": "UdiCarrier", "is_contained": True},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "deviceName": {"class_name": "DeviceName", "is_contained": True},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "specialization": {"class_name": "Specialization", "is_contained": True},
        "version": {"class_name": "Version", "is_contained": True},
        "property": {"class_name": "Property", "is_contained": True},
        "patient": {"class_name": "Reference", "is_contained": False},
        "owner": {"class_name": "Reference", "is_contained": False},
        "contact": {"class_name": "ContactPoint", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "safety": {"class_name": "CodeableConcept", "is_contained": False},
        "parent": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        definition: "Reference" = None,
        udiCarrier: list["UdiCarrier"] = None,
        status: "str" = None,
        statusReason: list["CodeableConcept"] = None,
        distinctIdentifier: "str" = None,
        manufacturer: "str" = None,
        manufactureDate: "str" = None,
        expirationDate: "str" = None,
        lotNumber: "str" = None,
        serialNumber: "str" = None,
        deviceName: list["DeviceName"] = None,
        modelNumber: "str" = None,
        partNumber: "str" = None,
        type: "CodeableConcept" = None,
        specialization: list["Specialization"] = None,
        version: list["Version"] = None,
        property: list["Property"] = None,
        patient: "Reference" = None,
        owner: "Reference" = None,
        contact: list["ContactPoint"] = None,
        location: "Reference" = None,
        url: "str" = None,
        note: list["Annotation"] = None,
        safety: list["CodeableConcept"] = None,
        parent: "Reference" = None,
    ):
        self.resourceType = resourceType or "Device"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.definition = definition
        self.udiCarrier = udiCarrier or []
        self.status = status
        self.statusReason = statusReason or []
        self.distinctIdentifier = distinctIdentifier
        self.manufacturer = manufacturer
        self.manufactureDate = manufactureDate
        self.expirationDate = expirationDate
        self.lotNumber = lotNumber
        self.serialNumber = serialNumber
        self.deviceName = deviceName or []
        self.modelNumber = modelNumber
        self.partNumber = partNumber
        self.type = type
        self.specialization = specialization or []
        self.version = version or []
        self.property = property or []
        self.patient = patient
        self.owner = owner
        self.contact = contact or []
        self.location = location
        self.url = url
        self.note = note or []
        self.safety = safety or []
        self.parent = parent

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
