"""
Generated class for Location. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Address import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Coding import *
from fhan.models.R4.DomainResource import *


class Position(BaseModel):
    """The absolute geographic location of the Location, expressed using the WGS84 datum (This is the same co-ordinate system used in KML).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param float longitude: Longitude with WGS84 datum
    :param float latitude: Latitude with WGS84 datum
    :param float altitude: Altitude with WGS84 datum
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        longitude: "float" = None,
        latitude: "float" = None,
        altitude: "float" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude

    @classmethod
    def from_dict(cls, data: dict) -> "Location":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Location":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class HoursOfOperation(BaseModel):
    """What days/times during a week is this location usually open.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: The Location is open all day
    :param str openingTime: Time that the Location opens
    :param str closingTime: Time that the Location closes
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        daysOfWeek: list["str"] = None,
        allDay: "bool" = None,
        openingTime: "str" = None,
        closingTime: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.daysOfWeek = daysOfWeek or []
        self.allDay = allDay
        self.openingTime = openingTime
        self.closingTime = closingTime

    @classmethod
    def from_dict(cls, data: dict) -> "Location":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Location":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Location(DomainResource):
    """Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.
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
    :param Position position: The absolute geographic location
    :param Reference managingOrganization: Organization responsible for provisioning and upkeep
    :param Reference partOf: Another Location this one is physically a part of
    :param HoursOfOperation hoursOfOperation: What days/times during a week is this location usually open
    :param str availabilityExceptions: Description of availability exceptions
    :param Reference endpoint: Technical endpoints providing access to services operated for the location
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "operationalStatus": {"class_name": "Coding", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "address": {"class_name": "Address", "is_contained": False},
        "physicalType": {"class_name": "CodeableConcept", "is_contained": False},
        "position": {"class_name": "Position", "is_contained": True},
        "managingOrganization": {"class_name": "Reference", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "hoursOfOperation": {"class_name": "HoursOfOperation", "is_contained": True},
        "endpoint": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        status: "str" = None,
        operationalStatus: "Coding" = None,
        name: "str" = None,
        alias: list["str"] = None,
        description: "str" = None,
        mode: "str" = None,
        type: list["CodeableConcept"] = None,
        telecom: list["ContactPoint"] = None,
        address: "Address" = None,
        physicalType: "CodeableConcept" = None,
        position: "Position" = None,
        managingOrganization: "Reference" = None,
        partOf: "Reference" = None,
        hoursOfOperation: list["HoursOfOperation"] = None,
        availabilityExceptions: "str" = None,
        endpoint: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "Location"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status
        self.operationalStatus = operationalStatus
        self.name = name
        self.alias = alias or []
        self.description = description
        self.mode = mode
        self.type = type or []
        self.telecom = telecom or []
        self.address = address
        self.physicalType = physicalType
        self.position = position
        self.managingOrganization = managingOrganization
        self.partOf = partOf
        self.hoursOfOperation = hoursOfOperation or []
        self.availabilityExceptions = availabilityExceptions
        self.endpoint = endpoint or []

    @classmethod
    def from_dict(cls, data: dict) -> "Location":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Location":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
