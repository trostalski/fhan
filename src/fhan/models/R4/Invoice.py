"""
Generated class for Invoice. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Money import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Participant(ModelBase):
    """ Indicates who or what performed or participated in the charged service.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' role: Type of involvement in creation of this Invoice
    :param 'Reference' actor: Individual who was involved
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  role: 'CodeableConcept' = None,  actor: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.role: 'CodeableConcept' = role 
        self.actor: 'Reference' = actor 
        

    
        
    
    

class PriceComponent(ModelBase):
    """ The price for a ChargeItem may be calculated as a base price with surcharges/deductions that apply in certain conditions. A ChargeItemDefinition resource that defines the prices, factors and conditions that apply to a billing code is currently under development. The priceComponent element can be used to offer transparency to the recipient of the Invoice as to how the prices have been calculated.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: base | surcharge | deduction | discount | tax | informational
    :param 'CodeableConcept' code: Code identifying the specific component
    :param float factor: Factor used for calculating this component
    :param 'Money' amount: Monetary amount associated with this component
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  code: 'CodeableConcept' = None,  factor: float = None,  amount: 'Money' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.code: 'CodeableConcept' = code 
        self.factor: float = factor 
        self.amount: 'Money' = amount 
        

  
    
    

class LineItem(ModelBase):
    """ Each line item represents one charge for goods and services rendered. Details such as date, code and amount are found in the referenced ChargeItem resource.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Sequence number of line item
    :param 'Reference' chargeItemReference: Reference to ChargeItem containing details of this line item or an inline billing code
    :param list['PriceComponent'] priceComponent: Components of total line item price
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  chargeItemReference: 'Reference' = None,  priceComponent: list['PriceComponent'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.chargeItemReference: 'Reference' = chargeItemReference 
        self.priceComponent: list['PriceComponent'] = priceComponent or []
        

class Invoice(DomainResource):
    """ Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for item
    :param str status: draft | issued | balanced | cancelled | entered-in-error
    :param str cancelledReason: Reason for cancellation of this Invoice
    :param 'CodeableConcept' type: Type of Invoice
    :param 'Reference' subject: Recipient(s) of goods and services
    :param 'Reference' recipient: Recipient of this invoice
    :param str date: Invoice date / posting date
    :param list['Participant'] participant: Participant in creation of this Invoice
    :param 'Reference' issuer: Issuing Organization of Invoice
    :param 'Reference' account: Account that is being balanced
    :param list['LineItem'] lineItem: Line items of this Invoice
    :param 'Money' totalNet: Net total of this Invoice
    :param 'Money' totalGross: Gross total of this Invoice
    :param str paymentTerms: Payment details
    :param list['Annotation'] note: Comments made about the invoice
    """
    def __init__(self, resourceType: str = "Invoice",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  cancelledReason: str = None,  type: 'CodeableConcept' = None,  subject: 'Reference' = None,  recipient: 'Reference' = None,  date: str = None,  participant: list['Participant'] = None,  issuer: 'Reference' = None,  account: 'Reference' = None,  lineItem: list['LineItem'] = None,  totalNet: 'Money' = None,  totalGross: 'Money' = None,  paymentTerms: str = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "Invoice"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.cancelledReason: str = cancelledReason 
        self.type: 'CodeableConcept' = type 
        self.subject: 'Reference' = subject 
        self.recipient: 'Reference' = recipient 
        self.date: str = date 
        self.participant: list['Participant'] = participant or []
        self.issuer: 'Reference' = issuer 
        self.account: 'Reference' = account 
        self.lineItem: list['LineItem'] = lineItem or []
        self.totalNet: 'Money' = totalNet 
        self.totalGross: 'Money' = totalGross 
        self.paymentTerms: str = paymentTerms 
        self.note: list['Annotation'] = note or []
        