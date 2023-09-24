"""
Generated class for Contract. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Money import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class ContentDefinition(Element):
    """ Precusory content developed with a focus and intent of supporting the formation a Contract instance, which may be associated with and transformable into a Contract.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Content structure and use
    :param CodeableConcept subType: Detailed Content Type Definition
    :param Reference publisher: Publisher Entity
    :param str publicationDate: When published
    :param str publicationStatus: amended | appended | cancelled | disputed | entered-in-error | executable | executed | negotiable | offered | policy | rejected | renewed | revoked | resolved | terminated
    :param str copyright: Publication Ownership
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type:  "CodeableConcept" = CodeableConcept()
    
    subType:  "CodeableConcept" = CodeableConcept()
    
    publisher:  "Reference" = Reference()
    
    publicationDate: str = None
    
    publicationStatus: str = None
    
    copyright: str = None
    

    
        
    
    
@dataclass
class SecurityLabel(Element):
    """ Security labels that protect the handling of information about the term and its elements, which may be specifically identified..:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Link to Security Labels
    :param Coding classification: Confidentiality Protection
    :param Coding category: Applicable Policy
    :param Coding control: Handling Instructions
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    number: int = None
    
    classification:  "Coding" = Coding()
    
    category:  list["Coding"] = [Coding()]
    
    control:  list["Coding"] = [Coding()]
    

    
        
    
    
@dataclass
class Party(Element):
    """ Offer Recipient.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Referenced entity
    :param CodeableConcept role: Participant engagement type
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    reference:  list["Reference"] = [Reference()]
    
    role:  "CodeableConcept" = CodeableConcept()
    

    
    
@dataclass
class Answer(Element):
    """ Response to offer text.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueBoolean: The actual answer response
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    valueBoolean: bool = None
    

  
    
    
@dataclass
class Offer(Element):
    """ The matter of concern in the context of this provision of the agrement.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Offer business ID
    :param Party party: Offer Recipient
    :param Reference topic: Negotiable offer asset
    :param CodeableConcept type: Contract Offer Type or Form
    :param CodeableConcept decision: Accepting party choice
    :param CodeableConcept decisionMode: How decision is conveyed
    :param Answer answer: Response to offer text
    :param str text: Human readable offer text
    :param str linkId: Pointer to text
    :param int securityLabelNumber: Offer restriction numbers
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    identifier:  list["Identifier"] = [Identifier()]
    
    party:  list["Party"] = [Party()]
    
    topic:  "Reference" = Reference()
    
    type:  "CodeableConcept" = CodeableConcept()
    
    decision:  "CodeableConcept" = CodeableConcept()
    
    decisionMode:  list["CodeableConcept"] = [CodeableConcept()]
    
    answer:  list["Answer"] = [Answer()]
    
    text: str = None
    
    linkId: str = None
    
    securityLabelNumber: int = None
    

    
        
    
    
@dataclass
class Context(Element):
    """ Circumstance of the asset.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Creator,custodian or owner
    :param CodeableConcept code: Codeable asset context
    :param str text: Context description
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    reference:  "Reference" = Reference()
    
    code:  list["CodeableConcept"] = [CodeableConcept()]
    
    text: str = None
    

    
    
@dataclass
class ValuedItem(Element):
    """ Contract Valued Item List.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept entityCodeableConcept: Contract Valued Item Type
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
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    entityCodeableConcept:  "CodeableConcept" = CodeableConcept()
    
    identifier:  "Identifier" = Identifier()
    
    effectiveTime: str = None
    
    quantity:  "Quantity" = Quantity()
    
    unitPrice:  "Money" = Money()
    
    factor: float = None
    
    points: float = None
    
    net:  "Money" = Money()
    
    payment: str = None
    
    paymentDate: str = None
    
    responsible:  "Reference" = Reference()
    
    recipient:  "Reference" = Reference()
    
    linkId: str = None
    
    securityLabelNumber: int = None
    

  
    
    
@dataclass
class Asset(Element):
    """ Contract Term Asset List.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept scope: Range of asset
    :param CodeableConcept type: Asset category
    :param Reference typeReference: Associated entities
    :param CodeableConcept subtype: Asset sub-category
    :param Coding relationship: Kinship of the asset
    :param Context context: Circumstance of the asset
    :param str condition: Quality desctiption of asset
    :param CodeableConcept periodType: Asset availability types
    :param Period period: Time period of the asset
    :param Period usePeriod: Time period
    :param str text: Asset clause or question text
    :param str linkId: Pointer to asset text
    :param int securityLabelNumber: Asset restriction numbers
    :param ValuedItem valuedItem: Contract Valued Item List
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    scope:  "CodeableConcept" = CodeableConcept()
    
    type:  list["CodeableConcept"] = [CodeableConcept()]
    
    typeReference:  list["Reference"] = [Reference()]
    
    subtype:  list["CodeableConcept"] = [CodeableConcept()]
    
    relationship:  "Coding" = Coding()
    
    context:  list["Context"] = [Context()]
    
    condition: str = None
    
    periodType:  list["CodeableConcept"] = [CodeableConcept()]
    
    period:  list["Period"] = [Period()]
    
    usePeriod:  list["Period"] = [Period()]
    
    text: str = None
    
    linkId: str = None
    
    securityLabelNumber: int = None
    
    valuedItem:  list["ValuedItem"] = [ValuedItem()]
    

    
        
    
    
@dataclass
class Subject(Element):
    """ Entity of the action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Entity of the action
    :param CodeableConcept role: Role type of the agent
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    reference:  list["Reference"] = [Reference()]
    
    role:  "CodeableConcept" = CodeableConcept()
    

  
    
    
