"""
Generated class for Substance. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Ratio import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Instance(BaseModel):
    """Substance may be used to describe a kind of substance, or a specific package/container of the substance: an instance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier of the package/container
    :param str expiry: When no longer valid to use
    :param Quantity quantity: Amount of substance in the package
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: "Identifier" = None,
        expiry: "str" = None,
        quantity: "Quantity" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.expiry = expiry
        self.quantity = quantity

    @classmethod
    def from_dict(cls, data: dict) -> "Substance":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Substance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Ingredient(BaseModel):
    """A substance can be composed of other substances.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio quantity: Optional amount (concentration)
    :param CodeableConcept substanceCodeableConcept: A component of the substance
    :param Reference substanceReference: A component of the substance
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "quantity": {"class_name": "Ratio", "is_contained": False},
        "substanceCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "substanceReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        quantity: "Ratio" = None,
        substanceCodeableConcept: "CodeableConcept" = None,
        substanceReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.quantity = quantity
        self.substanceCodeableConcept = substanceCodeableConcept
        self.substanceReference = substanceReference

    @classmethod
    def from_dict(cls, data: dict) -> "Substance":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Substance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Substance(DomainResource):
    """A homogeneous material with a definite composition.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: What class/type of substance this is
    :param CodeableConcept code: What substance this is
    :param str description: Textual description of the substance, comments
    :param Instance instance: If this describes a specific package/container of the substance
    :param Ingredient ingredient: Composition information about the substance
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "instance": {"class_name": "Instance", "is_contained": True},
        "ingredient": {"class_name": "Ingredient", "is_contained": True},
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
        status: "str" = None,
        category: list["CodeableConcept"] = None,
        code: "CodeableConcept" = None,
        description: "str" = None,
        instance: list["Instance"] = None,
        ingredient: list["Ingredient"] = None,
    ):
        self.resourceType = resourceType or "Substance"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status
        self.category = category or []
        self.code = code
        self.description = description
        self.instance = instance or []
        self.ingredient = ingredient or []

    @classmethod
    def from_dict(cls, data: dict) -> "Substance":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Substance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
