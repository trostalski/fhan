"""
Generated class for Invoice. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Money import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Participant(Element):
    """ Indicates who or what performed or participated in the charged service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Type of involvement in creation of this Invoice
    :param Reference actor: Individual who was involved
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    role: "CodeableConcept" = None
    actor: "Reference" = None
    

    
        
    
    
@dataclass
class PriceComponent(Element):
    """ The price for a ChargeItem may be calculated as a base price with surcharges/deductions that apply in certain conditions. A ChargeItemDefinition resource that defines the prices, factors and conditions that apply to a billing code is currently under development. The priceComponent element can be used to offer transparency to the recipient of the Invoice as to how the prices have been calculated.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: base | surcharge | deduction | discount | tax | informational
    :param CodeableConcept code: Code identifying the specific component
    :param float factor: Factor used for calculating this component
    :param Money amount: Monetary amount associated with this component
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    type: str = None
    code: "CodeableConcept" = None
    
    factor: float = None
    amount: "Money" = None
    

  
    
    
@dataclass
class LineItem(Element):
    """ Each line item represents one charge for goods and services rendered. Details such as date, code and amount are found in the referenced ChargeItem resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Sequence number of line item
    :param Reference chargeItemReference: Reference to ChargeItem containing details of this line item or an inline billing code
    :param PriceComponent priceComponent: Components of total line item price
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    chargeItemReference: "Reference" = None
    priceComponent: list[PriceComponent] = None
    

@dataclass
class Invoice(ModelBase):
    """ Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for item
    :param str status: draft | issued | balanced | cancelled | entered-in-error
    :param str cancelledReason: Reason for cancellation of this Invoice
    :param CodeableConcept type: Type of Invoice
    :param Reference subject: Recipient(s) of goods and services
    :param Reference recipient: Recipient of this invoice
    :param str date: Invoice date / posting date
    :param Participant participant: Participant in creation of this Invoice
    :param Reference issuer: Issuing Organization of Invoice
    :param Reference account: Account that is being balanced
    :param LineItem lineItem: Line items of this Invoice
    :param Money totalNet: Net total of this Invoice
    :param Money totalGross: Gross total of this Invoice
    :param str paymentTerms: Payment details
    :param Annotation note: Comments made about the invoice
    """

    resourceType: str = "Invoice"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    status: str = None
    
    cancelledReason: str = None
    
    type: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    recipient: "Reference" = None
    
    date: str = None
    
    participant: list["Participant"] = None
    
    issuer: "Reference" = None
    
    account: "Reference" = None
    
    lineItem: list["LineItem"] = None
    
    totalNet: "Money" = None
    
    totalGross: "Money" = None
    
    paymentTerms: str = None
    
    note: list["Annotation"] = None
    