"""
Generated class for ChargeItemDefinition. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Applicability(BaseModel):
    """Expressions that describe applicability criteria for the billing code.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Natural language description of the condition
    :param str language: Language of the expression
    :param str expression: Boolean-valued expression
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
        description: "str" = None,
        language: "str" = None,
        expression: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.language = language
        self.expression = expression

    @classmethod
    def from_dict(cls, data: dict) -> "ChargeItemDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ChargeItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PriceComponent(BaseModel):
    """The price for a ChargeItem may be calculated as a base price with surcharges/deductions that apply in certain conditions. A ChargeItemDefinition resource that defines the prices, factors and conditions that apply to a billing code is currently under development. The priceComponent element can be used to offer transparency to the recipient of the Invoice of how the prices have been calculated.:param str id: Unique id for inter-element referencing
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
    def from_dict(cls, data: dict) -> "ChargeItemDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ChargeItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PropertyGroup(BaseModel):
    """Group of properties which are applicable under the same conditions. If no applicability rules are established for the group, then all properties always apply.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Applicability applicability: Conditions under which the priceComponent is applicable
    :param PriceComponent priceComponent: Components of total line item price
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "applicability": {"class_name": "Applicability", "is_contained": True},
        "priceComponent": {"class_name": "PriceComponent", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        applicability: list["Applicability"] = None,
        priceComponent: list["PriceComponent"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.applicability = applicability or []
        self.priceComponent = priceComponent or []

    @classmethod
    def from_dict(cls, data: dict) -> "ChargeItemDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ChargeItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ChargeItemDefinition(DomainResource):
    """The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to calculate costs and prices. The properties may differ largely depending on type and realm, therefore this resource gives only a rough structure and requires profiling for each type of billing code system.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this charge item definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the charge item definition
    :param str version: Business version of the charge item definition
    :param str title: Name for this charge item definition (human friendly)
    :param str derivedFromUri: Underlying externally-defined charge item definition
    :param str partOf: A larger definition of which this particular definition is a component or step
    :param str replaces: Completed or terminated request(s) whose function is taken by this new request
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the charge item definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for charge item definition (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the charge item definition was approved by publisher
    :param str lastReviewDate: When the charge item definition was last reviewed
    :param Period effectivePeriod: When the charge item definition is expected to be used
    :param CodeableConcept code: Billing codes or product types this definition applies to
    :param Reference instance: Instances this definition applies to
    :param Applicability applicability: Whether or not the billing code is applicable
    :param PropertyGroup propertyGroup: Group of properties which are applicable under the same conditions
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "instance": {"class_name": "Reference", "is_contained": False},
        "applicability": {"class_name": "Applicability", "is_contained": True},
        "propertyGroup": {"class_name": "PropertyGroup", "is_contained": True},
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
        url: "str" = None,
        identifier: list["Identifier"] = None,
        version: "str" = None,
        title: "str" = None,
        derivedFromUri: list["str"] = None,
        partOf: list["str"] = None,
        replaces: list["str"] = None,
        status: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        copyright: "str" = None,
        approvalDate: "str" = None,
        lastReviewDate: "str" = None,
        effectivePeriod: "Period" = None,
        code: "CodeableConcept" = None,
        instance: list["Reference"] = None,
        applicability: list["Applicability"] = None,
        propertyGroup: list["PropertyGroup"] = None,
    ):
        self.resourceType = resourceType or "ChargeItemDefinition"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.identifier = identifier or []
        self.version = version
        self.title = title
        self.derivedFromUri = derivedFromUri or []
        self.partOf = partOf or []
        self.replaces = replaces or []
        self.status = status
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.copyright = copyright
        self.approvalDate = approvalDate
        self.lastReviewDate = lastReviewDate
        self.effectivePeriod = effectivePeriod
        self.code = code
        self.instance = instance or []
        self.applicability = applicability or []
        self.propertyGroup = propertyGroup or []

    @classmethod
    def from_dict(cls, data: dict) -> "ChargeItemDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ChargeItemDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
