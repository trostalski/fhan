"""
Generated class for Location. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Address import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Position(ModelBase):
    """ The absolute geographic location of the Location, expressed using the WGS84 datum (This is the same co-ordinate system used in KML).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param float longitude: Longitude with WGS84 datum
    :param float latitude: Latitude with WGS84 datum
    :param float altitude: Altitude with WGS84 datum
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  longitude: float = None,  latitude: float = None,  altitude: float = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.longitude: float = longitude 
        self.latitude: float = latitude 
        self.altitude: float = altitude 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Position":
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


    
    

class HoursOfOperation(ModelBase):
    """ What days/times during a week is this location usually open.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: The Location is open all day
    :param str openingTime: Time that the Location opens
    :param str closingTime: Time that the Location closes
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  daysOfWeek: str = None,  allDay: bool = None,  openingTime: str = None,  closingTime: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.daysOfWeek: str = daysOfWeek or []
        self.allDay: bool = allDay 
        self.openingTime: str = openingTime 
        self.closingTime: str = closingTime 
        

    @classmethod
    def from_dict(cls, data: dict) -> "HoursOfOperation":
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


class Location(DomainResource):
    """ Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique code or number identifying the location to its users
    :param str status: active | suspended | inactive
    :param 'Coding' operationalStatus: The operational status of the location (typically only for a bed/room)
    :param str name: Name of the location as used by humans
    :param str alias: A list of alternate names that the location is known as, or was known as, in the past
    :param str description: Additional details about the location that could be displayed as further information to identify the location beyond its name
    :param str mode: instance | kind
    :param list['CodeableConcept'] type: Type of function performed
    :param list['ContactPoint'] telecom: Contact details of the location
    :param 'Address' address: Physical location
    :param 'CodeableConcept' physicalType: Physical form of the location
    :param 'Position' position: The absolute geographic location
    :param 'Reference' managingOrganization: Organization responsible for provisioning and upkeep
    :param 'Reference' partOf: Another Location this one is physically a part of
    :param list['HoursOfOperation'] hoursOfOperation: What days/times during a week is this location usually open
    :param str availabilityExceptions: Description of availability exceptions
    :param list['Reference'] endpoint: Technical endpoints providing access to services operated for the location
    """
    def __init__(self, resourceType: str = "Location",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  operationalStatus: 'Coding' = None,  name: str = None,  alias: str = None,  description: str = None,  mode: str = None,  type: list['CodeableConcept'] = None,  telecom: list['ContactPoint'] = None,  address: 'Address' = None,  physicalType: 'CodeableConcept' = None,  position: 'Position' = None,  managingOrganization: 'Reference' = None,  partOf: 'Reference' = None,  hoursOfOperation: list['HoursOfOperation'] = None,  availabilityExceptions: str = None,  endpoint: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "Location"
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
        self.operationalStatus: 'Coding' = operationalStatus 
        self.name: str = name 
        self.alias: str = alias or []
        self.description: str = description 
        self.mode: str = mode 
        self.type: list['CodeableConcept'] = type or []
        self.telecom: list['ContactPoint'] = telecom or []
        self.address: 'Address' = address 
        self.physicalType: 'CodeableConcept' = physicalType 
        self.position: 'Position' = position 
        self.managingOrganization: 'Reference' = managingOrganization 
        self.partOf: 'Reference' = partOf 
        self.hoursOfOperation: list['HoursOfOperation'] = hoursOfOperation or []
        self.availabilityExceptions: str = availabilityExceptions 
        self.endpoint: list['Reference'] = endpoint or []
        

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