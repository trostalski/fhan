"""
Generated class for Period. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel


class Period(BaseModel):
    """Base StructureDefinition for Period Type: A time period defined by a start and end date and optionally time.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str start: Starting time with inclusive boundary
    :param str end: End time with inclusive boundary, if not ongoing
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        start: "str" = None,
        end: "str" = None,
    ):
        self.resourceType = resourceType or "Period"
        self.id = id
        self.extension = extension or []
        self.start = start
        self.end = end

    @classmethod
    def from_dict(cls, data: dict) -> "Period":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Period":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
