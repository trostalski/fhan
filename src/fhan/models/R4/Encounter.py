"""
Generated class for Encounter. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class StatusHistory(ModelBase):
    """ The status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store them.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    :param 'Period' period: The time that the episode was in the specified status
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


    
    

class ClassHistory(ModelBase):
    """ The class history permits the tracking of the encounters transitions without needing to go  through the resource history.  This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatient.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Coding' _class: inpatient | outpatient | ambulatory | emergency +
    :param 'Period' period: The time that the episode was in the specified class
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  _class: 'Coding' = None,  period: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self._class: 'Coding' = _class 
        self.period: 'Period' = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClassHistory":
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


    
    

class Participant(ModelBase):
    """ The list of people responsible for providing the service.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['CodeableConcept'] type: Role of participant in encounter
    :param 'Period' period: Period of time during the encounter that the participant participated
    :param 'Reference' individual: Persons involved in the encounter other than the patient
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: list['CodeableConcept'] = None,  period: 'Period' = None,  individual: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: list['CodeableConcept'] = type or []
        self.period: 'Period' = period 
        self.individual: 'Reference' = individual 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Participant":
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
    """ The list of diagnosis relevant to this encounter.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' condition: The diagnosis or procedure relevant to the encounter
    :param 'CodeableConcept' use: Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)
    :param int rank: Ranking of the diagnosis (for each role type)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  condition: 'Reference' = None,  use: 'CodeableConcept' = None,  rank: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.condition: 'Reference' = condition 
        self.use: 'CodeableConcept' = use 
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


    
    

class Hospitalization(ModelBase):
    """ Details about the admission to a healthcare service.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' preAdmissionIdentifier: Pre-admission identifier
    :param 'Reference' origin: The location/organization from which the patient came before admission
    :param 'CodeableConcept' admitSource: From where patient was admitted (physician referral, transfer)
    :param 'CodeableConcept' reAdmission: The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
    :param list['CodeableConcept'] dietPreference: Diet preferences reported by the patient
    :param list['CodeableConcept'] specialCourtesy: Special courtesies (VIP, board member)
    :param list['CodeableConcept'] specialArrangement: Wheelchair, translator, stretcher, etc.
    :param 'Reference' destination: Location/organization to which the patient is discharged
    :param 'CodeableConcept' dischargeDisposition: Category or kind of location after discharge
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  preAdmissionIdentifier: 'Identifier' = None,  origin: 'Reference' = None,  admitSource: 'CodeableConcept' = None,  reAdmission: 'CodeableConcept' = None,  dietPreference: list['CodeableConcept'] = None,  specialCourtesy: list['CodeableConcept'] = None,  specialArrangement: list['CodeableConcept'] = None,  destination: 'Reference' = None,  dischargeDisposition: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.preAdmissionIdentifier: 'Identifier' = preAdmissionIdentifier 
        self.origin: 'Reference' = origin 
        self.admitSource: 'CodeableConcept' = admitSource 
        self.reAdmission: 'CodeableConcept' = reAdmission 
        self.dietPreference: list['CodeableConcept'] = dietPreference or []
        self.specialCourtesy: list['CodeableConcept'] = specialCourtesy or []
        self.specialArrangement: list['CodeableConcept'] = specialArrangement or []
        self.destination: 'Reference' = destination 
        self.dischargeDisposition: 'CodeableConcept' = dischargeDisposition 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Hospitalization":
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


    
    

class Location(ModelBase):
    """ List of locations where  the patient has been during this encounter.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' location: Location the encounter takes place
    :param str status: planned | active | reserved | completed
    :param 'CodeableConcept' physicalType: The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
    :param 'Period' period: Time period during which the patient was present at the location
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  location: 'Reference' = None,  status: str = None,  physicalType: 'CodeableConcept' = None,  period: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.location: 'Reference' = location 
        self.status: str = status 
        self.physicalType: 'CodeableConcept' = physicalType 
        self.period: 'Period' = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Location":
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


class Encounter(DomainResource):
    """ An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Identifier(s) by which this encounter is known
    :param str status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    :param list['StatusHistory'] statusHistory: List of past encounter statuses
    :param 'Coding' _class: Classification of patient encounter
    :param list['ClassHistory'] classHistory: List of past encounter classes
    :param list['CodeableConcept'] type: Specific type of encounter
    :param 'CodeableConcept' serviceType: Specific type of service
    :param 'CodeableConcept' priority: Indicates the urgency of the encounter
    :param 'Reference' subject: The patient or group present at the encounter
    :param list['Reference'] episodeOfCare: Episode(s) of care that this encounter should be recorded against
    :param list['Reference'] basedOn: The ServiceRequest that initiated this encounter
    :param list['Participant'] participant: List of participants involved in the encounter
    :param list['Reference'] appointment: The appointment that scheduled this encounter
    :param 'Period' period: The start and end time of the encounter
    :param 'Duration' length: Quantity of time the encounter lasted (less time absent)
    :param list['CodeableConcept'] reasonCode: Coded reason the encounter takes place
    :param list['Reference'] reasonReference: Reason the encounter takes place (reference)
    :param list['Diagnosis'] diagnosis: The list of diagnosis relevant to this encounter
    :param list['Reference'] account: The set of accounts that may be used for billing for this Encounter
    :param 'Hospitalization' hospitalization: Details about the admission to a healthcare service
    :param list['Location'] location: List of locations where the patient has been
    :param 'Reference' serviceProvider: The organization (facility) responsible for this encounter
    :param 'Reference' partOf: Another Encounter this encounter is part of
    """
    def __init__(self, resourceType: str = "Encounter",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  statusHistory: list['StatusHistory'] = None,  _class: 'Coding' = None,  classHistory: list['ClassHistory'] = None,  type: list['CodeableConcept'] = None,  serviceType: 'CodeableConcept' = None,  priority: 'CodeableConcept' = None,  subject: 'Reference' = None,  episodeOfCare: list['Reference'] = None,  basedOn: list['Reference'] = None,  participant: list['Participant'] = None,  appointment: list['Reference'] = None,  period: 'Period' = None,  length: 'Duration' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  diagnosis: list['Diagnosis'] = None,  account: list['Reference'] = None,  hospitalization: 'Hospitalization' = None,  location: list['Location'] = None,  serviceProvider: 'Reference' = None,  partOf: 'Reference' = None, ):
        self.resourceType: str = resourceType or "Encounter"
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
        self._class: 'Coding' = _class 
        self.classHistory: list['ClassHistory'] = classHistory or []
        self.type: list['CodeableConcept'] = type or []
        self.serviceType: 'CodeableConcept' = serviceType 
        self.priority: 'CodeableConcept' = priority 
        self.subject: 'Reference' = subject 
        self.episodeOfCare: list['Reference'] = episodeOfCare or []
        self.basedOn: list['Reference'] = basedOn or []
        self.participant: list['Participant'] = participant or []
        self.appointment: list['Reference'] = appointment or []
        self.period: 'Period' = period 
        self.length: 'Duration' = length 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.diagnosis: list['Diagnosis'] = diagnosis or []
        self.account: list['Reference'] = account or []
        self.hospitalization: 'Hospitalization' = hospitalization 
        self.location: list['Location'] = location or []
        self.serviceProvider: 'Reference' = serviceProvider 
        self.partOf: 'Reference' = partOf 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Encounter":
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