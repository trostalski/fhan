"""
Generated class for ProdCharacteristic. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Attachment import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.generator_models import BaseModel


class ProdCharacteristic(BaseModel):
    """Base StructureDefinition for ProdCharacteristic Type: The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity height: Where applicable, the height can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity width: Where applicable, the width can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity depth: Where applicable, the depth can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity weight: Where applicable, the weight can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity nominalVolume: Where applicable, the nominal volume can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity externalDiameter: Where applicable, the external diameter can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param str shape: Where applicable, the shape can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used
    :param str color: Where applicable, the color can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used
    :param str imprint: Where applicable, the imprint can be specified as text
    :param Attachment image: Where applicable, the image can be provided The format of the image attachment shall be specified by regional implementations
    :param CodeableConcept scoring: Where applicable, the scoring can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "height": {"class_name": "Quantity", "is_contained": False},
        "width": {"class_name": "Quantity", "is_contained": False},
        "depth": {"class_name": "Quantity", "is_contained": False},
        "weight": {"class_name": "Quantity", "is_contained": False},
        "nominalVolume": {"class_name": "Quantity", "is_contained": False},
        "externalDiameter": {"class_name": "Quantity", "is_contained": False},
        "image": {"class_name": "Attachment", "is_contained": False},
        "scoring": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        height: "Quantity" = None,
        width: "Quantity" = None,
        depth: "Quantity" = None,
        weight: "Quantity" = None,
        nominalVolume: "Quantity" = None,
        externalDiameter: "Quantity" = None,
        shape: "str" = None,
        color: list["str"] = None,
        imprint: list["str"] = None,
        image: list["Attachment"] = None,
        scoring: "CodeableConcept" = None,
    ):
        self.resourceType = resourceType or "ProdCharacteristic"
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
        self.nominalVolume = nominalVolume
        self.externalDiameter = externalDiameter
        self.shape = shape
        self.color = color or []
        self.imprint = imprint or []
        self.image = image or []
        self.scoring = scoring

    @classmethod
    def from_dict(cls, data: dict) -> "ProdCharacteristic":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ProdCharacteristic":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
