"""
Generated class for Medication. 
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


class Ingredient(BaseModel):
    """Identifies a particular constituent of interest in the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept itemCodeableConcept: The actual ingredient or content
    :param Reference itemReference: The actual ingredient or content
    :param bool isActive: Active ingredient indicator
    :param Ratio strength: Quantity of ingredient present
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "itemCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        "itemReference": {"class_name": "Reference", "is_contained": False},
        "strength": {"class_name": "Ratio", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        itemCodeableConcept: "CodeableConcept" = None,
        itemReference: "Reference" = None,
        isActive: "bool" = None,
        strength: "Ratio" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemCodeableConcept = itemCodeableConcept
        self.itemReference = itemReference
        self.isActive = isActive
        self.strength = strength

    @classmethod
    def from_dict(cls, data: dict) -> "Medication":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Medication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Batch(BaseModel):
    """Information that only applies to packages (not products).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lotNumber: Identifier assigned to batch
    :param str expirationDate: When batch will expire
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
        lotNumber: "str" = None,
        expirationDate: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.lotNumber = lotNumber
        self.expirationDate = expirationDate

    @classmethod
    def from_dict(cls, data: dict) -> "Medication":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Medication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Medication(DomainResource):
    """This resource is primarily used for the identification and definition of a medication for the purposes of prescribing, dispensing, and administering a medication as well as for making statements about medication use.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this medication
    :param CodeableConcept code: Codes that identify this medication
    :param str status: active | inactive | entered-in-error
    :param Reference manufacturer: Manufacturer of the item
    :param CodeableConcept form: powder | tablets | capsule +
    :param Ratio amount: Amount of drug in package
    :param Ingredient ingredient: Active or inactive ingredient
    :param Batch batch: Details about packaged medications
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        "form": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Ratio", "is_contained": False},
        "ingredient": {"class_name": "Ingredient", "is_contained": True},
        "batch": {"class_name": "Batch", "is_contained": True},
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
        code: "CodeableConcept" = None,
        status: "str" = None,
        manufacturer: "Reference" = None,
        form: "CodeableConcept" = None,
        amount: "Ratio" = None,
        ingredient: list["Ingredient"] = None,
        batch: "Batch" = None,
    ):
        self.resourceType = resourceType or "Medication"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.code = code
        self.status = status
        self.manufacturer = manufacturer
        self.form = form
        self.amount = amount
        self.ingredient = ingredient or []
        self.batch = batch

    @classmethod
    def from_dict(cls, data: dict) -> "Medication":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Medication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
