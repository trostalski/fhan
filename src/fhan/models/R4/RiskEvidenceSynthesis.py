"""
Generated class for RiskEvidenceSynthesis. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class SampleSize(BaseModel):
    """ A description of the size of the sample involved in the synthesis.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of sample size
    :param int numberOfStudies: How many studies?
    :param int numberOfParticipants: How many participants?
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  description: str = None,  numberOfStudies: int = None,  numberOfParticipants: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.description: str = description 
        self.numberOfStudies: int = numberOfStudies 
        self.numberOfParticipants: int = numberOfParticipants 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SampleSize":
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


    
        
    
    

class PrecisionEstimate(BaseModel):
    """ A description of the precision of the estimate for the effect.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of precision estimate
    :param float level: Level of confidence interval
    :param float _from: Lower bound
    :param float to: Upper bound
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  level: float = None,  _from: float = None,  to: float = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.level: float = level 
        self._from: float = _from 
        self.to: float = to 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PrecisionEstimate":
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


  
    
    

class RiskEstimate(BaseModel):
    """ The estimated risk of the outcome.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of risk estimate
    :param 'CodeableConcept' type: Type of risk estimate
    :param float value: Point estimate
    :param 'CodeableConcept' unitOfMeasure: What unit is the outcome described in?
    :param int denominatorCount: Sample size for group measured
    :param int numeratorCount: Number with the outcome
    :param 'PrecisionEstimate' precisionEstimate: How precise the estimate is
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  description: str = None,  type: 'CodeableConcept' = None,  value: float = None,  unitOfMeasure: 'CodeableConcept' = None,  denominatorCount: int = None,  numeratorCount: int = None,  precisionEstimate: 'PrecisionEstimate' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.description: str = description 
        self.type: 'CodeableConcept' = type 
        self.value: float = value 
        self.unitOfMeasure: 'CodeableConcept' = unitOfMeasure 
        self.denominatorCount: int = denominatorCount 
        self.numeratorCount: int = numeratorCount 
        self.precisionEstimate: list['PrecisionEstimate'] = precisionEstimate or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RiskEstimate":
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


    
        
    
    

class CertaintySubcomponent(BaseModel):
    """ A description of a component of the overall certainty.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of subcomponent of certainty rating
    :param 'CodeableConcept' rating: Subcomponent certainty rating
    :param 'Annotation' note: Used for footnotes or explanatory notes
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  rating: 'CodeableConcept' = None,  note: 'Annotation' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.rating: list['CodeableConcept'] = rating or []
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "CertaintySubcomponent":
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


  
    
    

class Certainty(BaseModel):
    """ A description of the certainty of the risk estimate.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' rating: Certainty rating
    :param 'Annotation' note: Used for footnotes or explanatory notes
    :param 'CertaintySubcomponent' certaintySubcomponent: A component that contributes to the overall certainty
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  rating: 'CodeableConcept' = None,  note: 'Annotation' = None,  certaintySubcomponent: 'CertaintySubcomponent' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.rating: list['CodeableConcept'] = rating or []
        self.note: list['Annotation'] = note or []
        self.certaintySubcomponent: list['CertaintySubcomponent'] = certaintySubcomponent or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Certainty":
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


class RiskEvidenceSynthesis(DomainResource):
    """ The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state where the risk estimate is derived from a combination of research studies.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this risk evidence synthesis, represented as a URI (globally unique)
    :param 'Identifier' identifier: Additional identifier for the risk evidence synthesis
    :param str version: Business version of the risk evidence synthesis
    :param str name: Name for this risk evidence synthesis (computer friendly)
    :param str title: Name for this risk evidence synthesis (human friendly)
    :param str status: draft | active | retired | unknown
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param 'ContactDetail' contact: Contact details for the publisher
    :param str description: Natural language description of the risk evidence synthesis
    :param 'Annotation' note: Used for footnotes or explanatory notes
    :param 'UsageContext' useContext: The context that the content is intended to support
    :param 'CodeableConcept' jurisdiction: Intended jurisdiction for risk evidence synthesis (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the risk evidence synthesis was approved by publisher
    :param str lastReviewDate: When the risk evidence synthesis was last reviewed
    :param 'Period' effectivePeriod: When the risk evidence synthesis is expected to be used
    :param 'CodeableConcept' topic: The category of the EffectEvidenceSynthesis, such as Education, Treatment, Assessment, etc.
    :param 'ContactDetail' author: Who authored the content
    :param 'ContactDetail' editor: Who edited the content
    :param 'ContactDetail' reviewer: Who reviewed the content
    :param 'ContactDetail' endorser: Who endorsed the content
    :param 'RelatedArtifact' relatedArtifact: Additional documentation, citations, etc.
    :param 'CodeableConcept' synthesisType: Type of synthesis
    :param 'CodeableConcept' studyType: Type of study
    :param 'Reference' population: What population?
    :param 'Reference' exposure: What exposure?
    :param 'Reference' outcome: What outcome?
    :param 'SampleSize' sampleSize: What sample size was involved?
    :param 'RiskEstimate' riskEstimate: What was the estimated risk
    :param 'Certainty' certainty: How certain is the risk
    """
    def __init__(self, resourceType: str = "RiskEvidenceSynthesis",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  url: str = None,  identifier: 'Identifier' = None,  version: str = None,  name: str = None,  title: str = None,  status: str = None,  date: str = None,  publisher: str = None,  contact: 'ContactDetail' = None,  description: str = None,  note: 'Annotation' = None,  useContext: 'UsageContext' = None,  jurisdiction: 'CodeableConcept' = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  topic: 'CodeableConcept' = None,  author: 'ContactDetail' = None,  editor: 'ContactDetail' = None,  reviewer: 'ContactDetail' = None,  endorser: 'ContactDetail' = None,  relatedArtifact: 'RelatedArtifact' = None,  synthesisType: 'CodeableConcept' = None,  studyType: 'CodeableConcept' = None,  population: 'Reference' = None,  exposure: 'Reference' = None,  outcome: 'Reference' = None,  sampleSize: 'SampleSize' = None,  riskEstimate: 'RiskEstimate' = None,  certainty: 'Certainty' = None, ):
        self.resourceType: str = resourceType or "RiskEvidenceSynthesis"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.url: str = url 
        self.identifier: list['Identifier'] = identifier or []
        self.version: str = version 
        self.name: str = name 
        self.title: str = title 
        self.status: str = status 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.note: list['Annotation'] = note or []
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.copyright: str = copyright 
        self.approvalDate: str = approvalDate 
        self.lastReviewDate: str = lastReviewDate 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.topic: list['CodeableConcept'] = topic or []
        self.author: list['ContactDetail'] = author or []
        self.editor: list['ContactDetail'] = editor or []
        self.reviewer: list['ContactDetail'] = reviewer or []
        self.endorser: list['ContactDetail'] = endorser or []
        self.relatedArtifact: list['RelatedArtifact'] = relatedArtifact or []
        self.synthesisType: 'CodeableConcept' = synthesisType 
        self.studyType: 'CodeableConcept' = studyType 
        self.population: 'Reference' = population 
        self.exposure: 'Reference' = exposure 
        self.outcome: 'Reference' = outcome 
        self.sampleSize: 'SampleSize' = sampleSize 
        self.riskEstimate: 'RiskEstimate' = riskEstimate 
        self.certainty: list['Certainty'] = certainty or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RiskEvidenceSynthesis":
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