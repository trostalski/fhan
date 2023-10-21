"""
Generated class for CoverageEligibilityRequest. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class SupportingInfo(BaseModel):
    """Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Information instance identifier
    :param Reference information: Data to be provided
    :param bool appliesToAll: Applies to all items
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "information": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        information: "Reference" = None,
        appliesToAll: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.information = information
        self.appliesToAll = appliesToAll

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Insurance(BaseModel):
    """Financial instruments for reimbursement for the health care products and services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool focal: Applicable coverage
    :param Reference coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "coverage": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        focal: "bool" = None,
        coverage: "Reference" = None,
        businessArrangement: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.focal = focal
        self.coverage = coverage
        self.businessArrangement = businessArrangement

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Diagnosis(BaseModel):
    """Patient diagnosis for which care is sought.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept diagnosisCodeableConcept: Nature of illness or problem
    :param Reference diagnosisReference: Nature of illness or problem
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "diagnosisCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "diagnosisReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        diagnosisCodeableConcept: "CodeableConcept" = None,
        diagnosisReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.diagnosisCodeableConcept = diagnosisCodeableConcept
        self.diagnosisReference = diagnosisReference

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Item(BaseModel):
    """Service categories or billable services for which benefit details and/or an authorization prior to service delivery may be required by the payor.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int supportingInfoSequence: Applicable exception or supporting information
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Product or service billing modifiers
    :param Reference provider: Perfoming practitioner
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param Reference facility: Servicing facility
    :param Diagnosis diagnosis: Applicable diagnosis
    :param Reference detail: Product or service details
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "facility": {"class_name": "Reference", "is_contained": False},
        "diagnosis": {"class_name": "Diagnosis", "is_contained": True},
        "detail": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        supportingInfoSequence: list["int"] = None,
        category: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        provider: "Reference" = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        facility: "Reference" = None,
        diagnosis: list["Diagnosis"] = None,
        detail: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.supportingInfoSequence = supportingInfoSequence or []
        self.category = category
        self.productOrService = productOrService
        self.modifier = modifier or []
        self.provider = provider
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.facility = facility
        self.diagnosis = diagnosis or []
        self.detail = detail or []

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CoverageEligibilityRequest(DomainResource):
    """The CoverageEligibilityRequest provides patient and insurance coverage information to an insurer for them to respond, in the form of an CoverageEligibilityResponse, with information regarding whether the stated coverage is valid and in-force and optionally to provide the insurance details of the policy.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for coverage eligiblity request
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept priority: Desired processing priority
    :param str purpose: auth-requirements | benefits | discovery | validation
    :param Reference patient: Intended recipient of products and services
    :param str servicedDate: Estimated date or dates of service
    :param Period servicedPeriod: Estimated date or dates of service
    :param str created: Creation date
    :param Reference enterer: Author
    :param Reference provider: Party responsible for the request
    :param Reference insurer: Coverage issuer
    :param Reference facility: Servicing facility
    :param SupportingInfo supportingInfo: Supporting information
    :param Insurance insurance: Patient insurance information
    :param Item item: Item to be evaluated for eligibiity
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "priority": {"class_name": "CodeableConcept", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "servicedPeriod": {"class_name": "Period", "is_contained": False},
        "enterer": {"class_name": "Reference", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "insurer": {"class_name": "Reference", "is_contained": False},
        "facility": {"class_name": "Reference", "is_contained": False},
        "supportingInfo": {"class_name": "SupportingInfo", "is_contained": True},
        "insurance": {"class_name": "Insurance", "is_contained": True},
        "item": {"class_name": "Item", "is_contained": True},
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
        priority: "CodeableConcept" = None,
        purpose: list["str"] = None,
        patient: "Reference" = None,
        servicedDate: "str" = None,
        servicedPeriod: "Period" = None,
        created: "str" = None,
        enterer: "Reference" = None,
        provider: "Reference" = None,
        insurer: "Reference" = None,
        facility: "Reference" = None,
        supportingInfo: list["SupportingInfo"] = None,
        insurance: list["Insurance"] = None,
        item: list["Item"] = None,
    ):
        self.resourceType = resourceType or "CoverageEligibilityRequest"
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
        self.priority = priority
        self.purpose = purpose or []
        self.patient = patient
        self.servicedDate = servicedDate
        self.servicedPeriod = servicedPeriod
        self.created = created
        self.enterer = enterer
        self.provider = provider
        self.insurer = insurer
        self.facility = facility
        self.supportingInfo = supportingInfo or []
        self.insurance = insurance or []
        self.item = item or []

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
