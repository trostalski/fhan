"""
Generated class for MetadataResource. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.generator_models import BaseModel


class MetadataResource(BaseModel):
    """Common Ancestor declaration for conformance and knowledge artifact resources.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this metadata resource, represented as a URI (globally unique)
    :param str version: Business version of the metadata resource
    :param str name: Name for this metadata resource (computer friendly)
    :param str title: Name for this metadata resource (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the metadata resource
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for metadata resource (if applicable)
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
        title: "str" = None,
        status: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
    ):
        self.resourceType = resourceType or "MetadataResource"
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
        self.title = title
        self.status = status
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []

    @classmethod
    def from_dict(cls, data: dict) -> "MetadataResource":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MetadataResource":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
