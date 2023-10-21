"""
Generated class for MedicinalProductContraindication. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Population import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class OtherTherapy(BaseModel):
    """Information about the use of the medicinal product in relation to other therapies described as part of the indication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept therapyRelationshipType: The type of relationship between the medicinal product indication or contraindication and another therapy
    :param CodeableConcept medicationCodeableConcept: Reference to a specific medication (active substance, medicinal product or class of products) as part of an indication or contraindication
    :param Reference medicationReference: Reference to a specific medication (active substance, medicinal product or class of products) as part of an indication or contraindication
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "therapyRelationshipType": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "medicationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "medicationReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        therapyRelationshipType: "CodeableConcept" = None,
        medicationCodeableConcept: "CodeableConcept" = None,
        medicationReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.therapyRelationshipType = therapyRelationshipType
        self.medicationCodeableConcept = medicationCodeableConcept
        self.medicationReference = medicationReference

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductContraindication":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductContraindication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicinalProductContraindication(DomainResource):
    """The clinical particulars - indications, contraindications etc. of a medicinal product, including for regulatory purposes.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference subject: The medication for which this is an indication
    :param CodeableConcept disease: The disease, symptom or procedure for the contraindication
    :param CodeableConcept diseaseStatus: The status of the disease or symptom for the contraindication
    :param CodeableConcept comorbidity: A comorbidity (concurrent condition) or coinfection
    :param Reference therapeuticIndication: Information about the use of the medicinal product in relation to other therapies as part of the indication
    :param OtherTherapy otherTherapy: Information about the use of the medicinal product in relation to other therapies described as part of the indication
    :param Population population: The population group to which this applies
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "disease": {"class_name": "CodeableConcept", "is_contained": False},
        "diseaseStatus": {"class_name": "CodeableConcept", "is_contained": False},
        "comorbidity": {"class_name": "CodeableConcept", "is_contained": False},
        "therapeuticIndication": {"class_name": "Reference", "is_contained": False},
        "otherTherapy": {"class_name": "OtherTherapy", "is_contained": True},
        "population": {"class_name": "Population", "is_contained": False},
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
        subject: list["Reference"] = None,
        disease: "CodeableConcept" = None,
        diseaseStatus: "CodeableConcept" = None,
        comorbidity: list["CodeableConcept"] = None,
        therapeuticIndication: list["Reference"] = None,
        otherTherapy: list["OtherTherapy"] = None,
        population: list["Population"] = None,
    ):
        self.resourceType = resourceType or "MedicinalProductContraindication"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.subject = subject or []
        self.disease = disease
        self.diseaseStatus = diseaseStatus
        self.comorbidity = comorbidity or []
        self.therapeuticIndication = therapeuticIndication or []
        self.otherTherapy = otherTherapy or []
        self.population = population or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductContraindication":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductContraindication":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
