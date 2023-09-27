"""
Generated class for FiveWs. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Timing import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import BaseModel

class FiveWs(BaseModel):
    """ Logical Model: Who What When Where Why - Common pattern for all resources that deals with attribution.
    :param 'Identifier' identifier: Business Identifier
    :param str version: Identifier for this version
    :param str status: Status Field
    :param 'CodeableConcept' _class: Classifier Field
    :param 'CodeableConcept' grade: A field that indicates the potential impact of the content of the resource
    :param 'CodeableConcept' whatCodeableConcept: What this resource is about
    :param 'Reference' whatReference: What this resource is about
    :param 'Reference' subject: Who this resource is about
    :param 'Reference' context: Context for the work described in this resource
    :param str init: When the work described in this resource was started (or will be)
    :param 'Timing' planned: When this resource is planned to occur
    :param str doneDateTime: When the work described in this resource was completed (or will be)
    :param 'Period' donePeriod: When the work described in this resource was completed (or will be)
    :param str recorded: When this resource itself was created
    :param 'Reference' author: Who authored the content of the resource
    :param 'Reference' source: Who provided the information in this resource
    :param 'Reference' actor: Who did the work described the resource (or will do)
    :param 'Reference' cause: Who prompted the work described in the resource
    :param 'Reference' witness: Who attests to the content of the resource (individual or org)
    :param 'Reference' who: An actor involved in the work described by this resource
    :param 'CodeableConcept' whereCodeableConcept: The location of the work described
    :param 'Reference' whereReference: The location of the work described
    :param 'CodeableConcept' whyCodeableConcept: Why this work was done
    :param 'Reference' whyReference: Why this work was done
    """
    def __init__(self, resourceType: str = "FiveWs",  identifier: 'Identifier' = None,  version: str = None,  status: str = None,  _class: 'CodeableConcept' = None,  grade: 'CodeableConcept' = None,  whatCodeableConcept: 'CodeableConcept' = None,  whatReference: 'Reference' = None,  subject: 'Reference' = None,  context: 'Reference' = None,  init: str = None,  planned: 'Timing' = None,  doneDateTime: str = None,  donePeriod: 'Period' = None,  recorded: str = None,  author: 'Reference' = None,  source: 'Reference' = None,  actor: 'Reference' = None,  cause: 'Reference' = None,  witness: 'Reference' = None,  who: 'Reference' = None,  whereCodeableConcept: 'CodeableConcept' = None,  whereReference: 'Reference' = None,  whyCodeableConcept: 'CodeableConcept' = None,  whyReference: 'Reference' = None, ):
        self.resourceType: str = resourceType or "FiveWs"
        self.identifier: list['Identifier'] = identifier or []
        self.version: str = version 
        self.status: str = status 
        self._class: list['CodeableConcept'] = _class or []
        self.grade: 'CodeableConcept' = grade 
        self.whatCodeableConcept: 'CodeableConcept' = whatCodeableConcept 
        self.whatReference: 'Reference' = whatReference 
        self.subject: list['Reference'] = subject or []
        self.context: 'Reference' = context 
        self.init: str = init 
        self.planned: list['Timing'] = planned or []
        self.doneDateTime: str = doneDateTime 
        self.donePeriod: 'Period' = donePeriod 
        self.recorded: str = recorded 
        self.author: list['Reference'] = author or []
        self.source: list['Reference'] = source or []
        self.actor: list['Reference'] = actor or []
        self.cause: list['Reference'] = cause or []
        self.witness: list['Reference'] = witness or []
        self.who: list['Reference'] = who or []
        self.whereCodeableConcept: list['CodeableConcept'] = whereCodeableConcept or []
        self.whereReference: list['Reference'] = whereReference or []
        self.whyCodeableConcept: list['CodeableConcept'] = whyCodeableConcept or []
        self.whyReference: list['Reference'] = whyReference or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "FiveWs":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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