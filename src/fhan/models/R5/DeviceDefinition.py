"""
Generated class for DeviceDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Period import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Range import *
from fhan.models.R5.ProductShelfLife import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Coding import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class MarketDistribution(BaseModel):
    """ Indicates where and when the device is available on the market.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Period marketPeriod: Begin and end dates for the commercial distribution of the device
    :param str subJurisdiction: National state or territory where the device is commercialized
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "marketPeriod": {"class_name": "Period", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  marketPeriod:  'Period'  = None,  subJurisdiction:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.marketPeriod = marketPeriod 
        self.subJurisdiction = subJurisdiction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class UdiDeviceIdentifier(BaseModel):
    """ Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str deviceIdentifier: The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdiction provided in the DeviceDefinition.udiDeviceIdentifier
    :param str issuer: The organization that assigns the identifier algorithm
    :param str jurisdiction: The jurisdiction to which the deviceIdentifier applies
    :param MarketDistribution marketDistribution: Indicates whether and when the device is available on the market
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        "marketDistribution": {"class_name": "MarketDistribution", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  deviceIdentifier:  'str'  = None,  issuer:  'str'  = None,  jurisdiction:  'str'  = None,  marketDistribution:  list['MarketDistribution']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.deviceIdentifier = deviceIdentifier 
        self.issuer = issuer 
        self.jurisdiction = jurisdiction 
        self.marketDistribution = marketDistribution or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class RegulatoryIdentifier(BaseModel):
    """ Identifier associated with the regulatory documentation (certificates, technical documentation, post-market surveillance documentation and reports) of a set of device models sharing the same intended purpose, risk class and essential design and manufacturing characteristics. One example is the Basic UDI-DI in Europe.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: basic | master | license
    :param str deviceIdentifier: The identifier itself
    :param str issuer: The organization that issued this identifier
    :param str jurisdiction: The jurisdiction to which the deviceIdentifier applies
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'str'  = None,  deviceIdentifier:  'str'  = None,  issuer:  'str'  = None,  jurisdiction:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.deviceIdentifier = deviceIdentifier 
        self.issuer = issuer 
        self.jurisdiction = jurisdiction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class DeviceName(BaseModel):
    """ The name or names of the device as given by the manufacturer.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: A name that is used to refer to the device
    :param str type: registered-name | user-friendly-name | patient-reported-name
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  type:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.type = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Classification(BaseModel):
    """ What kind of device or device system this is.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A classification or risk class of the device model
    :param RelatedArtifact justification: Further information qualifying this classification of the device model
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "justification": {"class_name": "RelatedArtifact", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  justification:  list['RelatedArtifact']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.justification = justification or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ConformsTo(BaseModel):
    """ Identifies the standards, specifications, or formal guidances for the capabilities supported by the device. The device may be certified as conformant to these specifications e.g., communication, performance, process, measurement, or specialization standards.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Describes the common type of the standard, specification, or formal guidance
    :param CodeableConcept specification: Identifies the standard, specification, or formal guidance that the device adheres to the Device Specification type
    :param str version: The specific form or variant of the standard, specification or formal guidance
    :param RelatedArtifact source: Standard, regulation, certification, or guidance website, document, or other publication, or similar, supporting the conformance
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "specification": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "source": {"class_name": "RelatedArtifact", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  category:  'CodeableConcept'  = None,  specification:  'CodeableConcept'  = None,  version:  list['str']  = None,  source:  list['RelatedArtifact']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category 
        self.specification = specification 
        self.version = version or []
        self.source = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class HasPart(BaseModel):
    """ A device that is part (for example a component) of the present device.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Reference to the part
    :param int count: Number of occurrences of the part
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  reference:  'Reference'  = None,  count:  'int'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.reference = reference 
        self.count = count 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Distributor(BaseModel):
    """ An organization that distributes the packaged device.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Distributor's human-readable name
    :param Reference organizationReference: Distributor as an Organization resource
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "organizationReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  organizationReference:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.organizationReference = organizationReference or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Packaging(BaseModel):
    """ Information about the packaging of the device, i.e. how the device is packaged.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business identifier of the packaged medication
    :param CodeableConcept type: A code that defines the specific type of packaging
    :param int count: The number of items contained in the package (devices or sub-packages)
    :param Distributor distributor: An organization that distributes the packaged device
    :param UdiDeviceIdentifier udiDeviceIdentifier: Unique Device Identifier (UDI) Barcode string on the packaging
    :param Packaging packaging: Allows packages within packages
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "distributor": {"class_name": "Distributor", "is_contained": True},
        
        
        "udiDeviceIdentifier": {"class_name": "UdiDeviceIdentifier", "is_contained": True},
        
        
        "packaging": {"class_name": "Packaging", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  'Identifier'  = None,  type:  'CodeableConcept'  = None,  count:  'int'  = None,  distributor:  list['Distributor']  = None,  udiDeviceIdentifier:  list['UdiDeviceIdentifier']  = None,  packaging:  list['Packaging']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier 
        self.type = type 
        self.count = count 
        self.distributor = distributor or []
        self.udiDeviceIdentifier = udiDeviceIdentifier or []
        self.packaging = packaging or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Version(BaseModel):
    """ The version of the device or software.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of the device version, e.g. manufacturer, approved, internal
    :param Identifier component: The hardware or software module of the device to which the version applies
    :param str value: The version text
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "component": {"class_name": "Identifier", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  component:  'Identifier'  = None,  value:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.component = component 
        self.value = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Property(BaseModel):
    """ Static or essentially fixed characteristics or features of this kind of device that are otherwise not captured in more specific attributes, e.g., time or timing attributes, resolution, accuracy, and physical attributes.:param str id: Unique id for inter-element referencing
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
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Link(BaseModel):
    """ An associated device, attached to, used with, communicating with or linking a previous or new device model to the focal device.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding relation: The type indicates the relationship of the related device to the device instance
    :param CodeableReference relatedDevice: A reference to the linked device
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "relation": {"class_name": "Coding", "is_contained": False},
        
        
        "relatedDevice": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  relation:  'Coding'  = None,  relatedDevice:  'CodeableReference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.relation = relation 
        self.relatedDevice = relatedDevice 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Material(BaseModel):
    """ A substance used to create the material(s) of which the device is made.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept substance: A relevant substance that the device contains, may contain, or is made of
    :param bool alternate: Indicates an alternative material of the device
    :param bool allergenicIndicator: Whether the substance is a known or suspected allergen
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "substance": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  substance:  'CodeableConcept'  = None,  alternate:  'bool'  = None,  allergenicIndicator:  'bool'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.substance = substance 
        self.alternate = alternate 
        self.allergenicIndicator = allergenicIndicator 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Guideline(BaseModel):
    """ Information aimed at providing directions for the usage of this model of device.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param UsageContext useContext: The circumstances that form the setting for using the device
    :param str usageInstruction: Detailed written and visual directions for the user on how to use the device
    :param RelatedArtifact relatedArtifact: A source of information or reference for this guideline
    :param CodeableConcept indication: A clinical condition for which the device was designed to be used
    :param CodeableConcept contraindication: A specific situation when a device should not be used because it may cause harm
    :param CodeableConcept warning: Specific hazard alert information that a user needs to know before using the device
    :param str intendedUse: A description of the general purpose or medical use of the device or its function
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        "indication": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "contraindication": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "warning": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  useContext:  list['UsageContext']  = None,  usageInstruction:  'str'  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  indication:  list['CodeableConcept']  = None,  contraindication:  list['CodeableConcept']  = None,  warning:  list['CodeableConcept']  = None,  intendedUse:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.useContext = useContext or []
        self.usageInstruction = usageInstruction 
        self.relatedArtifact = relatedArtifact or []
        self.indication = indication or []
        self.contraindication = contraindication or []
        self.warning = warning or []
        self.intendedUse = intendedUse 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class CorrectiveAction(BaseModel):
    """ Tracking of latest field safety corrective action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool recall: Whether the corrective action was a recall
    :param str scope: model | lot-numbers | serial-numbers
    :param Period period: Start and end dates of the  corrective action
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  recall:  'bool'  = None,  scope:  'str'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.recall = recall 
        self.scope = scope 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ChargeItem(BaseModel):
    """ Billing code or reference associated with the device.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference chargeItemCode: The code or reference for the charge item
    :param Quantity count: Coefficient applicable to the billing code
    :param Period effectivePeriod: A specific time period in which this charge item applies
    :param UsageContext useContext: The context to which this charge item applies
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "chargeItemCode": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "count": {"class_name": "Quantity", "is_contained": False},
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  chargeItemCode:  'CodeableReference'  = None,  count:  'Quantity'  = None,  effectivePeriod:  'Period'  = None,  useContext:  list['UsageContext']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.chargeItemCode = chargeItemCode 
        self.count = count 
        self.effectivePeriod = effectivePeriod 
        self.useContext = useContext or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DeviceDefinition(DomainResource):
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
    :param UdiDeviceIdentifier udiDeviceIdentifier: Unique Device Identifier (UDI) Barcode string
    :param RegulatoryIdentifier regulatoryIdentifier: Regulatory identifier(s) associated with this device
    :param str partNumber: The part number or catalog number of the device
    :param Reference manufacturer: Name of device manufacturer
    :param DeviceName deviceName: The name or names of the device as given by the manufacturer
    :param str modelNumber: The catalog or model number for the device for example as defined by the manufacturer
    :param Classification classification: What kind of device or device system this is
    :param ConformsTo conformsTo: Identifies the standards, specifications, or formal guidances for the capabilities supported by the device
    :param HasPart hasPart: A device, part of the current one
    :param Packaging packaging: Information about the packaging of the device, i.e. how the device is packaged
    :param Version version: The version of the device or software
    :param CodeableConcept safety: Safety characteristics of the device
    :param ProductShelfLife shelfLifeStorage: Shelf Life and storage information
    :param CodeableConcept languageCode: Language code for the human-readable text strings produced by the device (all supported)
    :param Property property: Inherent, essentially fixed, characteristics of this kind of device, e.g., time properties, size, etc
    :param Reference owner: Organization responsible for device
    :param ContactPoint contact: Details for human/organization for support
    :param Link link: An associated device, attached to, used with, communicating with or linking a previous or new device model to the focal device
    :param Annotation note: Device notes and comments
    :param Material material: A substance used to create the material(s) of which the device is made
    :param str productionIdentifierInUDI: lot-number | manufactured-date | serial-number | expiration-date | biological-source | software-version
    :param Guideline guideline: Information aimed at providing directions for the usage of this model of device
    :param CorrectiveAction correctiveAction: Tracking of latest field safety corrective action
    :param ChargeItem chargeItem: Billing code or reference associated with the device
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "udiDeviceIdentifier": {"class_name": "UdiDeviceIdentifier", "is_contained": True},
        
        
        "regulatoryIdentifier": {"class_name": "RegulatoryIdentifier", "is_contained": True},
        
        
        
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        
        
        "deviceName": {"class_name": "DeviceName", "is_contained": True},
        
        
        
        "classification": {"class_name": "Classification", "is_contained": True},
        
        
        "conformsTo": {"class_name": "ConformsTo", "is_contained": True},
        
        
        "hasPart": {"class_name": "HasPart", "is_contained": True},
        
        
        "packaging": {"class_name": "Packaging", "is_contained": True},
        
        
        "version": {"class_name": "Version", "is_contained": True},
        
        
        "safety": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "shelfLifeStorage": {"class_name": "ProductShelfLife", "is_contained": False},
        
        
        "languageCode": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "owner": {"class_name": "Reference", "is_contained": False},
        
        
        "contact": {"class_name": "ContactPoint", "is_contained": False},
        
        
        "link": {"class_name": "Link", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "material": {"class_name": "Material", "is_contained": True},
        
        
        
        "guideline": {"class_name": "Guideline", "is_contained": True},
        
        
        "correctiveAction": {"class_name": "CorrectiveAction", "is_contained": True},
        
        
        "chargeItem": {"class_name": "ChargeItem", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  identifier:  list['Identifier']  = None,  udiDeviceIdentifier:  list['UdiDeviceIdentifier']  = None,  regulatoryIdentifier:  list['RegulatoryIdentifier']  = None,  partNumber:  'str'  = None,  manufacturer:  'Reference'  = None,  deviceName:  list['DeviceName']  = None,  modelNumber:  'str'  = None,  classification:  list['Classification']  = None,  conformsTo:  list['ConformsTo']  = None,  hasPart:  list['HasPart']  = None,  packaging:  list['Packaging']  = None,  version:  list['Version']  = None,  safety:  list['CodeableConcept']  = None,  shelfLifeStorage:  list['ProductShelfLife']  = None,  languageCode:  list['CodeableConcept']  = None,  property:  list['Property']  = None,  owner:  'Reference'  = None,  contact:  list['ContactPoint']  = None,  link:  list['Link']  = None,  note:  list['Annotation']  = None,  material:  list['Material']  = None,  productionIdentifierInUDI:  list['str']  = None,  guideline:  'Guideline'  = None,  correctiveAction:  'CorrectiveAction'  = None,  chargeItem:  list['ChargeItem']  = None, ):
        self.resourceType = resourceType or "DeviceDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.identifier = identifier or []
        self.udiDeviceIdentifier = udiDeviceIdentifier or []
        self.regulatoryIdentifier = regulatoryIdentifier or []
        self.partNumber = partNumber 
        self.manufacturer = manufacturer 
        self.deviceName = deviceName or []
        self.modelNumber = modelNumber 
        self.classification = classification or []
        self.conformsTo = conformsTo or []
        self.hasPart = hasPart or []
        self.packaging = packaging or []
        self.version = version or []
        self.safety = safety or []
        self.shelfLifeStorage = shelfLifeStorage or []
        self.languageCode = languageCode or []
        self.property = property or []
        self.owner = owner 
        self.contact = contact or []
        self.link = link or []
        self.note = note or []
        self.material = material or []
        self.productionIdentifierInUDI = productionIdentifierInUDI or []
        self.guideline = guideline 
        self.correctiveAction = correctiveAction 
        self.chargeItem = chargeItem or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DeviceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()