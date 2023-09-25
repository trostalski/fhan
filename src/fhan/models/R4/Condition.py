"""
Generated class for Condition. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Age import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Stage(ModelBase):
    """ Clinical stage or grade of a condition. May include formal severity assessments.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' summary: Simple summary (disease specific)
    :param list['Reference'] assessment: Formal record of assessment
    :param 'CodeableConcept' type: Kind of staging
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  summary: 'CodeableConcept' = None,  assessment: list['Reference'] = None,  type: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.summary: 'CodeableConcept' = summary 
        self.assessment: list['Reference'] = assessment or []
        self.type: 'CodeableConcept' = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Stage":
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


    
    

class Evidence(ModelBase):
    """ Supporting evidence / manifestations that are the basis of the Condition's verification status, such as evidence that confirmed or refuted the condition.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['CodeableConcept'] code: Manifestation/symptom
    :param list['Reference'] detail: Supporting information found elsewhere
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: list['CodeableConcept'] = None,  detail: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: list['CodeableConcept'] = code or []
        self.detail: list['Reference'] = detail or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
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


class Condition(DomainResource):
    """ A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Ids for this condition
    :param 'CodeableConcept' clinicalStatus: active | recurrence | relapse | inactive | remission | resolved
    :param 'CodeableConcept' verificationStatus: unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
    :param list['CodeableConcept'] category: problem-list-item | encounter-diagnosis
    :param 'CodeableConcept' severity: Subjective severity of condition
    :param 'CodeableConcept' code: Identification of the condition, problem or diagnosis
    :param list['CodeableConcept'] bodySite: Anatomical location, if relevant
    :param 'Reference' subject: Who has the condition?
    :param 'Reference' encounter: Encounter created as part of
    :param str onsetDateTime: Estimated or actual date,  date-time, or age
    :param 'Age' onsetAge: Estimated or actual date,  date-time, or age
    :param 'Period' onsetPeriod: Estimated or actual date,  date-time, or age
    :param 'Range' onsetRange: Estimated or actual date,  date-time, or age
    :param str onsetString: Estimated or actual date,  date-time, or age
    :param str abatementDateTime: When in resolution/remission
    :param 'Age' abatementAge: When in resolution/remission
    :param 'Period' abatementPeriod: When in resolution/remission
    :param 'Range' abatementRange: When in resolution/remission
    :param str abatementString: When in resolution/remission
    :param str recordedDate: Date record was first recorded
    :param 'Reference' recorder: Who recorded the condition
    :param 'Reference' asserter: Person who asserts this condition
    :param list['Stage'] stage: Stage/grade, usually assessed formally
    :param list['Evidence'] evidence: Supporting evidence
    :param list['Annotation'] note: Additional information about the Condition
    """
    def __init__(self, resourceType: str = "Condition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  clinicalStatus: 'CodeableConcept' = None,  verificationStatus: 'CodeableConcept' = None,  category: list['CodeableConcept'] = None,  severity: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  bodySite: list['CodeableConcept'] = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  onsetDateTime: str = None,  onsetAge: 'Age' = None,  onsetPeriod: 'Period' = None,  onsetRange: 'Range' = None,  onsetString: str = None,  abatementDateTime: str = None,  abatementAge: 'Age' = None,  abatementPeriod: 'Period' = None,  abatementRange: 'Range' = None,  abatementString: str = None,  recordedDate: str = None,  recorder: 'Reference' = None,  asserter: 'Reference' = None,  stage: list['Stage'] = None,  evidence: list['Evidence'] = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "Condition"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.clinicalStatus: 'CodeableConcept' = clinicalStatus 
        self.verificationStatus: 'CodeableConcept' = verificationStatus 
        self.category: list['CodeableConcept'] = category or []
        self.severity: 'CodeableConcept' = severity 
        self.code: 'CodeableConcept' = code 
        self.bodySite: list['CodeableConcept'] = bodySite or []
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.onsetDateTime: str = onsetDateTime 
        self.onsetAge: 'Age' = onsetAge 
        self.onsetPeriod: 'Period' = onsetPeriod 
        self.onsetRange: 'Range' = onsetRange 
        self.onsetString: str = onsetString 
        self.abatementDateTime: str = abatementDateTime 
        self.abatementAge: 'Age' = abatementAge 
        self.abatementPeriod: 'Period' = abatementPeriod 
        self.abatementRange: 'Range' = abatementRange 
        self.abatementString: str = abatementString 
        self.recordedDate: str = recordedDate 
        self.recorder: 'Reference' = recorder 
        self.asserter: 'Reference' = asserter 
        self.stage: list['Stage'] = stage or []
        self.evidence: list['Evidence'] = evidence or []
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Condition":
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