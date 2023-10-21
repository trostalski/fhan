"""
Generated class for Schedule. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Schedule(DomainResource):
    """A container for slots of time that may be available for booking appointments.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this item
    :param bool active: Whether this schedule is in active use
    :param CodeableConcept serviceCategory: High-level category
    :param CodeableConcept serviceType: Specific service
    :param CodeableConcept specialty: Type of specialty needed
    :param Reference actor: Resource(s) that availability information is being provided for
    :param Period planningHorizon: Period of time covered by schedule
    :param str comment: Comments on availability
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "serviceCategory": {"class_name": "CodeableConcept", "is_contained": False},
        "serviceType": {"class_name": "CodeableConcept", "is_contained": False},
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
        "planningHorizon": {"class_name": "Period", "is_contained": False},
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
        active: "bool" = None,
        serviceCategory: list["CodeableConcept"] = None,
        serviceType: list["CodeableConcept"] = None,
        specialty: list["CodeableConcept"] = None,
        actor: list["Reference"] = None,
        planningHorizon: "Period" = None,
        comment: "str" = None,
    ):
        self.resourceType = resourceType or "Schedule"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.active = active
        self.serviceCategory = serviceCategory or []
        self.serviceType = serviceType or []
        self.specialty = specialty or []
        self.actor = actor or []
        self.planningHorizon = planningHorizon
        self.comment = comment

    @classmethod
    def from_dict(cls, data: dict) -> "Schedule":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Schedule":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
