"""
Generated class for VisionPrescription. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Prism(BaseModel):
    """Allows for adjustment on two axis.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param float amount: Amount of adjustment
    :param str base: up | down | in | out
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
        amount: "float" = None,
        base: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.amount = amount
        self.base = base

    @classmethod
    def from_dict(cls, data: dict) -> "VisionPrescription":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "VisionPrescription":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class LensSpecification(BaseModel):
    """Contain the details of  the individual lens specifications and serves as the authorization for the fullfillment by certified professionals.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept product: Product to be supplied
    :param str eye: right | left
    :param float sphere: Power of the lens
    :param float cylinder: Lens power for astigmatism
    :param int axis: Lens meridian which contain no power for astigmatism
    :param Prism prism: Eye alignment compensation
    :param float add: Added power for multifocal levels
    :param float power: Contact lens power
    :param float backCurve: Contact lens back curvature
    :param float diameter: Contact lens diameter
    :param Quantity duration: Lens wear duration
    :param str color: Color required
    :param str brand: Brand required
    :param Annotation note: Notes for coatings
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "product": {"class_name": "CodeableConcept", "is_contained": False},
        "prism": {"class_name": "Prism", "is_contained": True},
        "duration": {"class_name": "Quantity", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        product: "CodeableConcept" = None,
        eye: "str" = None,
        sphere: "float" = None,
        cylinder: "float" = None,
        axis: "int" = None,
        prism: list["Prism"] = None,
        add: "float" = None,
        power: "float" = None,
        backCurve: "float" = None,
        diameter: "float" = None,
        duration: "Quantity" = None,
        color: "str" = None,
        brand: "str" = None,
        note: list["Annotation"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.product = product
        self.eye = eye
        self.sphere = sphere
        self.cylinder = cylinder
        self.axis = axis
        self.prism = prism or []
        self.add = add
        self.power = power
        self.backCurve = backCurve
        self.diameter = diameter
        self.duration = duration
        self.color = color
        self.brand = brand
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "VisionPrescription":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "VisionPrescription":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class VisionPrescription(DomainResource):
    """An authorization for the provision of glasses and/or contact lenses to a patient.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for vision prescription
    :param str status: active | cancelled | draft | entered-in-error
    :param str created: Response creation date
    :param Reference patient: Who prescription is for
    :param Reference encounter: Created during encounter / admission / stay
    :param str dateWritten: When prescription was authorized
    :param Reference prescriber: Who authorized the vision prescription
    :param LensSpecification lensSpecification: Vision lens authorization
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "prescriber": {"class_name": "Reference", "is_contained": False},
        "lensSpecification": {"class_name": "LensSpecification", "is_contained": True},
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
        created: "str" = None,
        patient: "Reference" = None,
        encounter: "Reference" = None,
        dateWritten: "str" = None,
        prescriber: "Reference" = None,
        lensSpecification: list["LensSpecification"] = None,
    ):
        self.resourceType = resourceType or "VisionPrescription"
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
        self.created = created
        self.patient = patient
        self.encounter = encounter
        self.dateWritten = dateWritten
        self.prescriber = prescriber
        self.lensSpecification = lensSpecification or []

    @classmethod
    def from_dict(cls, data: dict) -> "VisionPrescription":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "VisionPrescription":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
