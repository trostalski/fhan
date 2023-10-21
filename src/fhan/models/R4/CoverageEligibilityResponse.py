"""
Generated class for CoverageEligibilityResponse. 
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


class Benefit(BaseModel):
    """Benefits used to date.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Benefit classification
    :param int allowedUnsignedInt: Benefits allowed
    :param str allowedString: Benefits allowed
    :param Money allowedMoney: Benefits allowed
    :param int usedUnsignedInt: Benefits used
    :param str usedString: Benefits used
    :param Money usedMoney: Benefits used
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "allowedMoney": {"class_name": "Money", "is_contained": False},
        "usedMoney": {"class_name": "Money", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        allowedUnsignedInt: "int" = None,
        allowedString: "str" = None,
        allowedMoney: "Money" = None,
        usedUnsignedInt: "int" = None,
        usedString: "str" = None,
        usedMoney: "Money" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.allowedUnsignedInt = allowedUnsignedInt
        self.allowedString = allowedString
        self.allowedMoney = allowedMoney
        self.usedUnsignedInt = usedUnsignedInt
        self.usedString = usedString
        self.usedMoney = usedMoney

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Item(BaseModel):
    """Benefits and optionally current balances, and authorization details by category or service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Product or service billing modifiers
    :param Reference provider: Performing practitioner
    :param bool excluded: Excluded from the plan
    :param str name: Short name for the benefit
    :param str description: Description of the benefit or services covered
    :param CodeableConcept network: In or out of network
    :param CodeableConcept unit: Individual or family
    :param CodeableConcept term: Annual or lifetime
    :param Benefit benefit: Benefit Summary
    :param bool authorizationRequired: Authorization required flag
    :param CodeableConcept authorizationSupporting: Type of required supporting materials
    :param str authorizationUrl: Preauthorization requirements endpoint
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "network": {"class_name": "CodeableConcept", "is_contained": False},
        "unit": {"class_name": "CodeableConcept", "is_contained": False},
        "term": {"class_name": "CodeableConcept", "is_contained": False},
        "benefit": {"class_name": "Benefit", "is_contained": True},
        "authorizationSupporting": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        category: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        provider: "Reference" = None,
        excluded: "bool" = None,
        name: "str" = None,
        description: "str" = None,
        network: "CodeableConcept" = None,
        unit: "CodeableConcept" = None,
        term: "CodeableConcept" = None,
        benefit: list["Benefit"] = None,
        authorizationRequired: "bool" = None,
        authorizationSupporting: list["CodeableConcept"] = None,
        authorizationUrl: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category
        self.productOrService = productOrService
        self.modifier = modifier or []
        self.provider = provider
        self.excluded = excluded
        self.name = name
        self.description = description
        self.network = network
        self.unit = unit
        self.term = term
        self.benefit = benefit or []
        self.authorizationRequired = authorizationRequired
        self.authorizationSupporting = authorizationSupporting or []
        self.authorizationUrl = authorizationUrl

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Insurance(BaseModel):
    """Financial instruments for reimbursement for the health care products and services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference coverage: Insurance information
    :param bool inforce: Coverage inforce indicator
    :param Period benefitPeriod: When the benefits are applicable
    :param Item item: Benefits and authorization details
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "coverage": {"class_name": "Reference", "is_contained": False},
        "benefitPeriod": {"class_name": "Period", "is_contained": False},
        "item": {"class_name": "Item", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        coverage: "Reference" = None,
        inforce: "bool" = None,
        benefitPeriod: "Period" = None,
        item: list["Item"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.coverage = coverage
        self.inforce = inforce
        self.benefitPeriod = benefitPeriod
        self.item = item or []

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Error(BaseModel):
    """Errors encountered during the processing of the request.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
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
        code: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CoverageEligibilityResponse(DomainResource):
    """This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.
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
    :param str purpose: auth-requirements | benefits | discovery | validation
    :param Reference patient: Intended recipient of products and services
    :param str servicedDate: Estimated date or dates of service
    :param Period servicedPeriod: Estimated date or dates of service
    :param str created: Response creation date
    :param Reference requestor: Party responsible for the request
    :param Reference request: Eligibility request reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param Reference insurer: Coverage issuer
    :param Insurance insurance: Patient insurance information
    :param str preAuthRef: Preauthorization reference
    :param CodeableConcept form: Printed form identifier
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
        "patient": {"class_name": "Reference", "is_contained": False},
        "servicedPeriod": {"class_name": "Period", "is_contained": False},
        "requestor": {"class_name": "Reference", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "insurer": {"class_name": "Reference", "is_contained": False},
        "insurance": {"class_name": "Insurance", "is_contained": True},
        "form": {"class_name": "CodeableConcept", "is_contained": False},
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
        purpose: list["str"] = None,
        patient: "Reference" = None,
        servicedDate: "str" = None,
        servicedPeriod: "Period" = None,
        created: "str" = None,
        requestor: "Reference" = None,
        request: "Reference" = None,
        outcome: "str" = None,
        disposition: "str" = None,
        insurer: "Reference" = None,
        insurance: list["Insurance"] = None,
        preAuthRef: "str" = None,
        form: "CodeableConcept" = None,
        error: list["Error"] = None,
    ):
        self.resourceType = resourceType or "CoverageEligibilityResponse"
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
        self.purpose = purpose or []
        self.patient = patient
        self.servicedDate = servicedDate
        self.servicedPeriod = servicedPeriod
        self.created = created
        self.requestor = requestor
        self.request = request
        self.outcome = outcome
        self.disposition = disposition
        self.insurer = insurer
        self.insurance = insurance or []
        self.preAuthRef = preAuthRef
        self.form = form
        self.error = error or []

    @classmethod
    def from_dict(cls, data: dict) -> "CoverageEligibilityResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CoverageEligibilityResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
