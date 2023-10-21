"""
Generated class for InsurancePlan. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Money import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Address import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Contact(BaseModel):
    """The contact for the health insurance product for a certain purpose.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept purpose: The type of contact
    :param HumanName name: A name associated with the contact
    :param ContactPoint telecom: Contact details (telephone, email, etc.)  for a contact
    :param Address address: Visiting or postal addresses for the contact
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "purpose": {"class_name": "CodeableConcept", "is_contained": False},
        "name": {"class_name": "HumanName", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "address": {"class_name": "Address", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        purpose: "CodeableConcept" = None,
        name: "HumanName" = None,
        telecom: list["ContactPoint"] = None,
        address: "Address" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.purpose = purpose
        self.name = name
        self.telecom = telecom or []
        self.address = address

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Limit(BaseModel):
    """The specific limits on the benefit.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity value: Maximum value allowed
    :param CodeableConcept code: Benefit limit details
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "value": {"class_name": "Quantity", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        value: "Quantity" = None,
        code: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.value = value
        self.code = code

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Benefit(BaseModel):
    """Specific benefits under this type of coverage.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of benefit
    :param str requirement: Referral requirements
    :param Limit limit: Benefit limits
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "limit": {"class_name": "Limit", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        requirement: "str" = None,
        limit: list["Limit"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.requirement = requirement
        self.limit = limit or []

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Coverage(BaseModel):
    """Details about the coverage offered by the insurance product.:param Reference coverageArea: Where product applies
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of coverage
    :param Reference network: What networks provide coverage
    :param Benefit benefit: List of benefits
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "coverageArea": {"class_name": "Reference", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "network": {"class_name": "Reference", "is_contained": False},
        "benefit": {"class_name": "Benefit", "is_contained": True},
    }

    def __init__(
        self,
        coverageArea: list["Reference"] = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        network: list["Reference"] = None,
        benefit: list["Benefit"] = None,
    ):
        self.coverageArea = coverageArea or []
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.network = network or []
        self.benefit = benefit or []

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class GeneralCost(BaseModel):
    """Overall costs associated with the plan.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param int groupSize: Number of enrollees
    :param Money cost: Cost value
    :param str comment: Additional cost information
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
        groupSize: "int" = None,
        cost: "Money" = None,
        comment: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.groupSize = groupSize
        self.cost = cost
        self.comment = comment

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Cost(BaseModel):
    """List of the costs associated with a specific benefit.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param CodeableConcept applicability: in-network | out-of-network | other
    :param CodeableConcept qualifiers: Additional information about the cost
    :param Quantity value: The actual cost value
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "applicability": {"class_name": "CodeableConcept", "is_contained": False},
        "qualifiers": {"class_name": "CodeableConcept", "is_contained": False},
        "value": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        applicability: "CodeableConcept" = None,
        qualifiers: list["CodeableConcept"] = None,
        value: "Quantity" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.applicability = applicability
        self.qualifiers = qualifiers or []
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Benefit(BaseModel):
    """List of the specific benefits under this category of benefit.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of specific benefit
    :param Cost cost: List of the costs
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "cost": {"class_name": "Cost", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        cost: list["Cost"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.cost = cost or []

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SpecificCost(BaseModel):
    """Costs associated with the coverage provided by the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: General category of benefit
    :param Benefit benefit: Benefits list
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "benefit": {"class_name": "Benefit", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        category: "CodeableConcept" = None,
        benefit: list["Benefit"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category
        self.benefit = benefit or []

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Plan(BaseModel):
    """Details about an insurance plan.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business Identifier for Product
    :param CodeableConcept type: Type of plan
    :param Reference coverageArea: Where product applies
    :param Reference network: What networks provide coverage
    :param GeneralCost generalCost: Overall costs
    :param SpecificCost specificCost: Specific costs
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "coverageArea": {"class_name": "Reference", "is_contained": False},
        "network": {"class_name": "Reference", "is_contained": False},
        "generalCost": {"class_name": "GeneralCost", "is_contained": True},
        "specificCost": {"class_name": "SpecificCost", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        type: "CodeableConcept" = None,
        coverageArea: list["Reference"] = None,
        network: list["Reference"] = None,
        generalCost: list["GeneralCost"] = None,
        specificCost: list["SpecificCost"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type
        self.coverageArea = coverageArea or []
        self.network = network or []
        self.generalCost = generalCost or []
        self.specificCost = specificCost or []

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class InsurancePlan(DomainResource):
    """Details of a Health Insurance product/plan provided by an organization.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for Product
    :param str status: draft | active | retired | unknown
    :param CodeableConcept type: Kind of product
    :param str name: Official name
    :param str alias: Alternate names
    :param Period period: When the product is available
    :param Reference ownedBy: Plan issuer
    :param Reference administeredBy: Product administrator
    :param Reference coverageArea: Where product applies
    :param Contact contact: Contact for the product
    :param Reference endpoint: Technical endpoint
    :param Reference network: What networks are Included
    :param Coverage coverage: Coverage details
    :param Plan plan: Plan details
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
        "period": {"class_name": "Period", "is_contained": False},
        "ownedBy": {"class_name": "Reference", "is_contained": False},
        "administeredBy": {"class_name": "Reference", "is_contained": False},
        "coverageArea": {"class_name": "Reference", "is_contained": False},
        "contact": {"class_name": "Contact", "is_contained": True},
        "endpoint": {"class_name": "Reference", "is_contained": False},
        "network": {"class_name": "Reference", "is_contained": False},
        "coverage": {"class_name": "Coverage", "is_contained": True},
        "plan": {"class_name": "Plan", "is_contained": True},
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
        type: list["CodeableConcept"] = None,
        name: "str" = None,
        alias: list["str"] = None,
        period: "Period" = None,
        ownedBy: "Reference" = None,
        administeredBy: "Reference" = None,
        coverageArea: list["Reference"] = None,
        contact: list["Contact"] = None,
        endpoint: list["Reference"] = None,
        network: list["Reference"] = None,
        coverage: list["Coverage"] = None,
        plan: list["Plan"] = None,
    ):
        self.resourceType = resourceType or "InsurancePlan"
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
        self.type = type or []
        self.name = name
        self.alias = alias or []
        self.period = period
        self.ownedBy = ownedBy
        self.administeredBy = administeredBy
        self.coverageArea = coverageArea or []
        self.contact = contact or []
        self.endpoint = endpoint or []
        self.network = network or []
        self.coverage = coverage or []
        self.plan = plan or []

    @classmethod
    def from_dict(cls, data: dict) -> "InsurancePlan":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "InsurancePlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
