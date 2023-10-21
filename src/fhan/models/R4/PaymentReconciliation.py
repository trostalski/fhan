"""
Generated class for PaymentReconciliation. 
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
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Detail(BaseModel):
    """Distribution of the payment amount for a previously acknowledged payable.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business identifier of the payment detail
    :param Identifier predecessor: Business identifier of the prior payment detail
    :param CodeableConcept type: Category of payment
    :param Reference request: Request giving rise to the payment
    :param Reference submitter: Submitter of the request
    :param Reference response: Response committing to a payment
    :param str date: Date of commitment to pay
    :param Reference responsible: Contact for the response
    :param Reference payee: Recipient of the payment
    :param Money amount: Amount allocated to this payable
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "predecessor": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "submitter": {"class_name": "Reference", "is_contained": False},
        "response": {"class_name": "Reference", "is_contained": False},
        "responsible": {"class_name": "Reference", "is_contained": False},
        "payee": {"class_name": "Reference", "is_contained": False},
        "amount": {"class_name": "Money", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: "Identifier" = None,
        predecessor: "Identifier" = None,
        type: "CodeableConcept" = None,
        request: "Reference" = None,
        submitter: "Reference" = None,
        response: "Reference" = None,
        date: "str" = None,
        responsible: "Reference" = None,
        payee: "Reference" = None,
        amount: "Money" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.predecessor = predecessor
        self.type = type
        self.request = request
        self.submitter = submitter
        self.response = response
        self.date = date
        self.responsible = responsible
        self.payee = payee
        self.amount = amount

    @classmethod
    def from_dict(cls, data: dict) -> "PaymentReconciliation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "PaymentReconciliation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ProcessNote(BaseModel):
    """A note that describes or explains the processing in a human readable form.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: display | print | printoper
    :param str text: Note explanatory text
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "str" = None,
        text: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.text = text

    @classmethod
    def from_dict(cls, data: dict) -> "PaymentReconciliation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "PaymentReconciliation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PaymentReconciliation(DomainResource):
    """This resource provides the details including amount of a payment and allocates the payment items being paid.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for a payment reconciliation
    :param str status: active | cancelled | draft | entered-in-error
    :param Period period: Period covered
    :param str created: Creation date
    :param Reference paymentIssuer: Party generating payment
    :param Reference request: Reference to requesting resource
    :param Reference requestor: Responsible practitioner
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition message
    :param str paymentDate: When payment issued
    :param Money paymentAmount: Total amount of Payment
    :param Identifier paymentIdentifier: Business identifier for the payment
    :param Detail detail: Settlement particulars
    :param CodeableConcept formCode: Printed form identifier
    :param ProcessNote processNote: Note concerning processing
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "paymentIssuer": {"class_name": "Reference", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "requestor": {"class_name": "Reference", "is_contained": False},
        "paymentAmount": {"class_name": "Money", "is_contained": False},
        "paymentIdentifier": {"class_name": "Identifier", "is_contained": False},
        "detail": {"class_name": "Detail", "is_contained": True},
        "formCode": {"class_name": "CodeableConcept", "is_contained": False},
        "processNote": {"class_name": "ProcessNote", "is_contained": True},
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
        period: "Period" = None,
        created: "str" = None,
        paymentIssuer: "Reference" = None,
        request: "Reference" = None,
        requestor: "Reference" = None,
        outcome: "str" = None,
        disposition: "str" = None,
        paymentDate: "str" = None,
        paymentAmount: "Money" = None,
        paymentIdentifier: "Identifier" = None,
        detail: list["Detail"] = None,
        formCode: "CodeableConcept" = None,
        processNote: list["ProcessNote"] = None,
    ):
        self.resourceType = resourceType or "PaymentReconciliation"
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
        self.period = period
        self.created = created
        self.paymentIssuer = paymentIssuer
        self.request = request
        self.requestor = requestor
        self.outcome = outcome
        self.disposition = disposition
        self.paymentDate = paymentDate
        self.paymentAmount = paymentAmount
        self.paymentIdentifier = paymentIdentifier
        self.detail = detail or []
        self.formCode = formCode
        self.processNote = processNote or []

    @classmethod
    def from_dict(cls, data: dict) -> "PaymentReconciliation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "PaymentReconciliation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
