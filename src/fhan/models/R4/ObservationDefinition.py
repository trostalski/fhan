"""
Generated class for ObservationDefinition. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class QuantitativeDetails(ModelBase):
    """ Characteristics for quantitative results of this observation.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' customaryUnit: Customary unit for quantitative results
    :param 'CodeableConcept' unit: SI unit for quantitative results
    :param float conversionFactor: SI to Customary unit conversion factor
    :param int decimalPrecision: Decimal precision of observation quantitative results
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  customaryUnit: 'CodeableConcept' = None,  unit: 'CodeableConcept' = None,  conversionFactor: float = None,  decimalPrecision: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.customaryUnit: 'CodeableConcept' = customaryUnit 
        self.unit: 'CodeableConcept' = unit 
        self.conversionFactor: float = conversionFactor 
        self.decimalPrecision: int = decimalPrecision 
        

    @classmethod
    def from_dict(cls, data: dict) -> "QuantitativeDetails":
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


    
    

class QualifiedInterval(ModelBase):
    """ Multiple  ranges of results qualified by different contexts for ordinal or continuous observations conforming to this ObservationDefinition.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str category: reference | critical | absolute
    :param 'Range' range: The interval itself, for continuous or ordinal observations
    :param 'CodeableConcept' context: Range context qualifier
    :param list['CodeableConcept'] appliesTo: Targetted population of the range
    :param str gender: male | female | other | unknown
    :param 'Range' age: Applicable age range, if relevant
    :param 'Range' gestationalAge: Applicable gestational age range, if relevant
    :param str condition: Condition associated with the reference range
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  category: str = None,  range: 'Range' = None,  context: 'CodeableConcept' = None,  appliesTo: list['CodeableConcept'] = None,  gender: str = None,  age: 'Range' = None,  gestationalAge: 'Range' = None,  condition: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.category: str = category 
        self.range: 'Range' = range 
        self.context: 'CodeableConcept' = context 
        self.appliesTo: list['CodeableConcept'] = appliesTo or []
        self.gender: str = gender 
        self.age: 'Range' = age 
        self.gestationalAge: 'Range' = gestationalAge 
        self.condition: str = condition 
        

    @classmethod
    def from_dict(cls, data: dict) -> "QualifiedInterval":
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


class ObservationDefinition(DomainResource):
    """ Set of definitional characteristics for a kind of observation or measurement produced or consumed by an orderable health care service.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['CodeableConcept'] category: Category of observation
    :param 'CodeableConcept' code: Type of observation (code / type)
    :param list['Identifier'] identifier: Business identifier for this ObservationDefinition instance
    :param str permittedDataType: Quantity | CodeableConcept | string | boolean | integer | Range | Ratio | SampledData | time | dateTime | Period
    :param bool multipleResultsAllowed: Multiple results allowed
    :param 'CodeableConcept' method: Method used to produce the observation
    :param str preferredReportName: Preferred report name
    :param 'QuantitativeDetails' quantitativeDetails: Characteristics of quantitative results
    :param list['QualifiedInterval'] qualifiedInterval: Qualified range for continuous and ordinal observation results
    :param 'Reference' validCodedValueSet: Value set of valid coded values for the observations conforming to this ObservationDefinition
    :param 'Reference' normalCodedValueSet: Value set of normal coded values for the observations conforming to this ObservationDefinition
    :param 'Reference' abnormalCodedValueSet: Value set of abnormal coded values for the observations conforming to this ObservationDefinition
    :param 'Reference' criticalCodedValueSet: Value set of critical coded values for the observations conforming to this ObservationDefinition
    """
    def __init__(self, resourceType: str = "ObservationDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  category: list['CodeableConcept'] = None,  code: 'CodeableConcept' = None,  identifier: list['Identifier'] = None,  permittedDataType: str = None,  multipleResultsAllowed: bool = None,  method: 'CodeableConcept' = None,  preferredReportName: str = None,  quantitativeDetails: 'QuantitativeDetails' = None,  qualifiedInterval: list['QualifiedInterval'] = None,  validCodedValueSet: 'Reference' = None,  normalCodedValueSet: 'Reference' = None,  abnormalCodedValueSet: 'Reference' = None,  criticalCodedValueSet: 'Reference' = None, ):
        self.resourceType: str = resourceType or "ObservationDefinition"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.category: list['CodeableConcept'] = category or []
        self.code: 'CodeableConcept' = code 
        self.identifier: list['Identifier'] = identifier or []
        self.permittedDataType: str = permittedDataType or []
        self.multipleResultsAllowed: bool = multipleResultsAllowed 
        self.method: 'CodeableConcept' = method 
        self.preferredReportName: str = preferredReportName 
        self.quantitativeDetails: 'QuantitativeDetails' = quantitativeDetails 
        self.qualifiedInterval: list['QualifiedInterval'] = qualifiedInterval or []
        self.validCodedValueSet: 'Reference' = validCodedValueSet 
        self.normalCodedValueSet: 'Reference' = normalCodedValueSet 
        self.abnormalCodedValueSet: 'Reference' = abnormalCodedValueSet 
        self.criticalCodedValueSet: 'Reference' = criticalCodedValueSet 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ObservationDefinition":
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