"""
Generated class for MedicinalProductAuthorization. 
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


class JurisdictionalAuthorization(BaseModel):
    """Authorization in areas within a country.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: The assigned number for the marketing authorization
    :param CodeableConcept country: Country of authorization
    :param CodeableConcept jurisdiction: Jurisdiction within a country
    :param CodeableConcept legalStatusOfSupply: The legal status of supply in a jurisdiction or region
    :param Period validityPeriod: The start and expected end date of the authorization
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "country": {"class_name": "CodeableConcept", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "legalStatusOfSupply": {"class_name": "CodeableConcept", "is_contained": False},
        "validityPeriod": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        country: "CodeableConcept" = None,
        jurisdiction: list["CodeableConcept"] = None,
        legalStatusOfSupply: "CodeableConcept" = None,
        validityPeriod: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.country = country
        self.jurisdiction = jurisdiction or []
        self.legalStatusOfSupply = legalStatusOfSupply
        self.validityPeriod = validityPeriod

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductAuthorization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductAuthorization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Procedure(BaseModel):
    """The regulatory procedure for granting or amending a marketing authorization.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier for this procedure
    :param CodeableConcept type: Type of procedure
    :param Period datePeriod: Date of procedure
    :param str dateDateTime: Date of procedure
    :param Application application: Applcations submitted to obtain a marketing authorization
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "datePeriod": {"class_name": "Period", "is_contained": False},
        "application": {"class_name": "Application", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: "Identifier" = None,
        type: "CodeableConcept" = None,
        datePeriod: "Period" = None,
        dateDateTime: "str" = None,
        application: list["Application"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.type = type
        self.datePeriod = datePeriod
        self.dateDateTime = dateDateTime
        self.application = application or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductAuthorization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductAuthorization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicinalProductAuthorization(DomainResource):
    """The regulatory authorization of a medicinal product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the marketing authorization, as assigned by a regulator
    :param Reference subject: The medicinal product that is being authorized
    :param CodeableConcept country: The country in which the marketing authorization has been granted
    :param CodeableConcept jurisdiction: Jurisdiction within a country
    :param CodeableConcept status: The status of the marketing authorization
    :param str statusDate: The date at which the given status has become applicable
    :param str restoreDate: The date when a suspended the marketing or the marketing authorization of the product is anticipated to be restored
    :param Period validityPeriod: The beginning of the time period in which the marketing authorization is in the specific status shall be specified A complete date consisting of day, month and year shall be specified using the ISO 8601 date format
    :param Period dataExclusivityPeriod: A period of time after authorization before generic product applicatiosn can be submitted
    :param str dateOfFirstAuthorization: The date when the first authorization was granted by a Medicines Regulatory Agency
    :param str internationalBirthDate: Date of first marketing authorization for a company's new medicinal product in any country in the World
    :param CodeableConcept legalBasis: The legal framework against which this authorization is granted
    :param JurisdictionalAuthorization jurisdictionalAuthorization: Authorization in areas within a country
    :param Reference holder: Marketing Authorization Holder
    :param Reference regulator: Medicines Regulatory Agency
    :param Procedure procedure: The regulatory procedure for granting or amending a marketing authorization
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "country": {"class_name": "CodeableConcept", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        "validityPeriod": {"class_name": "Period", "is_contained": False},
        "dataExclusivityPeriod": {"class_name": "Period", "is_contained": False},
        "legalBasis": {"class_name": "CodeableConcept", "is_contained": False},
        "jurisdictionalAuthorization": {
            "class_name": "JurisdictionalAuthorization",
            "is_contained": True,
        },
        "holder": {"class_name": "Reference", "is_contained": False},
        "regulator": {"class_name": "Reference", "is_contained": False},
        "procedure": {"class_name": "Procedure", "is_contained": True},
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
        subject: "Reference" = None,
        country: list["CodeableConcept"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        status: "CodeableConcept" = None,
        statusDate: "str" = None,
        restoreDate: "str" = None,
        validityPeriod: "Period" = None,
        dataExclusivityPeriod: "Period" = None,
        dateOfFirstAuthorization: "str" = None,
        internationalBirthDate: "str" = None,
        legalBasis: "CodeableConcept" = None,
        jurisdictionalAuthorization: list["JurisdictionalAuthorization"] = None,
        holder: "Reference" = None,
        regulator: "Reference" = None,
        procedure: "Procedure" = None,
    ):
        self.resourceType = resourceType or "MedicinalProductAuthorization"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.subject = subject
        self.country = country or []
        self.jurisdiction = jurisdiction or []
        self.status = status
        self.statusDate = statusDate
        self.restoreDate = restoreDate
        self.validityPeriod = validityPeriod
        self.dataExclusivityPeriod = dataExclusivityPeriod
        self.dateOfFirstAuthorization = dateOfFirstAuthorization
        self.internationalBirthDate = internationalBirthDate
        self.legalBasis = legalBasis
        self.jurisdictionalAuthorization = jurisdictionalAuthorization or []
        self.holder = holder
        self.regulator = regulator
        self.procedure = procedure

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductAuthorization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductAuthorization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
