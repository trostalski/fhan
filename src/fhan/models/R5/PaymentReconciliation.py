"""
Generated class for PaymentReconciliation. 
Time: 2023-09-29 13:03:58
"""
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


    
    

class Allocation(BaseModel):
    """ Distribution of the payment amount for a previously acknowledged payable.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business identifier of the payment detail
    :param Identifier predecessor: Business identifier of the prior payment detail
    :param Reference target: Subject of the payment
    :param str targetItemString: Sub-element of the subject
    :param Identifier targetItemIdentifier: Sub-element of the subject
    :param int targetItemPositiveInt: Sub-element of the subject
    :param Reference encounter: Applied-to encounter
    :param Reference account: Applied-to account
    :param CodeableConcept type: Category of payment
    :param Reference submitter: Submitter of the request
    :param Reference response: Response committing to a payment
    :param str date: Date of commitment to pay
    :param Reference responsible: Contact for the response
    :param Reference payee: Recipient of the payment
    :param Money amount: Amount allocated to this payable
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "predecessor": {"class_name": "Identifier", "is_contained": False},
        
        
        "target": {"class_name": "Reference", "is_contained": False},
        
        
        
        "targetItemIdentifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        "account": {"class_name": "Reference", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "submitter": {"class_name": "Reference", "is_contained": False},
        
        
        "response": {"class_name": "Reference", "is_contained": False},
        
        
        
        "responsible": {"class_name": "Reference", "is_contained": False},
        
        
        "payee": {"class_name": "Reference", "is_contained": False},
        
        
        "amount": {"class_name": "Money", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  'Identifier'  = None,  predecessor:  'Identifier'  = None,  target:  'Reference'  = None,  targetItemString:  'str'  = None,  targetItemIdentifier:  'Identifier'  = None,  targetItemPositiveInt:  'int'  = None,  encounter:  'Reference'  = None,  account:  'Reference'  = None,  type:  'CodeableConcept'  = None,  submitter:  'Reference'  = None,  response:  'Reference'  = None,  date:  'str'  = None,  responsible:  'Reference'  = None,  payee:  'Reference'  = None,  amount:  'Money'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier 
        self.predecessor = predecessor 
        self.target = target 
        self.targetItemString = targetItemString 
        self.targetItemIdentifier = targetItemIdentifier 
        self.targetItemPositiveInt = targetItemPositiveInt 
        self.encounter = encounter 
        self.account = account 
        self.type = type 
        self.submitter = submitter 
        self.response = response 
        self.date = date 
        self.responsible = responsible 
        self.payee = payee 
        self.amount = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PaymentReconciliation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PaymentReconciliation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ProcessNote(BaseModel):
    """ A note that describes or explains the processing in a human readable form.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: display | print | printoper
    :param str text: Note explanatory text
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'str'  = None,  text:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.text = text 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PaymentReconciliation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PaymentReconciliation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PaymentReconciliation(DomainResource):
    """ This resource provides the details including amount of a payment and allocates the payment items being paid.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for a payment reconciliation
    :param CodeableConcept type: Category of payment
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept kind: Workflow originating payment
    :param Period period: Period covered
    :param str created: Creation date
    :param Reference enterer: Who entered the payment
    :param CodeableConcept issuerType: Nature of the source
    :param Reference paymentIssuer: Party generating payment
    :param Reference request: Reference to requesting resource
    :param Reference requestor: Responsible practitioner
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition message
    :param str date: When payment issued
    :param Reference location: Where payment collected
    :param CodeableConcept method: Payment instrument
    :param str cardBrand: Type of card
    :param str accountNumber: Digits for verification
    :param str expirationDate: Expiration year-month
    :param str processor: Processor name
    :param str referenceNumber: Check number or payment reference
    :param str authorization: Authorization number
    :param Money tenderedAmount: Amount offered by the issuer
    :param Money returnedAmount: Amount returned by the receiver
    :param Money amount: Total amount of Payment
    :param Identifier paymentIdentifier: Business identifier for the payment
    :param Allocation allocation: Settlement particulars
    :param CodeableConcept formCode: Printed form identifier
    :param ProcessNote processNote: Note concerning processing
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
        
        
        
        "kind": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        
        "enterer": {"class_name": "Reference", "is_contained": False},
        
        
        "issuerType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "paymentIssuer": {"class_name": "Reference", "is_contained": False},
        
        
        "request": {"class_name": "Reference", "is_contained": False},
        
        
        "requestor": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        
        "tenderedAmount": {"class_name": "Money", "is_contained": False},
        
        
        "returnedAmount": {"class_name": "Money", "is_contained": False},
        
        
        "amount": {"class_name": "Money", "is_contained": False},
        
        
        "paymentIdentifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "allocation": {"class_name": "Allocation", "is_contained": True},
        
        
        "formCode": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "processNote": {"class_name": "ProcessNote", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  type:  'CodeableConcept'  = None,  status:  'str'  = None,  kind:  'CodeableConcept'  = None,  period:  'Period'  = None,  created:  'str'  = None,  enterer:  'Reference'  = None,  issuerType:  'CodeableConcept'  = None,  paymentIssuer:  'Reference'  = None,  request:  'Reference'  = None,  requestor:  'Reference'  = None,  outcome:  'str'  = None,  disposition:  'str'  = None,  date:  'str'  = None,  location:  'Reference'  = None,  method:  'CodeableConcept'  = None,  cardBrand:  'str'  = None,  accountNumber:  'str'  = None,  expirationDate:  'str'  = None,  processor:  'str'  = None,  referenceNumber:  'str'  = None,  authorization:  'str'  = None,  tenderedAmount:  'Money'  = None,  returnedAmount:  'Money'  = None,  amount:  'Money'  = None,  paymentIdentifier:  'Identifier'  = None,  allocation:  list['Allocation']  = None,  formCode:  'CodeableConcept'  = None,  processNote:  list['ProcessNote']  = None, ):
        self.resourceType = resourceType or "PaymentReconciliation"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type 
        self.status = status 
        self.kind = kind 
        self.period = period 
        self.created = created 
        self.enterer = enterer 
        self.issuerType = issuerType 
        self.paymentIssuer = paymentIssuer 
        self.request = request 
        self.requestor = requestor 
        self.outcome = outcome 
        self.disposition = disposition 
        self.date = date 
        self.location = location 
        self.method = method 
        self.cardBrand = cardBrand 
        self.accountNumber = accountNumber 
        self.expirationDate = expirationDate 
        self.processor = processor 
        self.referenceNumber = referenceNumber 
        self.authorization = authorization 
        self.tenderedAmount = tenderedAmount 
        self.returnedAmount = returnedAmount 
        self.amount = amount 
        self.paymentIdentifier = paymentIdentifier 
        self.allocation = allocation or []
        self.formCode = formCode 
        self.processNote = processNote or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PaymentReconciliation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PaymentReconciliation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()