"""
Generated class for Appointment. 
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


    
    

class Participant(ModelBase):
    """ List of participants involved in the appointment.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['CodeableConcept'] type: Role of participant in the appointment
    :param 'Reference' actor: Person, Location/HealthcareService or Device
    :param str required: required | optional | information-only
    :param str status: accepted | declined | tentative | needs-action
    :param 'Period' period: Participation period of the actor
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: list['CodeableConcept'] = None,  actor: 'Reference' = None,  required: str = None,  status: str = None,  period: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: list['CodeableConcept'] = type or []
        self.actor: 'Reference' = actor 
        self.required: str = required 
        self.status: str = status 
        self.period: 'Period' = period 
        

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


class Appointment(DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Ids for this item
    :param str status: proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist
    :param 'CodeableConcept' cancelationReason: The coded reason for the appointment being cancelled
    :param list['CodeableConcept'] serviceCategory: A broad categorization of the service that is to be performed during this appointment
    :param list['CodeableConcept'] serviceType: The specific service that is to be performed during this appointment
    :param list['CodeableConcept'] specialty: The specialty of a practitioner that would be required to perform the service requested in this appointment
    :param 'CodeableConcept' appointmentType: The style of appointment or patient that has been booked in the slot (not service type)
    :param list['CodeableConcept'] reasonCode: Coded reason this appointment is scheduled
    :param list['Reference'] reasonReference: Reason the appointment is to take place (resource)
    :param int priority: Used to make informed decisions if needing to re-prioritize
    :param str description: Shown on a subject line in a meeting request, or appointment list
    :param list['Reference'] supportingInformation: Additional information to support the appointment
    :param str start: When appointment is to take place
    :param str end: When appointment is to conclude
    :param int minutesDuration: Can be less than start/end (e.g. estimate)
    :param list['Reference'] slot: The slots that this appointment is filling
    :param str created: The date that this appointment was initially created
    :param str comment: Additional comments
    :param str patientInstruction: Detailed information and instructions for the patient
    :param list['Reference'] basedOn: The service request this appointment is allocated to assess
    :param list['Participant'] participant: Participants involved in appointment
    :param list['Period'] requestedPeriod: Potential date/time interval(s) requested to allocate the appointment within
    """
    def __init__(self, resourceType: str = "Appointment",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  cancelationReason: 'CodeableConcept' = None,  serviceCategory: list['CodeableConcept'] = None,  serviceType: list['CodeableConcept'] = None,  specialty: list['CodeableConcept'] = None,  appointmentType: 'CodeableConcept' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  priority: int = None,  description: str = None,  supportingInformation: list['Reference'] = None,  start: str = None,  end: str = None,  minutesDuration: int = None,  slot: list['Reference'] = None,  created: str = None,  comment: str = None,  patientInstruction: str = None,  basedOn: list['Reference'] = None,  participant: list['Participant'] = None,  requestedPeriod: list['Period'] = None, ):
        self.resourceType: str = resourceType or "Appointment"
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
        self.cancelationReason: 'CodeableConcept' = cancelationReason 
        self.serviceCategory: list['CodeableConcept'] = serviceCategory or []
        self.serviceType: list['CodeableConcept'] = serviceType or []
        self.specialty: list['CodeableConcept'] = specialty or []
        self.appointmentType: 'CodeableConcept' = appointmentType 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.priority: int = priority 
        self.description: str = description 
        self.supportingInformation: list['Reference'] = supportingInformation or []
        self.start: str = start 
        self.end: str = end 
        self.minutesDuration: int = minutesDuration 
        self.slot: list['Reference'] = slot or []
        self.created: str = created 
        self.comment: str = comment 
        self.patientInstruction: str = patientInstruction 
        self.basedOn: list['Reference'] = basedOn or []
        self.participant: list['Participant'] = participant or []
        self.requestedPeriod: list['Period'] = requestedPeriod or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
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