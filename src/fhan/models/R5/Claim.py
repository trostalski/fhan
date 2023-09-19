"""
Generated class for Claim. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Money import *
from fhan.models.R5.Address import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Claim:
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
    :param Identifier traceNumber: Number for tracking
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
    :param CodeableConcept priority: Desired processing urgency
    :param CodeableConcept fundsReserve: For whom to reserve funds
    :param BackboneElement related: Prior or corollary claims
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference claim: Reference to the related claim
    :param CodeableConcept relationship: How the reference claim is related
    :param Identifier reference: File or case reference
    :param Reference prescription: Prescription authorizing services and products
    :param Reference originalPrescription: Original prescription if superseded by fulfiller
    :param BackboneElement payee: Recipient of benefits payable
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of recipient
    :param Reference party: Recipient reference
    :param Reference referral: Treatment referral
    :param Reference encounter: Encounters associated with the listed treatments
    :param Reference facility: Servicing facility
    :param CodeableConcept diagnosisRelatedGroup: Package billing code
    :param BackboneElement event: Event information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Specific event
    :param str whendateTime: Occurance date or period
    :param Period whendateTime: Occurance date or period
    :param BackboneElement careTeam: Members of the care team
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Order of care team
    :param Reference provider: Practitioner or organization
    :param bool responsible: Indicator of the lead practitioner
    :param CodeableConcept role: Function within the team
    :param CodeableConcept specialty: Practitioner or provider specialization
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
    :param Identifier valueboolean: Data to be provided
    :param CodeableConcept reason: Explanation for the information
    :param BackboneElement diagnosis: Pertinent diagnosis information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Diagnosis instance identifier
    :param CodeableConcept diagnosisCodeableConcept: Nature of illness or problem
    :param Reference diagnosisCodeableConcept: Nature of illness or problem
    :param CodeableConcept type: Timing or nature of the diagnosis
    :param CodeableConcept onAdmission: Present on admission
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
    :param BackboneElement insurance: Patient insurance information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Insurance instance identifier
    :param bool focal: Coverage to be used for adjudication
    :param Identifier identifier: Pre-assigned Claim number
    :param Reference coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    :param str preAuthRef: Prior authorization reference number
    :param Reference claimResponse: Adjudication results
    :param BackboneElement accident: Details of the event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When the incident occurred
    :param CodeableConcept type: The nature of the accident
    :param Address locationAddress: Where the event occurred
    :param Reference locationAddress: Where the event occurred
    :param Money patientPaid: Paid by the patient
    :param BackboneElement item: Product or service provided
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param Identifier traceNumber: Number for tracking
    :param int careTeamSequence: Applicable careTeam members
    :param int diagnosisSequence: Applicable diagnoses
    :param int procedureSequence: Applicable procedures
    :param int informationSequence: Applicable exception and supporting information
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept productOrServiceEnd: End of a range of codes
    :param Reference request: Request or Referral for Service
    :param CodeableConcept modifier: Product or service billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param str serviceddate: Date or dates of service or product delivery
    :param Period serviceddate: Date or dates of service or product delivery
    :param CodeableConcept locationCodeableConcept: Place of service or where product was supplied
    :param Address locationCodeableConcept: Place of service or where product was supplied
    :param Reference locationCodeableConcept: Place of service or where product was supplied
    :param Money patientPaid: Paid by the patient
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money tax: Total tax
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param BackboneElement bodySite: Anatomical location
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference site: Location
    :param CodeableConcept subSite: Sub-location
    :param Reference encounter: Encounters associated with the listed treatments
    :param BackboneElement detail: Product or service provided
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param Identifier traceNumber: Number for tracking
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept productOrServiceEnd: End of a range of codes
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param Money patientPaid: Paid by the patient
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money tax: Total tax
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param BackboneElement subDetail: Product or service provided
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param Identifier traceNumber: Number for tracking
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept productOrServiceEnd: End of a range of codes
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param Money patientPaid: Paid by the patient
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money tax: Total tax
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param Money total: Total claim cost
    
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
    
    traceNumber: "Identifier" = None
    
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
    
    encounter: "Reference" = None
    
    facility: "Reference" = None
    
    diagnosisRelatedGroup: "CodeableConcept" = None
    
    event: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    whendateTime: str = None
    
    whendateTime: "Period" = None
    
    careTeam: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    provider: "Reference" = None
    
    responsible: bool = None
    
    role: "CodeableConcept" = None
    
    specialty: "CodeableConcept" = None
    
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
    
    valueboolean: "Identifier" = None
    
    reason: "CodeableConcept" = None
    
    diagnosis: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    diagnosisCodeableConcept: "CodeableConcept" = None
    
    diagnosisCodeableConcept: "Reference" = None
    
    type: "CodeableConcept" = None
    
    onAdmission: "CodeableConcept" = None
    
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
    
    insurance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    focal: bool = None
    
    identifier: "Identifier" = None
    
    coverage: "Reference" = None
    
    businessArrangement: str = None
    
    preAuthRef: str = None
    
    claimResponse: "Reference" = None
    
    accident: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    date: str = None
    
    type: "CodeableConcept" = None
    
    locationAddress: "Address" = None
    
    locationAddress: "Reference" = None
    
    patientPaid: "Money" = None
    
    item: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    traceNumber: "Identifier" = None
    
    careTeamSequence: int = None
    
    diagnosisSequence: int = None
    
    procedureSequence: int = None
    
    informationSequence: int = None
    
    revenue: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    productOrServiceEnd: "CodeableConcept" = None
    
    request: "Reference" = None
    
    modifier: "CodeableConcept" = None
    
    programCode: "CodeableConcept" = None
    
    serviceddate: str = None
    
    serviceddate: "Period" = None
    
    locationCodeableConcept: "CodeableConcept" = None
    
    locationCodeableConcept: "Address" = None
    
    locationCodeableConcept: "Reference" = None
    
    patientPaid: "Money" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    factor: float = None
    
    tax: "Money" = None
    
    net: "Money" = None
    
    udi: "Reference" = None
    
    bodySite: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    site: "CodeableReference" = None
    
    subSite: "CodeableConcept" = None
    
    encounter: "Reference" = None
    
    detail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    traceNumber: "Identifier" = None
    
    revenue: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    productOrServiceEnd: "CodeableConcept" = None
    
    modifier: "CodeableConcept" = None
    
    programCode: "CodeableConcept" = None
    
    patientPaid: "Money" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    factor: float = None
    
    tax: "Money" = None
    
    net: "Money" = None
    
    udi: "Reference" = None
    
    subDetail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    traceNumber: "Identifier" = None
    
    revenue: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    productOrServiceEnd: "CodeableConcept" = None
    
    modifier: "CodeableConcept" = None
    
    programCode: "CodeableConcept" = None
    
    patientPaid: "Money" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    factor: float = None
    
    tax: "Money" = None
    
    net: "Money" = None
    
    udi: "Reference" = None
    
    total: "Money" = None
    