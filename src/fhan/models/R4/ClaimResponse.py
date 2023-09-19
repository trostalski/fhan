"""
Generated class for ClaimResponse. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Address import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class ClaimResponse:
    """
    This resource provides the adjudication details from the processing of a Claim resource.
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
    