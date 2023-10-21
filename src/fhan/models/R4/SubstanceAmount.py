"""
Generated class for SubstanceAmount. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Range import *
from fhan.models.R4.Element import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.generator_models import BaseModel


class ReferenceRange(BaseModel):
    """Reference range of possible or expected values.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity lowLimit: Lower limit possible or expected
    :param Quantity highLimit: Upper limit possible or expected
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "lowLimit": {"class_name": "Quantity", "is_contained": False},
        "highLimit": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        lowLimit: "Quantity" = None,
        highLimit: "Quantity" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.lowLimit = lowLimit
        self.highLimit = highLimit

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceAmount":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceAmount":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubstanceAmount(BaseModel):
    """Base StructureDefinition for SubstanceAmount Type: Chemical substances are a single substance type whose primary defining element is the molecular structure. Chemical substances shall be defined on the basis of their complete covalent molecular structure; the presence of a salt (counter-ion) and/or solvates (water, alcohols) is also captured. Purity, grade, physical form or particle size are not taken into account in the definition of a chemical substance or in the assignment of a Substance ID.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity amountQuantity: Used to capture quantitative values for a variety of elements. If only limits are given, the arithmetic mean would be the average. If only a single definite value for a given element is given, it would be captured in this field
    :param Range amountRange: Used to capture quantitative values for a variety of elements. If only limits are given, the arithmetic mean would be the average. If only a single definite value for a given element is given, it would be captured in this field
    :param str amountString: Used to capture quantitative values for a variety of elements. If only limits are given, the arithmetic mean would be the average. If only a single definite value for a given element is given, it would be captured in this field
    :param CodeableConcept amountType: Most elements that require a quantitative value will also have a field called amount type. Amount type should always be specified because the actual value of the amount is often dependent on it. EXAMPLE: In capturing the actual relative amounts of substances or molecular fragments it is essential to indicate whether the amount refers to a mole ratio or weight ratio. For any given element an effort should be made to use same the amount type for all related definitional elements
    :param str amountText: A textual comment on a numeric value
    :param ReferenceRange referenceRange: Reference range of possible or expected values
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "amountQuantity": {"class_name": "Quantity", "is_contained": False},
        "amountRange": {"class_name": "Range", "is_contained": False},
        "amountType": {"class_name": "CodeableConcept", "is_contained": False},
        "referenceRange": {"class_name": "ReferenceRange", "is_contained": True},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        amountQuantity: "Quantity" = None,
        amountRange: "Range" = None,
        amountString: "str" = None,
        amountType: "CodeableConcept" = None,
        amountText: "str" = None,
        referenceRange: "ReferenceRange" = None,
    ):
        self.resourceType = resourceType or "SubstanceAmount"
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.amountQuantity = amountQuantity
        self.amountRange = amountRange
        self.amountString = amountString
        self.amountType = amountType
        self.amountText = amountText
        self.referenceRange = referenceRange

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceAmount":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceAmount":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
