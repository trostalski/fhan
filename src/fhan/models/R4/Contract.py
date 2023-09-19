"""
Generated class for Contract. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Contract:
    """
    Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
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
    
    url: str = None
    
    version: str = None
    
    status: str = None
    
    legalState: "CodeableConcept" = None
    
    instantiatesCanonical: "Reference" = None
    
    instantiatesUri: str = None
    
    contentDerivative: "CodeableConcept" = None
    
    issued: str = None
    
    applies: "Period" = None
    
    expirationType: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    authority: "Reference" = None
    
    domain: "Reference" = None
    
    site: "Reference" = None
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    alias: str = None
    
    author: "Reference" = None
    
    scope: "CodeableConcept" = None
    
    topicCodeableConcept: "CodeableConcept" = None
    
    topicCodeableConcept: "Reference" = None
    
    type: "CodeableConcept" = None
    
    subType: "CodeableConcept" = None
    
    contentDefinition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    subType: "CodeableConcept" = None
    
    publisher: "Reference" = None
    
    publicationDate: str = None
    
    publicationStatus: str = None
    
    copyright: str = None
    
    term: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    issued: str = None
    
    applies: "Period" = None
    
    topicCodeableConcept: "CodeableConcept" = None
    
    topicCodeableConcept: "Reference" = None
    
    type: "CodeableConcept" = None
    
    subType: "CodeableConcept" = None
    
    text: str = None
    
    securityLabel: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    number: int = None
    
    classification: "Coding" = None
    
    category: "Coding" = None
    
    control: "Coding" = None
    
    offer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    party: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    reference: "Reference" = None
    
    role: "CodeableConcept" = None
    
    topic: "Reference" = None
    
    type: "CodeableConcept" = None
    
    decision: "CodeableConcept" = None
    
    decisionMode: "CodeableConcept" = None
    
    answer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    valueboolean: bool = None
    
    valueboolean: float = None
    
    valueboolean: int = None
    
    valueboolean: str = None
    
    valueboolean: str = None
    
    valueboolean: str = None
    
    valueboolean: str = None
    
    valueboolean: str = None
    
    valueboolean: "Attachment" = None
    
    valueboolean: "Coding" = None
    
    valueboolean: "Quantity" = None
    
    valueboolean: "Reference" = None
    
    text: str = None
    
    linkId: str = None
    
    securityLabelNumber: int = None
    
    asset: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    scope: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    typeReference: "Reference" = None
    
    subtype: "CodeableConcept" = None
    
    relationship: "Coding" = None
    
    context: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    reference: "Reference" = None
    
    code: "CodeableConcept" = None
    
    text: str = None
    
    condition: str = None
    
    periodType: "CodeableConcept" = None
    
    period: "Period" = None
    
    usePeriod: "Period" = None
    
    text: str = None
    
    linkId: str = None
    
    answer: "BackboneElement" = None
    
    securityLabelNumber: int = None
    
    valuedItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    entityCodeableConcept: "CodeableConcept" = None
    
    entityCodeableConcept: "Reference" = None
    
    identifier: "Identifier" = None
    
    effectiveTime: str = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    factor: float = None
    
    points: float = None
    
    net: "Money" = None
    
    payment: str = None
    
    paymentDate: str = None
    
    responsible: "Reference" = None
    
    recipient: "Reference" = None
    
    linkId: str = None
    
    securityLabelNumber: int = None
    
    action: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    doNotPerform: bool = None
    
    type: "CodeableConcept" = None
    
    subject: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    reference: "Reference" = None
    
    role: "CodeableConcept" = None
    
    intent: "CodeableConcept" = None
    
    linkId: str = None
    
    status: "CodeableConcept" = None
    
    context: "Reference" = None
    
    contextLinkId: str = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: "Timing" = None
    
    requester: "Reference" = None
    
    requesterLinkId: str = None
    
    performerType: "CodeableConcept" = None
    
    performerRole: "CodeableConcept" = None
    
    performer: "Reference" = None
    
    performerLinkId: str = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    reason: str = None
    
    reasonLinkId: str = None
    
    note: "Annotation" = None
    
    securityLabelNumber: int = None
    
    group: "BackboneElement" = None
    
    supportingInfo: "Reference" = None
    
    relevantHistory: "Reference" = None
    
    signer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "Coding" = None
    
    party: "Reference" = None
    
    signature: "Signature" = None
    
    friendly: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    contentAttachment: "Attachment" = None
    
    contentAttachment: "Reference" = None
    
    legal: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    contentAttachment: "Attachment" = None
    
    contentAttachment: "Reference" = None
    
    rule: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    contentAttachment: "Attachment" = None
    
    contentAttachment: "Reference" = None
    
    legallyBindingAttachment: "Attachment" = None
    
    legallyBindingAttachment: "Reference" = None
    