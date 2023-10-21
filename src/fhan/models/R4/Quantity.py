"""
Generated class for Quantity. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel


class Quantity(BaseModel):
    """Base StructureDefinition for Quantity Type: A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str comparator: < | <= | >= | > - how to understand the value
    :param str unit: Unit representation
    :param str system: System that defines coded unit form
    :param str code: Coded form of the unit
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
        comparator: "str" = None,
        unit: "str" = None,
        system: "str" = None,
        code: "str" = None,
    ):
        self.resourceType = resourceType or "Quantity"
        self.id = id
        self.extension = extension or []
        self.value = value
        self.comparator = comparator
        self.unit = unit
        self.system = system
        self.code = code

    @classmethod
    def from_dict(cls, data: dict) -> "Quantity":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Quantity":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
