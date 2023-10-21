"""
Generated class for PaymentNotice. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Money import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class PaymentNotice(DomainResource):
    """This resource provides the status of the payment for goods and services rendered, and the request and response resource references.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for the payment noctice
    :param str status: active | cancelled | draft | entered-in-error
    :param Reference request: Request reference
    :param Reference response: Response reference
    :param str created: Creation date
    :param Reference provider: Responsible practitioner
    :param Reference payment: Payment reference
    :param str paymentDate: Payment or clearing date
    :param Reference payee: Party being paid
    :param Reference recipient: Party being notified
    :param Money amount: Monetary amount of the payment
    :param CodeableConcept paymentStatus: Issued or cleared Status of the payment
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "response": {"class_name": "Reference", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "payment": {"class_name": "Reference", "is_contained": False},
        "payee": {"class_name": "Reference", "is_contained": False},
        "recipient": {"class_name": "Reference", "is_contained": False},
        "amount": {"class_name": "Money", "is_contained": False},
        "paymentStatus": {"class_name": "CodeableConcept", "is_contained": False},
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
        request: "Reference" = None,
        response: "Reference" = None,
        created: "str" = None,
        provider: "Reference" = None,
        payment: "Reference" = None,
        paymentDate: "str" = None,
        payee: "Reference" = None,
        recipient: "Reference" = None,
        amount: "Money" = None,
        paymentStatus: "CodeableConcept" = None,
    ):
        self.resourceType = resourceType or "PaymentNotice"
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
        self.request = request
        self.response = response
        self.created = created
        self.provider = provider
        self.payment = payment
        self.paymentDate = paymentDate
        self.payee = payee
        self.recipient = recipient
        self.amount = amount
        self.paymentStatus = paymentStatus

    @classmethod
    def from_dict(cls, data: dict) -> "PaymentNotice":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "PaymentNotice":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
