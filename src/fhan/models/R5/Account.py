"""
Generated class for Account. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
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


    
    

class Coverage(BaseModel):
    """ The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference coverage: The party(s), such as insurances, that may contribute to the payment of this account
    :param int priority: The priority of the coverage in the context of this account
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "coverage": {"class_name": "Reference", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  coverage:  'Reference'  = None,  priority:  'int'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.coverage = coverage 
        self.priority = priority 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Guarantor(BaseModel):
    """ The parties responsible for balancing the account if other payment options fall short.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference party: Responsible entity
    :param bool onHold: Credit or other hold applied
    :param Period period: Guarantee account during
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "party": {"class_name": "Reference", "is_contained": False},
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  party:  'Reference'  = None,  onHold:  'bool'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.party = party 
        self.onHold = onHold 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Diagnosis(BaseModel):
    """ When using an account for billing a specific Encounter the set of diagnoses that are relevant for billing are stored here on the account where they are able to be sequenced appropriately prior to processing to produce claim(s).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Ranking of the diagnosis (for each type)
    :param CodeableReference condition: The diagnosis relevant to the account
    :param str dateOfDiagnosis: Date of the diagnosis (when coded diagnosis)
    :param CodeableConcept type: Type that this diagnosis has relevant to the account (e.g. admission, billing, discharge …)
    :param bool onAdmission: Diagnosis present on Admission
    :param CodeableConcept packageCode: Package Code specific for billing
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "condition": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "packageCode": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  sequence:  'int'  = None,  condition:  'CodeableReference'  = None,  dateOfDiagnosis:  'str'  = None,  type:  list['CodeableConcept']  = None,  onAdmission:  'bool'  = None,  packageCode:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence 
        self.condition = condition 
        self.dateOfDiagnosis = dateOfDiagnosis 
        self.type = type or []
        self.onAdmission = onAdmission 
        self.packageCode = packageCode or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Procedure(BaseModel):
    """ When using an account for billing a specific Encounter the set of procedures that are relevant for billing are stored here on the account where they are able to be sequenced appropriately prior to processing to produce claim(s).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Ranking of the procedure (for each type)
    :param CodeableReference code: The procedure relevant to the account
    :param str dateOfService: Date of the procedure (when coded procedure)
    :param CodeableConcept type: How this procedure value should be used in charging the account
    :param CodeableConcept packageCode: Package Code specific for billing
    :param Reference device: Any devices that were associated with the procedure
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "packageCode": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "device": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  sequence:  'int'  = None,  code:  'CodeableReference'  = None,  dateOfService:  'str'  = None,  type:  list['CodeableConcept']  = None,  packageCode:  list['CodeableConcept']  = None,  device:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence 
        self.code = code 
        self.dateOfService = dateOfService 
        self.type = type or []
        self.packageCode = packageCode or []
        self.device = device or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class RelatedAccount(BaseModel):
    """ Other associated accounts related to this account.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept relationship: Relationship of the associated Account
    :param Reference account: Reference to an associated Account
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "relationship": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "account": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  relationship:  'CodeableConcept'  = None,  account:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.relationship = relationship 
        self.account = account 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Balance(BaseModel):
    """ The calculated account balances - these are calculated and processed by the finance system.The balances with a `term` that is not current are usually generated/updated by an invoicing or similar process.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept aggregate: Who is expected to pay this part of the balance
    :param CodeableConcept term: current | 30 | 60 | 90 | 120
    :param bool estimate: Estimated balance
    :param Money amount: Calculated amount
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "aggregate": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "term": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "amount": {"class_name": "Money", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  aggregate:  'CodeableConcept'  = None,  term:  'CodeableConcept'  = None,  estimate:  'bool'  = None,  amount:  'Money'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.aggregate = aggregate 
        self.term = term 
        self.estimate = estimate 
        self.amount = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Account(DomainResource):
    """ A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Account number
    :param str status: active | inactive | entered-in-error | on-hold | unknown
    :param CodeableConcept billingStatus: Tracks the lifecycle of the account through the billing process
    :param CodeableConcept type: E.g. patient, expense, depreciation
    :param str name: Human-readable label
    :param Reference subject: The entity that caused the expenses
    :param Period servicePeriod: Transaction window
    :param Coverage coverage: The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
    :param Reference owner: Entity managing the Account
    :param str description: Explanation of purpose/use
    :param Guarantor guarantor: The parties ultimately responsible for balancing the Account
    :param Diagnosis diagnosis: The list of diagnoses relevant to this account
    :param Procedure procedure: The list of procedures relevant to this account
    :param RelatedAccount relatedAccount: Other associated accounts related to this account
    :param CodeableConcept currency: The base or default currency
    :param Balance balance: Calculated account balance(s)
    :param str calculatedAt: Time the balance amount was calculated
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "billingStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "servicePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "coverage": {"class_name": "Coverage", "is_contained": True},
        
        
        "owner": {"class_name": "Reference", "is_contained": False},
        
        
        
        "guarantor": {"class_name": "Guarantor", "is_contained": True},
        
        
        "diagnosis": {"class_name": "Diagnosis", "is_contained": True},
        
        
        "procedure": {"class_name": "Procedure", "is_contained": True},
        
        
        "relatedAccount": {"class_name": "RelatedAccount", "is_contained": True},
        
        
        "currency": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "balance": {"class_name": "Balance", "is_contained": True},
        
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  billingStatus:  'CodeableConcept'  = None,  type:  'CodeableConcept'  = None,  name:  'str'  = None,  subject:  list['Reference']  = None,  servicePeriod:  'Period'  = None,  coverage:  list['Coverage']  = None,  owner:  'Reference'  = None,  description:  'str'  = None,  guarantor:  list['Guarantor']  = None,  diagnosis:  list['Diagnosis']  = None,  procedure:  list['Procedure']  = None,  relatedAccount:  list['RelatedAccount']  = None,  currency:  'CodeableConcept'  = None,  balance:  list['Balance']  = None,  calculatedAt:  'str'  = None, ):
        self.resourceType = resourceType or "Account"
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
        self.billingStatus = billingStatus 
        self.type = type 
        self.name = name 
        self.subject = subject or []
        self.servicePeriod = servicePeriod 
        self.coverage = coverage or []
        self.owner = owner 
        self.description = description 
        self.guarantor = guarantor or []
        self.diagnosis = diagnosis or []
        self.procedure = procedure or []
        self.relatedAccount = relatedAccount or []
        self.currency = currency 
        self.balance = balance or []
        self.calculatedAt = calculatedAt 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()