"""
Generated class for Timing. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Range import *
from fhan.models.R4.Duration import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.generator_models import BaseModel


class Repeat(BaseModel):
    """A set of rules that describe when the event is scheduled.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Duration boundsDuration: Length/Range of lengths, or (Start and/or end) limits
    :param Range boundsRange: Length/Range of lengths, or (Start and/or end) limits
    :param Period boundsPeriod: Length/Range of lengths, or (Start and/or end) limits
    :param int count: Number of times to repeat
    :param int countMax: Maximum number of times to repeat
    :param float duration: How long when it happens
    :param float durationMax: How long when it happens (Max)
    :param str durationUnit: s | min | h | d | wk | mo | a - unit of time (UCUM)
    :param int frequency: Event occurs frequency times per period
    :param int frequencyMax: Event occurs up to frequencyMax times per period
    :param float period: Event occurs frequency times per period
    :param float periodMax: Upper limit of period (3-4 hours)
    :param str periodUnit: s | min | h | d | wk | mo | a - unit of time (UCUM)
    :param str dayOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param str timeOfDay: Time of day for action
    :param str when: Code for time period of occurrence
    :param int offset: Minutes from event (before or after)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "boundsDuration": {"class_name": "Duration", "is_contained": False},
        "boundsRange": {"class_name": "Range", "is_contained": False},
        "boundsPeriod": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        boundsDuration: "Duration" = None,
        boundsRange: "Range" = None,
        boundsPeriod: "Period" = None,
        count: "int" = None,
        countMax: "int" = None,
        duration: "float" = None,
        durationMax: "float" = None,
        durationUnit: "str" = None,
        frequency: "int" = None,
        frequencyMax: "int" = None,
        period: "float" = None,
        periodMax: "float" = None,
        periodUnit: "str" = None,
        dayOfWeek: list["str"] = None,
        timeOfDay: list["str"] = None,
        when: list["str"] = None,
        offset: "int" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.boundsDuration = boundsDuration
        self.boundsRange = boundsRange
        self.boundsPeriod = boundsPeriod
        self.count = count
        self.countMax = countMax
        self.duration = duration
        self.durationMax = durationMax
        self.durationUnit = durationUnit
        self.frequency = frequency
        self.frequencyMax = frequencyMax
        self.period = period
        self.periodMax = periodMax
        self.periodUnit = periodUnit
        self.dayOfWeek = dayOfWeek or []
        self.timeOfDay = timeOfDay or []
        self.when = when or []
        self.offset = offset

    @classmethod
    def from_dict(cls, data: dict) -> "Timing":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Timing":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Timing(BaseModel):
    """Base StructureDefinition for Timing Type: Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str event: When the event occurs
    :param Repeat repeat: When the event is to occur
    :param CodeableConcept code: BID | TID | QID | AM | PM | QD | QOD | +
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "repeat": {"class_name": "Repeat", "is_contained": True},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        event: list["str"] = None,
        repeat: "Repeat" = None,
        code: "CodeableConcept" = None,
    ):
        self.resourceType = resourceType or "Timing"
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.event = event or []
        self.repeat = repeat
        self.code = code

    @classmethod
    def from_dict(cls, data: dict) -> "Timing":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Timing":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
