"""
Generated class for Contract. 
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
from fhan.models.R4.Signature import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase


@dataclass
class Contract(ModelBase):
    """ Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Contract number
    :param str url: Basal definition
    :param str version: Business edition
    :param str status: amended | appended | cancelled | disputed | entered-in-error | executable | executed | negotiable | offered | policy | rejected | renewed | revoked | resolved | terminated
    :param CodeableConcept legalState: Negotiation status
    :param Reference instantiatesCanonical: Source Contract Definition
    :param str instantiatesUri: External Contract Definition
    :param CodeableConcept contentDerivative: Content derived from the basal information
    :param str issued: When this Contract was issued
    :param Period applies: Effective time
    :param CodeableConcept expirationType: Contract cessation cause
    :param Reference subject: Contract Target Entity
    :param Reference authority: Authority under which this Contract has standing
    :param Reference domain: A sphere of control governed by an authoritative jurisdiction, organization, or person
    :param Reference site: Specific Location
    :param str name: Computer friendly designation
    :param str title: Human Friendly name
    :param str subtitle: Subordinate Friendly name
    :param str alias: Acronym or short name
    :param Reference author: Source of Contract
    :param CodeableConcept scope: Range of Legal Concerns
    :param CodeableConcept topicCodeableConcept: Focus of contract interest
    :param Reference topicCodeableConcept: Focus of contract interest
    :param CodeableConcept type: Legal instrument category
    :param CodeableConcept subType: Subtype within the context of type
    :param BackboneElement contentDefinition: Contract precursor content
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Content structure and use
    :param CodeableConcept subType: Detailed Content Type Definition
    :param Reference publisher: Publisher Entity
    :param str publicationDate: When published
    :param str publicationStatus: amended | appended | cancelled | disputed | entered-in-error | executable | executed | negotiable | offered | policy | rejected | renewed | revoked | resolved | terminated
    :param str copyright: Publication Ownership
    :param BackboneElement term: Contract Term List
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Contract Term Number
    :param str issued: Contract Term Issue Date Time
    :param Period applies: Contract Term Effective Time
    :param CodeableConcept topicCodeableConcept: Term Concern
    :param Reference topicCodeableConcept: Term Concern
    :param CodeableConcept type: Contract Term Type or Form
    :param CodeableConcept subType: Contract Term Type specific classification
    :param str text: Term Statement
    :param BackboneElement securityLabel: Protection for the Term
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Link to Security Labels
    :param Coding classification: Confidentiality Protection
    :param Coding category: Applicable Policy
    :param Coding control: Handling Instructions
    :param BackboneElement offer: Context of the Contract term
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Offer business ID
    :param BackboneElement party: Offer Recipient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Referenced entity
    :param CodeableConcept role: Participant engagement type
    :param Reference topic: Negotiable offer asset
    :param CodeableConcept type: Contract Offer Type or Form
    :param CodeableConcept decision: Accepting party choice
    :param CodeableConcept decisionMode: How decision is conveyed
    :param BackboneElement answer: Response to offer text
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueboolean: The actual answer response
    :param float valueboolean: The actual answer response
    :param int valueboolean: The actual answer response
    :param str valueboolean: The actual answer response
    :param str valueboolean: The actual answer response
    :param str valueboolean: The actual answer response
    :param str valueboolean: The actual answer response
    :param str valueboolean: The actual answer response
    :param Attachment valueboolean: The actual answer response
    :param Coding valueboolean: The actual answer response
    :param Quantity valueboolean: The actual answer response
    :param Reference valueboolean: The actual answer response
    :param str text: Human readable offer text
    :param str linkId: Pointer to text
    :param int securityLabelNumber: Offer restriction numbers
    :param BackboneElement asset: Contract Term Asset List
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept scope: Range of asset
    :param CodeableConcept type: Asset category
    :param Reference typeReference: Associated entities
    :param CodeableConcept subtype: Asset sub-category
    :param Coding relationship: Kinship of the asset
    :param BackboneElement context: Circumstance of the asset
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Creator,custodian or owner
    :param CodeableConcept code: Codeable asset context
    :param str text: Context description
    :param str condition: Quality desctiption of asset
    :param CodeableConcept periodType: Asset availability types
    :param Period period: Time period of the asset
    :param Period usePeriod: Time period
    :param str text: Asset clause or question text
    :param str linkId: Pointer to asset text
    :param BackboneElement answer: Response to offer text
    :param int securityLabelNumber: Asset restriction numbers
    :param BackboneElement valuedItem: Contract Valued Item List
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept entityCodeableConcept: Contract Valued Item Type
    :param Reference entityCodeableConcept: Contract Valued Item Type
    :param Identifier identifier: Contract Valued Item Number
    :param str effectiveTime: Contract Valued Item Effective Tiem
    :param Quantity quantity: Count of Contract Valued Items
    :param Money unitPrice: Contract Valued Item fee, charge, or cost
    :param float factor: Contract Valued Item Price Scaling Factor
    :param float points: Contract Valued Item Difficulty Scaling Factor
    :param Money net: Total Contract Valued Item Value
    :param str payment: Terms of valuation
    :param str paymentDate: When payment is due
    :param Reference responsible: Who will make payment
    :param Reference recipient: Who will receive payment
    :param str linkId: Pointer to specific item
    :param int securityLabelNumber: Security Labels that define affected terms
    :param BackboneElement action: Entity being ascribed responsibility
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool doNotPerform: True if the term prohibits the  action
    :param CodeableConcept type: Type or form of the action
    :param BackboneElement subject: Entity of the action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Entity of the action
    :param CodeableConcept role: Role type of the agent
    :param CodeableConcept intent: Purpose for the Contract Term Action
    :param str linkId: Pointer to specific item
    :param CodeableConcept status: State of the action
    :param Reference context: Episode associated with action
    :param str contextLinkId: Pointer to specific item
    :param str occurrencedateTime: When action happens
    :param Period occurrencedateTime: When action happens
    :param Timing occurrencedateTime: When action happens
    :param Reference requester: Who asked for action
    :param str requesterLinkId: Pointer to specific item
    :param CodeableConcept performerType: Kind of service performer
    :param CodeableConcept performerRole: Competency of the performer
    :param Reference performer: Actor that wil execute (or not) the action
    :param str performerLinkId: Pointer to specific item
    :param CodeableConcept reasonCode: Why is action (not) needed?
    :param Reference reasonReference: Why is action (not) needed?
    :param str reason: Why action is to be performed
    :param str reasonLinkId: Pointer to specific item
    :param Annotation note: Comments about the action
    :param int securityLabelNumber: Action restriction numbers
    :param BackboneElement group: Contract Term List
    :param Reference supportingInfo: Extra Information
    :param Reference relevantHistory: Key event in Contract History
    :param BackboneElement signer: Contract Signatory
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: Contract Signatory Role
    :param Reference party: Contract Signatory Party
    :param Signature signature: Contract Documentation Signature
    :param BackboneElement friendly: Contract Friendly Language
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Easily comprehended representation of this Contract
    :param Reference contentAttachment: Easily comprehended representation of this Contract
    :param BackboneElement legal: Contract Legal Language
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Contract Legal Text
    :param Reference contentAttachment: Contract Legal Text
    :param BackboneElement rule: Computable Contract Language
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Computable Contract Rules
    :param Reference contentAttachment: Computable Contract Rules
    :param Attachment legallyBindingAttachment: Binding Contract
    :param Reference legallyBindingAttachment: Binding Contract
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
    