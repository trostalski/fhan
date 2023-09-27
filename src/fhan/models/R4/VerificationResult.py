"""
Generated class for VerificationResult. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Resource import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class PrimarySource(BaseModel):
    """ Information about the primary source(s) involved in validation.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' who: Reference to the primary source
    :param 'CodeableConcept' type: Type of primary source (License Board; Primary Education; Continuing Education; Postal Service; Relationship owner; Registration Authority; legal source; issuing source; authoritative source)
    :param 'CodeableConcept' communicationMethod: Method for exchanging information with the primary source
    :param 'CodeableConcept' validationStatus: successful | failed | unknown
    :param str validationDate: When the target was validated against the primary source
    :param 'CodeableConcept' canPushUpdates: yes | no | undetermined
    :param 'CodeableConcept' pushTypeAvailable: specific | any | source
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  who: 'Reference' = None,  type: 'CodeableConcept' = None,  communicationMethod: 'CodeableConcept' = None,  validationStatus: 'CodeableConcept' = None,  validationDate: str = None,  canPushUpdates: 'CodeableConcept' = None,  pushTypeAvailable: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.who: 'Reference' = who 
        self.type: list['CodeableConcept'] = type or []
        self.communicationMethod: list['CodeableConcept'] = communicationMethod or []
        self.validationStatus: 'CodeableConcept' = validationStatus 
        self.validationDate: str = validationDate 
        self.canPushUpdates: 'CodeableConcept' = canPushUpdates 
        self.pushTypeAvailable: list['CodeableConcept'] = pushTypeAvailable or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PrimarySource":
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


    
    

class Attestation(BaseModel):
    """ Information about the entity attesting to information.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' who: The individual or organization attesting to information
    :param 'Reference' onBehalfOf: When the who is asserting on behalf of another (organization or individual)
    :param 'CodeableConcept' communicationMethod: The method by which attested information was submitted/retrieved
    :param str date: The date the information was attested to
    :param str sourceIdentityCertificate: A digital identity certificate associated with the attestation source
    :param str proxyIdentityCertificate: A digital identity certificate associated with the proxy entity submitting attested information on behalf of the attestation source
    :param 'Signature' proxySignature: Proxy signature
    :param 'Signature' sourceSignature: Attester signature
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  who: 'Reference' = None,  onBehalfOf: 'Reference' = None,  communicationMethod: 'CodeableConcept' = None,  date: str = None,  sourceIdentityCertificate: str = None,  proxyIdentityCertificate: str = None,  proxySignature: 'Signature' = None,  sourceSignature: 'Signature' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.who: 'Reference' = who 
        self.onBehalfOf: 'Reference' = onBehalfOf 
        self.communicationMethod: 'CodeableConcept' = communicationMethod 
        self.date: str = date 
        self.sourceIdentityCertificate: str = sourceIdentityCertificate 
        self.proxyIdentityCertificate: str = proxyIdentityCertificate 
        self.proxySignature: 'Signature' = proxySignature 
        self.sourceSignature: 'Signature' = sourceSignature 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Attestation":
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


    
    

class Validator(BaseModel):
    """ Information about the entity validating information.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' organization: Reference to the organization validating information
    :param str identityCertificate: A digital identity certificate associated with the validator
    :param 'Signature' attestationSignature: Validator signature
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  organization: 'Reference' = None,  identityCertificate: str = None,  attestationSignature: 'Signature' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.organization: 'Reference' = organization 
        self.identityCertificate: str = identityCertificate 
        self.attestationSignature: 'Signature' = attestationSignature 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Validator":
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


class VerificationResult(DomainResource):
    """ Describes validation requirements, source(s), status and dates for one or more elements.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Reference' target: A resource that was validated
    :param str targetLocation: The fhirpath location(s) within the resource that was validated
    :param 'CodeableConcept' need: none | initial | periodic
    :param str status: attested | validated | in-process | req-revalid | val-fail | reval-fail
    :param str statusDate: When the validation status was updated
    :param 'CodeableConcept' validationType: nothing | primary | multiple
    :param 'CodeableConcept' validationProcess: The primary process by which the target is validated (edit check; value set; primary source; multiple sources; standalone; in context)
    :param 'Timing' frequency: Frequency of revalidation
    :param str lastPerformed: The date/time validation was last completed (including failed validations)
    :param str nextScheduled: The date when target is next validated, if appropriate
    :param 'CodeableConcept' failureAction: fatal | warn | rec-only | none
    :param 'PrimarySource' primarySource: Information about the primary source(s) involved in validation
    :param 'Attestation' attestation: Information about the entity attesting to information
    :param 'Validator' validator: Information about the entity validating information
    """
    def __init__(self, resourceType: str = "VerificationResult",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  target: 'Reference' = None,  targetLocation: str = None,  need: 'CodeableConcept' = None,  status: str = None,  statusDate: str = None,  validationType: 'CodeableConcept' = None,  validationProcess: 'CodeableConcept' = None,  frequency: 'Timing' = None,  lastPerformed: str = None,  nextScheduled: str = None,  failureAction: 'CodeableConcept' = None,  primarySource: 'PrimarySource' = None,  attestation: 'Attestation' = None,  validator: 'Validator' = None, ):
        self.resourceType: str = resourceType or "VerificationResult"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.target: list['Reference'] = target or []
        self.targetLocation: list[str] = targetLocation or []
        self.need: 'CodeableConcept' = need 
        self.status: str = status 
        self.statusDate: str = statusDate 
        self.validationType: 'CodeableConcept' = validationType 
        self.validationProcess: list['CodeableConcept'] = validationProcess or []
        self.frequency: 'Timing' = frequency 
        self.lastPerformed: str = lastPerformed 
        self.nextScheduled: str = nextScheduled 
        self.failureAction: 'CodeableConcept' = failureAction 
        self.primarySource: list['PrimarySource'] = primarySource or []
        self.attestation: 'Attestation' = attestation 
        self.validator: list['Validator'] = validator or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "VerificationResult":
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