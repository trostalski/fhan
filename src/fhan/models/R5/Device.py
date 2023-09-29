"""
Generated class for Device. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Count import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class UdiCarrier(BaseModel):
    """ Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str deviceIdentifier: Mandatory fixed portion of UDI
    :param str issuer: UDI Issuing Organization
    :param str jurisdiction: Regional UDI authority
    :param str carrierAIDC: UDI Machine Readable Barcode String
    :param str carrierHRF: UDI Human Readable Barcode String
    :param str entryType: barcode | rfid | manual | card | self-reported | electronic-transmission | unknown
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  deviceIdentifier:  'str'  = None,  issuer:  'str'  = None,  jurisdiction:  'str'  = None,  carrierAIDC:  'str'  = None,  carrierHRF:  'str'  = None,  entryType:  'str'  = None, ):
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


    
    

class Name(BaseModel):
    """ This represents the manufacturer's name of the device as provided by the device, from a UDI label, or by a person describing the Device.  This typically would be used when a person provides the name(s) or when the device represents one of the names available from DeviceDefinition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str value: The term that names the device
    :param str type: registered-name | user-friendly-name | patient-reported-name
    :param bool display: The preferred device name
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  value:  'str'  = None,  type:  'str'  = None,  display:  'bool'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.value = value 
        self.type = type 
        self.display = display 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Version(BaseModel):
    """ The actual design of the device or software version running on the device.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of the device version, e.g. manufacturer, approved, internal
    :param Identifier component: The hardware or software module of the device to which the version applies
    :param str installDate: The date the version was installed on the device
    :param str value: The version text
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "component": {"class_name": "Identifier", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  component:  'Identifier'  = None,  installDate:  'str'  = None,  value:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.component = component 
        self.installDate = installDate 
        self.value = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ConformsTo(BaseModel):
    """ Identifies the standards, specifications, or formal guidances for the capabilities supported by the device. The device may be certified as conformant to these specifications e.g., communication, performance, process, measurement, or specialization standards.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Describes the common type of the standard, specification, or formal guidance.  communication | performance | measurement
    :param CodeableConcept specification: Identifies the standard, specification, or formal guidance that the device adheres to
    :param str version: Specific form or variant of the standard
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "specification": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  category:  'CodeableConcept'  = None,  specification:  'CodeableConcept'  = None,  version:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category 
        self.specification = specification 
        self.version = version 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Property(BaseModel):
    """ Static or essentially fixed characteristics or features of the device (e.g., time or timing attributes, resolution, accuracy, intended use or instructions for use, and physical attributes) that are not otherwise captured in more specific attributes.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code that specifies the property being represented
    :param Quantity valueQuantity: Value of the property
    :param CodeableConcept valueCodeableConcept: Value of the property
    :param str valueString: Value of the property
    :param bool valueBoolean: Value of the property
    :param int valueInteger: Value of the property
    :param Range valueRange: Value of the property
    :param Attachment valueAttachment: Value of the property
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueString:  'str'  = None,  valueBoolean:  'bool'  = None,  valueInteger:  'int'  = None,  valueRange:  'Range'  = None,  valueAttachment:  'Attachment'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueQuantity = valueQuantity 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueString = valueString 
        self.valueBoolean = valueBoolean 
        self.valueInteger = valueInteger 
        self.valueRange = valueRange 
        self.valueAttachment = valueAttachment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Device":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Device":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Device(DomainResource):
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
    :param UdiCarrier udiCarrier: Unique Device Identifier (UDI) Barcode string
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept availabilityStatus: lost | damaged | destroyed | available
    :param Identifier biologicalSourceEvent: An identifier that supports traceability to the event during which material in this product from one or more biological entities was obtained or pooled
    :param str manufacturer: Name of device manufacturer
    :param str manufactureDate: Date when the device was made
    :param str expirationDate: Date and time of expiry of this device (if applicable)
    :param str lotNumber: Lot number of manufacture
    :param str serialNumber: Serial number assigned by the manufacturer
    :param Name name: The name or names of the device as known to the manufacturer and/or patient
    :param str modelNumber: The manufacturer's model number for the device
    :param str partNumber: The part number or catalog number of the device
    :param CodeableConcept category: Indicates a high-level grouping of the device
    :param CodeableConcept type: The kind or type of device
    :param Version version: The actual design of the device or software version running on the device
    :param ConformsTo conformsTo: Identifies the standards, specifications, or formal guidances for the capabilities supported by the device
    :param Property property: Inherent, essentially fixed, characteristics of the device.  e.g., time properties, size, material, etc.
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
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "definition": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "udiCarrier": {"class_name": "UdiCarrier", "is_contained": True},
        
        
        
        "availabilityStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "biologicalSourceEvent": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        
        
        "name": {"class_name": "Name", "is_contained": True},
        
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "version": {"class_name": "Version", "is_contained": True},
        
        
        "conformsTo": {"class_name": "ConformsTo", "is_contained": True},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "mode": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "cycle": {"class_name": "Count", "is_contained": False},
        
        
        "duration": {"class_name": "Duration", "is_contained": False},
        
        
        "owner": {"class_name": "Reference", "is_contained": False},
        
        
        "contact": {"class_name": "ContactPoint", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        
        "endpoint": {"class_name": "Reference", "is_contained": False},
        
        
        "gateway": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "safety": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "parent": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  displayName:  'str'  = None,  definition:  'CodeableReference'  = None,  udiCarrier:  list['UdiCarrier']  = None,  status:  'str'  = None,  availabilityStatus:  'CodeableConcept'  = None,  biologicalSourceEvent:  'Identifier'  = None,  manufacturer:  'str'  = None,  manufactureDate:  'str'  = None,  expirationDate:  'str'  = None,  lotNumber:  'str'  = None,  serialNumber:  'str'  = None,  name:  list['Name']  = None,  modelNumber:  'str'  = None,  partNumber:  'str'  = None,  category:  list['CodeableConcept']  = None,  type:  list['CodeableConcept']  = None,  version:  list['Version']  = None,  conformsTo:  list['ConformsTo']  = None,  property:  list['Property']  = None,  mode:  'CodeableConcept'  = None,  cycle:  'Count'  = None,  duration:  'Duration'  = None,  owner:  'Reference'  = None,  contact:  list['ContactPoint']  = None,  location:  'Reference'  = None,  url:  'str'  = None,  endpoint:  list['Reference']  = None,  gateway:  list['CodeableReference']  = None,  note:  list['Annotation']  = None,  safety:  list['CodeableConcept']  = None,  parent:  'Reference'  = None, ):
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
        self.displayName = displayName 
        self.definition = definition 
        self.udiCarrier = udiCarrier or []
        self.status = status 
        self.availabilityStatus = availabilityStatus 
        self.biologicalSourceEvent = biologicalSourceEvent 
        self.manufacturer = manufacturer 
        self.manufactureDate = manufactureDate 
        self.expirationDate = expirationDate 
        self.lotNumber = lotNumber 
        self.serialNumber = serialNumber 
        self.name = name or []
        self.modelNumber = modelNumber 
        self.partNumber = partNumber 
        self.category = category or []
        self.type = type or []
        self.version = version or []
        self.conformsTo = conformsTo or []
        self.property = property or []
        self.mode = mode 
        self.cycle = cycle 
        self.duration = duration 
        self.owner = owner 
        self.contact = contact or []
        self.location = location 
        self.url = url 
        self.endpoint = endpoint or []
        self.gateway = gateway or []
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