"""
Generated class for QuestionnaireResponse. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Answer(ModelBase):
    """ The respondent's answer(s) to the question.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool valueBoolean: Single-valued answer to the question
    :param float valueDecimal: Single-valued answer to the question
    :param int valueInteger: Single-valued answer to the question
    :param str valueDate: Single-valued answer to the question
    :param str valueDateTime: Single-valued answer to the question
    :param str valueTime: Single-valued answer to the question
    :param str valueString: Single-valued answer to the question
    :param str valueUri: Single-valued answer to the question
    :param 'Attachment' valueAttachment: Single-valued answer to the question
    :param 'Coding' valueCoding: Single-valued answer to the question
    :param 'Quantity' valueQuantity: Single-valued answer to the question
    :param 'Reference' valueReference: Single-valued answer to the question
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  valueBoolean: bool = None,  valueDecimal: float = None,  valueInteger: int = None,  valueDate: str = None,  valueDateTime: str = None,  valueTime: str = None,  valueString: str = None,  valueUri: str = None,  valueAttachment: 'Attachment' = None,  valueCoding: 'Coding' = None,  valueQuantity: 'Quantity' = None,  valueReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.valueBoolean: bool = valueBoolean 
        self.valueDecimal: float = valueDecimal 
        self.valueInteger: int = valueInteger 
        self.valueDate: str = valueDate 
        self.valueDateTime: str = valueDateTime 
        self.valueTime: str = valueTime 
        self.valueString: str = valueString 
        self.valueUri: str = valueUri 
        self.valueAttachment: 'Attachment' = valueAttachment 
        self.valueCoding: 'Coding' = valueCoding 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueReference: 'Reference' = valueReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Answer":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


  
    
    

class Item(ModelBase):
    """ A group or question item from the original questionnaire for which answers are provided.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific item from Questionnaire
    :param str definition: ElementDefinition - details for the item
    :param str text: Name for group or question text
    :param list['Answer'] answer: The response(s) to the question
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  linkId: str = None,  definition: str = None,  text: str = None,  answer: list['Answer'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.linkId: str = linkId 
        self.definition: str = definition 
        self.text: str = text 
        self.answer: list['Answer'] = answer or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Item":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


class QuestionnaireResponse(DomainResource):
    """ A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Unique id for this set of answers
    :param list['Reference'] basedOn: Request fulfilled by this QuestionnaireResponse
    :param list['Reference'] partOf: Part of this action
    :param str questionnaire: Form being answered
    :param str status: in-progress | completed | amended | entered-in-error | stopped
    :param 'Reference' subject: The subject of the questions
    :param 'Reference' encounter: Encounter created as part of
    :param str authored: Date the answers were gathered
    :param 'Reference' author: Person who received and recorded the answers
    :param 'Reference' source: The person who answered the questions
    :param list['Item'] item: Groups and questions
    """
    def __init__(self, resourceType: str = "QuestionnaireResponse",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  basedOn: list['Reference'] = None,  partOf: list['Reference'] = None,  questionnaire: str = None,  status: str = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  authored: str = None,  author: 'Reference' = None,  source: 'Reference' = None,  item: list['Item'] = None, ):
        self.resourceType: str = resourceType or "QuestionnaireResponse"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.basedOn: list['Reference'] = basedOn or []
        self.partOf: list['Reference'] = partOf or []
        self.questionnaire: str = questionnaire 
        self.status: str = status 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.authored: str = authored 
        self.author: 'Reference' = author 
        self.source: 'Reference' = source 
        self.item: list['Item'] = item or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "QuestionnaireResponse":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance