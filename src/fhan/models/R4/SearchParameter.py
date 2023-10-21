"""
Generated class for SearchParameter. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Component(BaseModel):
    """Used to define the parts of a composite search parameter.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str definition: Defines how the part works
    :param str expression: Subexpression relative to main expression
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
        definition: "str" = None,
        expression: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.definition = definition
        self.expression = expression

    @classmethod
    def from_dict(cls, data: dict) -> "SearchParameter":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SearchParameter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SearchParameter(DomainResource):
    """A search parameter that defines a named search item that can be used to search/filter on a resource.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this search parameter, represented as a URI (globally unique)
    :param str version: Business version of the search parameter
    :param str name: Name for this search parameter (computer friendly)
    :param str derivedFrom: Original definition for the search parameter
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the search parameter
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for search parameter (if applicable)
    :param str purpose: Why this search parameter is defined
    :param str code: Code used in URL
    :param str base: The resource type(s) this search parameter applies to
    :param str type: number | date | string | token | reference | composite | quantity | uri | special
    :param str expression: FHIRPath expression that extracts the values
    :param str xpath: XPath that extracts the values
    :param str xpathUsage: normal | phonetic | nearby | distance | other
    :param str target: Types of resource (if a resource reference)
    :param bool multipleOr: Allow multiple values per parameter (or)
    :param bool multipleAnd: Allow multiple parameters (and)
    :param str comparator: eq | ne | gt | lt | ge | le | sa | eb | ap
    :param str modifier: missing | exact | contains | not | text | in | not-in | below | above | type | identifier | ofType
    :param str chain: Chained names supported
    :param Component component: For Composite resources to define the parts
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "component": {"class_name": "Component", "is_contained": True},
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
        version: "str" = None,
        name: "str" = None,
        derivedFrom: "str" = None,
        status: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        code: "str" = None,
        base: list["str"] = None,
        type: "str" = None,
        expression: "str" = None,
        xpath: "str" = None,
        xpathUsage: "str" = None,
        target: list["str"] = None,
        multipleOr: "bool" = None,
        multipleAnd: "bool" = None,
        comparator: list["str"] = None,
        modifier: list["str"] = None,
        chain: list["str"] = None,
        component: list["Component"] = None,
    ):
        self.resourceType = resourceType or "SearchParameter"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.version = version
        self.name = name
        self.derivedFrom = derivedFrom
        self.status = status
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.code = code
        self.base = base or []
        self.type = type
        self.expression = expression
        self.xpath = xpath
        self.xpathUsage = xpathUsage
        self.target = target or []
        self.multipleOr = multipleOr
        self.multipleAnd = multipleAnd
        self.comparator = comparator or []
        self.modifier = modifier or []
        self.chain = chain or []
        self.component = component or []

    @classmethod
    def from_dict(cls, data: dict) -> "SearchParameter":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SearchParameter":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
