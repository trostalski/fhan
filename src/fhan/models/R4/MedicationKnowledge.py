"""
Generated class for MedicationKnowledge. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Ratio import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Duration import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class RelatedMedicationKnowledge(BaseModel):
    """Associated or related knowledge about a medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of medicationKnowledge
    :param Reference reference: Associated documentation about the associated medication knowledge
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        reference: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.reference = reference or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Monograph(BaseModel):
    """Associated documentation about the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of medication document
    :param Reference source: Associated documentation about the medication
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        source: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.source = source

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Ingredient(BaseModel):
    """Identifies a particular constituent of interest in the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept itemCodeableConcept: Medication(s) or substance(s) contained in the medication
    :param Reference itemReference: Medication(s) or substance(s) contained in the medication
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
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Cost(BaseModel):
    """The price of the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of the cost information
    :param str source: The source or owner for the price information
    :param Money cost: The price of the medication
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "cost": {"class_name": "Money", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        source: "str" = None,
        cost: "Money" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.source = source
        self.cost = cost

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MonitoringProgram(BaseModel):
    """The program under which the medication is reviewed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of program under which the medication is monitored
    :param str name: Name of the reviewing program
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        name: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.name = name

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Dosage(BaseModel):
    """Dosage for the medication for the specific guidelines.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of dosage
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "dosage": {"class_name": "Dosage", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        dosage: list["Dosage"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.dosage = dosage or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PatientCharacteristics(BaseModel):
    """Characteristics of the patient that are relevant to the administration guidelines (for example, height, weight, gender, etc.).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param Quantity characteristicQuantity: Specific characteristic that is relevant to the administration guideline
    :param str value: The specific characteristic
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "characteristicCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "characteristicQuantity": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        characteristicCodeableConcept: "CodeableConcept" = None,
        characteristicQuantity: "Quantity" = None,
        value: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.characteristicCodeableConcept = characteristicCodeableConcept
        self.characteristicQuantity = characteristicQuantity
        self.value = value or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AdministrationGuidelines(BaseModel):
    """Guidelines for the administration of the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    :param CodeableConcept indicationCodeableConcept: Indication for use that apply to the specific administration guidelines
    :param Reference indicationReference: Indication for use that apply to the specific administration guidelines
    :param PatientCharacteristics patientCharacteristics: Characteristics of the patient that are relevant to the administration guidelines
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "dosage": {"class_name": "Dosage", "is_contained": True},
        "indicationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "indicationReference": {"class_name": "Reference", "is_contained": False},
        "patientCharacteristics": {
            "class_name": "PatientCharacteristics",
            "is_contained": True,
        },
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        dosage: list["Dosage"] = None,
        indicationCodeableConcept: "CodeableConcept" = None,
        indicationReference: "Reference" = None,
        patientCharacteristics: list["PatientCharacteristics"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.dosage = dosage or []
        self.indicationCodeableConcept = indicationCodeableConcept
        self.indicationReference = indicationReference
        self.patientCharacteristics = patientCharacteristics or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicineClassification(BaseModel):
    """Categorization of the medication within a formulary or classification system.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of category for the medication (for example, therapeutic classification, therapeutic sub-classification)
    :param CodeableConcept classification: Specific category assigned to the medication
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "classification": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        classification: list["CodeableConcept"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.classification = classification or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Packaging(BaseModel):
    """Information that only applies to packages (not products).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code that defines the specific type of packaging that the medication can be found in
    :param Quantity quantity: The number of product units the package would contain if fully loaded
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        quantity: "Quantity" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.quantity = quantity

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DrugCharacteristic(BaseModel):
    """Specifies descriptive properties of the medicine, such as color, shape, imprints, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code specifying the type of characteristic of medication
    :param CodeableConcept valueCodeableConcept: Description of the characteristic
    :param str valueString: Description of the characteristic
    :param Quantity valueQuantity: Description of the characteristic
    :param str valueBase64Binary: Description of the characteristic
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "valueCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        valueCodeableConcept: "CodeableConcept" = None,
        valueString: "str" = None,
        valueQuantity: "Quantity" = None,
        valueBase64Binary: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.valueCodeableConcept = valueCodeableConcept
        self.valueString = valueString
        self.valueQuantity = valueQuantity
        self.valueBase64Binary = valueBase64Binary

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Substitution(BaseModel):
    """Specifies if changes are allowed when dispensing a medication from a regulatory perspective.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Specifies the type of substitution allowed
    :param bool allowed: Specifies if regulation allows for changes in the medication when dispensing
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        allowed: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.allowed = allowed

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Schedule(BaseModel):
    """Specifies the schedule of a medication in jurisdiction.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept schedule: Specifies the specific drug schedule
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "schedule": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        schedule: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.schedule = schedule

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MaxDispense(BaseModel):
    """The maximum number of units of the medication that can be dispensed in a period.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: The maximum number of units of the medication that can be dispensed
    :param Duration period: The period that applies to the maximum number of units
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "period": {"class_name": "Duration", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        quantity: "Quantity" = None,
        period: "Duration" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.quantity = quantity
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Regulatory(BaseModel):
    """Regulatory information about a medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference regulatoryAuthority: Specifies the authority of the regulation
    :param Substitution substitution: Specifies if changes are allowed when dispensing a medication from a regulatory perspective
    :param Schedule schedule: Specifies the schedule of a medication in jurisdiction
    :param MaxDispense maxDispense: The maximum number of units of the medication that can be dispensed in a period
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "regulatoryAuthority": {"class_name": "Reference", "is_contained": False},
        "substitution": {"class_name": "Substitution", "is_contained": True},
        "schedule": {"class_name": "Schedule", "is_contained": True},
        "maxDispense": {"class_name": "MaxDispense", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        regulatoryAuthority: "Reference" = None,
        substitution: list["Substitution"] = None,
        schedule: list["Schedule"] = None,
        maxDispense: "MaxDispense" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.regulatoryAuthority = regulatoryAuthority
        self.substitution = substitution or []
        self.schedule = schedule or []
        self.maxDispense = maxDispense

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Kinetics(BaseModel):
    """The time course of drug absorption, distribution, metabolism and excretion of a medication from the body.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity areaUnderCurve: The drug concentration measured at certain discrete points in time
    :param Quantity lethalDose50: The median lethal dose of a drug
    :param Duration halfLifePeriod: Time required for concentration in the body to decrease by half
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "areaUnderCurve": {"class_name": "Quantity", "is_contained": False},
        "lethalDose50": {"class_name": "Quantity", "is_contained": False},
        "halfLifePeriod": {"class_name": "Duration", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        areaUnderCurve: list["Quantity"] = None,
        lethalDose50: list["Quantity"] = None,
        halfLifePeriod: "Duration" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.areaUnderCurve = areaUnderCurve or []
        self.lethalDose50 = lethalDose50 or []
        self.halfLifePeriod = halfLifePeriod

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicationKnowledge(DomainResource):
    """Information about a medication that is used to support knowledge.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept code: Code that identifies this medication
    :param str status: active | inactive | entered-in-error
    :param Reference manufacturer: Manufacturer of the item
    :param CodeableConcept doseForm: powder | tablets | capsule +
    :param Quantity amount: Amount of drug in package
    :param str synonym: Additional names for a medication
    :param RelatedMedicationKnowledge relatedMedicationKnowledge: Associated or related medication information
    :param Reference associatedMedication: A medication resource that is associated with this medication
    :param CodeableConcept productType: Category of the medication or product
    :param Monograph monograph: Associated documentation about the medication
    :param Ingredient ingredient: Active or inactive ingredient
    :param str preparationInstruction: The instructions for preparing the medication
    :param CodeableConcept intendedRoute: The intended or approved route of administration
    :param Cost cost: The pricing of the medication
    :param MonitoringProgram monitoringProgram: Program under which a medication is reviewed
    :param AdministrationGuidelines administrationGuidelines: Guidelines for administration of the medication
    :param MedicineClassification medicineClassification: Categorization of the medication within a formulary or classification system
    :param Packaging packaging: Details about packaged medications
    :param DrugCharacteristic drugCharacteristic: Specifies descriptive properties of the medicine
    :param Reference contraindication: Potential clinical issue with or between medication(s)
    :param Regulatory regulatory: Regulatory information about a medication
    :param Kinetics kinetics: The time course of drug absorption, distribution, metabolism and excretion of a medication from the body
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        "doseForm": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Quantity", "is_contained": False},
        "relatedMedicationKnowledge": {
            "class_name": "RelatedMedicationKnowledge",
            "is_contained": True,
        },
        "associatedMedication": {"class_name": "Reference", "is_contained": False},
        "productType": {"class_name": "CodeableConcept", "is_contained": False},
        "monograph": {"class_name": "Monograph", "is_contained": True},
        "ingredient": {"class_name": "Ingredient", "is_contained": True},
        "intendedRoute": {"class_name": "CodeableConcept", "is_contained": False},
        "cost": {"class_name": "Cost", "is_contained": True},
        "monitoringProgram": {"class_name": "MonitoringProgram", "is_contained": True},
        "administrationGuidelines": {
            "class_name": "AdministrationGuidelines",
            "is_contained": True,
        },
        "medicineClassification": {
            "class_name": "MedicineClassification",
            "is_contained": True,
        },
        "packaging": {"class_name": "Packaging", "is_contained": True},
        "drugCharacteristic": {
            "class_name": "DrugCharacteristic",
            "is_contained": True,
        },
        "contraindication": {"class_name": "Reference", "is_contained": False},
        "regulatory": {"class_name": "Regulatory", "is_contained": True},
        "kinetics": {"class_name": "Kinetics", "is_contained": True},
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
        code: "CodeableConcept" = None,
        status: "str" = None,
        manufacturer: "Reference" = None,
        doseForm: "CodeableConcept" = None,
        amount: "Quantity" = None,
        synonym: list["str"] = None,
        relatedMedicationKnowledge: list["RelatedMedicationKnowledge"] = None,
        associatedMedication: list["Reference"] = None,
        productType: list["CodeableConcept"] = None,
        monograph: list["Monograph"] = None,
        ingredient: list["Ingredient"] = None,
        preparationInstruction: "str" = None,
        intendedRoute: list["CodeableConcept"] = None,
        cost: list["Cost"] = None,
        monitoringProgram: list["MonitoringProgram"] = None,
        administrationGuidelines: list["AdministrationGuidelines"] = None,
        medicineClassification: list["MedicineClassification"] = None,
        packaging: "Packaging" = None,
        drugCharacteristic: list["DrugCharacteristic"] = None,
        contraindication: list["Reference"] = None,
        regulatory: list["Regulatory"] = None,
        kinetics: list["Kinetics"] = None,
    ):
        self.resourceType = resourceType or "MedicationKnowledge"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.status = status
        self.manufacturer = manufacturer
        self.doseForm = doseForm
        self.amount = amount
        self.synonym = synonym or []
        self.relatedMedicationKnowledge = relatedMedicationKnowledge or []
        self.associatedMedication = associatedMedication or []
        self.productType = productType or []
        self.monograph = monograph or []
        self.ingredient = ingredient or []
        self.preparationInstruction = preparationInstruction
        self.intendedRoute = intendedRoute or []
        self.cost = cost or []
        self.monitoringProgram = monitoringProgram or []
        self.administrationGuidelines = administrationGuidelines or []
        self.medicineClassification = medicineClassification or []
        self.packaging = packaging
        self.drugCharacteristic = drugCharacteristic or []
        self.contraindication = contraindication or []
        self.regulatory = regulatory or []
        self.kinetics = kinetics or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
