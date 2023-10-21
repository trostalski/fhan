"""
Generated class for GraphDefinition. 
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


class Compartment(BaseModel):
    """Compartment Consistency Rules.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str use: condition | requirement
    :param str code: Patient | Encounter | RelatedPerson | Practitioner | Device
    :param str rule: identical | matching | different | custom
    :param str expression: Custom rule, as a FHIRPath expression
    :param str description: Documentation for FHIRPath expression
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
        use: "str" = None,
        code: "str" = None,
        rule: "str" = None,
        expression: "str" = None,
        description: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.use = use
        self.code = code
        self.rule = rule
        self.expression = expression
        self.description = description

    @classmethod
    def from_dict(cls, data: dict) -> "GraphDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "GraphDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Target(BaseModel):
    """Potential target for the link.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: Type of resource this link refers to
    :param str params: Criteria for reverse lookup
    :param str profile: Profile for the target resource
    :param Compartment compartment: Compartment Consistency Rules
    :param Link link: Additional links from target resource
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "compartment": {"class_name": "Compartment", "is_contained": True},
        "link": {"class_name": "Link", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "str" = None,
        params: "str" = None,
        profile: "str" = None,
        compartment: list["Compartment"] = None,
        link: list["Link"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.params = params
        self.profile = profile
        self.compartment = compartment or []
        self.link = link or []

    @classmethod
    def from_dict(cls, data: dict) -> "GraphDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "GraphDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Link(BaseModel):
    """Links this graph makes rules about.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: Path in the resource that contains the link
    :param str sliceName: Which slice (if profiled)
    :param int min: Minimum occurrences for this link
    :param str max: Maximum occurrences for this link
    :param str description: Why this link is specified
    :param Target target: Potential target for the link
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "target": {"class_name": "Target", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        path: "str" = None,
        sliceName: "str" = None,
        min: "int" = None,
        max: "str" = None,
        description: "str" = None,
        target: list["Target"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.path = path
        self.sliceName = sliceName
        self.min = min
        self.max = max
        self.description = description
        self.target = target or []

    @classmethod
    def from_dict(cls, data: dict) -> "GraphDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "GraphDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class GraphDefinition(DomainResource):
    """A formal computable definition of a graph of resources - that is, a coherent set of resources that form a graph by following references. The Graph Definition resource defines a set and makes rules about the set.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this graph definition, represented as a URI (globally unique)
    :param str version: Business version of the graph definition
    :param str name: Name for this graph definition (computer friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the graph definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for graph definition (if applicable)
    :param str purpose: Why this graph definition is defined
    :param str start: Type of resource at which the graph starts
    :param str profile: Profile on base resource
    :param Link link: Links this graph makes rules about
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
        "link": {"class_name": "Link", "is_contained": True},
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
        status: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        start: "str" = None,
        profile: "str" = None,
        link: list["Link"] = None,
    ):
        self.resourceType = resourceType or "GraphDefinition"
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
        self.status = status
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.start = start
        self.profile = profile
        self.link = link or []

    @classmethod
    def from_dict(cls, data: dict) -> "GraphDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "GraphDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
