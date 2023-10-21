"""
Generated class for Claim. 
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


class Related(BaseModel):
    """Other claims which are related to this claim such as prior submissions or claims for related services or for the same event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference claim: Reference to the related claim
    :param CodeableConcept relationship: How the reference claim is related
    :param Identifier reference: File or case reference
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "claim": {"class_name": "Reference", "is_contained": False},
        "relationship": {"class_name": "CodeableConcept", "is_contained": False},
        "reference": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        claim: "Reference" = None,
        relationship: "CodeableConcept" = None,
        reference: "Identifier" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.claim = claim
        self.relationship = relationship
        self.reference = reference

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Payee(BaseModel):
    """The party to be reimbursed for cost of the products and services according to the terms of the policy.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of recipient
    :param Reference party: Recipient reference
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "party": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        party: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.party = party

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CareTeam(BaseModel):
    """The members of the team who provided the products and services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Order of care team
    :param Reference provider: Practitioner or organization
    :param bool responsible: Indicator of the lead practitioner
    :param CodeableConcept role: Function within the team
    :param CodeableConcept qualification: Practitioner credential or specialization
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "qualification": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        provider: "Reference" = None,
        responsible: "bool" = None,
        role: "CodeableConcept" = None,
        qualification: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.provider = provider
        self.responsible = responsible
        self.role = role
        self.qualification = qualification

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SupportingInfo(BaseModel):
    """Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Information instance identifier
    :param CodeableConcept category: Classification of the supplied information
    :param CodeableConcept code: Type of information
    :param str timingDate: When it occurred
    :param Period timingPeriod: When it occurred
    :param bool valueBoolean: Data to be provided
    :param str valueString: Data to be provided
    :param Quantity valueQuantity: Data to be provided
    :param Attachment valueAttachment: Data to be provided
    :param Reference valueReference: Data to be provided
    :param CodeableConcept reason: Explanation for the information
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "timingPeriod": {"class_name": "Period", "is_contained": False},
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        "valueReference": {"class_name": "Reference", "is_contained": False},
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        category: "CodeableConcept" = None,
        code: "CodeableConcept" = None,
        timingDate: "str" = None,
        timingPeriod: "Period" = None,
        valueBoolean: "bool" = None,
        valueString: "str" = None,
        valueQuantity: "Quantity" = None,
        valueAttachment: "Attachment" = None,
        valueReference: "Reference" = None,
        reason: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.category = category
        self.code = code
        self.timingDate = timingDate
        self.timingPeriod = timingPeriod
        self.valueBoolean = valueBoolean
        self.valueString = valueString
        self.valueQuantity = valueQuantity
        self.valueAttachment = valueAttachment
        self.valueReference = valueReference
        self.reason = reason

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Diagnosis(BaseModel):
    """Information about diagnoses relevant to the claim items.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Diagnosis instance identifier
    :param CodeableConcept diagnosisCodeableConcept: Nature of illness or problem
    :param Reference diagnosisReference: Nature of illness or problem
    :param CodeableConcept type: Timing or nature of the diagnosis
    :param CodeableConcept onAdmission: Present on admission
    :param CodeableConcept packageCode: Package billing code
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
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "onAdmission": {"class_name": "CodeableConcept", "is_contained": False},
        "packageCode": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        diagnosisCodeableConcept: "CodeableConcept" = None,
        diagnosisReference: "Reference" = None,
        type: list["CodeableConcept"] = None,
        onAdmission: "CodeableConcept" = None,
        packageCode: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.diagnosisCodeableConcept = diagnosisCodeableConcept
        self.diagnosisReference = diagnosisReference
        self.type = type or []
        self.onAdmission = onAdmission
        self.packageCode = packageCode

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Procedure(BaseModel):
    """Procedures performed on the patient relevant to the billing items with the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Procedure instance identifier
    :param CodeableConcept type: Category of Procedure
    :param str date: When the procedure was performed
    :param CodeableConcept procedureCodeableConcept: Specific clinical procedure
    :param Reference procedureReference: Specific clinical procedure
    :param Reference udi: Unique device identifier
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "procedureCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "procedureReference": {"class_name": "Reference", "is_contained": False},
        "udi": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        type: list["CodeableConcept"] = None,
        date: "str" = None,
        procedureCodeableConcept: "CodeableConcept" = None,
        procedureReference: "Reference" = None,
        udi: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.type = type or []
        self.date = date
        self.procedureCodeableConcept = procedureCodeableConcept
        self.procedureReference = procedureReference
        self.udi = udi or []

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Insurance(BaseModel):
    """Financial instruments for reimbursement for the health care products and services specified on the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Insurance instance identifier
    :param bool focal: Coverage to be used for adjudication
    :param Identifier identifier: Pre-assigned Claim number
    :param Reference coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    :param str preAuthRef: Prior authorization reference number
    :param Reference claimResponse: Adjudication results
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
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
        identifier: "Identifier" = None,
        coverage: "Reference" = None,
        businessArrangement: "str" = None,
        preAuthRef: list["str"] = None,
        claimResponse: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.focal = focal
        self.identifier = identifier
        self.coverage = coverage
        self.businessArrangement = businessArrangement
        self.preAuthRef = preAuthRef or []
        self.claimResponse = claimResponse

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Accident(BaseModel):
    """Details of an accident which resulted in injuries which required the products and services listed in the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When the incident occurred
    :param CodeableConcept type: The nature of the accident
    :param Address locationAddress: Where the event occurred
    :param Reference locationReference: Where the event occurred
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "locationAddress": {"class_name": "Address", "is_contained": False},
        "locationReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        date: "str" = None,
        type: "CodeableConcept" = None,
        locationAddress: "Address" = None,
        locationReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.date = date
        self.type = type
        self.locationAddress = locationAddress
        self.locationReference = locationReference

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubDetail(BaseModel):
    """A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple items.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "revenue": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "programCode": {"class_name": "CodeableConcept", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "udi": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        revenue: "CodeableConcept" = None,
        category: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        programCode: list["CodeableConcept"] = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        net: "Money" = None,
        udi: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.revenue = revenue
        self.category = category
        self.productOrService = productOrService
        self.modifier = modifier or []
        self.programCode = programCode or []
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.net = net
        self.udi = udi or []

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Detail(BaseModel):
    """A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple items.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param SubDetail subDetail: Product or service provided
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "revenue": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "programCode": {"class_name": "CodeableConcept", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "udi": {"class_name": "Reference", "is_contained": False},
        "subDetail": {"class_name": "SubDetail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        revenue: "CodeableConcept" = None,
        category: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        programCode: list["CodeableConcept"] = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        net: "Money" = None,
        udi: list["Reference"] = None,
        subDetail: list["SubDetail"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.revenue = revenue
        self.category = category
        self.productOrService = productOrService
        self.modifier = modifier or []
        self.programCode = programCode or []
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.net = net
        self.udi = udi or []
        self.subDetail = subDetail or []

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Item(BaseModel):
    """A claim line. Either a simple  product or service or a 'group' of details which can each be a simple items or groups of sub-details.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param int careTeamSequence: Applicable careTeam members
    :param int diagnosisSequence: Applicable diagnoses
    :param int procedureSequence: Applicable procedures
    :param int informationSequence: Applicable exception and supporting information
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Product or service billing modifiers
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
    :param Reference udi: Unique device identifier
    :param CodeableConcept bodySite: Anatomical location
    :param CodeableConcept subSite: Anatomical sub-location
    :param Reference encounter: Encounters related to this billed item
    :param Detail detail: Product or service provided
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "revenue": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
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
        "udi": {"class_name": "Reference", "is_contained": False},
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        "subSite": {"class_name": "CodeableConcept", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "detail": {"class_name": "Detail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        careTeamSequence: list["int"] = None,
        diagnosisSequence: list["int"] = None,
        procedureSequence: list["int"] = None,
        informationSequence: list["int"] = None,
        revenue: "CodeableConcept" = None,
        category: "CodeableConcept" = None,
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
        udi: list["Reference"] = None,
        bodySite: "CodeableConcept" = None,
        subSite: list["CodeableConcept"] = None,
        encounter: list["Reference"] = None,
        detail: list["Detail"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.careTeamSequence = careTeamSequence or []
        self.diagnosisSequence = diagnosisSequence or []
        self.procedureSequence = procedureSequence or []
        self.informationSequence = informationSequence or []
        self.revenue = revenue
        self.category = category
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
        self.udi = udi or []
        self.bodySite = bodySite
        self.subSite = subSite or []
        self.encounter = encounter or []
        self.detail = detail or []

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Claim(DomainResource):
    """A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for claim
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept type: Category or discipline
    :param CodeableConcept subType: More granular claim type
    :param str use: claim | preauthorization | predetermination
    :param Reference patient: The recipient of the products and services
    :param Period billablePeriod: Relevant time frame for the claim
    :param str created: Resource creation date
    :param Reference enterer: Author of the claim
    :param Reference insurer: Target
    :param Reference provider: Party responsible for the claim
    :param CodeableConcept priority: Desired processing ugency
    :param CodeableConcept fundsReserve: For whom to reserve funds
    :param Related related: Prior or corollary claims
    :param Reference prescription: Prescription authorizing services and products
    :param Reference originalPrescription: Original prescription if superseded by fulfiller
    :param Payee payee: Recipient of benefits payable
    :param Reference referral: Treatment referral
    :param Reference facility: Servicing facility
    :param CareTeam careTeam: Members of the care team
    :param SupportingInfo supportingInfo: Supporting information
    :param Diagnosis diagnosis: Pertinent diagnosis information
    :param Procedure procedure: Clinical procedures performed
    :param Insurance insurance: Patient insurance information
    :param Accident accident: Details of the event
    :param Item item: Product or service provided
    :param Money total: Total claim cost
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
        "billablePeriod": {"class_name": "Period", "is_contained": False},
        "enterer": {"class_name": "Reference", "is_contained": False},
        "insurer": {"class_name": "Reference", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "priority": {"class_name": "CodeableConcept", "is_contained": False},
        "fundsReserve": {"class_name": "CodeableConcept", "is_contained": False},
        "related": {"class_name": "Related", "is_contained": True},
        "prescription": {"class_name": "Reference", "is_contained": False},
        "originalPrescription": {"class_name": "Reference", "is_contained": False},
        "payee": {"class_name": "Payee", "is_contained": True},
        "referral": {"class_name": "Reference", "is_contained": False},
        "facility": {"class_name": "Reference", "is_contained": False},
        "careTeam": {"class_name": "CareTeam", "is_contained": True},
        "supportingInfo": {"class_name": "SupportingInfo", "is_contained": True},
        "diagnosis": {"class_name": "Diagnosis", "is_contained": True},
        "procedure": {"class_name": "Procedure", "is_contained": True},
        "insurance": {"class_name": "Insurance", "is_contained": True},
        "accident": {"class_name": "Accident", "is_contained": True},
        "item": {"class_name": "Item", "is_contained": True},
        "total": {"class_name": "Money", "is_contained": False},
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
        billablePeriod: "Period" = None,
        created: "str" = None,
        enterer: "Reference" = None,
        insurer: "Reference" = None,
        provider: "Reference" = None,
        priority: "CodeableConcept" = None,
        fundsReserve: "CodeableConcept" = None,
        related: list["Related"] = None,
        prescription: "Reference" = None,
        originalPrescription: "Reference" = None,
        payee: "Payee" = None,
        referral: "Reference" = None,
        facility: "Reference" = None,
        careTeam: list["CareTeam"] = None,
        supportingInfo: list["SupportingInfo"] = None,
        diagnosis: list["Diagnosis"] = None,
        procedure: list["Procedure"] = None,
        insurance: list["Insurance"] = None,
        accident: "Accident" = None,
        item: list["Item"] = None,
        total: "Money" = None,
    ):
        self.resourceType = resourceType or "Claim"
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
        self.billablePeriod = billablePeriod
        self.created = created
        self.enterer = enterer
        self.insurer = insurer
        self.provider = provider
        self.priority = priority
        self.fundsReserve = fundsReserve
        self.related = related or []
        self.prescription = prescription
        self.originalPrescription = originalPrescription
        self.payee = payee
        self.referral = referral
        self.facility = facility
        self.careTeam = careTeam or []
        self.supportingInfo = supportingInfo or []
        self.diagnosis = diagnosis or []
        self.procedure = procedure or []
        self.insurance = insurance or []
        self.accident = accident
        self.item = item or []
        self.total = total

    @classmethod
    def from_dict(cls, data: dict) -> "Claim":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Claim":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
