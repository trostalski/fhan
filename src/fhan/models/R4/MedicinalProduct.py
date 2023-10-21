"""
Generated class for MedicinalProduct. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.MarketingStatus import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Coding import *
from fhan.models.R4.DomainResource import *


class NamePart(BaseModel):
    """Coding words or phrases of the name.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str part: A fragment of a product name
    :param Coding type: Idenifying type for this part of the name (e.g. strength part)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        part: "str" = None,
        type: "Coding" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.part = part
        self.type = type

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CountryLanguage(BaseModel):
    """Country where the name applies.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept country: Country code for where this name applies
    :param CodeableConcept jurisdiction: Jurisdiction code for where this name applies
    :param CodeableConcept language: Language code for this name
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "country": {"class_name": "CodeableConcept", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "language": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        country: "CodeableConcept" = None,
        jurisdiction: "CodeableConcept" = None,
        language: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.country = country
        self.jurisdiction = jurisdiction
        self.language = language

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Name(BaseModel):
    """The product's name, including full name and possibly coded parts.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str productName: The full product name
    :param NamePart namePart: Coding words or phrases of the name
    :param CountryLanguage countryLanguage: Country where the name applies
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "namePart": {"class_name": "NamePart", "is_contained": True},
        "countryLanguage": {"class_name": "CountryLanguage", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        productName: "str" = None,
        namePart: list["NamePart"] = None,
        countryLanguage: list["CountryLanguage"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.productName = productName
        self.namePart = namePart or []
        self.countryLanguage = countryLanguage or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ManufacturingBusinessOperation(BaseModel):
    """An operation applied to the product, for manufacturing or adminsitrative purpose.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept operationType: The type of manufacturing operation
    :param Identifier authorisationReferenceNumber: Regulatory authorization reference number
    :param str effectiveDate: Regulatory authorization date
    :param CodeableConcept confidentialityIndicator: To indicate if this proces is commercially confidential
    :param Reference manufacturer: The manufacturer or establishment associated with the process
    :param Reference regulator: A regulator which oversees the operation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "operationType": {"class_name": "CodeableConcept", "is_contained": False},
        "authorisationReferenceNumber": {
            "class_name": "Identifier",
            "is_contained": False,
        },
        "confidentialityIndicator": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        "regulator": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        operationType: "CodeableConcept" = None,
        authorisationReferenceNumber: "Identifier" = None,
        effectiveDate: "str" = None,
        confidentialityIndicator: "CodeableConcept" = None,
        manufacturer: list["Reference"] = None,
        regulator: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.operationType = operationType
        self.authorisationReferenceNumber = authorisationReferenceNumber
        self.effectiveDate = effectiveDate
        self.confidentialityIndicator = confidentialityIndicator
        self.manufacturer = manufacturer or []
        self.regulator = regulator

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SpecialDesignation(BaseModel):
    """Indicates if the medicinal product has an orphan designation for the treatment of a rare disease.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier for the designation, or procedure number
    :param CodeableConcept type: The type of special designation, e.g. orphan drug, minor use
    :param CodeableConcept intendedUse: The intended use of the product, e.g. prevention, treatment
    :param CodeableConcept indicationCodeableConcept: Condition for which the medicinal use applies
    :param Reference indicationReference: Condition for which the medicinal use applies
    :param CodeableConcept status: For example granted, pending, expired or withdrawn
    :param str date: Date when the designation was granted
    :param CodeableConcept species: Animal species for which this applies
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "intendedUse": {"class_name": "CodeableConcept", "is_contained": False},
        "indicationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "indicationReference": {"class_name": "Reference", "is_contained": False},
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        "species": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        type: "CodeableConcept" = None,
        intendedUse: "CodeableConcept" = None,
        indicationCodeableConcept: "CodeableConcept" = None,
        indicationReference: "Reference" = None,
        status: "CodeableConcept" = None,
        date: "str" = None,
        species: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type
        self.intendedUse = intendedUse
        self.indicationCodeableConcept = indicationCodeableConcept
        self.indicationReference = indicationReference
        self.status = status
        self.date = date
        self.species = species

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicinalProduct(DomainResource):
    """Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this product. Could be an MPID
    :param CodeableConcept type: Regulatory type, e.g. Investigational or Authorized
    :param Coding domain: If this medicine applies to human or veterinary uses
    :param CodeableConcept combinedPharmaceuticalDoseForm: The dose form for a single part product, or combined form of a multiple part product
    :param CodeableConcept legalStatusOfSupply: The legal status of supply of the medicinal product as classified by the regulator
    :param CodeableConcept additionalMonitoringIndicator: Whether the Medicinal Product is subject to additional monitoring for regulatory reasons
    :param str specialMeasures: Whether the Medicinal Product is subject to special measures for regulatory reasons
    :param CodeableConcept paediatricUseIndicator: If authorised for use in children
    :param CodeableConcept productClassification: Allows the product to be classified by various systems
    :param MarketingStatus marketingStatus: Marketing status of the medicinal product, in contrast to marketing authorizaton
    :param Reference pharmaceuticalProduct: Pharmaceutical aspects of product
    :param Reference packagedMedicinalProduct: Package representation for the product
    :param Reference attachedDocument: Supporting documentation, typically for regulatory submission
    :param Reference masterFile: A master file for to the medicinal product (e.g. Pharmacovigilance System Master File)
    :param Reference contact: A product specific contact, person (in a role), or an organization
    :param Reference clinicalTrial: Clinical trials or studies that this product is involved in
    :param Name name: The product's name, including full name and possibly coded parts
    :param Identifier crossReference: Reference to another product, e.g. for linking authorised to investigational product
    :param ManufacturingBusinessOperation manufacturingBusinessOperation: An operation applied to the product, for manufacturing or adminsitrative purpose
    :param SpecialDesignation specialDesignation: Indicates if the medicinal product has an orphan designation for the treatment of a rare disease
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "domain": {"class_name": "Coding", "is_contained": False},
        "combinedPharmaceuticalDoseForm": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "legalStatusOfSupply": {"class_name": "CodeableConcept", "is_contained": False},
        "additionalMonitoringIndicator": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "paediatricUseIndicator": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "productClassification": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "marketingStatus": {"class_name": "MarketingStatus", "is_contained": False},
        "pharmaceuticalProduct": {"class_name": "Reference", "is_contained": False},
        "packagedMedicinalProduct": {"class_name": "Reference", "is_contained": False},
        "attachedDocument": {"class_name": "Reference", "is_contained": False},
        "masterFile": {"class_name": "Reference", "is_contained": False},
        "contact": {"class_name": "Reference", "is_contained": False},
        "clinicalTrial": {"class_name": "Reference", "is_contained": False},
        "name": {"class_name": "Name", "is_contained": True},
        "crossReference": {"class_name": "Identifier", "is_contained": False},
        "manufacturingBusinessOperation": {
            "class_name": "ManufacturingBusinessOperation",
            "is_contained": True,
        },
        "specialDesignation": {
            "class_name": "SpecialDesignation",
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
        type: "CodeableConcept" = None,
        domain: "Coding" = None,
        combinedPharmaceuticalDoseForm: "CodeableConcept" = None,
        legalStatusOfSupply: "CodeableConcept" = None,
        additionalMonitoringIndicator: "CodeableConcept" = None,
        specialMeasures: list["str"] = None,
        paediatricUseIndicator: "CodeableConcept" = None,
        productClassification: list["CodeableConcept"] = None,
        marketingStatus: list["MarketingStatus"] = None,
        pharmaceuticalProduct: list["Reference"] = None,
        packagedMedicinalProduct: list["Reference"] = None,
        attachedDocument: list["Reference"] = None,
        masterFile: list["Reference"] = None,
        contact: list["Reference"] = None,
        clinicalTrial: list["Reference"] = None,
        name: list["Name"] = None,
        crossReference: list["Identifier"] = None,
        manufacturingBusinessOperation: list["ManufacturingBusinessOperation"] = None,
        specialDesignation: list["SpecialDesignation"] = None,
    ):
        self.resourceType = resourceType or "MedicinalProduct"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type
        self.domain = domain
        self.combinedPharmaceuticalDoseForm = combinedPharmaceuticalDoseForm
        self.legalStatusOfSupply = legalStatusOfSupply
        self.additionalMonitoringIndicator = additionalMonitoringIndicator
        self.specialMeasures = specialMeasures or []
        self.paediatricUseIndicator = paediatricUseIndicator
        self.productClassification = productClassification or []
        self.marketingStatus = marketingStatus or []
        self.pharmaceuticalProduct = pharmaceuticalProduct or []
        self.packagedMedicinalProduct = packagedMedicinalProduct or []
        self.attachedDocument = attachedDocument or []
        self.masterFile = masterFile or []
        self.contact = contact or []
        self.clinicalTrial = clinicalTrial or []
        self.name = name or []
        self.crossReference = crossReference or []
        self.manufacturingBusinessOperation = manufacturingBusinessOperation or []
        self.specialDesignation = specialDesignation or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
