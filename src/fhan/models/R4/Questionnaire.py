"""
Generated class for Questionnaire. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Coding import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class Questionnaire(ModelBase):
    """ A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
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
    :param BackboneElement item: Questions and sections within the Questionnaire
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for item in questionnaire
    :param str definition: ElementDefinition - details for the item
    :param Coding code: Corresponding concept for this item in a terminology
    :param str prefix: E.g. "1(a)", "2.5.3"
    :param str text: Primary text for the item
    :param str type: group | display | boolean | decimal | integer | date | dateTime +
    :param BackboneElement enableWhen: Only allow data when
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str question: Question that determines whether item is enabled
    :param str operator: exists | = | != | > | < | >= | <=
    :param bool answerboolean: Value for question comparison based on operator
    :param float answerboolean: Value for question comparison based on operator
    :param int answerboolean: Value for question comparison based on operator
    :param str answerboolean: Value for question comparison based on operator
    :param str answerboolean: Value for question comparison based on operator
    :param str answerboolean: Value for question comparison based on operator
    :param str answerboolean: Value for question comparison based on operator
    :param Coding answerboolean: Value for question comparison based on operator
    :param Quantity answerboolean: Value for question comparison based on operator
    :param Reference answerboolean: Value for question comparison based on operator
    :param str enableBehavior: all | any
    :param bool required: Whether the item must be included in data results
    :param bool repeats: Whether the item may repeat
    :param bool readOnly: Don't allow human editing
    :param int maxLength: No more than this many characters
    :param str answerValueSet: Valueset containing permitted answers
    :param BackboneElement answerOption: Permitted answer
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int valueinteger: Answer value
    :param str valueinteger: Answer value
    :param str valueinteger: Answer value
    :param str valueinteger: Answer value
    :param Coding valueinteger: Answer value
    :param Reference valueinteger: Answer value
    :param bool initialSelected: Whether option is selected by default
    :param BackboneElement initial: Initial value(s) when item is first rendered
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueboolean: Actual value for initializing the question
    :param float valueboolean: Actual value for initializing the question
    :param int valueboolean: Actual value for initializing the question
    :param str valueboolean: Actual value for initializing the question
    :param str valueboolean: Actual value for initializing the question
    :param str valueboolean: Actual value for initializing the question
    :param str valueboolean: Actual value for initializing the question
    :param str valueboolean: Actual value for initializing the question
    :param Attachment valueboolean: Actual value for initializing the question
    :param Coding valueboolean: Actual value for initializing the question
    :param Quantity valueboolean: Actual value for initializing the question
    :param Reference valueboolean: Actual value for initializing the question
    :param BackboneElement item: Questions and sections within the Questionnaire
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    derivedFrom: str = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectType: str = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    code: "Coding" = None
    
    item: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    definition: str = None
    
    code: "Coding" = None
    
    prefix: str = None
    
    text: str = None
    
    type: str = None
    
    enableWhen: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    question: str = None
    
    operator: str = None
    
    answerboolean: bool = None
    
    answerboolean: float = None
    
    answerboolean: int = None
    
    answerboolean: str = None
    
    answerboolean: str = None
    
    answerboolean: str = None
    
    answerboolean: str = None
    
    answerboolean: "Coding" = None
    
    answerboolean: "Quantity" = None
    
    answerboolean: "Reference" = None
    
    enableBehavior: str = None
    
    required: bool = None
    
    repeats: bool = None
    
    readOnly: bool = None
    
    maxLength: int = None
    
    answerValueSet: str = None
    
    answerOption: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    valueinteger: int = None
    
    valueinteger: str = None
    
    valueinteger: str = None
    
    valueinteger: str = None
    
    valueinteger: "Coding" = None
    
    valueinteger: "Reference" = None
    
    initialSelected: bool = None
    
    initial: "BackboneElement" = None
    
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
    
    item: "BackboneElement" = None
    