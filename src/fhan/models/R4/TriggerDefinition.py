"""
Generated class for TriggerDefinition. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import BaseModel


class TriggerDefinition(BaseModel):
    """Base StructureDefinition for TriggerDefinition Type: A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: named-event | periodic | data-changed | data-added | data-modified | data-removed | data-accessed | data-access-ended
    :param str name: Name or URI that identifies the event
    :param Timing timingTiming: Timing of the event
    :param Reference timingReference: Timing of the event
    :param str timingDate: Timing of the event
    :param str timingDateTime: Timing of the event
    :param DataRequirement data: Triggering data of the event (multiple = 'and')
    :param Expression condition: Whether the event triggers (boolean expression)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "timingTiming": {"class_name": "Timing", "is_contained": False},
        "timingReference": {"class_name": "Reference", "is_contained": False},
        "data": {"class_name": "DataRequirement", "is_contained": False},
        "condition": {"class_name": "Expression", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        type: "str" = None,
        name: "str" = None,
        timingTiming: "Timing" = None,
        timingReference: "Reference" = None,
        timingDate: "str" = None,
        timingDateTime: "str" = None,
        data: list["DataRequirement"] = None,
        condition: "Expression" = None,
    ):
        self.resourceType = resourceType or "TriggerDefinition"
        self.id = id
        self.extension = extension or []
        self.type = type
        self.name = name
        self.timingTiming = timingTiming
        self.timingReference = timingReference
        self.timingDate = timingDate
        self.timingDateTime = timingDateTime
        self.data = data or []
        self.condition = condition

    @classmethod
    def from_dict(cls, data: dict) -> "TriggerDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TriggerDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
