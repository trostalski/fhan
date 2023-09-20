"""
Generated class for ExplanationOfBenefit. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Money import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Address import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Related(Element):
    """ Other claims which are related to this claim such as prior submissions or claims for related services or for the same event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference claim: Reference to the related claim
    :param CodeableConcept relationship: How the reference claim is related
    :param Identifier reference: File or case reference
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    claim: "Reference" = None
    relationship: "CodeableConcept" = None
    reference: "Identifier" = None
    

    
    
@dataclass
class Payee(Element):
    """ The party to be reimbursed for cost of the products and services according to the terms of the policy.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of recipient
    :param Reference party: Recipient reference
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    party: "Reference" = None
    

    
    
@dataclass
class CareTeam(Element):
    """ The members of the team who provided the products and services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Order of care team
    :param Reference provider: Practitioner or organization
    :param bool responsible: Indicator of the lead practitioner
    :param CodeableConcept role: Function within the team
    :param CodeableConcept qualification: Practitioner credential or specialization
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    provider: "Reference" = None
    
    responsible: bool = None
    role: "CodeableConcept" = None
    qualification: "CodeableConcept" = None
    

    
    
@dataclass
class SupportingInfo(Element):
    """ Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Information instance identifier
    :param CodeableConcept category: Classification of the supplied information
    :param CodeableConcept code: Type of information
    :param str timingDate: When it occurred
    :param bool valueBoolean: Data to be provided
    :param Coding reason: Explanation for the information
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    category: "CodeableConcept" = None
    code: "CodeableConcept" = None
    
    timingDate: str = None
    
    valueBoolean: bool = None
    reason: "Coding" = None
    

    
    
@dataclass
class Diagnosis(Element):
    """ Information about diagnoses relevant to the claim items.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Diagnosis instance identifier
    :param CodeableConcept diagnosisCodeableConcept: Nature of illness or problem
    :param CodeableConcept type: Timing or nature of the diagnosis
    :param CodeableConcept onAdmission: Present on admission
    :param CodeableConcept packageCode: Package billing code
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    diagnosisCodeableConcept: "CodeableConcept" = None
    type: list[CodeableConcept] = None
    onAdmission: "CodeableConcept" = None
    packageCode: "CodeableConcept" = None
    

    
    
@dataclass
class Procedure(Element):
    """ Procedures performed on the patient relevant to the billing items with the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Procedure instance identifier
    :param CodeableConcept type: Category of Procedure
    :param str date: When the procedure was performed
    :param CodeableConcept procedureCodeableConcept: Specific clinical procedure
    :param Reference udi: Unique device identifier
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    type: list[CodeableConcept] = None
    
    date: str = None
    procedureCodeableConcept: "CodeableConcept" = None
    udi: list[Reference] = None
    

    
    
@dataclass
class Insurance(Element):
    """ Financial instruments for reimbursement for the health care products and services specified on the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool focal: Coverage to be used for adjudication
    :param Reference coverage: Insurance information
    :param str preAuthRef: Prior authorization reference number
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    focal: bool = None
    coverage: "Reference" = None
    
    preAuthRef: str = None
    

    
    
@dataclass
class Accident(Element):
    """ Details of a accident which resulted in injuries which required the products and services listed in the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When the incident occurred
    :param CodeableConcept type: The nature of the accident
    :param Address locationAddress: Where the event occurred
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    date: str = None
    type: "CodeableConcept" = None
    locationAddress: "Address" = None
    

    
        
    
    
@dataclass
class Adjudication(Element):
    """ If this item is a group then the values here are a summary of the adjudication of the detail items. If this item is a simple product or service then this is the result of the adjudication of this item.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Type of adjudication information
    :param CodeableConcept reason: Explanation of adjudication outcome
    :param Money amount: Monetary amount
    :param float value: Non-monitary value
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    category: "CodeableConcept" = None
    reason: "CodeableConcept" = None
    amount: "Money" = None
    
    value: float = None
    

    
        
    
    
