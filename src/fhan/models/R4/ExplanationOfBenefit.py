"""
Generated class for ExplanationOfBenefit. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Coding import *
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
class ExplanationOfBenefit(ModelBase):
    """ This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for the resource
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept type: Category or discipline
    :param CodeableConcept subType: More granular claim type
    :param str use: claim | preauthorization | predetermination
    :param Reference patient: The recipient of the products and services
    :param Period billablePeriod: Relevant time frame for the claim
    :param str created: Response creation date
    :param Reference enterer: Author of the claim
    :param Reference insurer: Party responsible for reimbursement
    :param Reference provider: Party responsible for the claim
    :param CodeableConcept priority: Desired processing urgency
    :param CodeableConcept fundsReserveRequested: For whom to reserve funds
    :param CodeableConcept fundsReserve: Funds reserved status
    :param BackboneElement related: Prior or corollary claims
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference claim: Reference to the related claim
    :param CodeableConcept relationship: How the reference claim is related
    :param Identifier reference: File or case reference
    :param Reference prescription: Prescription authorizing services or products
    :param Reference originalPrescription: Original prescription if superceded by fulfiller
    :param BackboneElement payee: Recipient of benefits payable
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of recipient
    :param Reference party: Recipient reference
    :param Reference referral: Treatment Referral
    :param Reference facility: Servicing Facility
    :param Reference claim: Claim reference
    :param Reference claimResponse: Claim response reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param str preAuthRef: Preauthorization reference
    :param Period preAuthRefPeriod: Preauthorization in-effect period
    :param BackboneElement careTeam: Care Team members
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Order of care team
    :param Reference provider: Practitioner or organization
    :param bool responsible: Indicator of the lead practitioner
    :param CodeableConcept role: Function within the team
    :param CodeableConcept qualification: Practitioner credential or specialization
    :param BackboneElement supportingInfo: Supporting information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Information instance identifier
    :param CodeableConcept category: Classification of the supplied information
    :param CodeableConcept code: Type of information
    :param str timingdate: When it occurred
    :param Period timingdate: When it occurred
    :param bool valueboolean: Data to be provided
    :param str valueboolean: Data to be provided
    :param Quantity valueboolean: Data to be provided
    :param Attachment valueboolean: Data to be provided
    :param Reference valueboolean: Data to be provided
    :param Coding reason: Explanation for the information
    :param BackboneElement diagnosis: Pertinent diagnosis information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Diagnosis instance identifier
    :param CodeableConcept diagnosisCodeableConcept: Nature of illness or problem
    :param Reference diagnosisCodeableConcept: Nature of illness or problem
    :param CodeableConcept type: Timing or nature of the diagnosis
    :param CodeableConcept onAdmission: Present on admission
    :param CodeableConcept packageCode: Package billing code
    :param BackboneElement procedure: Clinical procedures performed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Procedure instance identifier
    :param CodeableConcept type: Category of Procedure
    :param str date: When the procedure was performed
    :param CodeableConcept procedureCodeableConcept: Specific clinical procedure
    :param Reference procedureCodeableConcept: Specific clinical procedure
    :param Reference udi: Unique device identifier
    :param int precedence: Precedence (primary, secondary, etc.)
    :param BackboneElement insurance: Patient insurance information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool focal: Coverage to be used for adjudication
    :param Reference coverage: Insurance information
    :param str preAuthRef: Prior authorization reference number
    :param BackboneElement accident: Details of the event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When the incident occurred
    :param CodeableConcept type: The nature of the accident
    :param Address locationAddress: Where the event occurred
    :param Reference locationAddress: Where the event occurred
    :param BackboneElement item: Product or service provided
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param int careTeamSequence: Applicable care team members
    :param int diagnosisSequence: Applicable diagnoses
    :param int procedureSequence: Applicable procedures
    :param int informationSequence: Applicable exception and supporting information
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Product or service billing modifiers
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
    :param Reference udi: Unique device identifier
    :param CodeableConcept bodySite: Anatomical location
    :param CodeableConcept subSite: Anatomical sub-location
    :param Reference encounter: Encounters related to this billed item
    :param int noteNumber: Applicable note numbers
    :param BackboneElement adjudication: Adjudication details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Type of adjudication information
    :param CodeableConcept reason: Explanation of adjudication outcome
    :param Money amount: Monetary amount
    :param float value: Non-monitary value
    :param BackboneElement detail: Additional items
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Product or service provided
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param int noteNumber: Applicable note numbers
    :param BackboneElement adjudication: Adjudication details
    :param BackboneElement subDetail: Additional items
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Product or service provided
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param int noteNumber: Applicable note numbers
    :param BackboneElement adjudication: Adjudication details
    :param BackboneElement addItem: Insurer added line items
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Item sequence number
    :param int detailSequence: Detail sequence number
    :param int subDetailSequence: Subdetail sequence number
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
    :param BackboneElement detail: Insurer added line items
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
    :param CodeableConcept adjustmentReason: Explanation for the variance
    :param str date: Expected date of payment
    :param Money amount: Payable amount after adjustment
    :param Identifier identifier: Business identifier for the payment
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
    :param Period benefitPeriod: When the benefits are applicable
    :param BackboneElement benefitBalance: Balance by Benefit Category
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Benefit classification
    :param bool excluded: Excluded from the plan
    :param str name: Short name for the benefit
    :param str description: Description of the benefit or services covered
    :param CodeableConcept network: In or out of network
    :param CodeableConcept unit: Individual or family
    :param CodeableConcept term: Annual or lifetime
    :param BackboneElement financial: Benefit Summary
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Benefit classification
    :param int allowedunsignedInt: Benefits allowed
    :param str allowedunsignedInt: Benefits allowed
    :param Money allowedunsignedInt: Benefits allowed
    :param int usedunsignedInt: Benefits used
    :param Money usedunsignedInt: Benefits used
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
    
    billablePeriod: "Period" = None
    
    created: str = None
    
    enterer: "Reference" = None
    
    insurer: "Reference" = None
    
    provider: "Reference" = None
    
    priority: "CodeableConcept" = None
    
    fundsReserveRequested: "CodeableConcept" = None
    
    fundsReserve: "CodeableConcept" = None
    
    related: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    claim: "Reference" = None
    
    relationship: "CodeableConcept" = None
    
    reference: "Identifier" = None
    
    prescription: "Reference" = None
    
    originalPrescription: "Reference" = None
    
    payee: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    party: "Reference" = None
    
    referral: "Reference" = None
    
    facility: "Reference" = None
    
    claim: "Reference" = None
    
    claimResponse: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    preAuthRef: str = None
    
    preAuthRefPeriod: "Period" = None
    
    careTeam: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    provider: "Reference" = None
    
    responsible: bool = None
    
    role: "CodeableConcept" = None
    
    qualification: "CodeableConcept" = None
    
    supportingInfo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    timingdate: str = None
    
    timingdate: "Period" = None
    
    valueboolean: bool = None
    
    valueboolean: str = None
    
    valueboolean: "Quantity" = None
    
    valueboolean: "Attachment" = None
    
    valueboolean: "Reference" = None
    
    reason: "Coding" = None
    
    diagnosis: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    diagnosisCodeableConcept: "CodeableConcept" = None
    
    diagnosisCodeableConcept: "Reference" = None
    
    type: "CodeableConcept" = None
    
    onAdmission: "CodeableConcept" = None
    
    packageCode: "CodeableConcept" = None
    
    procedure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    type: "CodeableConcept" = None
    
    date: str = None
    
    procedureCodeableConcept: "CodeableConcept" = None
    
    procedureCodeableConcept: "Reference" = None
    
    udi: "Reference" = None
    
    precedence: int = None
    
    insurance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    focal: bool = None
    
    coverage: "Reference" = None
    
    preAuthRef: str = None
    
    accident: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    date: str = None
    
    type: "CodeableConcept" = None
    
    locationAddress: "Address" = None
    
    locationAddress: "Reference" = None
    
    item: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    careTeamSequence: int = None
    
    diagnosisSequence: int = None
    
    procedureSequence: int = None
    
    informationSequence: int = None
    
    revenue: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
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
    
    udi: "Reference" = None
    
    bodySite: "CodeableConcept" = None
    
    subSite: "CodeableConcept" = None
    
    encounter: "Reference" = None
    
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
    
    sequence: int = None
    
    revenue: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: "CodeableConcept" = None
    
    programCode: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    factor: float = None
    
    net: "Money" = None
    
    udi: "Reference" = None
    
    noteNumber: int = None
    
    adjudication: "BackboneElement" = None
    
    subDetail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    revenue: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: "CodeableConcept" = None
    
    programCode: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    factor: float = None
    
    net: "Money" = None
    
    udi: "Reference" = None
    
    noteNumber: int = None
    
    adjudication: "BackboneElement" = None
    
    addItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemSequence: int = None
    
    detailSequence: int = None
    
    subDetailSequence: int = None
    
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
    
    benefitPeriod: "Period" = None
    
    benefitBalance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    excluded: bool = None
    
    name: str = None
    
    description: str = None
    
    network: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    term: "CodeableConcept" = None
    
    financial: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    allowedunsignedInt: int = None
    
    allowedunsignedInt: str = None
    
    allowedunsignedInt: "Money" = None
    
    usedunsignedInt: int = None
    
    usedunsignedInt: "Money" = None
    