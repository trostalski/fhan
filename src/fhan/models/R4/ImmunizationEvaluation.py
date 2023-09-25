"""
Generated class for ImmunizationEvaluation. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class ImmunizationEvaluation(DomainResource):
    """ Describes a comparison of an immunization event against published recommendations to determine if the administration is "valid" in relation to those  recommendations.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier
    :param str status: completed | entered-in-error
    :param 'Reference' patient: Who this evaluation is for
    :param str date: Date evaluation was performed
    :param 'Reference' authority: Who is responsible for publishing the recommendations
    :param 'CodeableConcept' targetDisease: Evaluation target disease
    :param 'Reference' immunizationEvent: Immunization being evaluated
    :param 'CodeableConcept' doseStatus: Status of the dose relative to published recommendations
    :param list['CodeableConcept'] doseStatusReason: Reason for the dose status
    :param str description: Evaluation notes
    :param str series: Name of vaccine series
    :param int doseNumberPositiveInt: Dose number within series
    :param str doseNumberString: Dose number within series
    :param int seriesDosesPositiveInt: Recommended number of doses for immunity
    :param str seriesDosesString: Recommended number of doses for immunity
    """
    def __init__(self, resourceType: str = "ImmunizationEvaluation",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  patient: 'Reference' = None,  date: str = None,  authority: 'Reference' = None,  targetDisease: 'CodeableConcept' = None,  immunizationEvent: 'Reference' = None,  doseStatus: 'CodeableConcept' = None,  doseStatusReason: list['CodeableConcept'] = None,  description: str = None,  series: str = None,  doseNumberPositiveInt: int = None,  doseNumberString: str = None,  seriesDosesPositiveInt: int = None,  seriesDosesString: str = None, ):
        self.resourceType: str = resourceType or "ImmunizationEvaluation"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.patient: 'Reference' = patient 
        self.date: str = date 
        self.authority: 'Reference' = authority 
        self.targetDisease: 'CodeableConcept' = targetDisease 
        self.immunizationEvent: 'Reference' = immunizationEvent 
        self.doseStatus: 'CodeableConcept' = doseStatus 
        self.doseStatusReason: list['CodeableConcept'] = doseStatusReason or []
        self.description: str = description 
        self.series: str = series 
        self.doseNumberPositiveInt: int = doseNumberPositiveInt 
        self.doseNumberString: str = doseNumberString 
        self.seriesDosesPositiveInt: int = seriesDosesPositiveInt 
        self.seriesDosesString: str = seriesDosesString 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ImmunizationEvaluation":
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