@dataclass
class SubDetail(Element):
    """ Third-tier of goods and services.:param str id: Unique id for inter-element referencing
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
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    revenue: "CodeableConcept" = None
    category: "CodeableConcept" = None
    productOrService: "CodeableConcept" = None
    modifier: list[CodeableConcept] = None
    programCode: list[CodeableConcept] = None
    quantity: "Quantity" = None
    unitPrice: "Money" = None
    
    factor: float = None
    net: "Money" = None
    udi: list[Reference] = None
    
    noteNumber: int = None
    
  
    
    
@dataclass
class Detail(Element):
    """ Second-tier of goods and services.:param str id: Unique id for inter-element referencing
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
    :param SubDetail subDetail: Additional items
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    revenue: "CodeableConcept" = None
    category: "CodeableConcept" = None
    productOrService: "CodeableConcept" = None
    modifier: list[CodeableConcept] = None
    programCode: list[CodeableConcept] = None
    quantity: "Quantity" = None
    unitPrice: "Money" = None
    
    factor: float = None
    net: "Money" = None
    udi: list[Reference] = None
    
    noteNumber: int = None
    subDetail: list[SubDetail] = None
    
  
    
    
@dataclass
class Item(Element):
    """ A claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-details.:param str id: Unique id for inter-element referencing
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
    :param str servicedDate: Date or dates of service or product delivery
    :param CodeableConcept locationCodeableConcept: Place of service or where product was supplied
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param CodeableConcept bodySite: Anatomical location
    :param CodeableConcept subSite: Anatomical sub-location
    :param Reference encounter: Encounters related to this billed item
    :param int noteNumber: Applicable note numbers
    :param Adjudication adjudication: Adjudication details
    :param Detail detail: Additional items
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    
    careTeamSequence: int = None
    
    diagnosisSequence: int = None
    
    procedureSequence: int = None
    
    informationSequence: int = None
    revenue: "CodeableConcept" = None
    category: "CodeableConcept" = None
    productOrService: "CodeableConcept" = None
    modifier: list[CodeableConcept] = None
    programCode: list[CodeableConcept] = None
    
    servicedDate: str = None
    locationCodeableConcept: "CodeableConcept" = None
    quantity: "Quantity" = None
    unitPrice: "Money" = None
    
    factor: float = None
    net: "Money" = None
    udi: list[Reference] = None
    bodySite: "CodeableConcept" = None
    subSite: list[CodeableConcept] = None
    encounter: list[Reference] = None
    
    noteNumber: int = None
    adjudication: list[Adjudication] = None
    detail: list[Detail] = None
    

    
        
    
        
    
    
@dataclass
class SubDetail(Element):
    """ The third-tier service adjudications for payor added services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param int noteNumber: Applicable note numbers
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    productOrService: "CodeableConcept" = None
    modifier: list[CodeableConcept] = None
    quantity: "Quantity" = None
    unitPrice: "Money" = None
    
    factor: float = None
    net: "Money" = None
    
    noteNumber: int = None
    
  
    
    
@dataclass
class Detail(Element):
    """ The second-tier service adjudications for payor added services.:param int detailSequence: Detail sequence number
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
    :param SubDetail subDetail: Insurer added line items
    """
    detailSequence: int = None
    
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    productOrService: "CodeableConcept" = None
    modifier: list[CodeableConcept] = None
    quantity: "Quantity" = None
    unitPrice: "Money" = None
    
    factor: float = None
    net: "Money" = None
    
    noteNumber: int = None
    subDetail: list[SubDetail] = None
    
  
    
    
@dataclass
class AddItem(Element):
    """ The first-tier service adjudications for payor added product or service lines.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Item sequence number
    :param int detailSequence: Detail sequence number
    :param int subDetailSequence: Subdetail sequence number
    :param Reference provider: Authorized providers
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param str servicedDate: Date or dates of service or product delivery
    :param CodeableConcept locationCodeableConcept: Place of service or where product was supplied
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param CodeableConcept bodySite: Anatomical location
    :param CodeableConcept subSite: Anatomical sub-location
    :param int noteNumber: Applicable note numbers
    :param Detail detail: Insurer added line items
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    itemSequence: int = None
    
    detailSequence: int = None
    
    subDetailSequence: int = None
    provider: list[Reference] = None
    productOrService: "CodeableConcept" = None
    modifier: list[CodeableConcept] = None
    programCode: list[CodeableConcept] = None
    
    servicedDate: str = None
    locationCodeableConcept: "CodeableConcept" = None
    quantity: "Quantity" = None
    unitPrice: "Money" = None
    
    factor: float = None
    net: "Money" = None
    bodySite: "CodeableConcept" = None
    subSite: list[CodeableConcept] = None
    
    noteNumber: int = None
    detail: list[Detail] = None
    

    
    
@dataclass
class Total(Element):
    """ Categorized monetary totals for the adjudication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Type of adjudication information
    :param Money amount: Financial total for the category
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    category: "CodeableConcept" = None
    amount: "Money" = None
    

    
    
