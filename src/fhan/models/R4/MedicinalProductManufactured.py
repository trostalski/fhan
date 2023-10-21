"""
Generated class for MedicinalProductManufactured. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class MedicinalProductManufactured(DomainResource):
    """The manufactured item as contained in the packaged medicinal product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept manufacturedDoseForm: Dose form as manufactured and before any transformation into the pharmaceutical product
    :param CodeableConcept unitOfPresentation: The “real world” units in which the quantity of the manufactured item is described
    :param Quantity quantity: The quantity or "count number" of the manufactured item
    :param Reference manufacturer: Manufacturer of the item (Note that this should be named "manufacturer" but it currently causes technical issues)
    :param Reference ingredient: Ingredient
    :param ProdCharacteristic physicalCharacteristics: Dimensions, color etc.
    :param CodeableConcept otherCharacteristics: Other codeable characteristics
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "manufacturedDoseForm": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "unitOfPresentation": {"class_name": "CodeableConcept", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        "ingredient": {"class_name": "Reference", "is_contained": False},
        "physicalCharacteristics": {
            "class_name": "ProdCharacteristic",
            "is_contained": False,
        },
        "otherCharacteristics": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
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
        manufacturedDoseForm: "CodeableConcept" = None,
        unitOfPresentation: "CodeableConcept" = None,
        quantity: "Quantity" = None,
        manufacturer: list["Reference"] = None,
        ingredient: list["Reference"] = None,
        physicalCharacteristics: "ProdCharacteristic" = None,
        otherCharacteristics: list["CodeableConcept"] = None,
    ):
        self.resourceType = resourceType or "MedicinalProductManufactured"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.manufacturedDoseForm = manufacturedDoseForm
        self.unitOfPresentation = unitOfPresentation
        self.quantity = quantity
        self.manufacturer = manufacturer or []
        self.ingredient = ingredient or []
        self.physicalCharacteristics = physicalCharacteristics
        self.otherCharacteristics = otherCharacteristics or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductManufactured":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductManufactured":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
