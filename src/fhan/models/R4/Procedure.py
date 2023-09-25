"""
Generated class for Procedure. 
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


    
    

class Performer(ModelBase):
    """ Limited to "real" people rather than equipment.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' function: Type of performance
    :param 'Reference' actor: The reference to the practitioner
    :param 'Reference' onBehalfOf: Organization the device or practitioner was acting for
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  function: 'CodeableConcept' = None,  actor: 'Reference' = None,  onBehalfOf: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.function: 'CodeableConcept' = function 
        self.actor: 'Reference' = actor 
        self.onBehalfOf: 'Reference' = onBehalfOf 
        

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


    
    

class FocalDevice(ModelBase):
    """ A device that is implanted, removed or otherwise manipulated (calibration, battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a focal portion of the Procedure.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' action: Kind of change to device
    :param 'Reference' manipulated: Device that was changed
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  action: 'CodeableConcept' = None,  manipulated: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.action: 'CodeableConcept' = action 
        self.manipulated: 'Reference' = manipulated 
        

    @classmethod
    def from_dict(cls, data: dict) -> "FocalDevice":
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


class Procedure(DomainResource):
    """ An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Identifiers for this procedure
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param list['Reference'] basedOn: A request for this procedure
    :param list['Reference'] partOf: Part of referenced event
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param 'CodeableConcept' statusReason: Reason for current status
    :param 'CodeableConcept' category: Classification of the procedure
    :param 'CodeableConcept' code: Identification of the procedure
    :param 'Reference' subject: Who the procedure was performed on
    :param 'Reference' encounter: Encounter created as part of
    :param str performedDateTime: When the procedure was performed
    :param 'Period' performedPeriod: When the procedure was performed
    :param str performedString: When the procedure was performed
    :param 'Age' performedAge: When the procedure was performed
    :param 'Range' performedRange: When the procedure was performed
    :param 'Reference' recorder: Who recorded the procedure
    :param 'Reference' asserter: Person who asserts this procedure
    :param list['Performer'] performer: The people who performed the procedure
    :param 'Reference' location: Where the procedure happened
    :param list['CodeableConcept'] reasonCode: Coded reason procedure performed
    :param list['Reference'] reasonReference: The justification that the procedure was performed
    :param list['CodeableConcept'] bodySite: Target body sites
    :param 'CodeableConcept' outcome: The result of procedure
    :param list['Reference'] report: Any report resulting from the procedure
    :param list['CodeableConcept'] complication: Complication following the procedure
    :param list['Reference'] complicationDetail: A condition that is a result of the procedure
    :param list['CodeableConcept'] followUp: Instructions for follow up
    :param list['Annotation'] note: Additional information about the procedure
    :param list['FocalDevice'] focalDevice: Manipulated, implanted, or removed device
    :param list['Reference'] usedReference: Items used during procedure
    :param list['CodeableConcept'] usedCode: Coded items used during the procedure
    """
    def __init__(self, resourceType: str = "Procedure",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  partOf: list['Reference'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  category: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  performedDateTime: str = None,  performedPeriod: 'Period' = None,  performedString: str = None,  performedAge: 'Age' = None,  performedRange: 'Range' = None,  recorder: 'Reference' = None,  asserter: 'Reference' = None,  performer: list['Performer'] = None,  location: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  bodySite: list['CodeableConcept'] = None,  outcome: 'CodeableConcept' = None,  report: list['Reference'] = None,  complication: list['CodeableConcept'] = None,  complicationDetail: list['Reference'] = None,  followUp: list['CodeableConcept'] = None,  note: list['Annotation'] = None,  focalDevice: list['FocalDevice'] = None,  usedReference: list['Reference'] = None,  usedCode: list['CodeableConcept'] = None, ):
        self.resourceType: str = resourceType or "Procedure"
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
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.category: 'CodeableConcept' = category 
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.performedDateTime: str = performedDateTime 
        self.performedPeriod: 'Period' = performedPeriod 
        self.performedString: str = performedString 
        self.performedAge: 'Age' = performedAge 
        self.performedRange: 'Range' = performedRange 
        self.recorder: 'Reference' = recorder 
        self.asserter: 'Reference' = asserter 
        self.performer: list['Performer'] = performer or []
        self.location: 'Reference' = location 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.bodySite: list['CodeableConcept'] = bodySite or []
        self.outcome: 'CodeableConcept' = outcome 
        self.report: list['Reference'] = report or []
        self.complication: list['CodeableConcept'] = complication or []
        self.complicationDetail: list['Reference'] = complicationDetail or []
        self.followUp: list['CodeableConcept'] = followUp or []
        self.note: list['Annotation'] = note or []
        self.focalDevice: list['FocalDevice'] = focalDevice or []
        self.usedReference: list['Reference'] = usedReference or []
        self.usedCode: list['CodeableConcept'] = usedCode or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Procedure":
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