"""
Generated class for RiskAssessment. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Prediction(ModelBase):
    """ Describes the expected outcome for the subject.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' outcome: Possible outcome for the subject
    :param float probabilityDecimal: Likelihood of specified outcome
    :param 'Range' probabilityRange: Likelihood of specified outcome
    :param 'CodeableConcept' qualitativeRisk: Likelihood of specified outcome as a qualitative value
    :param float relativeRisk: Relative likelihood
    :param 'Period' whenPeriod: Timeframe or age range
    :param 'Range' whenRange: Timeframe or age range
    :param str rationale: Explanation of prediction
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  outcome: 'CodeableConcept' = None,  probabilityDecimal: float = None,  probabilityRange: 'Range' = None,  qualitativeRisk: 'CodeableConcept' = None,  relativeRisk: float = None,  whenPeriod: 'Period' = None,  whenRange: 'Range' = None,  rationale: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.outcome: 'CodeableConcept' = outcome 
        self.probabilityDecimal: float = probabilityDecimal 
        self.probabilityRange: 'Range' = probabilityRange 
        self.qualitativeRisk: 'CodeableConcept' = qualitativeRisk 
        self.relativeRisk: float = relativeRisk 
        self.whenPeriod: 'Period' = whenPeriod 
        self.whenRange: 'Range' = whenRange 
        self.rationale: str = rationale 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Prediction":
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


class RiskAssessment(DomainResource):
    """ An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique identifier for the assessment
    :param 'Reference' basedOn: Request fulfilled by this assessment
    :param 'Reference' parent: Part of this occurrence
    :param str status: registered | preliminary | final | amended +
    :param 'CodeableConcept' method: Evaluation mechanism
    :param 'CodeableConcept' code: Type of assessment
    :param 'Reference' subject: Who/what does assessment apply to?
    :param 'Reference' encounter: Where was assessment performed?
    :param str occurrenceDateTime: When was assessment made?
    :param 'Period' occurrencePeriod: When was assessment made?
    :param 'Reference' condition: Condition assessed
    :param 'Reference' performer: Who did assessment?
    :param list['CodeableConcept'] reasonCode: Why the assessment was necessary?
    :param list['Reference'] reasonReference: Why the assessment was necessary?
    :param list['Reference'] basis: Information used in assessment
    :param list['Prediction'] prediction: Outcome predicted
    :param str mitigation: How to reduce risk
    :param list['Annotation'] note: Comments on the risk assessment
    """
    def __init__(self, resourceType: str = "RiskAssessment",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  basedOn: 'Reference' = None,  parent: 'Reference' = None,  status: str = None,  method: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  condition: 'Reference' = None,  performer: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  basis: list['Reference'] = None,  prediction: list['Prediction'] = None,  mitigation: str = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "RiskAssessment"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.basedOn: 'Reference' = basedOn 
        self.parent: 'Reference' = parent 
        self.status: str = status 
        self.method: 'CodeableConcept' = method 
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.condition: 'Reference' = condition 
        self.performer: 'Reference' = performer 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.basis: list['Reference'] = basis or []
        self.prediction: list['Prediction'] = prediction or []
        self.mitigation: str = mitigation 
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RiskAssessment":
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