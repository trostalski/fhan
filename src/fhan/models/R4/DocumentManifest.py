"""
Generated class for DocumentManifest. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Related(BaseModel):
    """Related identifiers or resources associated with the DocumentManifest.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifiers of things that are related
    :param Reference ref: Related Resource
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "ref": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: "Identifier" = None,
        ref: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.ref = ref

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentManifest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DocumentManifest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DocumentManifest(DomainResource):
    """A collection of documents compiled for a purpose together with metadata that applies to the collection.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier masterIdentifier: Unique Identifier for the set of documents
    :param Identifier identifier: Other identifiers for the manifest
    :param str status: current | superseded | entered-in-error
    :param CodeableConcept type: Kind of document set
    :param Reference subject: The subject of the set of documents
    :param str created: When this document manifest created
    :param Reference author: Who and/or what authored the DocumentManifest
    :param Reference recipient: Intended to get notified about this set of documents
    :param str source: The source system/application/software
    :param str description: Human-readable description (title)
    :param Reference content: Items in manifest
    :param Related related: Related things
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "masterIdentifier": {"class_name": "Identifier", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "recipient": {"class_name": "Reference", "is_contained": False},
        "content": {"class_name": "Reference", "is_contained": False},
        "related": {"class_name": "Related", "is_contained": True},
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
        masterIdentifier: "Identifier" = None,
        identifier: list["Identifier"] = None,
        status: "str" = None,
        type: "CodeableConcept" = None,
        subject: "Reference" = None,
        created: "str" = None,
        author: list["Reference"] = None,
        recipient: list["Reference"] = None,
        source: "str" = None,
        description: "str" = None,
        content: list["Reference"] = None,
        related: list["Related"] = None,
    ):
        self.resourceType = resourceType or "DocumentManifest"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.masterIdentifier = masterIdentifier
        self.identifier = identifier or []
        self.status = status
        self.type = type
        self.subject = subject
        self.created = created
        self.author = author or []
        self.recipient = recipient or []
        self.source = source
        self.description = description
        self.content = content or []
        self.related = related or []

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentManifest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DocumentManifest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
