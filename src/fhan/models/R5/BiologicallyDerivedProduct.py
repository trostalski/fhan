"""
Generated class for BiologicallyDerivedProduct. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Collection(BaseModel):
    """ How this product was collected.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Individual performing collection
    :param Reference source: The patient who underwent the medical procedure to collect the product or the organization that facilitated the collection
    :param str collectedDateTime: Time of product collection
    :param Period collectedPeriod: Time of product collection
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "collector": {"class_name": "Reference", "is_contained": False},
        
        
        "source": {"class_name": "Reference", "is_contained": False},
        
        
        
        "collectedPeriod": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  collector:  'Reference'  = None,  source:  'Reference'  = None,  collectedDateTime:  'str'  = None,  collectedPeriod:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.collector = collector 
        self.source = source 
        self.collectedDateTime = collectedDateTime 
        self.collectedPeriod = collectedPeriod 
        

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProduct":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Property(BaseModel):
    """ A property that is specific to this BiologicallyDerviedProduct instance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code that specifies the property
    :param bool valueBoolean: Property values
    :param int valueInteger: Property values
    :param CodeableConcept valueCodeableConcept: Property values
    :param Period valuePeriod: Property values
    :param Quantity valueQuantity: Property values
    :param Range valueRange: Property values
    :param Ratio valueRatio: Property values
    :param str valueString: Property values
    :param Attachment valueAttachment: Property values
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valuePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        "valueRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueBoolean:  'bool'  = None,  valueInteger:  'int'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valuePeriod:  'Period'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  valueRatio:  'Ratio'  = None,  valueString:  'str'  = None,  valueAttachment:  'Attachment'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueBoolean = valueBoolean 
        self.valueInteger = valueInteger 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valuePeriod = valuePeriod 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.valueRatio = valueRatio 
        self.valueString = valueString 
        self.valueAttachment = valueAttachment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProduct":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class BiologicallyDerivedProduct(DomainResource):
    """ A biological material originating from a biological entity intended to be transplanted or infused into another (possibly the same) biological entity.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Coding productCategory: organ | tissue | fluid | cells | biologicalAgent
    :param CodeableConcept productCode: A code that identifies the kind of this biologically derived product
    :param Reference parent: The parent biologically-derived product
    :param Reference request: Request to obtain and/or infuse this product
    :param Identifier identifier: Instance identifier
    :param Identifier biologicalSourceEvent: An identifier that supports traceability to the event during which material in this product from one or more biological entities was obtained or pooled
    :param Reference processingFacility: Processing facilities responsible for the labeling and distribution of this biologically derived product
    :param str division: A unique identifier for an aliquot of a product
    :param Coding productStatus: available | unavailable
    :param str expirationDate: Date, and where relevant time, of expiration
    :param Collection collection: How this product was collected
    :param Range storageTempRequirements: Product storage temperature requirements
    :param Property property: A property that is specific to this BiologicallyDerviedProduct instance
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "productCategory": {"class_name": "Coding", "is_contained": False},
        
        
        "productCode": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "parent": {"class_name": "Reference", "is_contained": False},
        
        
        "request": {"class_name": "Reference", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "biologicalSourceEvent": {"class_name": "Identifier", "is_contained": False},
        
        
        "processingFacility": {"class_name": "Reference", "is_contained": False},
        
        
        
        "productStatus": {"class_name": "Coding", "is_contained": False},
        
        
        
        "collection": {"class_name": "Collection", "is_contained": True},
        
        
        "storageTempRequirements": {"class_name": "Range", "is_contained": False},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  productCategory:  'Coding'  = None,  productCode:  'CodeableConcept'  = None,  parent:  list['Reference']  = None,  request:  list['Reference']  = None,  identifier:  list['Identifier']  = None,  biologicalSourceEvent:  'Identifier'  = None,  processingFacility:  list['Reference']  = None,  division:  'str'  = None,  productStatus:  'Coding'  = None,  expirationDate:  'str'  = None,  collection:  'Collection'  = None,  storageTempRequirements:  'Range'  = None,  property:  list['Property']  = None, ):
        self.resourceType = resourceType or "BiologicallyDerivedProduct"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.productCategory = productCategory 
        self.productCode = productCode 
        self.parent = parent or []
        self.request = request or []
        self.identifier = identifier or []
        self.biologicalSourceEvent = biologicalSourceEvent 
        self.processingFacility = processingFacility or []
        self.division = division 
        self.productStatus = productStatus 
        self.expirationDate = expirationDate 
        self.collection = collection 
        self.storageTempRequirements = storageTempRequirements 
        self.property = property or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProduct":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()