"""
Generated class for Definition. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Period import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import BaseModel


class Definition(BaseModel):
    """Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    :param str url: Logical canonical URL to reference this {{title}} (globally unique)
    :param Identifier identifier: Business Identifier for {{title}}
    :param str version: Business version of the {{title}}
    :param str title: Name for this {{title}} (Human friendly)
    :param str derivedFromCanonical: Based on FHIR protocol or definition
    :param str derivedFromUri: Based on external protocol or definition
    :param str partOf: Part of referenced definition
    :param str replaces: Request(s) replaced by this request
    :param str status: draft | active | retired | unknown
    :param bool experimental: If for testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: Type of individual the defined service is for
    :param Reference subjectReference: Type of individual the defined service is for
    :param str date: Date status first applied
    :param Reference publisher: The name of the individual or organization that published the {{title}}
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the {{title}}
    :param UsageContext useContext: Content intends to support these contexts
    :param CodeableConcept jurisdiction: Intended jurisdiction for {{title}} (if applicable)
    :param str purpose: Why this {{title}} is defined
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When {{title}} approved by publisher
    :param str lastReviewDate: Last review date for the {{title}}
    :param Period effectivePeriod: The effective date range for the {{title}}
    :param CodeableConcept performerType: Desired kind of service performer
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "subjectCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "subjectReference": {"class_name": "Reference", "is_contained": False},
        "publisher": {"class_name": "Reference", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        "performerType": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        url: "str" = None,
        identifier: "Identifier" = None,
        version: "str" = None,
        title: "str" = None,
        derivedFromCanonical: list["str"] = None,
        derivedFromUri: list["str"] = None,
        partOf: list["str"] = None,
        replaces: list["str"] = None,
        status: "str" = None,
        experimental: "bool" = None,
        subjectCodeableConcept: "CodeableConcept" = None,
        subjectReference: "Reference" = None,
        date: "str" = None,
        publisher: "Reference" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        copyright: "str" = None,
        approvalDate: "str" = None,
        lastReviewDate: "str" = None,
        effectivePeriod: "Period" = None,
        performerType: "CodeableConcept" = None,
    ):
        self.resourceType = resourceType or "Definition"
        self.url = url
        self.identifier = identifier
        self.version = version
        self.title = title
        self.derivedFromCanonical = derivedFromCanonical or []
        self.derivedFromUri = derivedFromUri or []
        self.partOf = partOf or []
        self.replaces = replaces or []
        self.status = status
        self.experimental = experimental
        self.subjectCodeableConcept = subjectCodeableConcept
        self.subjectReference = subjectReference
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.copyright = copyright
        self.approvalDate = approvalDate
        self.lastReviewDate = lastReviewDate
        self.effectivePeriod = effectivePeriod
        self.performerType = performerType

    @classmethod
    def from_dict(cls, data: dict) -> "Definition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Definition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
