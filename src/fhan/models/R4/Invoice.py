"""
Generated class for Invoice. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Invoice:
    """
    Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
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
    
    chargeItemReference: "Reference" = None
    
    chargeItemReference: "CodeableConcept" = None
    
    priceComponent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    code: "CodeableConcept" = None
    
    factor: float = None
    
    amount: "Money" = None
    
    totalPriceComponent: "BackboneElement" = None
    
    totalNet: "Money" = None
    
    totalGross: "Money" = None
    
    paymentTerms: str = None
    
    note: "Annotation" = None
    