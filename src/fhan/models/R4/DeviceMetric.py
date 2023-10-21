"""
Generated class for DeviceMetric. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Calibration(BaseModel):
    """Describes the calibrations that have been performed or that are required to be performed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: unspecified | offset | gain | two-point
    :param str state: not-calibrated | calibration-required | calibrated | unspecified
    :param str time: Describes the time last calibration has been performed
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
        type: "str" = None,
        state: "str" = None,
        time: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.state = state
        self.time = time

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceMetric":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DeviceMetric":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DeviceMetric(DomainResource):
    """Describes a measurement, calculation or setting capability of a medical device.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Instance identifier
    :param CodeableConcept type: Identity of metric, for example Heart Rate or PEEP Setting
    :param CodeableConcept unit: Unit of Measure for the Metric
    :param Reference source: Describes the link to the source Device
    :param Reference parent: Describes the link to the parent Device
    :param str operationalStatus: on | off | standby | entered-in-error
    :param str color: black | red | green | yellow | blue | magenta | cyan | white
    :param str category: measurement | setting | calculation | unspecified
    :param Timing measurementPeriod: Describes the measurement repetition time
    :param Calibration calibration: Describes the calibrations that have been performed or that are required to be performed
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "unit": {"class_name": "CodeableConcept", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
        "parent": {"class_name": "Reference", "is_contained": False},
        "measurementPeriod": {"class_name": "Timing", "is_contained": False},
        "calibration": {"class_name": "Calibration", "is_contained": True},
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
        type: "CodeableConcept" = None,
        unit: "CodeableConcept" = None,
        source: "Reference" = None,
        parent: "Reference" = None,
        operationalStatus: "str" = None,
        color: "str" = None,
        category: "str" = None,
        measurementPeriod: "Timing" = None,
        calibration: list["Calibration"] = None,
    ):
        self.resourceType = resourceType or "DeviceMetric"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type
        self.unit = unit
        self.source = source
        self.parent = parent
        self.operationalStatus = operationalStatus
        self.color = color
        self.category = category
        self.measurementPeriod = measurementPeriod
        self.calibration = calibration or []

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceMetric":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DeviceMetric":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
