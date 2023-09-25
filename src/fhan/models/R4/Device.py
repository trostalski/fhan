"""
Generated class for Device. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class UdiCarrier(ModelBase):
    """ Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str deviceIdentifier: Mandatory fixed portion of UDI
    :param str issuer: UDI Issuing Organization
    :param str jurisdiction: Regional UDI authority
    :param str carrierAIDC: UDI Machine Readable Barcode String
    :param str carrierHRF: UDI Human Readable Barcode String
    :param str entryType: barcode | rfid | manual +
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  deviceIdentifier: str = None,  issuer: str = None,  jurisdiction: str = None,  carrierAIDC: str = None,  carrierHRF: str = None,  entryType: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.deviceIdentifier: str = deviceIdentifier 
        self.issuer: str = issuer 
        self.jurisdiction: str = jurisdiction 
        self.carrierAIDC: str = carrierAIDC 
        self.carrierHRF: str = carrierHRF 
        self.entryType: str = entryType 
        

    @classmethod
    def from_dict(cls, data: dict) -> "UdiCarrier":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class DeviceName(ModelBase):
    """ This represents the manufacturer's name of the device as provided by the device, from a UDI label, or by a person describing the Device.  This typically would be used when a person provides the name(s) or when the device represents one of the names available from DeviceDefinition.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The name of the device
    :param str type: udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  type: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.type: str = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceName":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class Specialization(ModelBase):
    """ The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' systemType: The standard that is used to operate and communicate
    :param str version: The version of the standard that is used to operate and communicate
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  systemType: 'CodeableConcept' = None,  version: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.systemType: 'CodeableConcept' = systemType 
        self.version: str = version 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Specialization":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class Version(ModelBase):
    """ The actual design of the device or software version running on the device.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: The type of the device version
    :param 'Identifier' component: A single component of the device version
    :param str value: The version text
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  component: 'Identifier' = None,  value: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.component: 'Identifier' = component 
        self.value: str = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Version":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class Property(ModelBase):
    """ The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    :param list['Quantity'] valueQuantity: Property value as a quantity
    :param list['CodeableConcept'] valueCode: Property value as a code, e.g., NTP4 (synced to NTP)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  valueQuantity: list['Quantity'] = None,  valueCode: list['CodeableConcept'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.valueQuantity: list['Quantity'] = valueQuantity or []
        self.valueCode: list['CodeableConcept'] = valueCode or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Property":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


class Device(DomainResource):
    """ A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Instance identifier
    :param 'Reference' definition: The reference to the definition for the device
    :param list['UdiCarrier'] udiCarrier: Unique Device Identifier (UDI) Barcode string
    :param str status: active | inactive | entered-in-error | unknown
    :param list['CodeableConcept'] statusReason: online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off
    :param str distinctIdentifier: The distinct identification string
    :param str manufacturer: Name of device manufacturer
    :param str manufactureDate: Date when the device was made
    :param str expirationDate: Date and time of expiry of this device (if applicable)
    :param str lotNumber: Lot number of manufacture
    :param str serialNumber: Serial number assigned by the manufacturer
    :param list['DeviceName'] deviceName: The name of the device as given by the manufacturer
    :param str modelNumber: The model number for the device
    :param str partNumber: The part number of the device
    :param 'CodeableConcept' type: The kind or type of device
    :param list['Specialization'] specialization: The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    :param list['Version'] version: The actual design of the device or software version running on the device
    :param list['Property'] property: The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    :param 'Reference' patient: Patient to whom Device is affixed
    :param 'Reference' owner: Organization responsible for device
    :param list['ContactPoint'] contact: Details for human/organization for support
    :param 'Reference' location: Where the device is found
    :param str url: Network address to contact device
    :param list['Annotation'] note: Device notes and comments
    :param list['CodeableConcept'] safety: Safety Characteristics of Device
    :param 'Reference' parent: The parent device
    """
    def __init__(self, resourceType: str = "Device",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  definition: 'Reference' = None,  udiCarrier: list['UdiCarrier'] = None,  status: str = None,  statusReason: list['CodeableConcept'] = None,  distinctIdentifier: str = None,  manufacturer: str = None,  manufactureDate: str = None,  expirationDate: str = None,  lotNumber: str = None,  serialNumber: str = None,  deviceName: list['DeviceName'] = None,  modelNumber: str = None,  partNumber: str = None,  type: 'CodeableConcept' = None,  specialization: list['Specialization'] = None,  version: list['Version'] = None,  property: list['Property'] = None,  patient: 'Reference' = None,  owner: 'Reference' = None,  contact: list['ContactPoint'] = None,  location: 'Reference' = None,  url: str = None,  note: list['Annotation'] = None,  safety: list['CodeableConcept'] = None,  parent: 'Reference' = None, ):
        self.resourceType: str = resourceType or "Device"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.definition: 'Reference' = definition 
        self.udiCarrier: list['UdiCarrier'] = udiCarrier or []
        self.status: str = status 
        self.statusReason: list['CodeableConcept'] = statusReason or []
        self.distinctIdentifier: str = distinctIdentifier 
        self.manufacturer: str = manufacturer 
        self.manufactureDate: str = manufactureDate 
        self.expirationDate: str = expirationDate 
        self.lotNumber: str = lotNumber 
        self.serialNumber: str = serialNumber 
        self.deviceName: list['DeviceName'] = deviceName or []
        self.modelNumber: str = modelNumber 
        self.partNumber: str = partNumber 
        self.type: 'CodeableConcept' = type 
        self.specialization: list['Specialization'] = specialization or []
        self.version: list['Version'] = version or []
        self.property: list['Property'] = property or []
        self.patient: 'Reference' = patient 
        self.owner: 'Reference' = owner 
        self.contact: list['ContactPoint'] = contact or []
        self.location: 'Reference' = location 
        self.url: str = url 
        self.note: list['Annotation'] = note or []
        self.safety: list['CodeableConcept'] = safety or []
        self.parent: 'Reference' = parent 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance