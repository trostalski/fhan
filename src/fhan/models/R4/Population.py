"""
Generated class for Population. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import BaseModel


class Population(BaseModel):
    """Base StructureDefinition for Population Type: A populatioof people with some set of grouping criteria.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Range ageRange: The age of the specific population
    :param CodeableConcept ageCodeableConcept: The age of the specific population
    :param CodeableConcept gender: The gender of the specific population
    :param CodeableConcept race: Race of the specific population
    :param CodeableConcept physiologicalCondition: The existing physiological conditions of the specific population to which this applies
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "ageRange": {"class_name": "Range", "is_contained": False},
        "ageCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        "gender": {"class_name": "CodeableConcept", "is_contained": False},
        "race": {"class_name": "CodeableConcept", "is_contained": False},
        "physiologicalCondition": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        ageRange: "Range" = None,
        ageCodeableConcept: "CodeableConcept" = None,
        gender: "CodeableConcept" = None,
        race: "CodeableConcept" = None,
        physiologicalCondition: "CodeableConcept" = None,
    ):
        self.resourceType = resourceType or "Population"
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.ageRange = ageRange
        self.ageCodeableConcept = ageCodeableConcept
        self.gender = gender
        self.race = race
        self.physiologicalCondition = physiologicalCondition

    @classmethod
    def from_dict(cls, data: dict) -> "Population":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Population":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
