"""
Generated class for Claim. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Money import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Address import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Claim:
    """
    A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
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
    
    total: "Money" = None
    