"""
Generated class for ClaimResponse. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Money import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Address import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class ClaimResponse(ModelBase):
    """ This resource provides the adjudication details from the processing of a Claim resource.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for a claim response
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept type: More granular claim type
    :param CodeableConcept subType: More granular claim type
    :param str use: claim | preauthorization | predetermination
    :param Reference patient: The recipient of the products and services
    :param str created: Response creation date
    :param Reference insurer: Party responsible for reimbursement
    :param Reference requestor: Party responsible for the claim
    :param Reference request: Id of resource triggering adjudication
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param str preAuthRef: Preauthorization reference
    :param Period preAuthPeriod: Preauthorization reference effective period
    :param CodeableConcept payeeType: Party to be paid any benefits payable
    :param BackboneElement item: Adjudication for claim line items
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Claim item instance identifier
    :param int noteNumber: Applicable note numbers
    :param BackboneElement adjudication: Adjudication details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Type of adjudication information
    :param CodeableConcept reason: Explanation of adjudication outcome
    :param Money amount: Monetary amount
    :param float value: Non-monetary value
    :param BackboneElement detail: Adjudication for claim details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int detailSequence: Claim detail instance identifier
    :param int noteNumber: Applicable note numbers
    :param BackboneElement adjudication: Adjudication details
    :param BackboneElement subDetail: Adjudication for claim sub-details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int subDetailSequence: Claim sub-detail instance identifier
    :param int noteNumber: Applicable note numbers
    :param BackboneElement adjudication: Adjudication details
    :param BackboneElement addItem: Insurer added line items
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Item sequence number
    :param int detailSequence: Detail sequence number
    :param int subdetailSequence: Subdetail sequence number
    :param Reference provider: Authorized providers
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param str serviceddate: Date or dates of service or product delivery
    :param Period serviceddate: Date or dates of service or product delivery
    :param CodeableConcept locationCodeableConcept: Place of service or where product was supplied
    :param Address locationCodeableConcept: Place of service or where product was supplied
    :param Reference locationCodeableConcept: Place of service or where product was supplied
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param CodeableConcept bodySite: Anatomical location
    :param CodeableConcept subSite: Anatomical sub-location
    :param int noteNumber: Applicable note numbers
    :param BackboneElement adjudication: Adjudication details
    :param BackboneElement detail: Insurer added line details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param int noteNumber: Applicable note numbers
    :param BackboneElement adjudication: Adjudication details
    :param BackboneElement subDetail: Insurer added line items
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param int noteNumber: Applicable note numbers
    :param BackboneElement adjudication: Adjudication details
    :param BackboneElement adjudication: Adjudication details
    :param BackboneElement total: Adjudication totals
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Type of adjudication information
    :param Money amount: Financial total for the category
    :param BackboneElement payment: Payment Details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Partial or complete payment
    :param Money adjustment: Payment adjustment for non-claim issues
    :param CodeableConcept adjustmentReason: Explanation for the adjustment
    :param str date: Expected date of payment
    :param Money amount: Payable amount after adjustment
    :param Identifier identifier: Business identifier for the payment
    :param CodeableConcept fundsReserve: Funds reserved status
    :param CodeableConcept formCode: Printed form identifier
    :param Attachment form: Printed reference or actual form
    :param BackboneElement processNote: Note concerning adjudication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Note instance identifier
    :param str type: display | print | printoper
    :param str text: Note explanatory text
    :param CodeableConcept language: Language of the text
    :param Reference communicationRequest: Request for additional information
    :param BackboneElement insurance: Patient insurance information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Insurance instance identifier
    :param bool focal: Coverage to be used for adjudication
    :param Reference coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    :param Reference claimResponse: Adjudication results
    :param BackboneElement error: Processing errors
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Item sequence number
    :param int detailSequence: Detail sequence number
    :param int subDetailSequence: Subdetail sequence number
    :param CodeableConcept code: Error code detailing processing issues
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
    
    type: "CodeableConcept" = None
    
    subType: "CodeableConcept" = None
    
    use: str = None
    
    patient: "Reference" = None
    
    created: str = None
    
    insurer: "Reference" = None
    
    requestor: "Reference" = None
    
    request: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    preAuthRef: str = None
    
    preAuthPeriod: "Period" = None
    
    payeeType: "CodeableConcept" = None
    
    item: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemSequence: int = None
    
    noteNumber: int = None
    
    adjudication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    reason: "CodeableConcept" = None
    
    amount: "Money" = None
    
    value: float = None
    
    detail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    detailSequence: int = None
    
    noteNumber: int = None
    
    adjudication: "BackboneElement" = None
    
    subDetail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    subDetailSequence: int = None
    
    noteNumber: int = None
    
    adjudication: "BackboneElement" = None
    
    addItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemSequence: int = None
    
    detailSequence: int = None
    
    subdetailSequence: int = None
    
    provider: "Reference" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: "CodeableConcept" = None
    
    programCode: "CodeableConcept" = None
    
    serviceddate: str = None
    
    serviceddate: "Period" = None
    
    locationCodeableConcept: "CodeableConcept" = None
    
    locationCodeableConcept: "Address" = None
    
    locationCodeableConcept: "Reference" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    factor: float = None
    
    net: "Money" = None
    
    bodySite: "CodeableConcept" = None
    
    subSite: "CodeableConcept" = None
    
    noteNumber: int = None
    
    adjudication: "BackboneElement" = None
    
    detail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    factor: float = None
    
    net: "Money" = None
    
    noteNumber: int = None
    
    adjudication: "BackboneElement" = None
    
    subDetail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    factor: float = None
    
    net: "Money" = None
    
    noteNumber: int = None
    
    adjudication: "BackboneElement" = None
    
    adjudication: "BackboneElement" = None
    
    total: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    amount: "Money" = None
    
    payment: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    adjustment: "Money" = None
    
    adjustmentReason: "CodeableConcept" = None
    
    date: str = None
    
    amount: "Money" = None
    
    identifier: "Identifier" = None
    
    fundsReserve: "CodeableConcept" = None
    
    formCode: "CodeableConcept" = None
    
    form: "Attachment" = None
    
    processNote: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    number: int = None
    
    type: str = None
    
    text: str = None
    
    language: "CodeableConcept" = None
    
    communicationRequest: "Reference" = None
    
    insurance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    focal: bool = None
    
    coverage: "Reference" = None
    
    businessArrangement: str = None
    
    claimResponse: "Reference" = None
    
    error: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemSequence: int = None
    
    detailSequence: int = None
    
    subDetailSequence: int = None
    
    code: "CodeableConcept" = None
    