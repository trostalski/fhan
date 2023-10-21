"""
Generated class for Questionnaire. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Coding import *
from fhan.models.R4.DomainResource import *


class EnableWhen(BaseModel):
    """A constraint indicating that this item should only be enabled (displayed/allow answers to be captured) when the specified condition is true.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str question: Question that determines whether item is enabled
    :param str operator: exists | = | != | > | < | >= | <=
    :param bool answerBoolean: Value for question comparison based on operator
    :param float answerDecimal: Value for question comparison based on operator
    :param int answerInteger: Value for question comparison based on operator
    :param str answerDate: Value for question comparison based on operator
    :param str answerDateTime: Value for question comparison based on operator
    :param str answerTime: Value for question comparison based on operator
    :param str answerString: Value for question comparison based on operator
    :param Coding answerCoding: Value for question comparison based on operator
    :param Quantity answerQuantity: Value for question comparison based on operator
    :param Reference answerReference: Value for question comparison based on operator
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "answerCoding": {"class_name": "Coding", "is_contained": False},
        "answerQuantity": {"class_name": "Quantity", "is_contained": False},
        "answerReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        question: "str" = None,
        operator: "str" = None,
        answerBoolean: "bool" = None,
        answerDecimal: "float" = None,
        answerInteger: "int" = None,
        answerDate: "str" = None,
        answerDateTime: "str" = None,
        answerTime: "str" = None,
        answerString: "str" = None,
        answerCoding: "Coding" = None,
        answerQuantity: "Quantity" = None,
        answerReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.question = question
        self.operator = operator
        self.answerBoolean = answerBoolean
        self.answerDecimal = answerDecimal
        self.answerInteger = answerInteger
        self.answerDate = answerDate
        self.answerDateTime = answerDateTime
        self.answerTime = answerTime
        self.answerString = answerString
        self.answerCoding = answerCoding
        self.answerQuantity = answerQuantity
        self.answerReference = answerReference

    @classmethod
    def from_dict(cls, data: dict) -> "Questionnaire":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Questionnaire":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AnswerOption(BaseModel):
    """One of the permitted answers for a "choice" or "open-choice" question.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int valueInteger: Answer value
    :param str valueDate: Answer value
    :param str valueTime: Answer value
    :param str valueString: Answer value
    :param Coding valueCoding: Answer value
    :param Reference valueReference: Answer value
    :param bool initialSelected: Whether option is selected by default
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "valueCoding": {"class_name": "Coding", "is_contained": False},
        "valueReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        valueInteger: "int" = None,
        valueDate: "str" = None,
        valueTime: "str" = None,
        valueString: "str" = None,
        valueCoding: "Coding" = None,
        valueReference: "Reference" = None,
        initialSelected: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.valueInteger = valueInteger
        self.valueDate = valueDate
        self.valueTime = valueTime
        self.valueString = valueString
        self.valueCoding = valueCoding
        self.valueReference = valueReference
        self.initialSelected = initialSelected

    @classmethod
    def from_dict(cls, data: dict) -> "Questionnaire":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Questionnaire":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Initial(BaseModel):
    """One or more values that should be pre-populated in the answer when initially rendering the questionnaire for user input.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueBoolean: Actual value for initializing the question
    :param float valueDecimal: Actual value for initializing the question
    :param int valueInteger: Actual value for initializing the question
    :param str valueDate: Actual value for initializing the question
    :param str valueDateTime: Actual value for initializing the question
    :param str valueTime: Actual value for initializing the question
    :param str valueString: Actual value for initializing the question
    :param str valueUri: Actual value for initializing the question
    :param Attachment valueAttachment: Actual value for initializing the question
    :param Coding valueCoding: Actual value for initializing the question
    :param Quantity valueQuantity: Actual value for initializing the question
    :param Reference valueReference: Actual value for initializing the question
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
    def from_dict(cls, data: dict) -> "Questionnaire":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Questionnaire":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Item(BaseModel):
    """A particular question, question grouping or display text that is part of the questionnaire.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for item in questionnaire
    :param str definition: ElementDefinition - details for the item
    :param Coding code: Corresponding concept for this item in a terminology
    :param str prefix: E.g. "1(a)", "2.5.3"
    :param str text: Primary text for the item
    :param str type: group | display | boolean | decimal | integer | date | dateTime +
    :param EnableWhen enableWhen: Only allow data when
    :param str enableBehavior: all | any
    :param bool required: Whether the item must be included in data results
    :param bool repeats: Whether the item may repeat
    :param bool readOnly: Don't allow human editing
    :param int maxLength: No more than this many characters
    :param str answerValueSet: Valueset containing permitted answers
    :param AnswerOption answerOption: Permitted answer
    :param Initial initial: Initial value(s) when item is first rendered
    :param Item item: Nested questionnaire items
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "Coding", "is_contained": False},
        "enableWhen": {"class_name": "EnableWhen", "is_contained": True},
        "answerOption": {"class_name": "AnswerOption", "is_contained": True},
        "initial": {"class_name": "Initial", "is_contained": True},
        "item": {"class_name": "Item", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        linkId: "str" = None,
        definition: "str" = None,
        code: list["Coding"] = None,
        prefix: "str" = None,
        text: "str" = None,
        type: "str" = None,
        enableWhen: list["EnableWhen"] = None,
        enableBehavior: "str" = None,
        required: "bool" = None,
        repeats: "bool" = None,
        readOnly: "bool" = None,
        maxLength: "int" = None,
        answerValueSet: "str" = None,
        answerOption: list["AnswerOption"] = None,
        initial: list["Initial"] = None,
        item: list["Item"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId
        self.definition = definition
        self.code = code or []
        self.prefix = prefix
        self.text = text
        self.type = type
        self.enableWhen = enableWhen or []
        self.enableBehavior = enableBehavior
        self.required = required
        self.repeats = repeats
        self.readOnly = readOnly
        self.maxLength = maxLength
        self.answerValueSet = answerValueSet
        self.answerOption = answerOption or []
        self.initial = initial or []
        self.item = item or []

    @classmethod
    def from_dict(cls, data: dict) -> "Questionnaire":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Questionnaire":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Questionnaire(DomainResource):
    """A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this questionnaire, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the questionnaire
    :param str version: Business version of the questionnaire
    :param str name: Name for this questionnaire (computer friendly)
    :param str title: Name for this questionnaire (human friendly)
    :param str derivedFrom: Instantiates protocol or definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str subjectType: Resource that can be subject of QuestionnaireResponse
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the questionnaire
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for questionnaire (if applicable)
    :param str purpose: Why this questionnaire is defined
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the questionnaire was approved by publisher
    :param str lastReviewDate: When the questionnaire was last reviewed
    :param Period effectivePeriod: When the questionnaire is expected to be used
    :param Coding code: Concept that represents the overall questionnaire
    :param Item item: Questions and sections within the Questionnaire
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        "code": {"class_name": "Coding", "is_contained": False},
        "item": {"class_name": "Item", "is_contained": True},
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
        url: "str" = None,
        identifier: list["Identifier"] = None,
        version: "str" = None,
        name: "str" = None,
        title: "str" = None,
        derivedFrom: list["str"] = None,
        status: "str" = None,
        experimental: "bool" = None,
        subjectType: list["str"] = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        copyright: "str" = None,
        approvalDate: "str" = None,
        lastReviewDate: "str" = None,
        effectivePeriod: "Period" = None,
        code: list["Coding"] = None,
        item: list["Item"] = None,
    ):
        self.resourceType = resourceType or "Questionnaire"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.identifier = identifier or []
        self.version = version
        self.name = name
        self.title = title
        self.derivedFrom = derivedFrom or []
        self.status = status
        self.experimental = experimental
        self.subjectType = subjectType or []
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.copyright = copyright
        self.approvalDate = approvalDate
        self.lastReviewDate = lastReviewDate
        self.effectivePeriod = effectivePeriod
        self.code = code or []
        self.item = item or []

    @classmethod
    def from_dict(cls, data: dict) -> "Questionnaire":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Questionnaire":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
