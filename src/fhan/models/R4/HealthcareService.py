"""
Generated class for HealthcareService. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class Eligibility(BaseModel):
    """ Does this service have specific eligibility requirements that need to be met in order to use the service?:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Coded value for the eligibility
    :param str comment: Describes the eligibility conditions for the service
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  code: 'CodeableConcept' = None,  comment: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.comment: str = comment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Eligibility":
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


    
    

class AvailableTime(BaseModel):
    """ A collection of times that the Service Site is available.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: Always available? e.g. 24 hour service
    :param str availableStartTime: Opening time of day (ignored if allDay = true)
    :param str availableEndTime: Closing time of day (ignored if allDay = true)
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  daysOfWeek: str = None,  allDay: bool = None,  availableStartTime: str = None,  availableEndTime: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.daysOfWeek: list[str] = daysOfWeek or []
        self.allDay: bool = allDay 
        self.availableStartTime: str = availableStartTime 
        self.availableEndTime: str = availableEndTime 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AvailableTime":
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


    
    

class NotAvailable(BaseModel):
    """ The HealthcareService is not available during this period of time due to the provided reason.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Reason presented to the user explaining why time not available
    :param 'Period' during: Service not available from this date
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  description: str = None,  during: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.description: str = description 
        self.during: 'Period' = during 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NotAvailable":
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


class HealthcareService(DomainResource):
    """ The details of a healthcare service available at a location.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: External identifiers for this item
    :param bool active: Whether this HealthcareService record is in active use
    :param 'Reference' providedBy: Organization that provides this service
    :param 'CodeableConcept' category: Broad category of service being performed or delivered
    :param 'CodeableConcept' type: Type of service that may be delivered or performed
    :param 'CodeableConcept' specialty: Specialties handled by the HealthcareService
    :param 'Reference' location: Location(s) where service may be provided
    :param str name: Description of service as presented to a consumer while searching
    :param str comment: Additional description and/or any specific issues not covered elsewhere
    :param str extraDetails: Extra details about the service that can't be placed in the other fields
    :param 'Attachment' photo: Facilitates quick identification of the service
    :param 'ContactPoint' telecom: Contacts related to the healthcare service
    :param 'Reference' coverageArea: Location(s) service is intended for/available to
    :param 'CodeableConcept' serviceProvisionCode: Conditions under which service is available/offered
    :param 'Eligibility' eligibility: Specific eligibility requirements required to use the service
    :param 'CodeableConcept' program: Programs that this service is applicable to
    :param 'CodeableConcept' characteristic: Collection of characteristics (attributes)
    :param 'CodeableConcept' communication: The language that this service is offered in
    :param 'CodeableConcept' referralMethod: Ways that the service accepts referrals
    :param bool appointmentRequired: If an appointment is required for access to this service
    :param 'AvailableTime' availableTime: Times the Service Site is available
    :param 'NotAvailable' notAvailable: Not available during this time due to provided reason
    :param str availabilityExceptions: Description of availability exceptions
    :param 'Reference' endpoint: Technical endpoints providing access to electronic services operated for the healthcare service
    """
    def __init__(self, resourceType: str = "HealthcareService",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  active: bool = None,  providedBy: 'Reference' = None,  category: 'CodeableConcept' = None,  type: 'CodeableConcept' = None,  specialty: 'CodeableConcept' = None,  location: 'Reference' = None,  name: str = None,  comment: str = None,  extraDetails: str = None,  photo: 'Attachment' = None,  telecom: 'ContactPoint' = None,  coverageArea: 'Reference' = None,  serviceProvisionCode: 'CodeableConcept' = None,  eligibility: 'Eligibility' = None,  program: 'CodeableConcept' = None,  characteristic: 'CodeableConcept' = None,  communication: 'CodeableConcept' = None,  referralMethod: 'CodeableConcept' = None,  appointmentRequired: bool = None,  availableTime: 'AvailableTime' = None,  notAvailable: 'NotAvailable' = None,  availabilityExceptions: str = None,  endpoint: 'Reference' = None, ):
        self.resourceType: str = resourceType or "HealthcareService"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.active: bool = active 
        self.providedBy: 'Reference' = providedBy 
        self.category: list['CodeableConcept'] = category or []
        self.type: list['CodeableConcept'] = type or []
        self.specialty: list['CodeableConcept'] = specialty or []
        self.location: list['Reference'] = location or []
        self.name: str = name 
        self.comment: str = comment 
        self.extraDetails: str = extraDetails 
        self.photo: 'Attachment' = photo 
        self.telecom: list['ContactPoint'] = telecom or []
        self.coverageArea: list['Reference'] = coverageArea or []
        self.serviceProvisionCode: list['CodeableConcept'] = serviceProvisionCode or []
        self.eligibility: list['Eligibility'] = eligibility or []
        self.program: list['CodeableConcept'] = program or []
        self.characteristic: list['CodeableConcept'] = characteristic or []
        self.communication: list['CodeableConcept'] = communication or []
        self.referralMethod: list['CodeableConcept'] = referralMethod or []
        self.appointmentRequired: bool = appointmentRequired 
        self.availableTime: list['AvailableTime'] = availableTime or []
        self.notAvailable: list['NotAvailable'] = notAvailable or []
        self.availabilityExceptions: str = availabilityExceptions 
        self.endpoint: list['Reference'] = endpoint or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "HealthcareService":
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