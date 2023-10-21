"""
Generated class for Coverage. 
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


class _class(BaseModel):
    """A suite of underwriter specific classifiers.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of class such as 'group' or 'plan'
    :param str value: Value associated with the type
    :param str name: Human readable description of the type and value
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
        value: "str" = None,
        name: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.value = value
        self.name = name

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Coverage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Exception(BaseModel):
    """A suite of codes indicating exceptions or reductions to patient costs and their effective periods.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Exception category
    :param Period period: The effective period of the exception
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Coverage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CostToBeneficiary(BaseModel):
    """A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Cost category
    :param Quantity valueQuantity: The amount or percentage due from the beneficiary
    :param Money valueMoney: The amount or percentage due from the beneficiary
    :param Exception exception: Exceptions for patient payments
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueMoney": {"class_name": "Money", "is_contained": False},
        "exception": {"class_name": "Exception", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        valueQuantity: "Quantity" = None,
        valueMoney: "Money" = None,
        exception: list["Exception"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.valueQuantity = valueQuantity
        self.valueMoney = valueMoney
        self.exception = exception or []

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Coverage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Coverage(DomainResource):
    """Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for the coverage
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept type: Coverage category such as medical or accident
    :param Reference policyHolder: Owner of the policy
    :param Reference subscriber: Subscriber to the policy
    :param str subscriberId: ID assigned to the subscriber
    :param Reference beneficiary: Plan beneficiary
    :param str dependent: Dependent number
    :param CodeableConcept relationship: Beneficiary relationship to the subscriber
    :param Period period: Coverage start and end dates
    :param Reference payor: Issuer of the policy
    :param _class _class: Additional coverage classifications
    :param int order: Relative order of the coverage
    :param str network: Insurer network
    :param CostToBeneficiary costToBeneficiary: Patient payments for services/products
    :param bool subrogation: Reimbursement to insurer
    :param Reference contract: Contract details
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
        "policyHolder": {"class_name": "Reference", "is_contained": False},
        "subscriber": {"class_name": "Reference", "is_contained": False},
        "beneficiary": {"class_name": "Reference", "is_contained": False},
        "relationship": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "payor": {"class_name": "Reference", "is_contained": False},
        "_class": {"class_name": "_class", "is_contained": True},
        "costToBeneficiary": {"class_name": "CostToBeneficiary", "is_contained": True},
        "contract": {"class_name": "Reference", "is_contained": False},
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
        policyHolder: "Reference" = None,
        subscriber: "Reference" = None,
        subscriberId: "str" = None,
        beneficiary: "Reference" = None,
        dependent: "str" = None,
        relationship: "CodeableConcept" = None,
        period: "Period" = None,
        payor: list["Reference"] = None,
        _class: list["_class"] = None,
        order: "int" = None,
        network: "str" = None,
        costToBeneficiary: list["CostToBeneficiary"] = None,
        subrogation: "bool" = None,
        contract: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "Coverage"
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
        self.policyHolder = policyHolder
        self.subscriber = subscriber
        self.subscriberId = subscriberId
        self.beneficiary = beneficiary
        self.dependent = dependent
        self.relationship = relationship
        self.period = period
        self.payor = payor or []
        self._class = _class or []
        self.order = order
        self.network = network
        self.costToBeneficiary = costToBeneficiary or []
        self.subrogation = subrogation
        self.contract = contract or []

    @classmethod
    def from_dict(cls, data: dict) -> "Coverage":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Coverage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
