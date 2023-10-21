"""
Generated class for Ratio. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.generator_models import BaseModel


class Ratio(BaseModel):
    """Base StructureDefinition for Ratio Type: A relationship of two Quantity values - expressed as a numerator and a denominator.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity numerator: Numerator value
    :param Quantity denominator: Denominator value
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "numerator": {"class_name": "Quantity", "is_contained": False},
        "denominator": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        numerator: "Quantity" = None,
        denominator: "Quantity" = None,
    ):
        self.resourceType = resourceType or "Ratio"
        self.id = id
        self.extension = extension or []
        self.numerator = numerator
        self.denominator = denominator

    @classmethod
    def from_dict(cls, data: dict) -> "Ratio":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Ratio":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
