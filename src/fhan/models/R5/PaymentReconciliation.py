"""
Generated class for PaymentReconciliation. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Money import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class PaymentReconciliation:
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
    :param BackboneElement allocation: Settlement particulars
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business identifier of the payment detail
    :param Identifier predecessor: Business identifier of the prior payment detail
    :param Reference target: Subject of the payment
    :param str targetItemstring: Sub-element of the subject
    :param Identifier targetItemstring: Sub-element of the subject
    :param int targetItemstring: Sub-element of the subject
    :param Reference encounter: Applied-to encounter
    :param Reference account: Applied-to account
    :param CodeableConcept type: Category of payment
    :param Reference submitter: Submitter of the request
    :param Reference response: Response committing to a payment
    :param str date: Date of commitment to pay
    :param Reference responsible: Contact for the response
    :param Reference payee: Recipient of the payment
    :param Money amount: Amount allocated to this payable
    :param CodeableConcept formCode: Printed form identifier
    :param BackboneElement processNote: Note concerning processing
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: display | print | printoper
    :param str text: Note explanatory text
    
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
    
    type: "CodeableConcept" = None
    
    status: str = None
    
    kind: "CodeableConcept" = None
    
    period: "Period" = None
    
    created: str = None
    
    enterer: "Reference" = None
    
    issuerType: "CodeableConcept" = None
    
    paymentIssuer: "Reference" = None
    
    request: "Reference" = None
    
    requestor: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    date: str = None
    
    location: "Reference" = None
    
    method: "CodeableConcept" = None
    
    cardBrand: str = None
    
    accountNumber: str = None
    
    expirationDate: str = None
    
    processor: str = None
    
    referenceNumber: str = None
    
    authorization: str = None
    
    tenderedAmount: "Money" = None
    
    returnedAmount: "Money" = None
    
    amount: "Money" = None
    
    paymentIdentifier: "Identifier" = None
    
    allocation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    predecessor: "Identifier" = None
    
    target: "Reference" = None
    
    targetItemstring: str = None
    
    targetItemstring: "Identifier" = None
    
    targetItemstring: int = None
    
    encounter: "Reference" = None
    
    account: "Reference" = None
    
    type: "CodeableConcept" = None
    
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
    