"""
Generated class for MedicinalProductIngredient. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Ratio import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class ReferenceStrength(BaseModel):
    """Strength expressed in terms of a reference substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept substance: Relevant reference substance
    :param Ratio strength: Strength expressed in terms of a reference substance
    :param Ratio strengthLowLimit: Strength expressed in terms of a reference substance
    :param str measurementPoint: For when strength is measured at a particular point or distance
    :param CodeableConcept country: The country or countries for which the strength range applies
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "substance": {"class_name": "CodeableConcept", "is_contained": False},
        "strength": {"class_name": "Ratio", "is_contained": False},
        "strengthLowLimit": {"class_name": "Ratio", "is_contained": False},
        "country": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        substance: "CodeableConcept" = None,
        strength: "Ratio" = None,
        strengthLowLimit: "Ratio" = None,
        measurementPoint: "str" = None,
        country: list["CodeableConcept"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.substance = substance
        self.strength = strength
        self.strengthLowLimit = strengthLowLimit
        self.measurementPoint = measurementPoint
        self.country = country or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductIngredient":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductIngredient":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Strength(BaseModel):
    """Quantity of the substance or specified substance present in the manufactured item or pharmaceutical product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio presentation: The quantity of substance in the unit of presentation, or in the volume (or mass) of the single pharmaceutical product or manufactured item
    :param Ratio presentationLowLimit: A lower limit for the quantity of substance in the unit of presentation. For use when there is a range of strengths, this is the lower limit, with the presentation attribute becoming the upper limit
    :param Ratio concentration: The strength per unitary volume (or mass)
    :param Ratio concentrationLowLimit: A lower limit for the strength per unitary volume (or mass), for when there is a range. The concentration attribute then becomes the upper limit
    :param str measurementPoint: For when strength is measured at a particular point or distance
    :param CodeableConcept country: The country or countries for which the strength range applies
    :param ReferenceStrength referenceStrength: Strength expressed in terms of a reference substance
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "presentation": {"class_name": "Ratio", "is_contained": False},
        "presentationLowLimit": {"class_name": "Ratio", "is_contained": False},
        "concentration": {"class_name": "Ratio", "is_contained": False},
        "concentrationLowLimit": {"class_name": "Ratio", "is_contained": False},
        "country": {"class_name": "CodeableConcept", "is_contained": False},
        "referenceStrength": {"class_name": "ReferenceStrength", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        presentation: "Ratio" = None,
        presentationLowLimit: "Ratio" = None,
        concentration: "Ratio" = None,
        concentrationLowLimit: "Ratio" = None,
        measurementPoint: "str" = None,
        country: list["CodeableConcept"] = None,
        referenceStrength: list["ReferenceStrength"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.presentation = presentation
        self.presentationLowLimit = presentationLowLimit
        self.concentration = concentration
        self.concentrationLowLimit = concentrationLowLimit
        self.measurementPoint = measurementPoint
        self.country = country or []
        self.referenceStrength = referenceStrength or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductIngredient":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductIngredient":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SpecifiedSubstance(BaseModel):
    """A specified substance that comprises this ingredient.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The specified substance
    :param CodeableConcept group: The group of specified substance, e.g. group 1 to 4
    :param CodeableConcept confidentiality: Confidentiality level of the specified substance as the ingredient
    :param Strength strength: Quantity of the substance or specified substance present in the manufactured item or pharmaceutical product
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "group": {"class_name": "CodeableConcept", "is_contained": False},
        "confidentiality": {"class_name": "CodeableConcept", "is_contained": False},
        "strength": {"class_name": "Strength", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        group: "CodeableConcept" = None,
        confidentiality: "CodeableConcept" = None,
        strength: list["Strength"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.group = group
        self.confidentiality = confidentiality
        self.strength = strength or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductIngredient":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductIngredient":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Substance(BaseModel):
    """The ingredient substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The ingredient substance
    :param Strength strength: Quantity of the substance or specified substance present in the manufactured item or pharmaceutical product
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "strength": {"class_name": "Strength", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        strength: list["Strength"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.strength = strength or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductIngredient":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductIngredient":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicinalProductIngredient(DomainResource):
    """An ingredient of a manufactured item or pharmaceutical product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier for the ingredient
    :param CodeableConcept role: Ingredient role e.g. Active ingredient, excipient
    :param bool allergenicIndicator: If the ingredient is a known or suspected allergen
    :param Reference manufacturer: Manufacturer of this Ingredient
    :param SpecifiedSubstance specifiedSubstance: A specified substance that comprises this ingredient
    :param Substance substance: The ingredient substance
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        "specifiedSubstance": {
            "class_name": "SpecifiedSubstance",
            "is_contained": True,
        },
        "substance": {"class_name": "Substance", "is_contained": True},
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
        identifier: "Identifier" = None,
        role: "CodeableConcept" = None,
        allergenicIndicator: "bool" = None,
        manufacturer: list["Reference"] = None,
        specifiedSubstance: list["SpecifiedSubstance"] = None,
        substance: "Substance" = None,
    ):
        self.resourceType = resourceType or "MedicinalProductIngredient"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.role = role
        self.allergenicIndicator = allergenicIndicator
        self.manufacturer = manufacturer or []
        self.specifiedSubstance = specifiedSubstance or []
        self.substance = substance

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductIngredient":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductIngredient":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
