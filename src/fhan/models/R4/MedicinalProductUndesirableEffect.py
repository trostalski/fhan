"""
Generated class for MedicinalProductUndesirableEffect. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Population import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class MedicinalProductUndesirableEffect(DomainResource):
    """Describe the undesirable effects of the medicinal product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference subject: The medication for which this is an indication
    :param CodeableConcept symptomConditionEffect: The symptom, condition or undesirable effect
    :param CodeableConcept classification: Classification of the effect
    :param CodeableConcept frequencyOfOccurrence: The frequency of occurrence of the effect
    :param Population population: The population group to which this applies
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "symptomConditionEffect": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "classification": {"class_name": "CodeableConcept", "is_contained": False},
        "frequencyOfOccurrence": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "population": {"class_name": "Population", "is_contained": False},
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
        subject: list["Reference"] = None,
        symptomConditionEffect: "CodeableConcept" = None,
        classification: "CodeableConcept" = None,
        frequencyOfOccurrence: "CodeableConcept" = None,
        population: list["Population"] = None,
    ):
        self.resourceType = resourceType or "MedicinalProductUndesirableEffect"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.subject = subject or []
        self.symptomConditionEffect = symptomConditionEffect
        self.classification = classification
        self.frequencyOfOccurrence = frequencyOfOccurrence
        self.population = population or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductUndesirableEffect":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductUndesirableEffect":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
