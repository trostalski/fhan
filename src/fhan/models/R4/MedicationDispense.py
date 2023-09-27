"""
Generated class for MedicationDispense. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class Performer(BaseModel):
    """ Indicates who or what performed the event.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' function: Who performed the dispense and what they did
    :param 'Reference' actor: Individual who was performing
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  function: 'CodeableConcept' = None,  actor: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.function: 'CodeableConcept' = function 
        self.actor: 'Reference' = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Performer":
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


    
    

class Substitution(BaseModel):
    """ Indicates whether or not substitution was made as part of the dispense.  In some cases, substitution will be expected but does not happen, in other cases substitution is not expected but does happen.  This block explains what substitution did or did not happen and why.  If nothing is specified, substitution was not done.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool wasSubstituted: Whether a substitution was or was not performed on the dispense
    :param 'CodeableConcept' type: Code signifying whether a different drug was dispensed from what was prescribed
    :param 'CodeableConcept' reason: Why was substitution made
    :param 'Reference' responsibleParty: Who is responsible for the substitution
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  wasSubstituted: bool = None,  type: 'CodeableConcept' = None,  reason: 'CodeableConcept' = None,  responsibleParty: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.wasSubstituted: bool = wasSubstituted 
        self.type: 'CodeableConcept' = type 
        self.reason: list['CodeableConcept'] = reason or []
        self.responsibleParty: list['Reference'] = responsibleParty or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Substitution":
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


class MedicationDispense(DomainResource):
    """ Indicates that a medication product is to be or has been dispensed for a named person/patient.  This includes a description of the medication product (supply) provided and the instructions for administering the medication.  The medication dispense is the result of a pharmacy system responding to a medication order.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: External identifier
    :param 'Reference' partOf: Event that dispense is part of
    :param str status: preparation | in-progress | cancelled | on-hold | completed | entered-in-error | stopped | declined | unknown
    :param 'CodeableConcept' statusReasonCodeableConcept: Why a dispense was not performed
    :param 'Reference' statusReasonReference: Why a dispense was not performed
    :param 'CodeableConcept' category: Type of medication dispense
    :param 'CodeableConcept' medicationCodeableConcept: What medication was supplied
    :param 'Reference' medicationReference: What medication was supplied
    :param 'Reference' subject: Who the dispense is for
    :param 'Reference' context: Encounter / Episode associated with event
    :param 'Reference' supportingInformation: Information that supports the dispensing of the medication
    :param 'Performer' performer: Who performed event
    :param 'Reference' location: Where the dispense occurred
    :param 'Reference' authorizingPrescription: Medication order that authorizes the dispense
    :param 'CodeableConcept' type: Trial fill, partial fill, emergency fill, etc.
    :param 'Quantity' quantity: Amount dispensed
    :param 'Quantity' daysSupply: Amount of medication expressed as a timing amount
    :param str whenPrepared: When product was packaged and reviewed
    :param str whenHandedOver: When product was given out
    :param 'Reference' destination: Where the medication was sent
    :param 'Reference' receiver: Who collected the medication
    :param 'Annotation' note: Information about the dispense
    :param 'Dosage' dosageInstruction: How the medication is to be used by the patient or administered by the caregiver
    :param 'Substitution' substitution: Whether a substitution was performed on the dispense
    :param 'Reference' detectedIssue: Clinical issue with action
    :param 'Reference' eventHistory: A list of relevant lifecycle events
    """
    def __init__(self, resourceType: str = "MedicationDispense",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  partOf: 'Reference' = None,  status: str = None,  statusReasonCodeableConcept: 'CodeableConcept' = None,  statusReasonReference: 'Reference' = None,  category: 'CodeableConcept' = None,  medicationCodeableConcept: 'CodeableConcept' = None,  medicationReference: 'Reference' = None,  subject: 'Reference' = None,  context: 'Reference' = None,  supportingInformation: 'Reference' = None,  performer: 'Performer' = None,  location: 'Reference' = None,  authorizingPrescription: 'Reference' = None,  type: 'CodeableConcept' = None,  quantity: 'Quantity' = None,  daysSupply: 'Quantity' = None,  whenPrepared: str = None,  whenHandedOver: str = None,  destination: 'Reference' = None,  receiver: 'Reference' = None,  note: 'Annotation' = None,  dosageInstruction: 'Dosage' = None,  substitution: 'Substitution' = None,  detectedIssue: 'Reference' = None,  eventHistory: 'Reference' = None, ):
        self.resourceType: str = resourceType or "MedicationDispense"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.statusReasonCodeableConcept: 'CodeableConcept' = statusReasonCodeableConcept 
        self.statusReasonReference: 'Reference' = statusReasonReference 
        self.category: 'CodeableConcept' = category 
        self.medicationCodeableConcept: 'CodeableConcept' = medicationCodeableConcept 
        self.medicationReference: 'Reference' = medicationReference 
        self.subject: 'Reference' = subject 
        self.context: 'Reference' = context 
        self.supportingInformation: list['Reference'] = supportingInformation or []
        self.performer: list['Performer'] = performer or []
        self.location: 'Reference' = location 
        self.authorizingPrescription: list['Reference'] = authorizingPrescription or []
        self.type: 'CodeableConcept' = type 
        self.quantity: 'Quantity' = quantity 
        self.daysSupply: 'Quantity' = daysSupply 
        self.whenPrepared: str = whenPrepared 
        self.whenHandedOver: str = whenHandedOver 
        self.destination: 'Reference' = destination 
        self.receiver: list['Reference'] = receiver or []
        self.note: list['Annotation'] = note or []
        self.dosageInstruction: list['Dosage'] = dosageInstruction or []
        self.substitution: 'Substitution' = substitution 
        self.detectedIssue: list['Reference'] = detectedIssue or []
        self.eventHistory: list['Reference'] = eventHistory or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationDispense":
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