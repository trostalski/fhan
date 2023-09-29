"""
Generated class for InventoryReport. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class Item(BaseModel):
    """ The item or items in this listing.:param CodeableConcept itemStatus: The status of the items that are being reported
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: The inventory category or classification of the items being reported
    :param Quantity quantity: The quantity of the item or items being reported
    :param CodeableReference item: The code or reference to the item type
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        "itemStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "item": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self,  itemStatus:  'CodeableConcept'  = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  category:  'CodeableConcept'  = None,  quantity:  'Quantity'  = None,  item:  'CodeableReference'  = None, ):
        self.itemStatus = itemStatus 
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category 
        self.quantity = quantity 
        self.item = item 
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class InventoryListing(BaseModel):
    """ An inventory listing section (grouped by any of the attributes).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference location: Location of the inventory items
    :param CodeableConcept itemStatus: The status of the items that are being reported
    :param str countingDateTime: The date and time when the items were counted
    :param Item item: The item or items in this listing
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "itemStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "item": {"class_name": "Item", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  location:  'Reference'  = None,  itemStatus:  'CodeableConcept'  = None,  countingDateTime:  'str'  = None,  item:  list['Item']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.location = location 
        self.itemStatus = itemStatus 
        self.countingDateTime = countingDateTime 
        self.item = item or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class InventoryReport(DomainResource):
    """ A report of inventory or stock items.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the report
    :param str status: draft | requested | active | entered-in-error
    :param str countType: snapshot | difference
    :param CodeableConcept operationType: addition | subtraction
    :param CodeableConcept operationTypeReason: The reason for this count - regular count, ad-hoc count, new arrivals, etc
    :param str reportedDateTime: When the report has been submitted
    :param Reference reporter: Who submits the report
    :param Period reportingPeriod: The period the report refers to
    :param InventoryListing inventoryListing: An inventory listing section (grouped by any of the attributes)
    :param Annotation note: A note associated with the InventoryReport
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "operationType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "operationTypeReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "reporter": {"class_name": "Reference", "is_contained": False},
        
        
        "reportingPeriod": {"class_name": "Period", "is_contained": False},
        
        
        "inventoryListing": {"class_name": "InventoryListing", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  countType:  'str'  = None,  operationType:  'CodeableConcept'  = None,  operationTypeReason:  'CodeableConcept'  = None,  reportedDateTime:  'str'  = None,  reporter:  'Reference'  = None,  reportingPeriod:  'Period'  = None,  inventoryListing:  list['InventoryListing']  = None,  note:  list['Annotation']  = None, ):
        self.resourceType = resourceType or "InventoryReport"
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
        self.countType = countType 
        self.operationType = operationType 
        self.operationTypeReason = operationTypeReason 
        self.reportedDateTime = reportedDateTime 
        self.reporter = reporter 
        self.reportingPeriod = reportingPeriod 
        self.inventoryListing = inventoryListing or []
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "InventoryReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()