"""
Generated class for PackagedProductDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.MarketingStatus import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.ProductShelfLife import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class LegalStatusOfSupply(BaseModel):
    """ The legal status of supply of the packaged item as classified by the regulator.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The actual status of supply. In what situation this package type may be supplied for use
    :param CodeableConcept jurisdiction: The place where the legal status of supply applies
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  jurisdiction:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.jurisdiction = jurisdiction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PackagedProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PackagedProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Property(BaseModel):
    """ General characteristics of this item.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of characteristic
    :param CodeableConcept valueCodeableConcept: A value for the characteristic
    :param Quantity valueQuantity: A value for the characteristic
    :param str valueDate: A value for the characteristic
    :param bool valueBoolean: A value for the characteristic
    :param Attachment valueAttachment: A value for the characteristic
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueDate:  'str'  = None,  valueBoolean:  'bool'  = None,  valueAttachment:  'Attachment'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueQuantity = valueQuantity 
        self.valueDate = valueDate 
        self.valueBoolean = valueBoolean 
        self.valueAttachment = valueAttachment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PackagedProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PackagedProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ContainedItem(BaseModel):
    """ The item(s) within the packaging.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: The actual item(s) of medication, as manufactured, or a device, or other medically related item (food, biologicals, raw materials, medical fluids, gases etc.), as contained in the package
    :param Quantity amount: The number of this type of item within this packaging or for continuous items such as liquids it is the quantity (for example 25ml). See also PackagedProductDefinition.containedItemQuantity (especially the long definition)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "item": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "amount": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  item:  'CodeableReference'  = None,  amount:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.item = item 
        self.amount = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PackagedProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PackagedProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Packaging(BaseModel):
    """ A packaging item, as a container for medically related items, possibly with other packaging items within, or a packaging component, such as bottle cap (which is not a device or a medication manufactured item).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: An identifier that is specific to this particular part of the packaging. Including possibly a Data Carrier Identifier
    :param CodeableConcept type: The physical type of the container of the items
    :param bool componentPart: Is this a part of the packaging (e.g. a cap or bottle stopper), rather than the packaging itself (e.g. a bottle or vial)
    :param int quantity: The quantity of this level of packaging in the package that contains it (with the outermost level being 1)
    :param CodeableConcept material: Material type of the package item
    :param CodeableConcept alternateMaterial: A possible alternate material for this part of the packaging, that is allowed to be used instead of the usual material
    :param ProductShelfLife shelfLifeStorage: Shelf Life and storage information
    :param Reference manufacturer: Manufacturer of this packaging item (multiple means these are all potential manufacturers)
    :param Property property: General characteristics of this item
    :param ContainedItem containedItem: The item(s) within the packaging
    :param Packaging packaging: Allows containers (and parts of containers) within containers, still as a part of single packaged product
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "material": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "alternateMaterial": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "shelfLifeStorage": {"class_name": "ProductShelfLife", "is_contained": False},
        
        
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "containedItem": {"class_name": "ContainedItem", "is_contained": True},
        
        
        "packaging": {"class_name": "Packaging", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  type:  'CodeableConcept'  = None,  componentPart:  'bool'  = None,  quantity:  'int'  = None,  material:  list['CodeableConcept']  = None,  alternateMaterial:  list['CodeableConcept']  = None,  shelfLifeStorage:  list['ProductShelfLife']  = None,  manufacturer:  list['Reference']  = None,  property:  list['Property']  = None,  containedItem:  list['ContainedItem']  = None,  packaging:  list['Packaging']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type 
        self.componentPart = componentPart 
        self.quantity = quantity 
        self.material = material or []
        self.alternateMaterial = alternateMaterial or []
        self.shelfLifeStorage = shelfLifeStorage or []
        self.manufacturer = manufacturer or []
        self.property = property or []
        self.containedItem = containedItem or []
        self.packaging = packaging or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PackagedProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PackagedProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PackagedProductDefinition(DomainResource):
    """ A medically related item or items, in a container or package.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: A unique identifier for this package as whole - not for the content of the package
    :param str name: A name for this package. Typically as listed in a drug formulary, catalogue, inventory etc
    :param CodeableConcept type: A high level category e.g. medicinal product, raw material, shipping container etc
    :param Reference packageFor: The product that this is a pack for
    :param CodeableConcept status: The status within the lifecycle of this item. High level - not intended to duplicate details elsewhere e.g. legal status, or authorization/marketing status
    :param str statusDate: The date at which the given status became applicable
    :param Quantity containedItemQuantity: A total of the complete count of contained items of a particular type/form, independent of sub-packaging or organization. This can be considered as the pack size. See also packaging.containedItem.amount (especially the long definition)
    :param str description: Textual description. Note that this is not the name of the package or product
    :param LegalStatusOfSupply legalStatusOfSupply: The legal status of supply of the packaged item as classified by the regulator
    :param MarketingStatus marketingStatus: Allows specifying that an item is on the market for sale, or that it is not available, and the dates and locations associated
    :param bool copackagedIndicator: Identifies if the drug product is supplied with another item such as a diluent or adjuvant
    :param Reference manufacturer: Manufacturer of this package type (multiple means these are all possible manufacturers)
    :param Reference attachedDocument: Additional information or supporting documentation about the packaged product
    :param Packaging packaging: A packaging item, as a container for medically related items, possibly with other packaging items within, or a packaging component, such as bottle cap
    :param Characteristic characteristic: Allows the key features to be recorded, such as "hospital pack", "nurse prescribable"
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "packageFor": {"class_name": "Reference", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "containedItemQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        "legalStatusOfSupply": {"class_name": "LegalStatusOfSupply", "is_contained": True},
        
        
        "marketingStatus": {"class_name": "MarketingStatus", "is_contained": False},
        
        
        
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        
        
        "attachedDocument": {"class_name": "Reference", "is_contained": False},
        
        
        "packaging": {"class_name": "Packaging", "is_contained": True},
        
        
        "characteristic": {"class_name": "Characteristic", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  name:  'str'  = None,  type:  'CodeableConcept'  = None,  packageFor:  list['Reference']  = None,  status:  'CodeableConcept'  = None,  statusDate:  'str'  = None,  containedItemQuantity:  list['Quantity']  = None,  description:  'str'  = None,  legalStatusOfSupply:  list['LegalStatusOfSupply']  = None,  marketingStatus:  list['MarketingStatus']  = None,  copackagedIndicator:  'bool'  = None,  manufacturer:  list['Reference']  = None,  attachedDocument:  list['Reference']  = None,  packaging:  'Packaging'  = None,  characteristic:  list['Characteristic']  = None, ):
        self.resourceType = resourceType or "PackagedProductDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.name = name 
        self.type = type 
        self.packageFor = packageFor or []
        self.status = status 
        self.statusDate = statusDate 
        self.containedItemQuantity = containedItemQuantity or []
        self.description = description 
        self.legalStatusOfSupply = legalStatusOfSupply or []
        self.marketingStatus = marketingStatus or []
        self.copackagedIndicator = copackagedIndicator 
        self.manufacturer = manufacturer or []
        self.attachedDocument = attachedDocument or []
        self.packaging = packaging 
        self.characteristic = characteristic or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PackagedProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PackagedProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()