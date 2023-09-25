"""
Generated class for EpisodeOfCare. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class StatusHistory(ModelBase):
    """ The history of statuses that the EpisodeOfCare has been through (without requiring processing the history of the resource).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: planned | waitlist | active | onhold | finished | cancelled | entered-in-error
    :param 'Period' period: Duration the EpisodeOfCare was in the specified status
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  status: str = None,  period: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.status: str = status 
        self.period: 'Period' = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StatusHistory":
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


    
    

class Diagnosis(ModelBase):
    """ The list of diagnosis relevant to this episode of care.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' condition: Conditions/problems/diagnoses this episode of care is for
    :param 'CodeableConcept' role: Role that this diagnosis has within the episode of care (e.g. admission, billing, discharge …)
    :param int rank: Ranking of the diagnosis (for each role type)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  condition: 'Reference' = None,  role: 'CodeableConcept' = None,  rank: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.condition: 'Reference' = condition 
        self.role: 'CodeableConcept' = role 
        self.rank: int = rank 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Diagnosis":
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


class EpisodeOfCare(DomainResource):
    """ An association between a patient and an organization / healthcare provider(s) during which time encounters may occur. The managing organization assumes a level of responsibility for the patient during this time.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier(s) relevant for this EpisodeOfCare
    :param str status: planned | waitlist | active | onhold | finished | cancelled | entered-in-error
    :param list['StatusHistory'] statusHistory: Past list of status codes (the current status may be included to cover the start date of the status)
    :param list['CodeableConcept'] type: Type/class  - e.g. specialist referral, disease management
    :param list['Diagnosis'] diagnosis: The list of diagnosis relevant to this episode of care
    :param 'Reference' patient: The patient who is the focus of this episode of care
    :param 'Reference' managingOrganization: Organization that assumes care
    :param 'Period' period: Interval during responsibility is assumed
    :param list['Reference'] referralRequest: Originating Referral Request(s)
    :param 'Reference' careManager: Care manager/care coordinator for the patient
    :param list['Reference'] team: Other practitioners facilitating this episode of care
    :param list['Reference'] account: The set of accounts that may be used for billing for this EpisodeOfCare
    """
    def __init__(self, resourceType: str = "EpisodeOfCare",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  statusHistory: list['StatusHistory'] = None,  type: list['CodeableConcept'] = None,  diagnosis: list['Diagnosis'] = None,  patient: 'Reference' = None,  managingOrganization: 'Reference' = None,  period: 'Period' = None,  referralRequest: list['Reference'] = None,  careManager: 'Reference' = None,  team: list['Reference'] = None,  account: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "EpisodeOfCare"
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
        self.statusHistory: list['StatusHistory'] = statusHistory or []
        self.type: list['CodeableConcept'] = type or []
        self.diagnosis: list['Diagnosis'] = diagnosis or []
        self.patient: 'Reference' = patient 
        self.managingOrganization: 'Reference' = managingOrganization 
        self.period: 'Period' = period 
        self.referralRequest: list['Reference'] = referralRequest or []
        self.careManager: 'Reference' = careManager 
        self.team: list['Reference'] = team or []
        self.account: list['Reference'] = account or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EpisodeOfCare":
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