"""
Generated class for QuestionnaireResponse. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Answer(BaseModel):
    """The respondent's answer(s) to the question.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueBoolean: Single-valued answer to the question
    :param float valueDecimal: Single-valued answer to the question
    :param int valueInteger: Single-valued answer to the question
    :param str valueDate: Single-valued answer to the question
    :param str valueDateTime: Single-valued answer to the question
    :param str valueTime: Single-valued answer to the question
    :param str valueString: Single-valued answer to the question
    :param str valueUri: Single-valued answer to the question
    :param Attachment valueAttachment: Single-valued answer to the question
    :param Coding valueCoding: Single-valued answer to the question
    :param Quantity valueQuantity: Single-valued answer to the question
    :param Reference valueReference: Single-valued answer to the question
    :param Item item: Nested groups and questions
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        "valueCoding": {"class_name": "Coding", "is_contained": False},
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueReference": {"class_name": "Reference", "is_contained": False},
        "item": {"class_name": "Item", "is_contained": True},
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
        item: list["Item"] = None,
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
        self.item = item or []

    @classmethod
    def from_dict(cls, data: dict) -> "QuestionnaireResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "QuestionnaireResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Item(BaseModel):
    """A group or question item from the original questionnaire for which answers are provided.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific item from Questionnaire
    :param str definition: ElementDefinition - details for the item
    :param str text: Name for group or question text
    :param Answer answer: The response(s) to the question
    :param Item item: Nested questionnaire response items
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "answer": {"class_name": "Answer", "is_contained": True},
        "item": {"class_name": "Item", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        linkId: "str" = None,
        definition: "str" = None,
        text: "str" = None,
        answer: list["Answer"] = None,
        item: list["Item"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId
        self.definition = definition
        self.text = text
        self.answer = answer or []
        self.item = item or []

    @classmethod
    def from_dict(cls, data: dict) -> "QuestionnaireResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "QuestionnaireResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class QuestionnaireResponse(DomainResource):
    """A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique id for this set of answers
    :param Reference basedOn: Request fulfilled by this QuestionnaireResponse
    :param Reference partOf: Part of this action
    :param str questionnaire: Form being answered
    :param str status: in-progress | completed | amended | entered-in-error | stopped
    :param Reference subject: The subject of the questions
    :param Reference encounter: Encounter created as part of
    :param str authored: Date the answers were gathered
    :param Reference author: Person who received and recorded the answers
    :param Reference source: The person who answered the questions
    :param Item item: Groups and questions
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
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
        identifier: "Identifier" = None,
        basedOn: list["Reference"] = None,
        partOf: list["Reference"] = None,
        questionnaire: "str" = None,
        status: "str" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        authored: "str" = None,
        author: "Reference" = None,
        source: "Reference" = None,
        item: list["Item"] = None,
    ):
        self.resourceType = resourceType or "QuestionnaireResponse"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.questionnaire = questionnaire
        self.status = status
        self.subject = subject
        self.encounter = encounter
        self.authored = authored
        self.author = author
        self.source = source
        self.item = item or []

    @classmethod
    def from_dict(cls, data: dict) -> "QuestionnaireResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "QuestionnaireResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
