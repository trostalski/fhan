"""
Generated class for Count. 
Time: 2023-09-27 19:27:05
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel


class Count(BaseModel):
    """Base StructureDefinition for Count Type: A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str comparator: < | <= | >= | > - how to understand the value
    :param str unit: Unit representation
    :param str system: System that defines coded unit form
    :param str code: Coded form of the unit
    """

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
        self.resourceType = resourceType or "Count"
        self.id = id
        self.extension = extension or []
        self.value = value
        self.comparator = comparator
        self.unit = unit
        self.system = system
        self.code = code

    @classmethod
    def from_dict(cls, data: dict) -> "Count":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Count":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
