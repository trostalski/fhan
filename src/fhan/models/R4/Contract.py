"""
Generated class for Contract. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Signature import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class ContentDefinition(BaseModel):
    """Precusory content developed with a focus and intent of supporting the formation a Contract instance, which may be associated with and transformable into a Contract.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Content structure and use
    :param CodeableConcept subType: Detailed Content Type Definition
    :param Reference publisher: Publisher Entity
    :param str publicationDate: When published
    :param str publicationStatus: amended | appended | cancelled | disputed | entered-in-error | executable | executed | negotiable | offered | policy | rejected | renewed | revoked | resolved | terminated
    :param str copyright: Publication Ownership
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "subType": {"class_name": "CodeableConcept", "is_contained": False},
        "publisher": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        subType: "CodeableConcept" = None,
        publisher: "Reference" = None,
        publicationDate: "str" = None,
        publicationStatus: "str" = None,
        copyright: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.subType = subType
        self.publisher = publisher
        self.publicationDate = publicationDate
        self.publicationStatus = publicationStatus
        self.copyright = copyright

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SecurityLabel(BaseModel):
    """Security labels that protect the handling of information about the term and its elements, which may be specifically identified..:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Link to Security Labels
    :param Coding classification: Confidentiality Protection
    :param Coding category: Applicable Policy
    :param Coding control: Handling Instructions
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "classification": {"class_name": "Coding", "is_contained": False},
        "category": {"class_name": "Coding", "is_contained": False},
        "control": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        number: list["int"] = None,
        classification: "Coding" = None,
        category: list["Coding"] = None,
        control: list["Coding"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.number = number or []
        self.classification = classification
        self.category = category or []
        self.control = control or []

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Party(BaseModel):
    """Offer Recipient.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Referenced entity
    :param CodeableConcept role: Participant engagement type
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        reference: list["Reference"] = None,
        role: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.reference = reference or []
        self.role = role

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Answer(BaseModel):
    """Response to offer text.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueBoolean: The actual answer response
    :param float valueDecimal: The actual answer response
    :param int valueInteger: The actual answer response
    :param str valueDate: The actual answer response
    :param str valueDateTime: The actual answer response
    :param str valueTime: The actual answer response
    :param str valueString: The actual answer response
    :param str valueUri: The actual answer response
    :param Attachment valueAttachment: The actual answer response
    :param Coding valueCoding: The actual answer response
    :param Quantity valueQuantity: The actual answer response
    :param Reference valueReference: The actual answer response
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        "valueCoding": {"class_name": "Coding", "is_contained": False},
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        valueBoolean: "bool" = None,
        valueDecimal: "float" = None,
        valueInteger: "int" = None,
        valueDate: "str" = None,
        valueDateTime: "str" = None,
        valueTime: "str" = None,
        valueString: "str" = None,
        valueUri: "str" = None,
        valueAttachment: "Attachment" = None,
        valueCoding: "Coding" = None,
        valueQuantity: "Quantity" = None,
        valueReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.valueBoolean = valueBoolean
        self.valueDecimal = valueDecimal
        self.valueInteger = valueInteger
        self.valueDate = valueDate
        self.valueDateTime = valueDateTime
        self.valueTime = valueTime
        self.valueString = valueString
        self.valueUri = valueUri
        self.valueAttachment = valueAttachment
        self.valueCoding = valueCoding
        self.valueQuantity = valueQuantity
        self.valueReference = valueReference

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Offer(BaseModel):
    """The matter of concern in the context of this provision of the agrement.:param str id: Unique id for inter-element referencing
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

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "party": {"class_name": "Party", "is_contained": True},
        "topic": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "decision": {"class_name": "CodeableConcept", "is_contained": False},
        "decisionMode": {"class_name": "CodeableConcept", "is_contained": False},
        "answer": {"class_name": "Answer", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        party: list["Party"] = None,
        topic: "Reference" = None,
        type: "CodeableConcept" = None,
        decision: "CodeableConcept" = None,
        decisionMode: list["CodeableConcept"] = None,
        answer: list["Answer"] = None,
        text: "str" = None,
        linkId: list["str"] = None,
        securityLabelNumber: list["int"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.party = party or []
        self.topic = topic
        self.type = type
        self.decision = decision
        self.decisionMode = decisionMode or []
        self.answer = answer or []
        self.text = text
        self.linkId = linkId or []
        self.securityLabelNumber = securityLabelNumber or []

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Context(BaseModel):
    """Circumstance of the asset.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Creator,custodian or owner
    :param CodeableConcept code: Codeable asset context
    :param str text: Context description
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        reference: "Reference" = None,
        code: list["CodeableConcept"] = None,
        text: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.reference = reference
        self.code = code or []
        self.text = text

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ValuedItem(BaseModel):
    """Contract Valued Item List.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept entityCodeableConcept: Contract Valued Item Type
    :param Reference entityReference: Contract Valued Item Type
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

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "entityCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "entityReference": {"class_name": "Reference", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "responsible": {"class_name": "Reference", "is_contained": False},
        "recipient": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        entityCodeableConcept: "CodeableConcept" = None,
        entityReference: "Reference" = None,
        identifier: "Identifier" = None,
        effectiveTime: "str" = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        points: "float" = None,
        net: "Money" = None,
        payment: "str" = None,
        paymentDate: "str" = None,
        responsible: "Reference" = None,
        recipient: "Reference" = None,
        linkId: list["str"] = None,
        securityLabelNumber: list["int"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.entityCodeableConcept = entityCodeableConcept
        self.entityReference = entityReference
        self.identifier = identifier
        self.effectiveTime = effectiveTime
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.points = points
        self.net = net
        self.payment = payment
        self.paymentDate = paymentDate
        self.responsible = responsible
        self.recipient = recipient
        self.linkId = linkId or []
        self.securityLabelNumber = securityLabelNumber or []

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Asset(BaseModel):
    """Contract Term Asset List.:param str id: Unique id for inter-element referencing
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
    :param Answer answer: Response to assets
    :param int securityLabelNumber: Asset restriction numbers
    :param ValuedItem valuedItem: Contract Valued Item List
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "scope": {"class_name": "CodeableConcept", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "typeReference": {"class_name": "Reference", "is_contained": False},
        "subtype": {"class_name": "CodeableConcept", "is_contained": False},
        "relationship": {"class_name": "Coding", "is_contained": False},
        "context": {"class_name": "Context", "is_contained": True},
        "periodType": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "usePeriod": {"class_name": "Period", "is_contained": False},
        "answer": {"class_name": "Answer", "is_contained": True},
        "valuedItem": {"class_name": "ValuedItem", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        scope: "CodeableConcept" = None,
        type: list["CodeableConcept"] = None,
        typeReference: list["Reference"] = None,
        subtype: list["CodeableConcept"] = None,
        relationship: "Coding" = None,
        context: list["Context"] = None,
        condition: "str" = None,
        periodType: list["CodeableConcept"] = None,
        period: list["Period"] = None,
        usePeriod: list["Period"] = None,
        text: "str" = None,
        linkId: list["str"] = None,
        answer: list["Answer"] = None,
        securityLabelNumber: list["int"] = None,
        valuedItem: list["ValuedItem"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.scope = scope
        self.type = type or []
        self.typeReference = typeReference or []
        self.subtype = subtype or []
        self.relationship = relationship
        self.context = context or []
        self.condition = condition
        self.periodType = periodType or []
        self.period = period or []
        self.usePeriod = usePeriod or []
        self.text = text
        self.linkId = linkId or []
        self.answer = answer or []
        self.securityLabelNumber = securityLabelNumber or []
        self.valuedItem = valuedItem or []

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Subject(BaseModel):
    """Entity of the action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Entity of the action
    :param CodeableConcept role: Role type of the agent
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        reference: list["Reference"] = None,
        role: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.reference = reference or []
        self.role = role

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Action(BaseModel):
    """An actor taking a role in an activity for which it can be assigned some degree of responsibility for the activity taking place.:param str id: Unique id for inter-element referencing
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
    :param Period occurrencePeriod: When action happens
    :param Timing occurrenceTiming: When action happens
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

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Subject", "is_contained": True},
        "intent": {"class_name": "CodeableConcept", "is_contained": False},
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        "context": {"class_name": "Reference", "is_contained": False},
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        "requester": {"class_name": "Reference", "is_contained": False},
        "performerType": {"class_name": "CodeableConcept", "is_contained": False},
        "performerRole": {"class_name": "CodeableConcept", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        doNotPerform: "bool" = None,
        type: "CodeableConcept" = None,
        subject: list["Subject"] = None,
        intent: "CodeableConcept" = None,
        linkId: list["str"] = None,
        status: "CodeableConcept" = None,
        context: "Reference" = None,
        contextLinkId: list["str"] = None,
        occurrenceDateTime: "str" = None,
        occurrencePeriod: "Period" = None,
        occurrenceTiming: "Timing" = None,
        requester: list["Reference"] = None,
        requesterLinkId: list["str"] = None,
        performerType: list["CodeableConcept"] = None,
        performerRole: "CodeableConcept" = None,
        performer: "Reference" = None,
        performerLinkId: list["str"] = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        reason: list["str"] = None,
        reasonLinkId: list["str"] = None,
        note: list["Annotation"] = None,
        securityLabelNumber: list["int"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.doNotPerform = doNotPerform
        self.type = type
        self.subject = subject or []
        self.intent = intent
        self.linkId = linkId or []
        self.status = status
        self.context = context
        self.contextLinkId = contextLinkId or []
        self.occurrenceDateTime = occurrenceDateTime
        self.occurrencePeriod = occurrencePeriod
        self.occurrenceTiming = occurrenceTiming
        self.requester = requester or []
        self.requesterLinkId = requesterLinkId or []
        self.performerType = performerType or []
        self.performerRole = performerRole
        self.performer = performer
        self.performerLinkId = performerLinkId or []
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.reason = reason or []
        self.reasonLinkId = reasonLinkId or []
        self.note = note or []
        self.securityLabelNumber = securityLabelNumber or []

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Term(BaseModel):
    """One or more Contract Provisions, which may be related and conveyed as a group, and may contain nested groups.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Contract Term Number
    :param str issued: Contract Term Issue Date Time
    :param Period applies: Contract Term Effective Time
    :param CodeableConcept topicCodeableConcept: Term Concern
    :param Reference topicReference: Term Concern
    :param CodeableConcept type: Contract Term Type or Form
    :param CodeableConcept subType: Contract Term Type specific classification
    :param str text: Term Statement
    :param SecurityLabel securityLabel: Protection for the Term
    :param Offer offer: Context of the Contract term
    :param Asset asset: Contract Term Asset List
    :param Action action: Entity being ascribed responsibility
    :param Group group: Nested Contract Term Group
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "applies": {"class_name": "Period", "is_contained": False},
        "topicCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "topicReference": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "subType": {"class_name": "CodeableConcept", "is_contained": False},
        "securityLabel": {"class_name": "SecurityLabel", "is_contained": True},
        "offer": {"class_name": "Offer", "is_contained": True},
        "asset": {"class_name": "Asset", "is_contained": True},
        "action": {"class_name": "Action", "is_contained": True},
        "group": {"class_name": "Group", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: "Identifier" = None,
        issued: "str" = None,
        applies: "Period" = None,
        topicCodeableConcept: "CodeableConcept" = None,
        topicReference: "Reference" = None,
        type: "CodeableConcept" = None,
        subType: "CodeableConcept" = None,
        text: "str" = None,
        securityLabel: list["SecurityLabel"] = None,
        offer: "Offer" = None,
        asset: list["Asset"] = None,
        action: list["Action"] = None,
        group: list["Group"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.issued = issued
        self.applies = applies
        self.topicCodeableConcept = topicCodeableConcept
        self.topicReference = topicReference
        self.type = type
        self.subType = subType
        self.text = text
        self.securityLabel = securityLabel or []
        self.offer = offer
        self.asset = asset or []
        self.action = action or []
        self.group = group or []

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Signer(BaseModel):
    """Parties with legal standing in the Contract, including the principal parties, the grantor(s) and grantee(s), which are any person or organization bound by the contract, and any ancillary parties, which facilitate the execution of the contract such as a notary or witness.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: Contract Signatory Role
    :param Reference party: Contract Signatory Party
    :param Signature signature: Contract Documentation Signature
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "Coding", "is_contained": False},
        "party": {"class_name": "Reference", "is_contained": False},
        "signature": {"class_name": "Signature", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "Coding" = None,
        party: "Reference" = None,
        signature: list["Signature"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.party = party
        self.signature = signature or []

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Friendly(BaseModel):
    """The "patient friendly language" versionof the Contract in whole or in parts. "Patient friendly language" means the representation of the Contract and Contract Provisions in a manner that is readily accessible and understandable by a layperson in accordance with best practices for communication styles that ensure that those agreeing to or signing the Contract understand the roles, actions, obligations, responsibilities, and implication of the agreement.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Easily comprehended representation of this Contract
    :param Reference contentReference: Easily comprehended representation of this Contract
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "contentAttachment": {"class_name": "Attachment", "is_contained": False},
        "contentReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        contentAttachment: "Attachment" = None,
        contentReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Legal(BaseModel):
    """List of Legal expressions or representations of this Contract.:param CodeableConcept legalState: Negotiation status
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Contract Legal Text
    :param Reference contentReference: Contract Legal Text
    :param Attachment legallyBindingAttachment: Binding Contract
    :param Reference legallyBindingReference: Binding Contract
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "legalState": {"class_name": "CodeableConcept", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "contentAttachment": {"class_name": "Attachment", "is_contained": False},
        "contentReference": {"class_name": "Reference", "is_contained": False},
        "legallyBindingAttachment": {"class_name": "Attachment", "is_contained": False},
        "legallyBindingReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        legalState: "CodeableConcept" = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        contentAttachment: "Attachment" = None,
        contentReference: "Reference" = None,
        legallyBindingAttachment: "Attachment" = None,
        legallyBindingReference: "Reference" = None,
    ):
        self.legalState = legalState
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference
        self.legallyBindingAttachment = legallyBindingAttachment
        self.legallyBindingReference = legallyBindingReference

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Rule(BaseModel):
    """List of Computable Policy Rule Language Representations of this Contract.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Computable Contract Rules
    :param Reference contentReference: Computable Contract Rules
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "contentAttachment": {"class_name": "Attachment", "is_contained": False},
        "contentReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        contentAttachment: "Attachment" = None,
        contentReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.contentAttachment = contentAttachment
        self.contentReference = contentReference

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Contract(DomainResource):
    """Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
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
    :param Reference topicReference: Focus of contract interest
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

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "legalState": {"class_name": "CodeableConcept", "is_contained": False},
        "instantiatesCanonical": {"class_name": "Reference", "is_contained": False},
        "contentDerivative": {"class_name": "CodeableConcept", "is_contained": False},
        "applies": {"class_name": "Period", "is_contained": False},
        "expirationType": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "authority": {"class_name": "Reference", "is_contained": False},
        "domain": {"class_name": "Reference", "is_contained": False},
        "site": {"class_name": "Reference", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "scope": {"class_name": "CodeableConcept", "is_contained": False},
        "topicCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "topicReference": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "subType": {"class_name": "CodeableConcept", "is_contained": False},
        "contentDefinition": {"class_name": "ContentDefinition", "is_contained": True},
        "term": {"class_name": "Term", "is_contained": True},
        "supportingInfo": {"class_name": "Reference", "is_contained": False},
        "relevantHistory": {"class_name": "Reference", "is_contained": False},
        "signer": {"class_name": "Signer", "is_contained": True},
        "friendly": {"class_name": "Friendly", "is_contained": True},
        "legal": {"class_name": "Legal", "is_contained": True},
        "rule": {"class_name": "Rule", "is_contained": True},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        url: "str" = None,
        version: "str" = None,
        status: "str" = None,
        legalState: "CodeableConcept" = None,
        instantiatesCanonical: "Reference" = None,
        instantiatesUri: "str" = None,
        contentDerivative: "CodeableConcept" = None,
        issued: "str" = None,
        applies: "Period" = None,
        expirationType: "CodeableConcept" = None,
        subject: list["Reference"] = None,
        authority: list["Reference"] = None,
        domain: list["Reference"] = None,
        site: list["Reference"] = None,
        name: "str" = None,
        title: "str" = None,
        subtitle: "str" = None,
        alias: list["str"] = None,
        author: "Reference" = None,
        scope: "CodeableConcept" = None,
        topicCodeableConcept: "CodeableConcept" = None,
        topicReference: "Reference" = None,
        type: "CodeableConcept" = None,
        subType: list["CodeableConcept"] = None,
        contentDefinition: "ContentDefinition" = None,
        term: list["Term"] = None,
        supportingInfo: list["Reference"] = None,
        relevantHistory: list["Reference"] = None,
        signer: list["Signer"] = None,
        friendly: list["Friendly"] = None,
        legal: list["Legal"] = None,
        rule: list["Rule"] = None,
    ):
        self.resourceType = resourceType or "Contract"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.url = url
        self.version = version
        self.status = status
        self.legalState = legalState
        self.instantiatesCanonical = instantiatesCanonical
        self.instantiatesUri = instantiatesUri
        self.contentDerivative = contentDerivative
        self.issued = issued
        self.applies = applies
        self.expirationType = expirationType
        self.subject = subject or []
        self.authority = authority or []
        self.domain = domain or []
        self.site = site or []
        self.name = name
        self.title = title
        self.subtitle = subtitle
        self.alias = alias or []
        self.author = author
        self.scope = scope
        self.topicCodeableConcept = topicCodeableConcept
        self.topicReference = topicReference
        self.type = type
        self.subType = subType or []
        self.contentDefinition = contentDefinition
        self.term = term or []
        self.supportingInfo = supportingInfo or []
        self.relevantHistory = relevantHistory or []
        self.signer = signer or []
        self.friendly = friendly or []
        self.legal = legal or []
        self.rule = rule or []

    @classmethod
    def from_dict(cls, data: dict) -> "Contract":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Contract":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
