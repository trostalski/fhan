"""
Generated class for Money. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel


class Money(BaseModel):
    """Base StructureDefinition for Money Type: An amount of economic utility in some recognized currency.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str currency: ISO 4217 Currency Code
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
        value: "float" = None,
        currency: "str" = None,
    ):
        self.resourceType = resourceType or "Money"
        self.id = id
        self.extension = extension or []
        self.value = value
        self.currency = currency

    @classmethod
    def from_dict(cls, data: dict) -> "Money":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Money":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
