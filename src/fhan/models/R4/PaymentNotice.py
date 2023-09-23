"""
Generated class for PaymentNotice. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Money import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

@dataclass
class PaymentNotice(ModelBase):
    """ This resource provides the status of the payment for goods and services rendered, and the request and response resource references.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for the payment noctice
    :param str status: active | cancelled | draft | entered-in-error
    :param Reference request: Request reference
    :param Reference response: Response reference
    :param str created: Creation date
    :param Reference provider: Responsible practitioner
    :param Reference payment: Payment reference
    :param str paymentDate: Payment or clearing date
    :param Reference payee: Party being paid
    :param Reference recipient: Party being notified
    :param Money amount: Monetary amount of the payment
    :param CodeableConcept paymentStatus: Issued or cleared Status of the payment
    """

    resourceType: str = "PaymentNotice"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    request: "Reference" = Reference()
    
    response: "Reference" = Reference()
    
    created: str = None
    
    provider: "Reference" = Reference()
    
    payment: "Reference" = Reference()
    
    paymentDate: str = None
    
    payee: "Reference" = Reference()
    
    recipient: "Reference" = Reference()
    
    amount: "Money" = Money()
    
    paymentStatus: "CodeableConcept" = CodeableConcept()
    