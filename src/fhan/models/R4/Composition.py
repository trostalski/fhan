"""
Generated class for Composition. 
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


    
    

class Attester(ModelBase):
    """ A participant who has attested to the accuracy of the composition/document.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: personal | professional | legal | official
    :param str time: When the composition was attested
    :param 'Reference' party: Who attested the composition
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  mode: str = None,  time: str = None,  party: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.mode: str = mode 
        self.time: str = time 
        self.party: 'Reference' = party 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Attester":
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


    
    

class RelatesTo(ModelBase):
    """ Relationships that this composition has with other compositions or documents that already exist.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: replaces | transforms | signs | appends
    :param 'Identifier' targetIdentifier: Target of the relationship
    :param 'Reference' targetReference: Target of the relationship
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: str = None,  targetIdentifier: 'Identifier' = None,  targetReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: str = code 
        self.targetIdentifier: 'Identifier' = targetIdentifier 
        self.targetReference: 'Reference' = targetReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RelatesTo":
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


    
    

class Event(ModelBase):
    """ The clinical service, such as a colonoscopy or an appendectomy, being documented.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['CodeableConcept'] code: Code(s) that apply to the event being documented
    :param 'Period' period: The period covered by the documentation
    :param list['Reference'] detail: The event(s) being documented
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: list['CodeableConcept'] = None,  period: 'Period' = None,  detail: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: list['CodeableConcept'] = code or []
        self.period: 'Period' = period 
        self.detail: list['Reference'] = detail or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Event":
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


    
    

class Section(ModelBase):
    """ The root of the sections that make up the composition.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for section (e.g. for ToC)
    :param 'CodeableConcept' code: Classification of section (recommended)
    :param list['Reference'] author: Who and/or what authored the section
    :param 'Reference' focus: Who/what the section is about, when it is not about the subject of composition
    :param 'Narrative' text: Text summary of the section, for human interpretation
    :param str mode: working | snapshot | changes
    :param 'CodeableConcept' orderedBy: Order of section entries
    :param list['Reference'] entry: A reference to data that supports this section
    :param 'CodeableConcept' emptyReason: Why the section is empty
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  title: str = None,  code: 'CodeableConcept' = None,  author: list['Reference'] = None,  focus: 'Reference' = None,  text: 'Narrative' = None,  mode: str = None,  orderedBy: 'CodeableConcept' = None,  entry: list['Reference'] = None,  emptyReason: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.title: str = title 
        self.code: 'CodeableConcept' = code 
        self.author: list['Reference'] = author or []
        self.focus: 'Reference' = focus 
        self.text: 'Narrative' = text 
        self.mode: str = mode 
        self.orderedBy: 'CodeableConcept' = orderedBy 
        self.entry: list['Reference'] = entry or []
        self.emptyReason: 'CodeableConcept' = emptyReason 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Section":
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


class Composition(DomainResource):
    """ A set of healthcare-related information that is assembled together into a single logical package that provides a single coherent statement of meaning, establishes its own context and that has clinical attestation with regard to who is making the statement. A Composition defines the structure and narrative content necessary for a document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Version-independent identifier for the Composition
    :param str status: preliminary | final | amended | entered-in-error
    :param 'CodeableConcept' type: Kind of composition (LOINC if possible)
    :param list['CodeableConcept'] category: Categorization of Composition
    :param 'Reference' subject: Who and/or what the composition is about
    :param 'Reference' encounter: Context of the Composition
    :param str date: Composition editing time
    :param list['Reference'] author: Who and/or what authored the composition
    :param str title: Human Readable name/title
    :param str confidentiality: As defined by affinity domain
    :param list['Attester'] attester: Attests to accuracy of composition
    :param 'Reference' custodian: Organization which maintains the composition
    :param list['RelatesTo'] relatesTo: Relationships to other compositions/documents
    :param list['Event'] event: The clinical service(s) being documented
    :param list['Section'] section: Composition is broken into sections
    """
    def __init__(self, resourceType: str = "Composition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  status: str = None,  type: 'CodeableConcept' = None,  category: list['CodeableConcept'] = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  date: str = None,  author: list['Reference'] = None,  title: str = None,  confidentiality: str = None,  attester: list['Attester'] = None,  custodian: 'Reference' = None,  relatesTo: list['RelatesTo'] = None,  event: list['Event'] = None,  section: list['Section'] = None, ):
        self.resourceType: str = resourceType or "Composition"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.status: str = status 
        self.type: 'CodeableConcept' = type 
        self.category: list['CodeableConcept'] = category or []
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.date: str = date 
        self.author: list['Reference'] = author or []
        self.title: str = title 
        self.confidentiality: str = confidentiality 
        self.attester: list['Attester'] = attester or []
        self.custodian: 'Reference' = custodian 
        self.relatesTo: list['RelatesTo'] = relatesTo or []
        self.event: list['Event'] = event or []
        self.section: list['Section'] = section or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
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