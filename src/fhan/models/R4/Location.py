"""
Generated class for Location. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Coding import *
from fhan.models.R4.Reference import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Address import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class Location(ModelBase):
    """ Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique code or number identifying the location to its users
    :param str status: active | suspended | inactive
    :param Coding operationalStatus: The operational status of the location (typically only for a bed/room)
    :param str name: Name of the location as used by humans
    :param str alias: A list of alternate names that the location is known as, or was known as, in the past
    :param str description: Additional details about the location that could be displayed as further information to identify the location beyond its name
    :param str mode: instance | kind
    :param CodeableConcept type: Type of function performed
    :param ContactPoint telecom: Contact details of the location
    :param Address address: Physical location
    :param CodeableConcept physicalType: Physical form of the location
    :param BackboneElement position: The absolute geographic location
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param float longitude: Longitude with WGS84 datum
    :param float latitude: Latitude with WGS84 datum
    :param float altitude: Altitude with WGS84 datum
    :param Reference managingOrganization: Organization responsible for provisioning and upkeep
    :param Reference partOf: Another Location this one is physically a part of
    :param BackboneElement hoursOfOperation: What days/times during a week is this location usually open
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: The Location is open all day
    :param str openingTime: Time that the Location opens
    :param str closingTime: Time that the Location closes
    :param str availabilityExceptions: Description of availability exceptions
    :param Reference endpoint: Technical endpoints providing access to services operated for the location
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    operationalStatus: "Coding" = None
    
    name: str = None
    
    alias: str = None
    
    description: str = None
    
    mode: str = None
    
    type: "CodeableConcept" = None
    
    telecom: "ContactPoint" = None
    
    address: "Address" = None
    
    physicalType: "CodeableConcept" = None
    
    position: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    longitude: float = None
    
    latitude: float = None
    
    altitude: float = None
    
    managingOrganization: "Reference" = None
    
    partOf: "Reference" = None
    
    hoursOfOperation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    daysOfWeek: str = None
    
    allDay: bool = None
    
    openingTime: str = None
    
    closingTime: str = None
    
    availabilityExceptions: str = None
    
    endpoint: "Reference" = None
    