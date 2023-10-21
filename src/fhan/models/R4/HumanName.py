"""
Generated class for HumanName. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.generator_models import BaseModel


class HumanName(BaseModel):
    """Base StructureDefinition for HumanName Type: A human's name with the ability to identify parts and usage.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str use: usual | official | temp | nickname | anonymous | old | maiden
    :param str text: Text representation of the full name
    :param str family: Family name (often called 'Surname')
    :param str given: Given names (not always 'first'). Includes middle names
    :param str prefix: Parts that come before the name
    :param str suffix: Parts that come after the name
    :param Period period: Time period when name was/is in use
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
        text: "str" = None,
        family: "str" = None,
        given: list["str"] = None,
        prefix: list["str"] = None,
        suffix: list["str"] = None,
        period: "Period" = None,
    ):
        self.resourceType = resourceType or "HumanName"
        self.id = id
        self.extension = extension or []
        self.use = use
        self.text = text
        self.family = family
        self.given = given or []
        self.prefix = prefix or []
        self.suffix = suffix or []
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "HumanName":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "HumanName":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
