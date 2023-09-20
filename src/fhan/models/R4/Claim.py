"""
Generated class for Claim. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Attachment import *
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
    :param CodeableConcept reason: Explanation for the information
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    category: "CodeableConcept" = None
    code: "CodeableConcept" = None
    
    timingDate: str = None
    
    valueBoolean: bool = None
    reason: "CodeableConcept" = None
    

    
    
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
    :param int sequence: Insurance instance identifier
    :param bool focal: Coverage to be used for adjudication
    :param Identifier identifier: Pre-assigned Claim number
    :param Reference coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    :param str preAuthRef: Prior authorization reference number
    :param Reference claimResponse: Adjudication results
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    sequence: int = None
    
    focal: bool = None
    identifier: "Identifier" = None
    coverage: "Reference" = None
    
    businessArrangement: str = None
    
    preAuthRef: str = None
    claimResponse: "Reference" = None
    

    
    
@dataclass
class Accident(Element):
    """ Details of an accident which resulted in injuries which required the products and services listed in the claim.:param str id: Unique id for inter-element referencing
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
class SubDetail(Element):
    """ A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple items.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
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
    
  
    
    
@dataclass
class Detail(Element):
    """ A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple items.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
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
    :param SubDetail subDetail: Product or service provided
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
    subDetail: list[SubDetail] = None
    
  
    
    
@dataclass
class Item(Element):
    """ A claim line. Either a simple  product or service or a 'group' of details which can each be a simple items or groups of sub-details.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param int careTeamSequence: Applicable careTeam members
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
    :param Detail detail: Product or service provided
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
    detail: list[Detail] = None
    
@dataclass
class Claim(ModelBase):
    """ A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for claim
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept type: Category or discipline
    :param CodeableConcept subType: More granular claim type
    :param str use: claim | preauthorization | predetermination
    :param Reference patient: The recipient of the products and services
    :param Period billablePeriod: Relevant time frame for the claim
    :param str created: Resource creation date
    :param Reference enterer: Author of the claim
    :param Reference insurer: Target
    :param Reference provider: Party responsible for the claim
    :param CodeableConcept priority: Desired processing ugency
    :param CodeableConcept fundsReserve: For whom to reserve funds
    :param Related related: Prior or corollary claims
    :param Reference prescription: Prescription authorizing services and products
    :param Reference originalPrescription: Original prescription if superseded by fulfiller
    :param Payee payee: Recipient of benefits payable
    :param Reference referral: Treatment referral
    :param Reference facility: Servicing facility
    :param CareTeam careTeam: Members of the care team
    :param SupportingInfo supportingInfo: Supporting information
    :param Diagnosis diagnosis: Pertinent diagnosis information
    :param Procedure procedure: Clinical procedures performed
    :param Insurance insurance: Patient insurance information
    :param Accident accident: Details of the event
    :param Item item: Product or service provided
    :param Money total: Total claim cost
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
    
    fundsReserve: "CodeableConcept" = None
    
    related: list["Related"] = None
    
    prescription: "Reference" = None
    
    originalPrescription: "Reference" = None
    
    payee: "Payee" = None
    
    referral: "Reference" = None
    
    facility: "Reference" = None
    
    careTeam: list["CareTeam"] = None
    
    supportingInfo: list["SupportingInfo"] = None
    
    diagnosis: list["Diagnosis"] = None
    
    procedure: list["Procedure"] = None
    
    insurance: list["Insurance"] = None
    
    accident: "Accident" = None
    
    item: list["Item"] = None
    
    total: "Money" = None
    