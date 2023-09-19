"""
Generated class for PaymentReconciliation. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class PaymentReconciliation:
    """
    This resource provides the details including amount of a payment and allocates the payment items being paid.
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
    
    period: "Period" = None
    
    created: str = None
    
    paymentIssuer: "Reference" = None
    
    request: "Reference" = None
    
    requestor: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    paymentDate: str = None
    
    paymentAmount: "Money" = None
    
    paymentIdentifier: "Identifier" = None
    
    detail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    predecessor: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    request: "Reference" = None
    
    submitter: "Reference" = None
    
    response: "Reference" = None
    
    date: str = None
    
    responsible: "Reference" = None
    
    payee: "Reference" = None
    
    amount: "Money" = None
    
    formCode: "CodeableConcept" = None
    
    processNote: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    text: str = None
    