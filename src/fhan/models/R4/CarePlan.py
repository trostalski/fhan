"""
Generated class for CarePlan. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Detail(ModelBase):
    """ A simple summary of a planned activity suitable for a general care plan system (e.g. form driven) that doesn't know about specific resources such as procedure etc.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str kind: Appointment | CommunicationRequest | DeviceRequest | MedicationRequest | NutritionOrder | Task | ServiceRequest | VisionPrescription
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param 'CodeableConcept' code: Detail type of activity
    :param list['CodeableConcept'] reasonCode: Why activity should be done or why activity was prohibited
    :param list['Reference'] reasonReference: Why activity is needed
    :param list['Reference'] goal: Goals this activity relates to
    :param str status: not-started | scheduled | in-progress | on-hold | completed | cancelled | stopped | unknown | entered-in-error
    :param 'CodeableConcept' statusReason: Reason for current status
    :param bool doNotPerform: If true, activity is prohibiting action
    :param 'Timing' scheduledTiming: When activity is to occur
    :param 'Period' scheduledPeriod: When activity is to occur
    :param str scheduledString: When activity is to occur
    :param 'Reference' location: Where it should happen
    :param list['Reference'] performer: Who will be responsible?
    :param 'CodeableConcept' productCodeableConcept: What is to be administered/supplied
    :param 'Reference' productReference: What is to be administered/supplied
    :param 'Quantity' dailyAmount: How to consume/day?
    :param 'Quantity' quantity: How much to administer/supply/consume
    :param str description: Extra info describing activity to perform
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  kind: str = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  code: 'CodeableConcept' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  goal: list['Reference'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  doNotPerform: bool = None,  scheduledTiming: 'Timing' = None,  scheduledPeriod: 'Period' = None,  scheduledString: str = None,  location: 'Reference' = None,  performer: list['Reference'] = None,  productCodeableConcept: 'CodeableConcept' = None,  productReference: 'Reference' = None,  dailyAmount: 'Quantity' = None,  quantity: 'Quantity' = None,  description: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.kind: str = kind 
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.code: 'CodeableConcept' = code 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.goal: list['Reference'] = goal or []
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.doNotPerform: bool = doNotPerform 
        self.scheduledTiming: 'Timing' = scheduledTiming 
        self.scheduledPeriod: 'Period' = scheduledPeriod 
        self.scheduledString: str = scheduledString 
        self.location: 'Reference' = location 
        self.performer: list['Reference'] = performer or []
        self.productCodeableConcept: 'CodeableConcept' = productCodeableConcept 
        self.productReference: 'Reference' = productReference 
        self.dailyAmount: 'Quantity' = dailyAmount 
        self.quantity: 'Quantity' = quantity 
        self.description: str = description 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Detail":
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


  
    
    

class Activity(ModelBase):
    """ Identifies a planned action to occur as part of the plan.  For example, a medication to be used, lab tests to perform, self-monitoring, education, etc.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['CodeableConcept'] outcomeCodeableConcept: Results of the activity
    :param list['Reference'] outcomeReference: Appointment, Encounter, Procedure, etc.
    :param list['Annotation'] progress: Comments about the activity status/progress
    :param 'Reference' reference: Activity details defined in specific resource
    :param 'Detail' detail: In-line definition of activity
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  outcomeCodeableConcept: list['CodeableConcept'] = None,  outcomeReference: list['Reference'] = None,  progress: list['Annotation'] = None,  reference: 'Reference' = None,  detail: 'Detail' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.outcomeCodeableConcept: list['CodeableConcept'] = outcomeCodeableConcept or []
        self.outcomeReference: list['Reference'] = outcomeReference or []
        self.progress: list['Annotation'] = progress or []
        self.reference: 'Reference' = reference 
        self.detail: 'Detail' = detail 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Activity":
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


class CarePlan(DomainResource):
    """ Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Ids for this plan
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param list['Reference'] basedOn: Fulfills CarePlan
    :param list['Reference'] replaces: CarePlan replaced by this CarePlan
    :param list['Reference'] partOf: Part of referenced CarePlan
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | order | option
    :param list['CodeableConcept'] category: Type of plan
    :param str title: Human-friendly name for the care plan
    :param str description: Summary of nature of plan
    :param 'Reference' subject: Who the care plan is for
    :param 'Reference' encounter: Encounter created as part of
    :param 'Period' period: Time period plan covers
    :param str created: Date record was first recorded
    :param 'Reference' author: Who is the designated responsible party
    :param list['Reference'] contributor: Who provided the content of the care plan
    :param list['Reference'] careTeam: Who's involved in plan?
    :param list['Reference'] addresses: Health issues this plan addresses
    :param list['Reference'] supportingInfo: Information considered as part of plan
    :param list['Reference'] goal: Desired outcome of plan
    :param list['Activity'] activity: Action to occur as part of plan
    :param list['Annotation'] note: Comments about the plan
    """
    def __init__(self, resourceType: str = "CarePlan",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  replaces: list['Reference'] = None,  partOf: list['Reference'] = None,  status: str = None,  intent: str = None,  category: list['CodeableConcept'] = None,  title: str = None,  description: str = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  period: 'Period' = None,  created: str = None,  author: 'Reference' = None,  contributor: list['Reference'] = None,  careTeam: list['Reference'] = None,  addresses: list['Reference'] = None,  supportingInfo: list['Reference'] = None,  goal: list['Reference'] = None,  activity: list['Activity'] = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "CarePlan"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.basedOn: list['Reference'] = basedOn or []
        self.replaces: list['Reference'] = replaces or []
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.intent: str = intent 
        self.category: list['CodeableConcept'] = category or []
        self.title: str = title 
        self.description: str = description 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.period: 'Period' = period 
        self.created: str = created 
        self.author: 'Reference' = author 
        self.contributor: list['Reference'] = contributor or []
        self.careTeam: list['Reference'] = careTeam or []
        self.addresses: list['Reference'] = addresses or []
        self.supportingInfo: list['Reference'] = supportingInfo or []
        self.goal: list['Reference'] = goal or []
        self.activity: list['Activity'] = activity or []
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "CarePlan":
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