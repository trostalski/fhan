"""
Generated class for ClaimResponse. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Address import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Adjudication(BaseModel):
    """If this item is a group then the values here are a summary of the adjudication of the detail items. If this item is a simple product or service then this is the result of the adjudication of this item.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Type of adjudication information
    :param CodeableConcept reason: Explanation of adjudication outcome
    :param Money amount: Monetary amount
    :param float value: Non-monetary value
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Money", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        category: "CodeableConcept" = None,
        reason: "CodeableConcept" = None,
        amount: "Money" = None,
        value: "float" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category
        self.reason = reason
        self.amount = amount
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubDetail(BaseModel):
    """A sub-detail adjudication of a simple product or service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int subDetailSequence: Claim sub-detail instance identifier
    :param int noteNumber: Applicable note numbers
    :param Adjudication adjudication: Subdetail level adjudication details
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        subDetailSequence: "int" = None,
        noteNumber: list["int"] = None,
        adjudication: list["Adjudication"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.subDetailSequence = subDetailSequence
        self.noteNumber = noteNumber or []
        self.adjudication = adjudication or []

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Detail(BaseModel):
    """A claim detail. Either a simple (a product or service) or a 'group' of sub-details which are simple items.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int detailSequence: Claim detail instance identifier
    :param int noteNumber: Applicable note numbers
    :param Adjudication adjudication: Detail level adjudication details
    :param SubDetail subDetail: Adjudication for claim sub-details
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "subDetail": {"class_name": "SubDetail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        detailSequence: "int" = None,
        noteNumber: list["int"] = None,
        adjudication: list["Adjudication"] = None,
        subDetail: list["SubDetail"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.detailSequence = detailSequence
        self.noteNumber = noteNumber or []
        self.adjudication = adjudication or []
        self.subDetail = subDetail or []

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Item(BaseModel):
    """A claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-details.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Claim item instance identifier
    :param int noteNumber: Applicable note numbers
    :param Adjudication adjudication: Adjudication details
    :param Detail detail: Adjudication for claim details
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "detail": {"class_name": "Detail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        itemSequence: "int" = None,
        noteNumber: list["int"] = None,
        adjudication: list["Adjudication"] = None,
        detail: list["Detail"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemSequence = itemSequence
        self.noteNumber = noteNumber or []
        self.adjudication = adjudication or []
        self.detail = detail or []

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubDetail(BaseModel):
    """The third-tier service adjudications for payor added services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param int noteNumber: Applicable note numbers
    :param Adjudication adjudication: Added items detail adjudication
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        productOrService: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        net: "Money" = None,
        noteNumber: list["int"] = None,
        adjudication: list["Adjudication"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.productOrService = productOrService
        self.modifier = modifier or []
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.net = net
        self.noteNumber = noteNumber or []
        self.adjudication = adjudication or []

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Detail(BaseModel):
    """The second-tier service adjudications for payor added services.:param int detailSequence: Detail sequence number
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param int noteNumber: Applicable note numbers
    :param Adjudication adjudication: Added items detail adjudication
    :param SubDetail subDetail: Insurer added line items
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "subDetail": {"class_name": "SubDetail", "is_contained": True},
    }

    def __init__(
        self,
        detailSequence: list["int"] = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        productOrService: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        net: "Money" = None,
        noteNumber: list["int"] = None,
        adjudication: list["Adjudication"] = None,
        subDetail: list["SubDetail"] = None,
    ):
        self.detailSequence = detailSequence or []
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.productOrService = productOrService
        self.modifier = modifier or []
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.net = net
        self.noteNumber = noteNumber or []
        self.adjudication = adjudication or []
        self.subDetail = subDetail or []

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AddItem(BaseModel):
    """The first-tier service adjudications for payor added product or service lines.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Item sequence number
    :param int detailSequence: Detail sequence number
    :param int subdetailSequence: Subdetail sequence number
    :param Reference provider: Authorized providers
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param str servicedDate: Date or dates of service or product delivery
    :param Period servicedPeriod: Date or dates of service or product delivery
    :param CodeableConcept locationCodeableConcept: Place of service or where product was supplied
    :param Address locationAddress: Place of service or where product was supplied
    :param Reference locationReference: Place of service or where product was supplied
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param CodeableConcept bodySite: Anatomical location
    :param CodeableConcept subSite: Anatomical sub-location
    :param int noteNumber: Applicable note numbers
    :param Adjudication adjudication: Added items adjudication
    :param Detail detail: Insurer added line details
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "programCode": {"class_name": "CodeableConcept", "is_contained": False},
        "servicedPeriod": {"class_name": "Period", "is_contained": False},
        "locationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "locationAddress": {"class_name": "Address", "is_contained": False},
        "locationReference": {"class_name": "Reference", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        "subSite": {"class_name": "CodeableConcept", "is_contained": False},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "detail": {"class_name": "Detail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        itemSequence: list["int"] = None,
        detailSequence: list["int"] = None,
        subdetailSequence: list["int"] = None,
        provider: list["Reference"] = None,
        productOrService: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        programCode: list["CodeableConcept"] = None,
        servicedDate: "str" = None,
        servicedPeriod: "Period" = None,
        locationCodeableConcept: "CodeableConcept" = None,
        locationAddress: "Address" = None,
        locationReference: "Reference" = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        net: "Money" = None,
        bodySite: "CodeableConcept" = None,
        subSite: list["CodeableConcept"] = None,
        noteNumber: list["int"] = None,
        adjudication: list["Adjudication"] = None,
        detail: list["Detail"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemSequence = itemSequence or []
        self.detailSequence = detailSequence or []
        self.subdetailSequence = subdetailSequence or []
        self.provider = provider or []
        self.productOrService = productOrService
        self.modifier = modifier or []
        self.programCode = programCode or []
        self.servicedDate = servicedDate
        self.servicedPeriod = servicedPeriod
        self.locationCodeableConcept = locationCodeableConcept
        self.locationAddress = locationAddress
        self.locationReference = locationReference
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.net = net
        self.bodySite = bodySite
        self.subSite = subSite or []
        self.noteNumber = noteNumber or []
        self.adjudication = adjudication or []
        self.detail = detail or []

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Total(BaseModel):
    """Categorized monetary totals for the adjudication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Type of adjudication information
    :param Money amount: Financial total for the category
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Money", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        category: "CodeableConcept" = None,
        amount: "Money" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category
        self.amount = amount

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Payment(BaseModel):
    """Payment details for the adjudication of the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Partial or complete payment
    :param Money adjustment: Payment adjustment for non-claim issues
    :param CodeableConcept adjustmentReason: Explanation for the adjustment
    :param str date: Expected date of payment
    :param Money amount: Payable amount after adjustment
    :param Identifier identifier: Business identifier for the payment
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "adjustment": {"class_name": "Money", "is_contained": False},
        "adjustmentReason": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Money", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        adjustment: "Money" = None,
        adjustmentReason: "CodeableConcept" = None,
        date: "str" = None,
        amount: "Money" = None,
        identifier: "Identifier" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.adjustment = adjustment
        self.adjustmentReason = adjustmentReason
        self.date = date
        self.amount = amount
        self.identifier = identifier

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ProcessNote(BaseModel):
    """A note that describes or explains adjudication results in a human readable form.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Note instance identifier
    :param str type: display | print | printoper
    :param str text: Note explanatory text
    :param CodeableConcept language: Language of the text
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "language": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        number: "int" = None,
        type: "str" = None,
        text: "str" = None,
        language: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.number = number
        self.type = type
        self.text = text
        self.language = language

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Insurance(BaseModel):
    """Financial instruments for reimbursement for the health care products and services specified on the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Insurance instance identifier
    :param bool focal: Coverage to be used for adjudication
    :param Reference coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    :param Reference claimResponse: Adjudication results
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "coverage": {"class_name": "Reference", "is_contained": False},
        "claimResponse": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        focal: "bool" = None,
        coverage: "Reference" = None,
        businessArrangement: "str" = None,
        claimResponse: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.focal = focal
        self.coverage = coverage
        self.businessArrangement = businessArrangement
        self.claimResponse = claimResponse

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Error(BaseModel):
    """Errors encountered during the processing of the adjudication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Item sequence number
    :param int detailSequence: Detail sequence number
    :param int subDetailSequence: Subdetail sequence number
    :param CodeableConcept code: Error code detailing processing issues
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        itemSequence: "int" = None,
        detailSequence: "int" = None,
        subDetailSequence: "int" = None,
        code: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemSequence = itemSequence
        self.detailSequence = detailSequence
        self.subDetailSequence = subDetailSequence
        self.code = code

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ClaimResponse(DomainResource):
    """This resource provides the adjudication details from the processing of a Claim resource.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for a claim response
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept type: More granular claim type
    :param CodeableConcept subType: More granular claim type
    :param str use: claim | preauthorization | predetermination
    :param Reference patient: The recipient of the products and services
    :param str created: Response creation date
    :param Reference insurer: Party responsible for reimbursement
    :param Reference requestor: Party responsible for the claim
    :param Reference request: Id of resource triggering adjudication
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param str preAuthRef: Preauthorization reference
    :param Period preAuthPeriod: Preauthorization reference effective period
    :param CodeableConcept payeeType: Party to be paid any benefits payable
    :param Item item: Adjudication for claim line items
    :param AddItem addItem: Insurer added line items
    :param Adjudication adjudication: Header-level adjudication
    :param Total total: Adjudication totals
    :param Payment payment: Payment Details
    :param CodeableConcept fundsReserve: Funds reserved status
    :param CodeableConcept formCode: Printed form identifier
    :param Attachment form: Printed reference or actual form
    :param ProcessNote processNote: Note concerning adjudication
    :param Reference communicationRequest: Request for additional information
    :param Insurance insurance: Patient insurance information
    :param Error error: Processing errors
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
        "subType": {"class_name": "CodeableConcept", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "insurer": {"class_name": "Reference", "is_contained": False},
        "requestor": {"class_name": "Reference", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "preAuthPeriod": {"class_name": "Period", "is_contained": False},
        "payeeType": {"class_name": "CodeableConcept", "is_contained": False},
        "item": {"class_name": "Item", "is_contained": True},
        "addItem": {"class_name": "AddItem", "is_contained": True},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "total": {"class_name": "Total", "is_contained": True},
        "payment": {"class_name": "Payment", "is_contained": True},
        "fundsReserve": {"class_name": "CodeableConcept", "is_contained": False},
        "formCode": {"class_name": "CodeableConcept", "is_contained": False},
        "form": {"class_name": "Attachment", "is_contained": False},
        "processNote": {"class_name": "ProcessNote", "is_contained": True},
        "communicationRequest": {"class_name": "Reference", "is_contained": False},
        "insurance": {"class_name": "Insurance", "is_contained": True},
        "error": {"class_name": "Error", "is_contained": True},
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
        subType: "CodeableConcept" = None,
        use: "str" = None,
        patient: "Reference" = None,
        created: "str" = None,
        insurer: "Reference" = None,
        requestor: "Reference" = None,
        request: "Reference" = None,
        outcome: "str" = None,
        disposition: "str" = None,
        preAuthRef: "str" = None,
        preAuthPeriod: "Period" = None,
        payeeType: "CodeableConcept" = None,
        item: list["Item"] = None,
        addItem: list["AddItem"] = None,
        adjudication: list["Adjudication"] = None,
        total: list["Total"] = None,
        payment: "Payment" = None,
        fundsReserve: "CodeableConcept" = None,
        formCode: "CodeableConcept" = None,
        form: "Attachment" = None,
        processNote: list["ProcessNote"] = None,
        communicationRequest: list["Reference"] = None,
        insurance: list["Insurance"] = None,
        error: list["Error"] = None,
    ):
        self.resourceType = resourceType or "ClaimResponse"
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
        self.subType = subType
        self.use = use
        self.patient = patient
        self.created = created
        self.insurer = insurer
        self.requestor = requestor
        self.request = request
        self.outcome = outcome
        self.disposition = disposition
        self.preAuthRef = preAuthRef
        self.preAuthPeriod = preAuthPeriod
        self.payeeType = payeeType
        self.item = item or []
        self.addItem = addItem or []
        self.adjudication = adjudication or []
        self.total = total or []
        self.payment = payment
        self.fundsReserve = fundsReserve
        self.formCode = formCode
        self.form = form
        self.processNote = processNote or []
        self.communicationRequest = communicationRequest or []
        self.insurance = insurance or []
        self.error = error or []

    @classmethod
    def from_dict(cls, data: dict) -> "ClaimResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ClaimResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
