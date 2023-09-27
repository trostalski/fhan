"""
Generated class for ImmunizationRecommendation. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class DateCriterion(BaseModel):
    """ Vaccine date recommendations.  For example, earliest date to administer, latest date to administer, etc.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Type of date
    :param str value: Recommended date
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  code: 'CodeableConcept' = None,  value: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.value: str = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DateCriterion":
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


  
    
    

class Recommendation(BaseModel):
    """ Vaccine administration recommendations.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' vaccineCode: Vaccine  or vaccine group recommendation applies to
    :param 'CodeableConcept' targetDisease: Disease to be immunized against
    :param 'CodeableConcept' contraindicatedVaccineCode: Vaccine which is contraindicated to fulfill the recommendation
    :param 'CodeableConcept' forecastStatus: Vaccine recommendation status
    :param 'CodeableConcept' forecastReason: Vaccine administration status reason
    :param 'DateCriterion' dateCriterion: Dates governing proposed immunization
    :param str description: Protocol details
    :param str series: Name of vaccination series
    :param int doseNumberPositiveInt: Recommended dose number within series
    :param str doseNumberString: Recommended dose number within series
    :param int seriesDosesPositiveInt: Recommended number of doses for immunity
    :param str seriesDosesString: Recommended number of doses for immunity
    :param 'Reference' supportingImmunization: Past immunizations supporting recommendation
    :param 'Reference' supportingPatientInformation: Patient observations supporting recommendation
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  vaccineCode: 'CodeableConcept' = None,  targetDisease: 'CodeableConcept' = None,  contraindicatedVaccineCode: 'CodeableConcept' = None,  forecastStatus: 'CodeableConcept' = None,  forecastReason: 'CodeableConcept' = None,  dateCriterion: 'DateCriterion' = None,  description: str = None,  series: str = None,  doseNumberPositiveInt: int = None,  doseNumberString: str = None,  seriesDosesPositiveInt: int = None,  seriesDosesString: str = None,  supportingImmunization: 'Reference' = None,  supportingPatientInformation: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.vaccineCode: list['CodeableConcept'] = vaccineCode or []
        self.targetDisease: 'CodeableConcept' = targetDisease 
        self.contraindicatedVaccineCode: list['CodeableConcept'] = contraindicatedVaccineCode or []
        self.forecastStatus: 'CodeableConcept' = forecastStatus 
        self.forecastReason: list['CodeableConcept'] = forecastReason or []
        self.dateCriterion: list['DateCriterion'] = dateCriterion or []
        self.description: str = description 
        self.series: str = series 
        self.doseNumberPositiveInt: int = doseNumberPositiveInt 
        self.doseNumberString: str = doseNumberString 
        self.seriesDosesPositiveInt: int = seriesDosesPositiveInt 
        self.seriesDosesString: str = seriesDosesString 
        self.supportingImmunization: list['Reference'] = supportingImmunization or []
        self.supportingPatientInformation: list['Reference'] = supportingPatientInformation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Recommendation":
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


class ImmunizationRecommendation(DomainResource):
    """ A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with optional supporting justification.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Business identifier
    :param 'Reference' patient: Who this profile is for
    :param str date: Date recommendation(s) created
    :param 'Reference' authority: Who is responsible for protocol
    :param 'Recommendation' recommendation: Vaccine administration recommendations
    """
    def __init__(self, resourceType: str = "ImmunizationRecommendation",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  patient: 'Reference' = None,  date: str = None,  authority: 'Reference' = None,  recommendation: 'Recommendation' = None, ):
        self.resourceType: str = resourceType or "ImmunizationRecommendation"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.patient: 'Reference' = patient 
        self.date: str = date 
        self.authority: 'Reference' = authority 
        self.recommendation: list['Recommendation'] = recommendation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ImmunizationRecommendation":
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