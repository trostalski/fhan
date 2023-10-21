"""
Generated class for Account. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Coverage(BaseModel):
    """The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference coverage: The party(s), such as insurances, that may contribute to the payment of this account
    :param int priority: The priority of the coverage in the context of this account
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
        coverage: "Reference" = None,
        priority: "int" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.coverage = coverage
        self.priority = priority

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Guarantor(BaseModel):
    """The parties responsible for balancing the account if other payment options fall short.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference party: Responsible entity
    :param bool onHold: Credit or other hold applied
    :param Period period: Guarantee account during
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "party": {"class_name": "Reference", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        party: "Reference" = None,
        onHold: "bool" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.party = party
        self.onHold = onHold
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Account(DomainResource):
    """A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Account number
    :param str status: active | inactive | entered-in-error | on-hold | unknown
    :param CodeableConcept type: E.g. patient, expense, depreciation
    :param str name: Human-readable label
    :param Reference subject: The entity that caused the expenses
    :param Period servicePeriod: Transaction window
    :param Coverage coverage: The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
    :param Reference owner: Entity managing the Account
    :param str description: Explanation of purpose/use
    :param Guarantor guarantor: The parties ultimately responsible for balancing the Account
    :param Reference partOf: Reference to a parent Account
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
        "subject": {"class_name": "Reference", "is_contained": False},
        "servicePeriod": {"class_name": "Period", "is_contained": False},
        "coverage": {"class_name": "Coverage", "is_contained": True},
        "owner": {"class_name": "Reference", "is_contained": False},
        "guarantor": {"class_name": "Guarantor", "is_contained": True},
        "partOf": {"class_name": "Reference", "is_contained": False},
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
        type: "CodeableConcept" = None,
        name: "str" = None,
        subject: list["Reference"] = None,
        servicePeriod: "Period" = None,
        coverage: list["Coverage"] = None,
        owner: "Reference" = None,
        description: "str" = None,
        guarantor: list["Guarantor"] = None,
        partOf: "Reference" = None,
    ):
        self.resourceType = resourceType or "Account"
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
        self.type = type
        self.name = name
        self.subject = subject or []
        self.servicePeriod = servicePeriod
        self.coverage = coverage or []
        self.owner = owner
        self.description = description
        self.guarantor = guarantor or []
        self.partOf = partOf

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Account":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