@dataclass
class Action(Element):
    """ An actor taking a role in an activity for which it can be assigned some degree of responsibility for the activity taking place.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool doNotPerform: True if the term prohibits the  action
    :param CodeableConcept type: Type or form of the action
    :param Subject subject: Entity of the action
    :param CodeableConcept intent: Purpose for the Contract Term Action
    :param str linkId: Pointer to specific item
    :param CodeableConcept status: State of the action
    :param Reference context: Episode associated with action
    :param str contextLinkId: Pointer to specific item
    :param str occurrenceDateTime: When action happens
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
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    doNotPerform: bool = None
    
    type:  "CodeableConcept" = CodeableConcept()
    
    subject:  list["Subject"] = [Subject()]
    
    intent:  "CodeableConcept" = CodeableConcept()
    
    linkId: str = None
    
    status:  "CodeableConcept" = CodeableConcept()
    
    context:  "Reference" = Reference()
    
    contextLinkId: str = None
    
    occurrenceDateTime: str = None
    
    requester:  list["Reference"] = [Reference()]
    
    requesterLinkId: str = None
    
    performerType:  list["CodeableConcept"] = [CodeableConcept()]
    
    performerRole:  "CodeableConcept" = CodeableConcept()
    
    performer:  "Reference" = Reference()
    
    performerLinkId: str = None
    
    reasonCode:  list["CodeableConcept"] = [CodeableConcept()]
    
    reasonReference:  list["Reference"] = [Reference()]
    
    reason: str = None
    
    reasonLinkId: str = None
    
    note:  list["Annotation"] = [Annotation()]
    
    securityLabelNumber: int = None
    

  
    
    
@dataclass
class Term(Element):
    """ One or more Contract Provisions, which may be related and conveyed as a group, and may contain nested groups.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Contract Term Number
    :param str issued: Contract Term Issue Date Time
    :param Period applies: Contract Term Effective Time
    :param CodeableConcept topicCodeableConcept: Term Concern
    :param CodeableConcept type: Contract Term Type or Form
    :param CodeableConcept subType: Contract Term Type specific classification
    :param str text: Term Statement
    :param SecurityLabel securityLabel: Protection for the Term
    :param Offer offer: Context of the Contract term
    :param Asset asset: Contract Term Asset List
    :param Action action: Entity being ascribed responsibility
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    identifier:  "Identifier" = Identifier()
    
    issued: str = None
    
    applies:  "Period" = Period()
    
    topicCodeableConcept:  "CodeableConcept" = CodeableConcept()
    
    type:  "CodeableConcept" = CodeableConcept()
    
    subType:  "CodeableConcept" = CodeableConcept()
    
    text: str = None
    
    securityLabel:  list["SecurityLabel"] = [SecurityLabel()]
    
    offer:  "Offer" = Offer()
    
    asset:  list["Asset"] = [Asset()]
    
    action:  list["Action"] = [Action()]
    

    
    
@dataclass
class Signer(Element):
    """ Parties with legal standing in the Contract, including the principal parties, the grantor(s) and grantee(s), which are any person or organization bound by the contract, and any ancillary parties, which facilitate the execution of the contract such as a notary or witness.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: Contract Signatory Role
    :param Reference party: Contract Signatory Party
    :param Signature signature: Contract Documentation Signature
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type:  "Coding" = Coding()
    
    party:  "Reference" = Reference()
    
    signature:  list["Signature"] = [Signature()]
    

    
    
@dataclass
class Friendly(Element):
    """ The "patient friendly language" versionof the Contract in whole or in parts. "Patient friendly language" means the representation of the Contract and Contract Provisions in a manner that is readily accessible and understandable by a layperson in accordance with best practices for communication styles that ensure that those agreeing to or signing the Contract understand the roles, actions, obligations, responsibilities, and implication of the agreement.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Easily comprehended representation of this Contract
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    contentAttachment:  "Attachment" = Attachment()
    

    
    
@dataclass
class Legal(Element):
    """ List of Legal expressions or representations of this Contract.:param CodeableConcept legalState: Negotiation status
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Contract Legal Text
    :param Attachment legallyBindingAttachment: Binding Contract
    """
    legalState:  "CodeableConcept" = CodeableConcept()
    
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    contentAttachment:  "Attachment" = Attachment()
    
    legallyBindingAttachment:  "Attachment" = Attachment()
    

    
    
@dataclass
class Rule(Element):
    """ List of Computable Policy Rule Language Representations of this Contract.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Computable Contract Rules
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    contentAttachment:  "Attachment" = Attachment()
    

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
    :param CodeableConcept type: Legal instrument category
    :param CodeableConcept subType: Subtype within the context of type
    :param ContentDefinition contentDefinition: Contract precursor content
    :param Term term: Contract Term List
    :param Reference supportingInfo: Extra Information
    :param Reference relevantHistory: Key event in Contract History
    :param Signer signer: Contract Signatory
    :param Friendly friendly: Contract Friendly Language
    :param Legal legal: Contract Legal Language
    :param Rule rule: Computable Contract Language
    """

    resourceType: str = "Contract"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
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
    
    subject: list["Reference"] = None
    
    authority: list["Reference"] = None
    
    domain: list["Reference"] = None
    
    site: list["Reference"] = None
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    alias: str = None
    
    author: "Reference" = None
    
    scope: "CodeableConcept" = None
    
    topicCodeableConcept: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    subType: list["CodeableConcept"] = None
    
    contentDefinition: "ContentDefinition" = None
    
    term: list["Term"] = None
    
    supportingInfo: list["Reference"] = None
    
    relevantHistory: list["Reference"] = None
    
    signer: list["Signer"] = None
    
    friendly: list["Friendly"] = None
    
    legal: list["Legal"] = None
    
    rule: list["Rule"] = None
    