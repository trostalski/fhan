"""
Generated class for SupplyRequest. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Parameter(BaseModel):
    """ Specific parameters for the ordered item.  For example, the size of the indicated item.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Item detail
    :param CodeableConcept valueCodeableConcept: Value of detail
    :param Quantity valueQuantity: Value of detail
    :param Range valueRange: Value of detail
    :param bool valueBoolean: Value of detail
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  valueBoolean:  'bool'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.valueBoolean = valueBoolean 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SupplyRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SupplyRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SupplyRequest(DomainResource):
    """ A record of a non-patient specific request for a medication, substance, device, certain types of biologically derived product, and nutrition product used in the healthcare setting.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for SupplyRequest
    :param str status: draft | active | suspended +
    :param Reference basedOn: What other request is fulfilled by this supply request
    :param CodeableConcept category: The kind of supply (central, non-stock, etc.)
    :param str priority: routine | urgent | asap | stat
    :param Reference deliverFor: The patient for who the supply request is for
    :param CodeableReference item: Medication, Substance, or Device requested to be supplied
    :param Quantity quantity: The requested amount of the item indicated
    :param Parameter parameter: Ordered item details
    :param str occurrenceDateTime: When the request should be fulfilled
    :param Period occurrencePeriod: When the request should be fulfilled
    :param Timing occurrenceTiming: When the request should be fulfilled
    :param str authoredOn: When the request was made
    :param Reference requester: Individual making the request
    :param Reference supplier: Who is intended to fulfill the request
    :param CodeableReference reason: The reason why the supply item was requested
    :param Reference deliverFrom: The origin of the supply
    :param Reference deliverTo: The destination of the supply
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "deliverFor": {"class_name": "Reference", "is_contained": False},
        
        
        "item": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "parameter": {"class_name": "Parameter", "is_contained": True},
        
        
        
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        
        
        
        "requester": {"class_name": "Reference", "is_contained": False},
        
        
        "supplier": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "deliverFrom": {"class_name": "Reference", "is_contained": False},
        
        
        "deliverTo": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  basedOn:  list['Reference']  = None,  category:  'CodeableConcept'  = None,  priority:  'str'  = None,  deliverFor:  'Reference'  = None,  item:  'CodeableReference'  = None,  quantity:  'Quantity'  = None,  parameter:  list['Parameter']  = None,  occurrenceDateTime:  'str'  = None,  occurrencePeriod:  'Period'  = None,  occurrenceTiming:  'Timing'  = None,  authoredOn:  'str'  = None,  requester:  'Reference'  = None,  supplier:  list['Reference']  = None,  reason:  list['CodeableReference']  = None,  deliverFrom:  'Reference'  = None,  deliverTo:  'Reference'  = None, ):
        self.resourceType = resourceType or "SupplyRequest"
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
        self.basedOn = basedOn or []
        self.category = category 
        self.priority = priority 
        self.deliverFor = deliverFor 
        self.item = item 
        self.quantity = quantity 
        self.parameter = parameter or []
        self.occurrenceDateTime = occurrenceDateTime 
        self.occurrencePeriod = occurrencePeriod 
        self.occurrenceTiming = occurrenceTiming 
        self.authoredOn = authoredOn 
        self.requester = requester 
        self.supplier = supplier or []
        self.reason = reason or []
        self.deliverFrom = deliverFrom 
        self.deliverTo = deliverTo 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SupplyRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SupplyRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()