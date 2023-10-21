"""
Generated class for CompartmentDefinition. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Resource(BaseModel):
    """Information about how a resource is related to the compartment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Name of resource type
    :param str param: Search Parameter Name, or chained parameters
    :param str documentation: Additional documentation about the resource and compartment
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
        code: "str" = None,
        param: list["str"] = None,
        documentation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.param = param or []
        self.documentation = documentation

    @classmethod
    def from_dict(cls, data: dict) -> "CompartmentDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CompartmentDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CompartmentDefinition(DomainResource):
    """A compartment definition that defines how resources are accessed on a server.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this compartment definition, represented as a URI (globally unique)
    :param str version: Business version of the compartment definition
    :param str name: Name for this compartment definition (computer friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the compartment definition
    :param UsageContext useContext: The context that the content is intended to support
    :param str purpose: Why this compartment definition is defined
    :param str code: Patient | Encounter | RelatedPerson | Practitioner | Device
    :param bool search: Whether the search syntax is supported
    :param Resource resource: How a resource is related to the compartment
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
        "resource": {"class_name": "Resource", "is_contained": True},
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
        purpose: "str" = None,
        code: "str" = None,
        search: "bool" = None,
        resource: list["Resource"] = None,
    ):
        self.resourceType = resourceType or "CompartmentDefinition"
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
        self.purpose = purpose
        self.code = code
        self.search = search
        self.resource = resource or []

    @classmethod
    def from_dict(cls, data: dict) -> "CompartmentDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CompartmentDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