@dataclass
class Payment(Element):
    """ Payment details for the adjudication of the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Partial or complete payment
    :param Money adjustment: Payment adjustment for non-claim issues
    :param CodeableConcept adjustmentReason: Explanation for the variance
    :param str date: Expected date of payment
    :param Money amount: Payable amount after adjustment
    :param Identifier identifier: Business identifier for the payment
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    adjustment: "Money" = None
    adjustmentReason: "CodeableConcept" = None
    
    date: str = None
    amount: "Money" = None
    identifier: "Identifier" = None
    

    
    
@dataclass
class ProcessNote(Element):
    """ A note that describes or explains adjudication results in a human readable form.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Note instance identifier
    :param str type: display | print | printoper
    :param str text: Note explanatory text
    :param CodeableConcept language: Language of the text
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    number: int = None
    
    type: str = None
    
    text: str = None
    language: "CodeableConcept" = None
    

    
        
    
    
@dataclass
class Financial(Element):
    """ Benefits Used to date.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Benefit classification
    :param int allowedUnsignedInt: Benefits allowed
    :param int usedUnsignedInt: Benefits used
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    
    allowedUnsignedInt: int = None
    
    usedUnsignedInt: int = None
    
  
    
    
@dataclass
class BenefitBalance(Element):
    """ Balance by Benefit Category.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Benefit classification
    :param bool excluded: Excluded from the plan
    :param str name: Short name for the benefit
    :param str description: Description of the benefit or services covered
    :param CodeableConcept network: In or out of network
    :param CodeableConcept unit: Individual or family
    :param CodeableConcept term: Annual or lifetime
    :param Financial financial: Benefit Summary
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    category: "CodeableConcept" = None
    
    excluded: bool = None
    
    name: str = None
    
    description: str = None
    network: "CodeableConcept" = None
    unit: "CodeableConcept" = None
    term: "CodeableConcept" = None
    financial: list[Financial] = None
    
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
    :param Related related: Prior or corollary claims
    :param Reference prescription: Prescription authorizing services or products
    :param Reference originalPrescription: Original prescription if superceded by fulfiller
    :param Payee payee: Recipient of benefits payable
    :param Reference referral: Treatment Referral
    :param Reference facility: Servicing Facility
    :param Reference claim: Claim reference
    :param Reference claimResponse: Claim response reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param str preAuthRef: Preauthorization reference
    :param Period preAuthRefPeriod: Preauthorization in-effect period
    :param CareTeam careTeam: Care Team members
    :param SupportingInfo supportingInfo: Supporting information
    :param Diagnosis diagnosis: Pertinent diagnosis information
    :param Procedure procedure: Clinical procedures performed
    :param int precedence: Precedence (primary, secondary, etc.)
    :param Insurance insurance: Patient insurance information
    :param Accident accident: Details of the event
    :param Item item: Product or service provided
    :param AddItem addItem: Insurer added line items
    :param Total total: Adjudication totals
    :param Payment payment: Payment Details
    :param CodeableConcept formCode: Printed form identifier
    :param Attachment form: Printed reference or actual form
    :param ProcessNote processNote: Note concerning adjudication
    :param Period benefitPeriod: When the benefits are applicable
    :param BenefitBalance benefitBalance: Balance by Benefit Category
    """
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
    
    related: list["Related"] = None
    
    prescription: "Reference" = None
    
    originalPrescription: "Reference" = None
    
    payee: "Payee" = None
    
    referral: "Reference" = None
    
    facility: "Reference" = None
    
    claim: "Reference" = None
    
    claimResponse: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    preAuthRef: str = None
    
    preAuthRefPeriod: list["Period"] = None
    
    careTeam: list["CareTeam"] = None
    
    supportingInfo: list["SupportingInfo"] = None
    
    diagnosis: list["Diagnosis"] = None
    
    procedure: list["Procedure"] = None
    
    precedence: int = None
    
    insurance: list["Insurance"] = None
    
    accident: "Accident" = None
    
    item: list["Item"] = None
    
    addItem: list["AddItem"] = None
    
    total: list["Total"] = None
    
    payment: "Payment" = None
    
    formCode: "CodeableConcept" = None
    
    form: "Attachment" = None
    
    processNote: list["ProcessNote"] = None
    
    benefitPeriod: "Period" = None
    
    benefitBalance: list["BenefitBalance"] = None
    