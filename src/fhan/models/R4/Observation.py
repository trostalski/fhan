"""
Generated class for Observation. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class ReferenceRange(ModelBase):
    """ Guidance on how to interpret the value by comparison to a normal or recommended range.  Multiple reference ranges are interpreted as an "OR".   In other words, to represent two distinct target populations, two `referenceRange` elements would be used.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Quantity' low: Low Range, if relevant
    :param 'Quantity' high: High Range, if relevant
    :param 'CodeableConcept' type: Reference range qualifier
    :param list['CodeableConcept'] appliesTo: Reference range population
    :param 'Range' age: Applicable age range, if relevant
    :param str text: Text based reference range in an observation
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  low: 'Quantity' = None,  high: 'Quantity' = None,  type: 'CodeableConcept' = None,  appliesTo: list['CodeableConcept'] = None,  age: 'Range' = None,  text: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.low: 'Quantity' = low 
        self.high: 'Quantity' = high 
        self.type: 'CodeableConcept' = type 
        self.appliesTo: list['CodeableConcept'] = appliesTo or []
        self.age: 'Range' = age 
        self.text: str = text 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ReferenceRange":
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


    
    

class Component(ModelBase):
    """ Some observations have multiple component observations.  These component observations are expressed as separate code value pairs that share the same attributes.  Examples include systolic and diastolic component observations for blood pressure measurement and multiple component observations for genetics observations.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Type of component observation (code / type)
    :param 'Quantity' valueQuantity: Actual component result
    :param 'CodeableConcept' valueCodeableConcept: Actual component result
    :param str valueString: Actual component result
    :param bool valueBoolean: Actual component result
    :param int valueInteger: Actual component result
    :param 'Range' valueRange: Actual component result
    :param 'Ratio' valueRatio: Actual component result
    :param 'SampledData' valueSampledData: Actual component result
    :param str valueTime: Actual component result
    :param str valueDateTime: Actual component result
    :param 'Period' valuePeriod: Actual component result
    :param 'CodeableConcept' dataAbsentReason: Why the component result is missing
    :param list['CodeableConcept'] interpretation: High, low, normal, etc.
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  valueQuantity: 'Quantity' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueString: str = None,  valueBoolean: bool = None,  valueInteger: int = None,  valueRange: 'Range' = None,  valueRatio: 'Ratio' = None,  valueSampledData: 'SampledData' = None,  valueTime: str = None,  valueDateTime: str = None,  valuePeriod: 'Period' = None,  dataAbsentReason: 'CodeableConcept' = None,  interpretation: list['CodeableConcept'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueString: str = valueString 
        self.valueBoolean: bool = valueBoolean 
        self.valueInteger: int = valueInteger 
        self.valueRange: 'Range' = valueRange 
        self.valueRatio: 'Ratio' = valueRatio 
        self.valueSampledData: 'SampledData' = valueSampledData 
        self.valueTime: str = valueTime 
        self.valueDateTime: str = valueDateTime 
        self.valuePeriod: 'Period' = valuePeriod 
        self.dataAbsentReason: 'CodeableConcept' = dataAbsentReason 
        self.interpretation: list['CodeableConcept'] = interpretation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Component":
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


class Observation(DomainResource):
    """ Measurements and simple assertions made about a patient, device or other subject.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for observation
    :param list['Reference'] basedOn: Fulfills plan, proposal or order
    :param list['Reference'] partOf: Part of referenced event
    :param str status: registered | preliminary | final | amended +
    :param list['CodeableConcept'] category: Classification of  type of observation
    :param 'CodeableConcept' code: Type of observation (code / type)
    :param 'Reference' subject: Who and/or what the observation is about
    :param list['Reference'] focus: What the observation is about, when it is not about the subject of record
    :param 'Reference' encounter: Healthcare event during which this observation is made
    :param str effectiveDateTime: Clinically relevant time/time-period for observation
    :param 'Period' effectivePeriod: Clinically relevant time/time-period for observation
    :param 'Timing' effectiveTiming: Clinically relevant time/time-period for observation
    :param str effectiveInstant: Clinically relevant time/time-period for observation
    :param str issued: Date/Time this version was made available
    :param list['Reference'] performer: Who is responsible for the observation
    :param 'Quantity' valueQuantity: Actual result
    :param 'CodeableConcept' valueCodeableConcept: Actual result
    :param str valueString: Actual result
    :param bool valueBoolean: Actual result
    :param int valueInteger: Actual result
    :param 'Range' valueRange: Actual result
    :param 'Ratio' valueRatio: Actual result
    :param 'SampledData' valueSampledData: Actual result
    :param str valueTime: Actual result
    :param str valueDateTime: Actual result
    :param 'Period' valuePeriod: Actual result
    :param 'CodeableConcept' dataAbsentReason: Why the result is missing
    :param list['CodeableConcept'] interpretation: High, low, normal, etc.
    :param list['Annotation'] note: Comments about the observation
    :param 'CodeableConcept' bodySite: Observed body part
    :param 'CodeableConcept' method: How it was done
    :param 'Reference' specimen: Specimen used for this observation
    :param 'Reference' device: (Measurement) Device
    :param list['ReferenceRange'] referenceRange: Provides guide for interpretation
    :param list['Reference'] hasMember: Related resource that belongs to the Observation group
    :param list['Reference'] derivedFrom: Related measurements the observation is made from
    :param list['Component'] component: Component results
    """
    def __init__(self, resourceType: str = "Observation",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  basedOn: list['Reference'] = None,  partOf: list['Reference'] = None,  status: str = None,  category: list['CodeableConcept'] = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  focus: list['Reference'] = None,  encounter: 'Reference' = None,  effectiveDateTime: str = None,  effectivePeriod: 'Period' = None,  effectiveTiming: 'Timing' = None,  effectiveInstant: str = None,  issued: str = None,  performer: list['Reference'] = None,  valueQuantity: 'Quantity' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueString: str = None,  valueBoolean: bool = None,  valueInteger: int = None,  valueRange: 'Range' = None,  valueRatio: 'Ratio' = None,  valueSampledData: 'SampledData' = None,  valueTime: str = None,  valueDateTime: str = None,  valuePeriod: 'Period' = None,  dataAbsentReason: 'CodeableConcept' = None,  interpretation: list['CodeableConcept'] = None,  note: list['Annotation'] = None,  bodySite: 'CodeableConcept' = None,  method: 'CodeableConcept' = None,  specimen: 'Reference' = None,  device: 'Reference' = None,  referenceRange: list['ReferenceRange'] = None,  hasMember: list['Reference'] = None,  derivedFrom: list['Reference'] = None,  component: list['Component'] = None, ):
        self.resourceType: str = resourceType or "Observation"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.basedOn: list['Reference'] = basedOn or []
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.category: list['CodeableConcept'] = category or []
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.focus: list['Reference'] = focus or []
        self.encounter: 'Reference' = encounter 
        self.effectiveDateTime: str = effectiveDateTime 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.effectiveTiming: 'Timing' = effectiveTiming 
        self.effectiveInstant: str = effectiveInstant 
        self.issued: str = issued 
        self.performer: list['Reference'] = performer or []
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueString: str = valueString 
        self.valueBoolean: bool = valueBoolean 
        self.valueInteger: int = valueInteger 
        self.valueRange: 'Range' = valueRange 
        self.valueRatio: 'Ratio' = valueRatio 
        self.valueSampledData: 'SampledData' = valueSampledData 
        self.valueTime: str = valueTime 
        self.valueDateTime: str = valueDateTime 
        self.valuePeriod: 'Period' = valuePeriod 
        self.dataAbsentReason: 'CodeableConcept' = dataAbsentReason 
        self.interpretation: list['CodeableConcept'] = interpretation or []
        self.note: list['Annotation'] = note or []
        self.bodySite: 'CodeableConcept' = bodySite 
        self.method: 'CodeableConcept' = method 
        self.specimen: 'Reference' = specimen 
        self.device: 'Reference' = device 
        self.referenceRange: list['ReferenceRange'] = referenceRange or []
        self.hasMember: list['Reference'] = hasMember or []
        self.derivedFrom: list['Reference'] = derivedFrom or []
        self.component: list['Component'] = component or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Observation":
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