"""
Generated class for Coverage. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Money import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class PaymentBy(BaseModel):
    """ Link to the paying party and optionally what specifically they will be responsible to pay.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference party: Parties performing self-payment
    :param str responsibility: Party's responsibility
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "party": {"class_name": "Reference", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  party:  'Reference'  = None,  responsibility:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.party = party 
        self.responsibility = responsibility 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Coverage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class _class(BaseModel):
    """ A suite of underwriter specific classifiers.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of class such as 'group' or 'plan'
    :param Identifier value: Value associated with the type
    :param str name: Human readable description of the type and value
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "value": {"class_name": "Identifier", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  value:  'Identifier'  = None,  name:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.value = value 
        self.name = name 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Coverage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Exception(BaseModel):
    """ A suite of codes indicating exceptions or reductions to patient costs and their effective periods.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Exception category
    :param Period period: The effective period of the exception
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Coverage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class CostToBeneficiary(BaseModel):
    """ A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Cost category
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept network: In or out of network
    :param CodeableConcept unit: Individual or family
    :param CodeableConcept term: Annual or lifetime
    :param Quantity valueQuantity: The amount or percentage due from the beneficiary
    :param Money valueMoney: The amount or percentage due from the beneficiary
    :param Exception exception: Exceptions for patient payments
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "network": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "unit": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "term": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueMoney": {"class_name": "Money", "is_contained": False},
        
        
        "exception": {"class_name": "Exception", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  category:  'CodeableConcept'  = None,  network:  'CodeableConcept'  = None,  unit:  'CodeableConcept'  = None,  term:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueMoney:  'Money'  = None,  exception:  list['Exception']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.category = category 
        self.network = network 
        self.unit = unit 
        self.term = term 
        self.valueQuantity = valueQuantity 
        self.valueMoney = valueMoney 
        self.exception = exception or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Coverage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Coverage(DomainResource):
    """ Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier(s) for this coverage
    :param str status: active | cancelled | draft | entered-in-error
    :param str kind: insurance | self-pay | other
    :param PaymentBy paymentBy: Self-pay parties and responsibility
    :param CodeableConcept type: Coverage category such as medical or accident
    :param Reference policyHolder: Owner of the policy
    :param Reference subscriber: Subscriber to the policy
    :param Identifier subscriberId: ID assigned to the subscriber
    :param Reference beneficiary: Plan beneficiary
    :param str dependent: Dependent number
    :param CodeableConcept relationship: Beneficiary relationship to the subscriber
    :param Period period: Coverage start and end dates
    :param Reference insurer: Issuer of the policy
    :param _class _class: Additional coverage classifications
    :param int order: Relative order of the coverage
    :param str network: Insurer network
    :param CostToBeneficiary costToBeneficiary: Patient payments for services/products
    :param bool subrogation: Reimbursement to insurer
    :param Reference contract: Contract details
    :param Reference insurancePlan: Insurance plan details
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "paymentBy": {"class_name": "PaymentBy", "is_contained": True},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "policyHolder": {"class_name": "Reference", "is_contained": False},
        
        
        "subscriber": {"class_name": "Reference", "is_contained": False},
        
        
        "subscriberId": {"class_name": "Identifier", "is_contained": False},
        
        
        "beneficiary": {"class_name": "Reference", "is_contained": False},
        
        
        
        "relationship": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "insurer": {"class_name": "Reference", "is_contained": False},
        
        
        "_class": {"class_name": "_class", "is_contained": True},
        
        
        
        
        "costToBeneficiary": {"class_name": "CostToBeneficiary", "is_contained": True},
        
        
        
        "contract": {"class_name": "Reference", "is_contained": False},
        
        
        "insurancePlan": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  kind:  'str'  = None,  paymentBy:  list['PaymentBy']  = None,  type:  'CodeableConcept'  = None,  policyHolder:  'Reference'  = None,  subscriber:  'Reference'  = None,  subscriberId:  list['Identifier']  = None,  beneficiary:  'Reference'  = None,  dependent:  'str'  = None,  relationship:  'CodeableConcept'  = None,  period:  'Period'  = None,  insurer:  'Reference'  = None,  _class:  list['_class']  = None,  order:  'int'  = None,  network:  'str'  = None,  costToBeneficiary:  list['CostToBeneficiary']  = None,  subrogation:  'bool'  = None,  contract:  list['Reference']  = None,  insurancePlan:  'Reference'  = None, ):
        self.resourceType = resourceType or "Coverage"
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
        self.kind = kind 
        self.paymentBy = paymentBy or []
        self.type = type 
        self.policyHolder = policyHolder 
        self.subscriber = subscriber 
        self.subscriberId = subscriberId or []
        self.beneficiary = beneficiary 
        self.dependent = dependent 
        self.relationship = relationship 
        self.period = period 
        self.insurer = insurer 
        self._class = _class or []
        self.order = order 
        self.network = network 
        self.costToBeneficiary = costToBeneficiary or []
        self.subrogation = subrogation 
        self.contract = contract or []
        self.insurancePlan = insurancePlan 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Coverage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()