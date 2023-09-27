"""
Generated class for DeviceDefinition. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ProductShelfLife import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class UdiDeviceIdentifier(BaseModel):
    """ Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str deviceIdentifier: The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier
    :param str issuer: The organization that assigns the identifier algorithm
    :param str jurisdiction: The jurisdiction to which the deviceIdentifier applies
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  deviceIdentifier: str = None,  issuer: str = None,  jurisdiction: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.deviceIdentifier: str = deviceIdentifier 
        self.issuer: str = issuer 
        self.jurisdiction: str = jurisdiction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "UdiDeviceIdentifier":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
    

class DeviceName(BaseModel):
    """ A name given to the device to identify it.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The name of the device
    :param str type: udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  name: str = None,  type: str = None, ):
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
    

class Specialization(BaseModel):
    """ The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str systemType: The standard that is used to operate and communicate
    :param str version: The version of the standard that is used to operate and communicate
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  systemType: str = None,  version: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.systemType: str = systemType 
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
    

class Capability(BaseModel):
    """ Device capabilities.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of capability
    :param 'CodeableConcept' description: Description of capability
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  description: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.description: list['CodeableConcept'] = description or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Capability":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
    

class Property(BaseModel):
    """ The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    :param 'Quantity' valueQuantity: Property value as a quantity
    :param 'CodeableConcept' valueCode: Property value as a code, e.g., NTP4 (synced to NTP)
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  valueQuantity: 'Quantity' = None,  valueCode: 'CodeableConcept' = None, ):
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
    

class Material(BaseModel):
    """ A substance used to create the material(s) of which the device is made.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' substance: The substance
    :param bool alternate: Indicates an alternative material of the device
    :param bool allergenicIndicator: Whether the substance is a known or suspected allergen
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  substance: 'CodeableConcept' = None,  alternate: bool = None,  allergenicIndicator: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.substance: 'CodeableConcept' = substance 
        self.alternate: bool = alternate 
        self.allergenicIndicator: bool = allergenicIndicator 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Material":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


class DeviceDefinition(DomainResource):
    """ The characteristics, operational status and capabilities of a medical-related component of a medical device.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Instance identifier
    :param 'UdiDeviceIdentifier' udiDeviceIdentifier: Unique Device Identifier (UDI) Barcode string
    :param str manufacturerString: Name of device manufacturer
    :param 'Reference' manufacturerReference: Name of device manufacturer
    :param 'DeviceName' deviceName: A name given to the device to identify it
    :param str modelNumber: The model number for the device
    :param 'CodeableConcept' type: What kind of device or device system this is
    :param 'Specialization' specialization: The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    :param str version: Available versions
    :param 'CodeableConcept' safety: Safety characteristics of the device
    :param 'ProductShelfLife' shelfLifeStorage: Shelf Life and storage information
    :param 'ProdCharacteristic' physicalCharacteristics: Dimensions, color etc.
    :param 'CodeableConcept' languageCode: Language code for the human-readable text strings produced by the device (all supported)
    :param 'Capability' capability: Device capabilities
    :param 'Property' property: The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    :param 'Reference' owner: Organization responsible for device
    :param 'ContactPoint' contact: Details for human/organization for support
    :param str url: Network address to contact device
    :param str onlineInformation: Access to on-line information
    :param 'Annotation' note: Device notes and comments
    :param 'Quantity' quantity: The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product)
    :param 'Reference' parentDevice: The parent device it can be part of
    :param 'Material' material: A substance used to create the material(s) of which the device is made
    """
    def __init__(self, resourceType: str = "DeviceDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  udiDeviceIdentifier: 'UdiDeviceIdentifier' = None,  manufacturerString: str = None,  manufacturerReference: 'Reference' = None,  deviceName: 'DeviceName' = None,  modelNumber: str = None,  type: 'CodeableConcept' = None,  specialization: 'Specialization' = None,  version: str = None,  safety: 'CodeableConcept' = None,  shelfLifeStorage: 'ProductShelfLife' = None,  physicalCharacteristics: 'ProdCharacteristic' = None,  languageCode: 'CodeableConcept' = None,  capability: 'Capability' = None,  property: 'Property' = None,  owner: 'Reference' = None,  contact: 'ContactPoint' = None,  url: str = None,  onlineInformation: str = None,  note: 'Annotation' = None,  quantity: 'Quantity' = None,  parentDevice: 'Reference' = None,  material: 'Material' = None, ):
        self.resourceType: str = resourceType or "DeviceDefinition"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.udiDeviceIdentifier: list['UdiDeviceIdentifier'] = udiDeviceIdentifier or []
        self.manufacturerString: str = manufacturerString 
        self.manufacturerReference: 'Reference' = manufacturerReference 
        self.deviceName: list['DeviceName'] = deviceName or []
        self.modelNumber: str = modelNumber 
        self.type: 'CodeableConcept' = type 
        self.specialization: list['Specialization'] = specialization or []
        self.version: list[str] = version or []
        self.safety: list['CodeableConcept'] = safety or []
        self.shelfLifeStorage: list['ProductShelfLife'] = shelfLifeStorage or []
        self.physicalCharacteristics: 'ProdCharacteristic' = physicalCharacteristics 
        self.languageCode: list['CodeableConcept'] = languageCode or []
        self.capability: list['Capability'] = capability or []
        self.property: list['Property'] = property or []
        self.owner: 'Reference' = owner 
        self.contact: list['ContactPoint'] = contact or []
        self.url: str = url 
        self.onlineInformation: str = onlineInformation 
        self.note: list['Annotation'] = note or []
        self.quantity: 'Quantity' = quantity 
        self.parentDevice: 'Reference' = parentDevice 
        self.material: list['Material'] = material or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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