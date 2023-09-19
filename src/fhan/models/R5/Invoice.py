"""
Generated class for Invoice. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Money import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.MonetaryComponent import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Invoice:
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
    :param str date: DEPRICATED
    :param str creation: When posted
    :param str perioddate: Billing date or period
    :param Period perioddate: Billing date or period
    :param BackboneElement participant: Participant in creation of this Invoice
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Type of involvement in creation of this Invoice
    :param Reference actor: Individual who was involved
    :param Reference issuer: Issuing Organization of Invoice
    :param Reference account: Account that is being balanced
    :param BackboneElement lineItem: Line items of this Invoice
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Sequence number of line item
    :param str serviceddate: Service data or period
    :param Period serviceddate: Service data or period
    :param Reference chargeItemReference: Reference to ChargeItem containing details of this line item or an inline billing code
    :param CodeableConcept chargeItemReference: Reference to ChargeItem containing details of this line item or an inline billing code
    :param MonetaryComponent priceComponent: Components of total line item price
    :param MonetaryComponent totalPriceComponent: Components of Invoice total
    :param Money totalNet: Net total of this Invoice
    :param Money totalGross: Gross total of this Invoice
    :param str paymentTerms: Payment details
    :param Annotation note: Comments made about the invoice
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    cancelledReason: str = None
    
    type: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    recipient: "Reference" = None
    
    date: str = None
    
    creation: str = None
    
    perioddate: str = None
    
    perioddate: "Period" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    issuer: "Reference" = None
    
    account: "Reference" = None
    
    lineItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    serviceddate: str = None
    
    serviceddate: "Period" = None
    
    chargeItemReference: "Reference" = None
    
    chargeItemReference: "CodeableConcept" = None
    
    priceComponent: "MonetaryComponent" = None
    
    totalPriceComponent: "MonetaryComponent" = None
    
    totalNet: "Money" = None
    
    totalGross: "Money" = None
    
    paymentTerms: str = None
    
    note: "Annotation" = None
    