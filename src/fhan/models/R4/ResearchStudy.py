"""
Generated class for ResearchStudy. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
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


    
    

class Arm(BaseModel):
    """ Describes an expected sequence of events for one of the participants of a study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out, follow-up.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for study arm
    :param 'CodeableConcept' type: Categorization of study arm
    :param str description: Short explanation of study path
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  name: str = None,  type: 'CodeableConcept' = None,  description: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.type: 'CodeableConcept' = type 
        self.description: str = description 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Arm":
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


    
    

class Objective(BaseModel):
    """ A goal that the study is aiming to achieve in terms of a scientific question to be answered by the analysis of data collected during the study.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for the objective
    :param 'CodeableConcept' type: primary | secondary | exploratory
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  name: str = None,  type: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.type: 'CodeableConcept' = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Objective":
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


class ResearchStudy(DomainResource):
    """ A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge.  This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional and investigative techniques.  A ResearchStudy involves the gathering of information about human or animal subjects.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Business Identifier for study
    :param str title: Name for this study
    :param 'Reference' protocol: Steps followed in executing study
    :param 'Reference' partOf: Part of larger study
    :param str status: active | administratively-completed | approved | closed-to-accrual | closed-to-accrual-and-intervention | completed | disapproved | in-review | temporarily-closed-to-accrual | temporarily-closed-to-accrual-and-intervention | withdrawn
    :param 'CodeableConcept' primaryPurposeType: treatment | prevention | diagnostic | supportive-care | screening | health-services-research | basic-science | device-feasibility
    :param 'CodeableConcept' phase: n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | phase-2-phase-3 | phase-3 | phase-4
    :param 'CodeableConcept' category: Classifications for the study
    :param 'CodeableConcept' focus: Drugs, devices, etc. under study
    :param 'CodeableConcept' condition: Condition being studied
    :param 'ContactDetail' contact: Contact details for the study
    :param 'RelatedArtifact' relatedArtifact: References and dependencies
    :param 'CodeableConcept' keyword: Used to search for the study
    :param 'CodeableConcept' location: Geographic region(s) for study
    :param str description: What this is study doing
    :param 'Reference' enrollment: Inclusion & exclusion criteria
    :param 'Period' period: When the study began and ended
    :param 'Reference' sponsor: Organization that initiates and is legally responsible for the study
    :param 'Reference' principalInvestigator: Researcher who oversees multiple aspects of the study
    :param 'Reference' site: Facility where study activities are conducted
    :param 'CodeableConcept' reasonStopped: accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-study-progress | temporarily-closed-per-study-design
    :param 'Annotation' note: Comments made about the study
    :param 'Arm' arm: Defined path through the study for a subject
    :param 'Objective' objective: A goal for the study
    """
    def __init__(self, resourceType: str = "ResearchStudy",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  title: str = None,  protocol: 'Reference' = None,  partOf: 'Reference' = None,  status: str = None,  primaryPurposeType: 'CodeableConcept' = None,  phase: 'CodeableConcept' = None,  category: 'CodeableConcept' = None,  focus: 'CodeableConcept' = None,  condition: 'CodeableConcept' = None,  contact: 'ContactDetail' = None,  relatedArtifact: 'RelatedArtifact' = None,  keyword: 'CodeableConcept' = None,  location: 'CodeableConcept' = None,  description: str = None,  enrollment: 'Reference' = None,  period: 'Period' = None,  sponsor: 'Reference' = None,  principalInvestigator: 'Reference' = None,  site: 'Reference' = None,  reasonStopped: 'CodeableConcept' = None,  note: 'Annotation' = None,  arm: 'Arm' = None,  objective: 'Objective' = None, ):
        self.resourceType: str = resourceType or "ResearchStudy"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.title: str = title 
        self.protocol: list['Reference'] = protocol or []
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.primaryPurposeType: 'CodeableConcept' = primaryPurposeType 
        self.phase: 'CodeableConcept' = phase 
        self.category: list['CodeableConcept'] = category or []
        self.focus: list['CodeableConcept'] = focus or []
        self.condition: list['CodeableConcept'] = condition or []
        self.contact: list['ContactDetail'] = contact or []
        self.relatedArtifact: list['RelatedArtifact'] = relatedArtifact or []
        self.keyword: list['CodeableConcept'] = keyword or []
        self.location: list['CodeableConcept'] = location or []
        self.description: str = description 
        self.enrollment: list['Reference'] = enrollment or []
        self.period: 'Period' = period 
        self.sponsor: 'Reference' = sponsor 
        self.principalInvestigator: 'Reference' = principalInvestigator 
        self.site: list['Reference'] = site or []
        self.reasonStopped: 'CodeableConcept' = reasonStopped 
        self.note: list['Annotation'] = note or []
        self.arm: list['Arm'] = arm or []
        self.objective: list['Objective'] = objective or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
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