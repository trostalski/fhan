"""
Generated class for PaymentReconciliation. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Detail(Element):
    """ Distribution of the payment amount for a previously acknowledged payable.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business identifier of the payment detail
    :param Identifier predecessor: Business identifier of the prior payment detail
    :param CodeableConcept type: Category of payment
    :param Reference request: Request giving rise to the payment
    :param Reference submitter: Submitter of the request
    :param Reference response: Response committing to a payment
    :param str date: Date of commitment to pay
    :param Reference responsible: Contact for the response
    :param Reference payee: Recipient of the payment
    :param Money amount: Amount allocated to this payable
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    identifier:  "Identifier" = Identifier()
    
    predecessor:  "Identifier" = Identifier()
    
    type:  "CodeableConcept" = CodeableConcept()
    
    request:  "Reference" = Reference()
    
    submitter:  "Reference" = Reference()
    
    response:  "Reference" = Reference()
    
    date: str = None
    
    responsible:  "Reference" = Reference()
    
    payee:  "Reference" = Reference()
    
    amount:  "Money" = Money()
    

    
    
@dataclass
class ProcessNote(Element):
    """ A note that describes or explains the processing in a human readable form.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: display | print | printoper
    :param str text: Note explanatory text
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type: str = None
    
    text: str = None
    

@dataclass
class PaymentReconciliation(ModelBase):
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
    :param str status: active | cancelled | draft | entered-in-error
    :param Period period: Period covered
    :param str created: Creation date
    :param Reference paymentIssuer: Party generating payment
    :param Reference request: Reference to requesting resource
    :param Reference requestor: Responsible practitioner
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition message
    :param str paymentDate: When payment issued
    :param Money paymentAmount: Total amount of Payment
    :param Identifier paymentIdentifier: Business identifier for the payment
    :param Detail detail: Settlement particulars
    :param CodeableConcept formCode: Printed form identifier
    :param ProcessNote processNote: Note concerning processing
    """

    resourceType: str = "PaymentReconciliation"
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
    
    detail: list["Detail"] = None
    
    formCode: "CodeableConcept" = None
    
    processNote: list["ProcessNote"] = None
    