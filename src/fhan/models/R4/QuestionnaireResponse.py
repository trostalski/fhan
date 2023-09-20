"""
Generated class for QuestionnaireResponse. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class Answer(Element):
    """ The respondent's answer(s) to the question.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueBoolean: Single-valued answer to the question
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    valueBoolean: bool = None
    
  
    
    
@dataclass
class Item(Element):
    """ A group or question item from the original questionnaire for which answers are provided.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific item from Questionnaire
    :param str definition: ElementDefinition - details for the item
    :param str text: Name for group or question text
    :param Answer answer: The response(s) to the question
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    linkId: str = None
    
    definition: str = None
    
    text: str = None
    answer: list[Answer] = None
    
@dataclass
class QuestionnaireResponse(ModelBase):
    """ A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.
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
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: "Identifier" = None
    
    basedOn: list["Reference"] = None
    
    partOf: list["Reference"] = None
    
    questionnaire: str = None
    
    status: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    authored: str = None
    
    author: "Reference" = None
    
    source: "Reference" = None
    
    item: list["Item"] = None
    