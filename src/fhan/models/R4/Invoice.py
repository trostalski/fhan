"""
Generated class for Invoice. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Participant(BaseModel):
    """Indicates who or what performed or participated in the charged service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Type of involvement in creation of this Invoice
    :param Reference actor: Individual who was involved
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        role: "CodeableConcept" = None,
        actor: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role
        self.actor = actor

    @classmethod
    def from_dict(cls, data: dict) -> "Invoice":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Invoice":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PriceComponent(BaseModel):
    """The price for a ChargeItem may be calculated as a base price with surcharges/deductions that apply in certain conditions. A ChargeItemDefinition resource that defines the prices, factors and conditions that apply to a billing code is currently under development. The priceComponent element can be used to offer transparency to the recipient of the Invoice as to how the prices have been calculated.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: base | surcharge | deduction | discount | tax | informational
    :param CodeableConcept code: Code identifying the specific component
    :param float factor: Factor used for calculating this component
    :param Money amount: Monetary amount associated with this component
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Money", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "str" = None,
        code: "CodeableConcept" = None,
        factor: "float" = None,
        amount: "Money" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.code = code
        self.factor = factor
        self.amount = amount

    @classmethod
    def from_dict(cls, data: dict) -> "Invoice":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Invoice":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class LineItem(BaseModel):
    """Each line item represents one charge for goods and services rendered. Details such as date, code and amount are found in the referenced ChargeItem resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Sequence number of line item
    :param Reference chargeItemReference: Reference to ChargeItem containing details of this line item or an inline billing code
    :param CodeableConcept chargeItemCodeableConcept: Reference to ChargeItem containing details of this line item or an inline billing code
    :param PriceComponent priceComponent: Components of total line item price
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "chargeItemReference": {"class_name": "Reference", "is_contained": False},
        "chargeItemCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "priceComponent": {"class_name": "PriceComponent", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        chargeItemReference: "Reference" = None,
        chargeItemCodeableConcept: "CodeableConcept" = None,
        priceComponent: list["PriceComponent"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.chargeItemReference = chargeItemReference
        self.chargeItemCodeableConcept = chargeItemCodeableConcept
        self.priceComponent = priceComponent or []

    @classmethod
    def from_dict(cls, data: dict) -> "Invoice":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Invoice":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Invoice(DomainResource):
    """Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for item
    :param str status: draft | issued | balanced | cancelled | entered-in-error
    :param str cancelledReason: Reason for cancellation of this Invoice
    :param CodeableConcept type: Type of Invoice
    :param Reference subject: Recipient(s) of goods and services
    :param Reference recipient: Recipient of this invoice
    :param str date: Invoice date / posting date
    :param Participant participant: Participant in creation of this Invoice
    :param Reference issuer: Issuing Organization of Invoice
    :param Reference account: Account that is being balanced
    :param LineItem lineItem: Line items of this Invoice
    :param TotalPriceComponent totalPriceComponent: Components of Invoice total
    :param Money totalNet: Net total of this Invoice
    :param Money totalGross: Gross total of this Invoice
    :param str paymentTerms: Payment details
    :param Annotation note: Comments made about the invoice
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
        "recipient": {"class_name": "Reference", "is_contained": False},
        "participant": {"class_name": "Participant", "is_contained": True},
        "issuer": {"class_name": "Reference", "is_contained": False},
        "account": {"class_name": "Reference", "is_contained": False},
        "lineItem": {"class_name": "LineItem", "is_contained": True},
        "totalPriceComponent": {
            "class_name": "TotalPriceComponent",
            "is_contained": True,
        },
        "totalNet": {"class_name": "Money", "is_contained": False},
        "totalGross": {"class_name": "Money", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
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
        cancelledReason: "str" = None,
        type: "CodeableConcept" = None,
        subject: "Reference" = None,
        recipient: "Reference" = None,
        date: "str" = None,
        participant: list["Participant"] = None,
        issuer: "Reference" = None,
        account: "Reference" = None,
        lineItem: list["LineItem"] = None,
        totalPriceComponent: list["TotalPriceComponent"] = None,
        totalNet: "Money" = None,
        totalGross: "Money" = None,
        paymentTerms: "str" = None,
        note: list["Annotation"] = None,
    ):
        self.resourceType = resourceType or "Invoice"
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
        self.cancelledReason = cancelledReason
        self.type = type
        self.subject = subject
        self.recipient = recipient
        self.date = date
        self.participant = participant or []
        self.issuer = issuer
        self.account = account
        self.lineItem = lineItem or []
        self.totalPriceComponent = totalPriceComponent or []
        self.totalNet = totalNet
        self.totalGross = totalGross
        self.paymentTerms = paymentTerms
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "Invoice":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Invoice":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
