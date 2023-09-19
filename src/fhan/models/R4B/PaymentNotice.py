"""
Generated class for PaymentNotice. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Money import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


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
    