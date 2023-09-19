"""
Generated class for PaymentNotice. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Money import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class PaymentNotice:
    """
    This resource provides the status of the payment for goods and services rendered, and the request and response resource references.
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
    
    request: "Reference" = None
    
    response: "Reference" = None
    
    created: str = None
    
    provider: "Reference" = None
    
    payment: "Reference" = None
    
    paymentDate: str = None
    
    payee: "Reference" = None
    
    recipient: "Reference" = None
    
    amount: "Money" = None
    
    paymentStatus: "CodeableConcept" = None
    