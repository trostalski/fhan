"""
Generated class for MedicationRequest. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class InitialFill(ModelBase):
    """ Indicates the quantity or duration for the first dispense of the medication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Quantity' quantity: First fill quantity
    :param 'Duration' duration: First fill duration
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  quantity: 'Quantity' = None,  duration: 'Duration' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.quantity: 'Quantity' = quantity 
        self.duration: 'Duration' = duration 
        

    @classmethod
    def from_dict(cls, data: dict) -> "InitialFill":
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


  
    
    

class DispenseRequest(ModelBase):
    """ Indicates the specific details for the dispense or medication supply part of a medication request (also known as a Medication Prescription or Medication Order).  Note that this information is not always sent with the order.  There may be in some settings (e.g. hospitals) institutional or system support for completing the dispense details in the pharmacy department.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'InitialFill' initialFill: First fill details
    :param 'Duration' dispenseInterval: Minimum period of time between dispenses
    :param 'Period' validityPeriod: Time period supply is authorized for
    :param int numberOfRepeatsAllowed: Number of refills authorized
    :param 'Quantity' quantity: Amount of medication to supply per dispense
    :param 'Duration' expectedSupplyDuration: Number of days supply per dispense
    :param 'Reference' performer: Intended dispenser
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  initialFill: 'InitialFill' = None,  dispenseInterval: 'Duration' = None,  validityPeriod: 'Period' = None,  numberOfRepeatsAllowed: int = None,  quantity: 'Quantity' = None,  expectedSupplyDuration: 'Duration' = None,  performer: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.initialFill: 'InitialFill' = initialFill 
        self.dispenseInterval: 'Duration' = dispenseInterval 
        self.validityPeriod: 'Period' = validityPeriod 
        self.numberOfRepeatsAllowed: int = numberOfRepeatsAllowed 
        self.quantity: 'Quantity' = quantity 
        self.expectedSupplyDuration: 'Duration' = expectedSupplyDuration 
        self.performer: 'Reference' = performer 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DispenseRequest":
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


    
    

class Substitution(ModelBase):
    """ Indicates whether or not substitution can or should be part of the dispense. In some cases, substitution must happen, in other cases substitution must not happen. This block explains the prescriber's intent. If nothing is specified substitution may be done.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool allowedBoolean: Whether substitution is allowed or not
    :param 'CodeableConcept' allowedCodeableConcept: Whether substitution is allowed or not
    :param 'CodeableConcept' reason: Why should (not) substitution be made
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  allowedBoolean: bool = None,  allowedCodeableConcept: 'CodeableConcept' = None,  reason: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.allowedBoolean: bool = allowedBoolean 
        self.allowedCodeableConcept: 'CodeableConcept' = allowedCodeableConcept 
        self.reason: 'CodeableConcept' = reason 
        

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


class MedicationRequest(DomainResource):
    """ An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External ids for this request
    :param str status: active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown
    :param 'CodeableConcept' statusReason: Reason for current status
    :param str intent: proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
    :param list['CodeableConcept'] category: Type of medication usage
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if request is prohibiting action
    :param bool reportedBoolean: Reported rather than primary record
    :param 'Reference' reportedReference: Reported rather than primary record
    :param 'CodeableConcept' medicationCodeableConcept: Medication to be taken
    :param 'Reference' medicationReference: Medication to be taken
    :param 'Reference' subject: Who or group medication request is for
    :param 'Reference' encounter: Encounter created as part of encounter/admission/stay
    :param list['Reference'] supportingInformation: Information to support ordering of the medication
    :param str authoredOn: When request was initially authored
    :param 'Reference' requester: Who/What requested the Request
    :param 'Reference' performer: Intended performer of administration
    :param 'CodeableConcept' performerType: Desired kind of performer of the medication administration
    :param 'Reference' recorder: Person who entered the request
    :param list['CodeableConcept'] reasonCode: Reason or indication for ordering or not ordering the medication
    :param list['Reference'] reasonReference: Condition or observation that supports why the prescription is being written
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param list['Reference'] basedOn: What request fulfills
    :param 'Identifier' groupIdentifier: Composite request this is part of
    :param 'CodeableConcept' courseOfTherapyType: Overall pattern of medication administration
    :param list['Reference'] insurance: Associated insurance coverage
    :param list['Annotation'] note: Information about the prescription
    :param list['Dosage'] dosageInstruction: How the medication should be taken
    :param 'DispenseRequest' dispenseRequest: Medication supply authorization
    :param 'Substitution' substitution: Any restrictions on medication substitution
    :param 'Reference' priorPrescription: An order/prescription that is being replaced
    :param list['Reference'] detectedIssue: Clinical Issue with action
    :param list['Reference'] eventHistory: A list of events of interest in the lifecycle
    """
    def __init__(self, resourceType: str = "MedicationRequest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  intent: str = None,  category: list['CodeableConcept'] = None,  priority: str = None,  doNotPerform: bool = None,  reportedBoolean: bool = None,  reportedReference: 'Reference' = None,  medicationCodeableConcept: 'CodeableConcept' = None,  medicationReference: 'Reference' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  supportingInformation: list['Reference'] = None,  authoredOn: str = None,  requester: 'Reference' = None,  performer: 'Reference' = None,  performerType: 'CodeableConcept' = None,  recorder: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  groupIdentifier: 'Identifier' = None,  courseOfTherapyType: 'CodeableConcept' = None,  insurance: list['Reference'] = None,  note: list['Annotation'] = None,  dosageInstruction: list['Dosage'] = None,  dispenseRequest: 'DispenseRequest' = None,  substitution: 'Substitution' = None,  priorPrescription: 'Reference' = None,  detectedIssue: list['Reference'] = None,  eventHistory: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "MedicationRequest"
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
        self.intent: str = intent 
        self.category: list['CodeableConcept'] = category or []
        self.priority: str = priority 
        self.doNotPerform: bool = doNotPerform 
        self.reportedBoolean: bool = reportedBoolean 
        self.reportedReference: 'Reference' = reportedReference 
        self.medicationCodeableConcept: 'CodeableConcept' = medicationCodeableConcept 
        self.medicationReference: 'Reference' = medicationReference 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.supportingInformation: list['Reference'] = supportingInformation or []
        self.authoredOn: str = authoredOn 
        self.requester: 'Reference' = requester 
        self.performer: 'Reference' = performer 
        self.performerType: 'CodeableConcept' = performerType 
        self.recorder: 'Reference' = recorder 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.basedOn: list['Reference'] = basedOn or []
        self.groupIdentifier: 'Identifier' = groupIdentifier 
        self.courseOfTherapyType: 'CodeableConcept' = courseOfTherapyType 
        self.insurance: list['Reference'] = insurance or []
        self.note: list['Annotation'] = note or []
        self.dosageInstruction: list['Dosage'] = dosageInstruction or []
        self.dispenseRequest: 'DispenseRequest' = dispenseRequest 
        self.substitution: 'Substitution' = substitution 
        self.priorPrescription: 'Reference' = priorPrescription 
        self.detectedIssue: list['Reference'] = detectedIssue or []
        self.eventHistory: list['Reference'] = eventHistory or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationRequest":
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