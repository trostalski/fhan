"""
Generated class for MedicinalProductPharmaceutical. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Ratio import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Characteristics(BaseModel):
    """Characteristics e.g. a products onset of action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: A coded characteristic
    :param CodeableConcept status: The status of characteristic e.g. assigned or pending
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "status": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        status: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.status = status

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductPharmaceutical":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductPharmaceutical":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class WithdrawalPeriod(BaseModel):
    """A species specific time during which consumption of animal product is not appropriate.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept tissue: Coded expression for the type of tissue for which the withdrawal period applues, e.g. meat, milk
    :param Quantity value: A value for the time
    :param str supportingInformation: Extra information about the withdrawal period
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "tissue": {"class_name": "CodeableConcept", "is_contained": False},
        "value": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        tissue: "CodeableConcept" = None,
        value: "Quantity" = None,
        supportingInformation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.tissue = tissue
        self.value = value
        self.supportingInformation = supportingInformation

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductPharmaceutical":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductPharmaceutical":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class TargetSpecies(BaseModel):
    """A species for which this route applies.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the species
    :param WithdrawalPeriod withdrawalPeriod: A species specific time during which consumption of animal product is not appropriate
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "withdrawalPeriod": {"class_name": "WithdrawalPeriod", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        withdrawalPeriod: list["WithdrawalPeriod"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.withdrawalPeriod = withdrawalPeriod or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductPharmaceutical":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductPharmaceutical":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RouteOfAdministration(BaseModel):
    """The path by which the pharmaceutical product is taken into or makes contact with the body.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the route
    :param Quantity firstDose: The first dose (dose quantity) administered in humans can be specified, for a product under investigation, using a numerical value and its unit of measurement
    :param Quantity maxSingleDose: The maximum single dose that can be administered as per the protocol of a clinical trial can be specified using a numerical value and its unit of measurement
    :param Quantity maxDosePerDay: The maximum dose per day (maximum dose quantity to be administered in any one 24-h period) that can be administered as per the protocol referenced in the clinical trial authorisation
    :param Ratio maxDosePerTreatmentPeriod: The maximum dose per treatment period that can be administered as per the protocol referenced in the clinical trial authorisation
    :param Duration maxTreatmentPeriod: The maximum treatment period during which an Investigational Medicinal Product can be administered as per the protocol referenced in the clinical trial authorisation
    :param TargetSpecies targetSpecies: A species for which this route applies
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "firstDose": {"class_name": "Quantity", "is_contained": False},
        "maxSingleDose": {"class_name": "Quantity", "is_contained": False},
        "maxDosePerDay": {"class_name": "Quantity", "is_contained": False},
        "maxDosePerTreatmentPeriod": {"class_name": "Ratio", "is_contained": False},
        "maxTreatmentPeriod": {"class_name": "Duration", "is_contained": False},
        "targetSpecies": {"class_name": "TargetSpecies", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        firstDose: "Quantity" = None,
        maxSingleDose: "Quantity" = None,
        maxDosePerDay: "Quantity" = None,
        maxDosePerTreatmentPeriod: "Ratio" = None,
        maxTreatmentPeriod: "Duration" = None,
        targetSpecies: list["TargetSpecies"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.firstDose = firstDose
        self.maxSingleDose = maxSingleDose
        self.maxDosePerDay = maxDosePerDay
        self.maxDosePerTreatmentPeriod = maxDosePerTreatmentPeriod
        self.maxTreatmentPeriod = maxTreatmentPeriod
        self.targetSpecies = targetSpecies or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductPharmaceutical":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductPharmaceutical":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicinalProductPharmaceutical(DomainResource):
    """A pharmaceutical product described in terms of its composition and dose form.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: An identifier for the pharmaceutical medicinal product
    :param CodeableConcept administrableDoseForm: The administrable dose form, after necessary reconstitution
    :param CodeableConcept unitOfPresentation: Todo
    :param Reference ingredient: Ingredient
    :param Reference device: Accompanying device
    :param Characteristics characteristics: Characteristics e.g. a products onset of action
    :param RouteOfAdministration routeOfAdministration: The path by which the pharmaceutical product is taken into or makes contact with the body
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "administrableDoseForm": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "unitOfPresentation": {"class_name": "CodeableConcept", "is_contained": False},
        "ingredient": {"class_name": "Reference", "is_contained": False},
        "device": {"class_name": "Reference", "is_contained": False},
        "characteristics": {"class_name": "Characteristics", "is_contained": True},
        "routeOfAdministration": {
            "class_name": "RouteOfAdministration",
            "is_contained": True,
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
        identifier: list["Identifier"] = None,
        administrableDoseForm: "CodeableConcept" = None,
        unitOfPresentation: "CodeableConcept" = None,
        ingredient: list["Reference"] = None,
        device: list["Reference"] = None,
        characteristics: list["Characteristics"] = None,
        routeOfAdministration: list["RouteOfAdministration"] = None,
    ):
        self.resourceType = resourceType or "MedicinalProductPharmaceutical"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.administrableDoseForm = administrableDoseForm
        self.unitOfPresentation = unitOfPresentation
        self.ingredient = ingredient or []
        self.device = device or []
        self.characteristics = characteristics or []
        self.routeOfAdministration = routeOfAdministration or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductPharmaceutical":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductPharmaceutical":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
