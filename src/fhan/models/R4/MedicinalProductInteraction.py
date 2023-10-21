"""
Generated class for MedicinalProductInteraction. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Interactant(BaseModel):
    """The specific medication, food or laboratory test that interacts.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: The specific medication, food or laboratory test that interacts
    :param CodeableConcept itemCodeableConcept: The specific medication, food or laboratory test that interacts
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "itemReference": {"class_name": "Reference", "is_contained": False},
        "itemCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        itemReference: "Reference" = None,
        itemCodeableConcept: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemReference = itemReference
        self.itemCodeableConcept = itemCodeableConcept

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductInteraction":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductInteraction":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicinalProductInteraction(DomainResource):
    """The interactions of the medicinal product with other medicinal products, or other forms of interactions.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference subject: The medication for which this is a described interaction
    :param str description: The interaction described
    :param Interactant interactant: The specific medication, food or laboratory test that interacts
    :param CodeableConcept type: The type of the interaction e.g. drug-drug interaction, drug-food interaction, drug-lab test interaction
    :param CodeableConcept effect: The effect of the interaction, for example "reduced gastric absorption of primary medication"
    :param CodeableConcept incidence: The incidence of the interaction, e.g. theoretical, observed
    :param CodeableConcept management: Actions for managing the interaction
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "interactant": {"class_name": "Interactant", "is_contained": True},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "effect": {"class_name": "CodeableConcept", "is_contained": False},
        "incidence": {"class_name": "CodeableConcept", "is_contained": False},
        "management": {"class_name": "CodeableConcept", "is_contained": False},
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
        description: "str" = None,
        interactant: list["Interactant"] = None,
        type: "CodeableConcept" = None,
        effect: "CodeableConcept" = None,
        incidence: "CodeableConcept" = None,
        management: "CodeableConcept" = None,
    ):
        self.resourceType = resourceType or "MedicinalProductInteraction"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.subject = subject or []
        self.description = description
        self.interactant = interactant or []
        self.type = type
        self.effect = effect
        self.incidence = incidence
        self.management = management

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductInteraction":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductInteraction":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
