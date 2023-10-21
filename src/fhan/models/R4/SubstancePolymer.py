"""
Generated class for SubstancePolymer. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.SubstanceAmount import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class StartingMaterial(BaseModel):
    """Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: Todo
    :param CodeableConcept type: Todo
    :param bool isDefining: Todo
    :param SubstanceAmount amount: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "material": {"class_name": "CodeableConcept", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "SubstanceAmount", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        material: "CodeableConcept" = None,
        type: "CodeableConcept" = None,
        isDefining: "bool" = None,
        amount: "SubstanceAmount" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.material = material
        self.type = type
        self.isDefining = isDefining
        self.amount = amount

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MonomerSet(BaseModel):
    """Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept ratioType: Todo
    :param StartingMaterial startingMaterial: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "ratioType": {"class_name": "CodeableConcept", "is_contained": False},
        "startingMaterial": {"class_name": "StartingMaterial", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        ratioType: "CodeableConcept" = None,
        startingMaterial: list["StartingMaterial"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.ratioType = ratioType
        self.startingMaterial = startingMaterial or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DegreeOfPolymerisation(BaseModel):
    """Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept degree: Todo
    :param SubstanceAmount amount: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "degree": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "SubstanceAmount", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        degree: "CodeableConcept" = None,
        amount: "SubstanceAmount" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.degree = degree
        self.amount = amount

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class StructuralRepresentation(BaseModel):
    """Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Todo
    :param str representation: Todo
    :param Attachment attachment: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "attachment": {"class_name": "Attachment", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        representation: "str" = None,
        attachment: "Attachment" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.representation = representation
        self.attachment = attachment

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RepeatUnit(BaseModel):
    """Todo.:param CodeableConcept repeatUnitAmountType: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept orientationOfPolymerisation: Todo
    :param str repeatUnit: Todo
    :param SubstanceAmount amount: Todo
    :param DegreeOfPolymerisation degreeOfPolymerisation: Todo
    :param StructuralRepresentation structuralRepresentation: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "repeatUnitAmountType": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "orientationOfPolymerisation": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "amount": {"class_name": "SubstanceAmount", "is_contained": False},
        "degreeOfPolymerisation": {
            "class_name": "DegreeOfPolymerisation",
            "is_contained": True,
        },
        "structuralRepresentation": {
            "class_name": "StructuralRepresentation",
            "is_contained": True,
        },
    }

    def __init__(
        self,
        repeatUnitAmountType: "CodeableConcept" = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        orientationOfPolymerisation: "CodeableConcept" = None,
        repeatUnit: "str" = None,
        amount: "SubstanceAmount" = None,
        degreeOfPolymerisation: list["DegreeOfPolymerisation"] = None,
        structuralRepresentation: list["StructuralRepresentation"] = None,
    ):
        self.repeatUnitAmountType = repeatUnitAmountType
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.orientationOfPolymerisation = orientationOfPolymerisation
        self.repeatUnit = repeatUnit
        self.amount = amount
        self.degreeOfPolymerisation = degreeOfPolymerisation or []
        self.structuralRepresentation = structuralRepresentation or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Repeat(BaseModel):
    """Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int numberOfUnits: Todo
    :param str averageMolecularFormula: Todo
    :param CodeableConcept repeatUnitAmountType: Todo
    :param RepeatUnit repeatUnit: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "repeatUnitAmountType": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "repeatUnit": {"class_name": "RepeatUnit", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        numberOfUnits: "int" = None,
        averageMolecularFormula: "str" = None,
        repeatUnitAmountType: "CodeableConcept" = None,
        repeatUnit: list["RepeatUnit"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.numberOfUnits = numberOfUnits
        self.averageMolecularFormula = averageMolecularFormula
        self.repeatUnitAmountType = repeatUnitAmountType
        self.repeatUnit = repeatUnit or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubstancePolymer(DomainResource):
    """Todo.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept _class: Todo
    :param CodeableConcept geometry: Todo
    :param CodeableConcept copolymerConnectivity: Todo
    :param str modification: Todo
    :param MonomerSet monomerSet: Todo
    :param Repeat repeat: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "_class": {"class_name": "CodeableConcept", "is_contained": False},
        "geometry": {"class_name": "CodeableConcept", "is_contained": False},
        "copolymerConnectivity": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "monomerSet": {"class_name": "MonomerSet", "is_contained": True},
        "repeat": {"class_name": "Repeat", "is_contained": True},
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
        _class: "CodeableConcept" = None,
        geometry: "CodeableConcept" = None,
        copolymerConnectivity: list["CodeableConcept"] = None,
        modification: list["str"] = None,
        monomerSet: list["MonomerSet"] = None,
        repeat: list["Repeat"] = None,
    ):
        self.resourceType = resourceType or "SubstancePolymer"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self._class = _class
        self.geometry = geometry
        self.copolymerConnectivity = copolymerConnectivity or []
        self.modification = modification or []
        self.monomerSet = monomerSet or []
        self.repeat = repeat or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
