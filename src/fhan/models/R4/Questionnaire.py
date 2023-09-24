"""
Generated class for Questionnaire. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Coding import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class EnableWhen(ModelBase):
    """ A constraint indicating that this item should only be enabled (displayed/allow answers to be captured) when the specified condition is true.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str question: Question that determines whether item is enabled
    :param str operator: exists | = | != | > | < | >= | <=
    :param bool answerBoolean: Value for question comparison based on operator
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  question: str = None,  operator: str = None,  answerBoolean: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.question: str = question 
        self.operator: str = operator 
        self.answerBoolean: bool = answerBoolean 
        

    
    

class AnswerOption(ModelBase):
    """ One of the permitted answers for a "choice" or "open-choice" question.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int valueInteger: Answer value
    :param bool initialSelected: Whether option is selected by default
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  valueInteger: int = None,  initialSelected: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.valueInteger: int = valueInteger 
        self.initialSelected: bool = initialSelected 
        

    
    

class Initial(ModelBase):
    """ One or more values that should be pre-populated in the answer when initially rendering the questionnaire for user input.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueBoolean: Actual value for initializing the question
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  valueBoolean: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.valueBoolean: bool = valueBoolean 
        

  
    
    

class Item(ModelBase):
    """ A particular question, question grouping or display text that is part of the questionnaire.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for item in questionnaire
    :param str definition: ElementDefinition - details for the item
    :param list['Coding'] code: Corresponding concept for this item in a terminology
    :param str prefix: E.g. "1(a)", "2.5.3"
    :param str text: Primary text for the item
    :param str type: group | display | boolean | decimal | integer | date | dateTime +
    :param list['EnableWhen'] enableWhen: Only allow data when
    :param str enableBehavior: all | any
    :param bool required: Whether the item must be included in data results
    :param bool repeats: Whether the item may repeat
    :param bool readOnly: Don't allow human editing
    :param int maxLength: No more than this many characters
    :param str answerValueSet: Valueset containing permitted answers
    :param list['AnswerOption'] answerOption: Permitted answer
    :param list['Initial'] initial: Initial value(s) when item is first rendered
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  linkId: str = None,  definition: str = None,  code: list['Coding'] = None,  prefix: str = None,  text: str = None,  type: str = None,  enableWhen: list['EnableWhen'] = None,  enableBehavior: str = None,  required: bool = None,  repeats: bool = None,  readOnly: bool = None,  maxLength: int = None,  answerValueSet: str = None,  answerOption: list['AnswerOption'] = None,  initial: list['Initial'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.linkId: str = linkId 
        self.definition: str = definition 
        self.code: list['Coding'] = code or []
        self.prefix: str = prefix 
        self.text: str = text 
        self.type: str = type 
        self.enableWhen: list['EnableWhen'] = enableWhen or []
        self.enableBehavior: str = enableBehavior 
        self.required: bool = required 
        self.repeats: bool = repeats 
        self.readOnly: bool = readOnly 
        self.maxLength: int = maxLength 
        self.answerValueSet: str = answerValueSet 
        self.answerOption: list['AnswerOption'] = answerOption or []
        self.initial: list['Initial'] = initial or []
        

class Questionnaire(DomainResource):
    """ A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this questionnaire, represented as a URI (globally unique)
    :param list['Identifier'] identifier: Additional identifier for the questionnaire
    :param str version: Business version of the questionnaire
    :param str name: Name for this questionnaire (computer friendly)
    :param str title: Name for this questionnaire (human friendly)
    :param str derivedFrom: Instantiates protocol or definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str subjectType: Resource that can be subject of QuestionnaireResponse
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the questionnaire
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for questionnaire (if applicable)
    :param str purpose: Why this questionnaire is defined
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the questionnaire was approved by publisher
    :param str lastReviewDate: When the questionnaire was last reviewed
    :param 'Period' effectivePeriod: When the questionnaire is expected to be used
    :param list['Coding'] code: Concept that represents the overall questionnaire
    :param list['Item'] item: Questions and sections within the Questionnaire
    """
    def __init__(self, resourceType: str = "Questionnaire",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  identifier: list['Identifier'] = None,  version: str = None,  name: str = None,  title: str = None,  derivedFrom: str = None,  status: str = None,  experimental: bool = None,  subjectType: str = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  purpose: str = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  code: list['Coding'] = None,  item: list['Item'] = None, ):
        self.resourceType: str = resourceType or "Questionnaire"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.url: str = url 
        self.identifier: list['Identifier'] = identifier or []
        self.version: str = version 
        self.name: str = name 
        self.title: str = title 
        self.derivedFrom: str = derivedFrom or []
        self.status: str = status 
        self.experimental: bool = experimental 
        self.subjectType: str = subjectType or []
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.purpose: str = purpose 
        self.copyright: str = copyright 
        self.approvalDate: str = approvalDate 
        self.lastReviewDate: str = lastReviewDate 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.code: list['Coding'] = code or []
        self.item: list['Item'] = item or []
        