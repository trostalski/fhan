"""
Generated class for Event. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Element import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import ModelBase

    
    

class Performer(ModelBase):
    """ Indicates who or what performed the {{title}} and how they were involved.:param 'CodeableConcept' function: Type of performance
    :param 'Reference' actor: Who performed {{title}}
    """
    def __init__(self,  function: 'CodeableConcept' = None,  actor: 'Reference' = None, ):
        self.function: 'CodeableConcept' = function 
        self.actor: 'Reference' = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Performer":
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


class Event(ModelBase):
    """ Logical Model: A pattern to be followed by resources that represent the performance of some activity, possibly in accordance with a request or service definition.
    :param list['Identifier'] identifier: Business Identifier for {{title}}
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param list['Reference'] basedOn: Fulfills plan, proposal or order
    :param list['Reference'] partOf: Part of referenced event
    :param list['Reference'] researchStudy: Associated research study
    :param str status: preparation | in-progress | not-done | suspended | aborted | completed | entered-in-error | unknown
    :param 'CodeableConcept' statusReason: Reason for current status
    :param 'CodeableConcept' code: What was done
    :param 'Reference' subject: Individual service was done for/to
    :param 'Reference' encounter: Encounter created as part of
    :param str occurrenceDateTime: When {{title}} occurred/is occurring
    :param 'Period' occurrencePeriod: When {{title}} occurred/is occurring
    :param 'Timing' occurrenceTiming: When {{title}} occurred/is occurring
    :param str recorded: When {{title}} was first captured in the subject's record
    :param bool reportedBoolean: Reported rather than primary record
    :param 'Reference' reportedReference: Reported rather than primary record
    :param list['Performer'] performer: Who performed {{title}} and what they did
    :param 'Reference' location: Where {{title}} occurred
    :param list['CodeableConcept'] reasonCode: Why was {{title}} performed?
    :param list['Reference'] reasonReference: Why was {{title}} performed?
    :param list['Annotation'] note: Comments made about the event
    """
    def __init__(self, resourceType: str = "Event",  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  partOf: list['Reference'] = None,  researchStudy: list['Reference'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  occurrenceTiming: 'Timing' = None,  recorded: str = None,  reportedBoolean: bool = None,  reportedReference: 'Reference' = None,  performer: list['Performer'] = None,  location: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "Event"
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.basedOn: list['Reference'] = basedOn or []
        self.partOf: list['Reference'] = partOf or []
        self.researchStudy: list['Reference'] = researchStudy or []
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.occurrenceTiming: 'Timing' = occurrenceTiming 
        self.recorded: str = recorded 
        self.reportedBoolean: bool = reportedBoolean 
        self.reportedReference: 'Reference' = reportedReference 
        self.performer: list['Performer'] = performer or []
        self.location: 'Reference' = location 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Event":
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