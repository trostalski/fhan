"""
Generated class for QuestionnaireResponse. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    :param BackboneElement item: Groups and questions
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific item from Questionnaire
    :param str definition: ElementDefinition - details for the item
    :param str text: Name for group or question text
    :param BackboneElement answer: The response(s) to the question
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueboolean: Single-valued answer to the question
    :param float valueboolean: Single-valued answer to the question
    :param int valueboolean: Single-valued answer to the question
    :param str valueboolean: Single-valued answer to the question
    :param str valueboolean: Single-valued answer to the question
    :param str valueboolean: Single-valued answer to the question
    :param str valueboolean: Single-valued answer to the question
    :param str valueboolean: Single-valued answer to the question
    :param Attachment valueboolean: Single-valued answer to the question
    :param Coding valueboolean: Single-valued answer to the question
    :param Quantity valueboolean: Single-valued answer to the question
    :param Reference valueboolean: Single-valued answer to the question
    :param BackboneElement item: Groups and questions
    :param BackboneElement item: Groups and questions
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
    
    basedOn: "Reference" = None
    
    partOf: "Reference" = None
    
    questionnaire: str = None
    
    status: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    authored: str = None
    
    author: "Reference" = None
    
    source: "Reference" = None
    
    item: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    definition: str = None
    
    text: str = None
    
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
    
    item: "BackboneElement" = None
    
    item: "BackboneElement" = None
    