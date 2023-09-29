"""
Generated class for InventoryItem. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Address import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Range import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Name(BaseModel):
    """ The item name(s) - the brand name, or common name, functional name, generic name.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding nameType: The type of name e.g. 'brand-name', 'functional-name', 'common-name'
    :param str language: The language used to express the item name
    :param str name: The name or designation of the item
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "nameType": {"class_name": "Coding", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  nameType:  'Coding'  = None,  language:  'str'  = None,  name:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.nameType = nameType 
        self.language = language 
        self.name = name 
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryItem":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryItem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ResponsibleOrganization(BaseModel):
    """ Organization(s) responsible for the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: The role of the organization e.g. manufacturer, distributor, or other
    :param Reference organization: An organization that is associated with the item
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "organization": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  role:  'CodeableConcept'  = None,  organization:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role 
        self.organization = organization 
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryItem":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryItem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Description(BaseModel):
    """ The descriptive characteristics of the inventory item.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str language: The language that is used in the item description
    :param str description: Textual description of the item
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  language:  'str'  = None,  description:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.language = language 
        self.description = description 
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryItem":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryItem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Association(BaseModel):
    """ Association with other items or products.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept associationType: The type of association between the device and the other item
    :param Reference relatedItem: The related item or product
    :param Ratio quantity: The quantity of the product in this product
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "associationType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "relatedItem": {"class_name": "Reference", "is_contained": False},
        
        
        "quantity": {"class_name": "Ratio", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  associationType:  'CodeableConcept'  = None,  relatedItem:  'Reference'  = None,  quantity:  'Ratio'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.associationType = associationType 
        self.relatedItem = relatedItem 
        self.quantity = quantity 
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryItem":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryItem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Characteristic(BaseModel):
    """ The descriptive or identifying characteristics of the item.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept characteristicType: The characteristic that is being defined
    :param str valueString: The value of the attribute
    :param int valueInteger: The value of the attribute
    :param float valueDecimal: The value of the attribute
    :param bool valueBoolean: The value of the attribute
    :param str valueUrl: The value of the attribute
    :param str valueDateTime: The value of the attribute
    :param Quantity valueQuantity: The value of the attribute
    :param Range valueRange: The value of the attribute
    :param Ratio valueRatio: The value of the attribute
    :param Annotation valueAnnotation: The value of the attribute
    :param Address valueAddress: The value of the attribute
    :param Duration valueDuration: The value of the attribute
    :param CodeableConcept valueCodeableConcept: The value of the attribute
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "characteristicType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        "valueRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        "valueAnnotation": {"class_name": "Annotation", "is_contained": False},
        
        
        "valueAddress": {"class_name": "Address", "is_contained": False},
        
        
        "valueDuration": {"class_name": "Duration", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  characteristicType:  'CodeableConcept'  = None,  valueString:  'str'  = None,  valueInteger:  'int'  = None,  valueDecimal:  'float'  = None,  valueBoolean:  'bool'  = None,  valueUrl:  'str'  = None,  valueDateTime:  'str'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  valueRatio:  'Ratio'  = None,  valueAnnotation:  'Annotation'  = None,  valueAddress:  'Address'  = None,  valueDuration:  'Duration'  = None,  valueCodeableConcept:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.characteristicType = characteristicType 
        self.valueString = valueString 
        self.valueInteger = valueInteger 
        self.valueDecimal = valueDecimal 
        self.valueBoolean = valueBoolean 
        self.valueUrl = valueUrl 
        self.valueDateTime = valueDateTime 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.valueRatio = valueRatio 
        self.valueAnnotation = valueAnnotation 
        self.valueAddress = valueAddress 
        self.valueDuration = valueDuration 
        self.valueCodeableConcept = valueCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryItem":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryItem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Instance(BaseModel):
    """ Instances or occurrences of the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: The identifier for the physical instance, typically a serial number
    :param str lotNumber: The lot or batch number of the item
    :param str expiry: The expiry date or date and time for the product
    :param Reference subject: The subject that the item is associated with
    :param Reference location: The location that the item is associated with
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  lotNumber:  'str'  = None,  expiry:  'str'  = None,  subject:  'Reference'  = None,  location:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.lotNumber = lotNumber 
        self.expiry = expiry 
        self.subject = subject 
        self.location = location 
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryItem":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryItem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class InventoryItem(DomainResource):
    """ functional description of an inventory item used in inventory and supply-related workflows.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the inventory item
    :param str status: active | inactive | entered-in-error | unknown
    :param CodeableConcept category: Category or class of the item
    :param CodeableConcept code: Code designating the specific type of item
    :param Name name: The item name(s) - the brand name, or common name, functional name, generic name or others
    :param ResponsibleOrganization responsibleOrganization: Organization(s) responsible for the product
    :param Description description: Descriptive characteristics of the item
    :param CodeableConcept inventoryStatus: The usage status like recalled, in use, discarded
    :param CodeableConcept baseUnit: The base unit of measure - the unit in which the product is used or counted
    :param Quantity netContent: Net content or amount present in the item
    :param Association association: Association with other items or products
    :param Characteristic characteristic: Characteristic of the item
    :param Instance instance: Instances or occurrences of the product
    :param Reference productReference: Link to a product resource used in clinical workflows
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "name": {"class_name": "Name", "is_contained": True},
        
        
        "responsibleOrganization": {"class_name": "ResponsibleOrganization", "is_contained": True},
        
        
        "description": {"class_name": "Description", "is_contained": True},
        
        
        "inventoryStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "baseUnit": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "netContent": {"class_name": "Quantity", "is_contained": False},
        
        
        "association": {"class_name": "Association", "is_contained": True},
        
        
        "characteristic": {"class_name": "Characteristic", "is_contained": True},
        
        
        "instance": {"class_name": "Instance", "is_contained": True},
        
        
        "productReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  category:  list['CodeableConcept']  = None,  code:  list['CodeableConcept']  = None,  name:  list['Name']  = None,  responsibleOrganization:  list['ResponsibleOrganization']  = None,  description:  'Description'  = None,  inventoryStatus:  list['CodeableConcept']  = None,  baseUnit:  'CodeableConcept'  = None,  netContent:  'Quantity'  = None,  association:  list['Association']  = None,  characteristic:  list['Characteristic']  = None,  instance:  'Instance'  = None,  productReference:  'Reference'  = None, ):
        self.resourceType = resourceType or "InventoryItem"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status 
        self.category = category or []
        self.code = code or []
        self.name = name or []
        self.responsibleOrganization = responsibleOrganization or []
        self.description = description 
        self.inventoryStatus = inventoryStatus or []
        self.baseUnit = baseUnit 
        self.netContent = netContent 
        self.association = association or []
        self.characteristic = characteristic or []
        self.instance = instance 
        self.productReference = productReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryItem":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryItem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()