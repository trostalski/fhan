"""
Generated class for ProductShelfLife. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.generator_models import BaseModel


class ProductShelfLife(BaseModel):
    """Base StructureDefinition for ProductShelfLife Type: The shelf-life and storage information for a medicinal product item or container can be described using this class.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Unique identifier for the packaged Medicinal Product
    :param CodeableConcept type: This describes the shelf life, taking into account various scenarios such as shelf life of the packaged Medicinal Product itself, shelf life after transformation where necessary and shelf life after the first opening of a bottle, etc. The shelf life type shall be specified using an appropriate controlled vocabulary The controlled term and the controlled term identifier shall be specified
    :param Quantity period: The shelf life time period can be specified using a numerical value for the period of time and its unit of time measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param CodeableConcept specialPrecautionsForStorage: Special precautions for storage, if any, can be specified using an appropriate controlled vocabulary The controlled term and the controlled term identifier shall be specified
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Quantity", "is_contained": False},
        "specialPrecautionsForStorage": {
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
        identifier: "Identifier" = None,
        type: "CodeableConcept" = None,
        period: "Quantity" = None,
        specialPrecautionsForStorage: list["CodeableConcept"] = None,
    ):
        self.resourceType = resourceType or "ProductShelfLife"
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.type = type
        self.period = period
        self.specialPrecautionsForStorage = specialPrecautionsForStorage or []

    @classmethod
    def from_dict(cls, data: dict) -> "ProductShelfLife":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ProductShelfLife":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
