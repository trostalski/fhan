"""
Generated class for Address. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.generator_models import BaseModel


class Address(BaseModel):
    """Base StructureDefinition for Address Type: An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str use: home | work | temp | old | billing - purpose of this address
    :param str type: postal | physical | both
    :param str text: Text representation of the address
    :param str line: Street name, number, direction & P.O. Box etc.
    :param str city: Name of city, town etc.
    :param str district: District name (aka county)
    :param str state: Sub-unit of country (abbreviations ok)
    :param str postalCode: Postal code for area
    :param str country: Country (e.g. can be ISO 3166 2 or 3 letter code)
    :param Period period: Time period when address was/is in use
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        use: "str" = None,
        type: "str" = None,
        text: "str" = None,
        line: list["str"] = None,
        city: "str" = None,
        district: "str" = None,
        state: "str" = None,
        postalCode: "str" = None,
        country: "str" = None,
        period: "Period" = None,
    ):
        self.resourceType = resourceType or "Address"
        self.id = id
        self.extension = extension or []
        self.use = use
        self.type = type
        self.text = text
        self.line = line or []
        self.city = city
        self.district = district
        self.state = state
        self.postalCode = postalCode
        self.country = country
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Address":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Address":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
