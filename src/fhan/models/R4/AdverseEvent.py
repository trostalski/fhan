"""
Generated class for AdverseEvent. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Causality(ModelBase):
    """ Information on the possible cause of the event.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' assessment: Assessment of if the entity caused the event
    :param str productRelatedness: AdverseEvent.suspectEntity.causalityProductRelatedness
    :param 'Reference' author: AdverseEvent.suspectEntity.causalityAuthor
    :param 'CodeableConcept' method: ProbabilityScale | Bayesian | Checklist
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  assessment: 'CodeableConcept' = None,  productRelatedness: str = None,  author: 'Reference' = None,  method: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.assessment: 'CodeableConcept' = assessment 
        self.productRelatedness: str = productRelatedness 
        self.author: 'Reference' = author 
        self.method: 'CodeableConcept' = method 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Causality":
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


  
    
    

class SuspectEntity(ModelBase):
    """ Describes the entity that is suspected to have caused the adverse event.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' instance: Refers to the specific entity that caused the adverse event
    :param list['Causality'] causality: Information on the possible cause of the event
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  instance: 'Reference' = None,  causality: list['Causality'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.instance: 'Reference' = instance 
        self.causality: list['Causality'] = causality or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SuspectEntity":
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


class AdverseEvent(DomainResource):
    """ Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Business identifier for the event
    :param str actuality: actual | potential
    :param list['CodeableConcept'] category: product-problem | product-quality | product-use-error | wrong-dose | incorrect-prescribing-information | wrong-technique | wrong-route-of-administration | wrong-rate | wrong-duration | wrong-time | expired-drug | medical-device-use-error | problem-different-manufacturer | unsafe-physical-environment
    :param 'CodeableConcept' event: Type of the event itself in relation to the subject
    :param 'Reference' subject: Subject impacted by event
    :param 'Reference' encounter: Encounter created as part of
    :param str date: When the event occurred
    :param str detected: When the event was detected
    :param str recordedDate: When the event was recorded
    :param list['Reference'] resultingCondition: Effect on the subject due to this event
    :param 'Reference' location: Location where adverse event occurred
    :param 'CodeableConcept' seriousness: Seriousness of the event
    :param 'CodeableConcept' severity: mild | moderate | severe
    :param 'CodeableConcept' outcome: resolved | recovering | ongoing | resolvedWithSequelae | fatal | unknown
    :param 'Reference' recorder: Who recorded the adverse event
    :param list['Reference'] contributor: Who  was involved in the adverse event or the potential adverse event
    :param list['SuspectEntity'] suspectEntity: The suspected agent causing the adverse event
    :param list['Reference'] subjectMedicalHistory: AdverseEvent.subjectMedicalHistory
    :param list['Reference'] referenceDocument: AdverseEvent.referenceDocument
    :param list['Reference'] study: AdverseEvent.study
    """
    def __init__(self, resourceType: str = "AdverseEvent",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  actuality: str = None,  category: list['CodeableConcept'] = None,  event: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  date: str = None,  detected: str = None,  recordedDate: str = None,  resultingCondition: list['Reference'] = None,  location: 'Reference' = None,  seriousness: 'CodeableConcept' = None,  severity: 'CodeableConcept' = None,  outcome: 'CodeableConcept' = None,  recorder: 'Reference' = None,  contributor: list['Reference'] = None,  suspectEntity: list['SuspectEntity'] = None,  subjectMedicalHistory: list['Reference'] = None,  referenceDocument: list['Reference'] = None,  study: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "AdverseEvent"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.actuality: str = actuality 
        self.category: list['CodeableConcept'] = category or []
        self.event: 'CodeableConcept' = event 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.date: str = date 
        self.detected: str = detected 
        self.recordedDate: str = recordedDate 
        self.resultingCondition: list['Reference'] = resultingCondition or []
        self.location: 'Reference' = location 
        self.seriousness: 'CodeableConcept' = seriousness 
        self.severity: 'CodeableConcept' = severity 
        self.outcome: 'CodeableConcept' = outcome 
        self.recorder: 'Reference' = recorder 
        self.contributor: list['Reference'] = contributor or []
        self.suspectEntity: list['SuspectEntity'] = suspectEntity or []
        self.subjectMedicalHistory: list['Reference'] = subjectMedicalHistory or []
        self.referenceDocument: list['Reference'] = referenceDocument or []
        self.study: list['Reference'] = study or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdverseEvent":
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