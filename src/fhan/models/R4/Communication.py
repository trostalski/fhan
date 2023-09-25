"""
Generated class for Communication. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Payload(ModelBase):
    """ Text, attachment(s), or resource(s) that was communicated to the recipient.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str contentString: Message part content
    :param 'Attachment' contentAttachment: Message part content
    :param 'Reference' contentReference: Message part content
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  contentString: str = None,  contentAttachment: 'Attachment' = None,  contentReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.contentString: str = contentString 
        self.contentAttachment: 'Attachment' = contentAttachment 
        self.contentReference: 'Reference' = contentReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Payload":
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


class Communication(DomainResource):
    """ An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency that was notified about a reportable condition.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param list['Reference'] basedOn: Request fulfilled by this communication
    :param list['Reference'] partOf: Part of this action
    :param list['Reference'] inResponseTo: Reply to
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param 'CodeableConcept' statusReason: Reason for current status
    :param list['CodeableConcept'] category: Message category
    :param str priority: routine | urgent | asap | stat
    :param list['CodeableConcept'] medium: A channel of communication
    :param 'Reference' subject: Focus of message
    :param 'CodeableConcept' topic: Description of the purpose/content
    :param list['Reference'] about: Resources that pertain to this communication
    :param 'Reference' encounter: Encounter created as part of
    :param str sent: When sent
    :param str received: When received
    :param list['Reference'] recipient: Message recipient
    :param 'Reference' sender: Message sender
    :param list['CodeableConcept'] reasonCode: Indication for message
    :param list['Reference'] reasonReference: Why was communication done?
    :param list['Payload'] payload: Message payload
    :param list['Annotation'] note: Comments made about the communication
    """
    def __init__(self, resourceType: str = "Communication",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  partOf: list['Reference'] = None,  inResponseTo: list['Reference'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  category: list['CodeableConcept'] = None,  priority: str = None,  medium: list['CodeableConcept'] = None,  subject: 'Reference' = None,  topic: 'CodeableConcept' = None,  about: list['Reference'] = None,  encounter: 'Reference' = None,  sent: str = None,  received: str = None,  recipient: list['Reference'] = None,  sender: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  payload: list['Payload'] = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "Communication"
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
        self.inResponseTo: list['Reference'] = inResponseTo or []
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.category: list['CodeableConcept'] = category or []
        self.priority: str = priority 
        self.medium: list['CodeableConcept'] = medium or []
        self.subject: 'Reference' = subject 
        self.topic: 'CodeableConcept' = topic 
        self.about: list['Reference'] = about or []
        self.encounter: 'Reference' = encounter 
        self.sent: str = sent 
        self.received: str = received 
        self.recipient: list['Reference'] = recipient or []
        self.sender: 'Reference' = sender 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.payload: list['Payload'] = payload or []
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Communication":
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