"""
Generated class for ClinicalImpression. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class Investigation(BaseModel):
    """ One or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomes.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: A name/code for the set
    :param 'Reference' item: Record of a specific investigation
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  code: 'CodeableConcept' = None,  item: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.item: list['Reference'] = item or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Investigation":
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


    
    

class Finding(BaseModel):
    """ Specific findings or diagnoses that were considered likely or relevant to ongoing treatment.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' itemCodeableConcept: What was found
    :param 'Reference' itemReference: What was found
    :param str basis: Which investigations support finding
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  itemCodeableConcept: 'CodeableConcept' = None,  itemReference: 'Reference' = None,  basis: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemCodeableConcept: 'CodeableConcept' = itemCodeableConcept 
        self.itemReference: 'Reference' = itemReference 
        self.basis: str = basis 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Finding":
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


class ClinicalImpression(DomainResource):
    """ A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient's condition. Assessments are often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the recording of assessment tools such as Apgar score.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Business identifier
    :param str status: in-progress | completed | entered-in-error
    :param 'CodeableConcept' statusReason: Reason for current status
    :param 'CodeableConcept' code: Kind of assessment performed
    :param str description: Why/how the assessment was performed
    :param 'Reference' subject: Patient or group assessed
    :param 'Reference' encounter: Encounter created as part of
    :param str effectiveDateTime: Time of assessment
    :param 'Period' effectivePeriod: Time of assessment
    :param str date: When the assessment was documented
    :param 'Reference' assessor: The clinician performing the assessment
    :param 'Reference' previous: Reference to last assessment
    :param 'Reference' problem: Relevant impressions of patient state
    :param 'Investigation' investigation: One or more sets of investigations (signs, symptoms, etc.)
    :param str protocol: Clinical Protocol followed
    :param str summary: Summary of the assessment
    :param 'Finding' finding: Possible or likely findings and diagnoses
    :param 'CodeableConcept' prognosisCodeableConcept: Estimate of likely outcome
    :param 'Reference' prognosisReference: RiskAssessment expressing likely outcome
    :param 'Reference' supportingInfo: Information supporting the clinical impression
    :param 'Annotation' note: Comments made about the ClinicalImpression
    """
    def __init__(self, resourceType: str = "ClinicalImpression",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  description: str = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  effectiveDateTime: str = None,  effectivePeriod: 'Period' = None,  date: str = None,  assessor: 'Reference' = None,  previous: 'Reference' = None,  problem: 'Reference' = None,  investigation: 'Investigation' = None,  protocol: str = None,  summary: str = None,  finding: 'Finding' = None,  prognosisCodeableConcept: 'CodeableConcept' = None,  prognosisReference: 'Reference' = None,  supportingInfo: 'Reference' = None,  note: 'Annotation' = None, ):
        self.resourceType: str = resourceType or "ClinicalImpression"
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
        self.statusReason: 'CodeableConcept' = statusReason 
        self.code: 'CodeableConcept' = code 
        self.description: str = description 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.effectiveDateTime: str = effectiveDateTime 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.date: str = date 
        self.assessor: 'Reference' = assessor 
        self.previous: 'Reference' = previous 
        self.problem: list['Reference'] = problem or []
        self.investigation: list['Investigation'] = investigation or []
        self.protocol: list[str] = protocol or []
        self.summary: str = summary 
        self.finding: list['Finding'] = finding or []
        self.prognosisCodeableConcept: list['CodeableConcept'] = prognosisCodeableConcept or []
        self.prognosisReference: list['Reference'] = prognosisReference or []
        self.supportingInfo: list['Reference'] = supportingInfo or []
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalImpression":
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