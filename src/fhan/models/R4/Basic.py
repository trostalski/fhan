"""
Generated class for Basic. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Basic(DomainResource):
    """Basic is used for handling concepts not yet defined in FHIR, narrative-only resources that don't map to an existing resource, and custom resources not appropriate for inclusion in the FHIR specification.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param CodeableConcept code: Kind of Resource
    :param Reference subject: Identifies the focus of this resource
    :param str created: When created
    :param Reference author: Who created
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
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
        code: "CodeableConcept" = None,
        subject: "Reference" = None,
        created: "str" = None,
        author: "Reference" = None,
    ):
        self.resourceType = resourceType or "Basic"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.code = code
        self.subject = subject
        self.created = created
        self.author = author

    @classmethod
    def from_dict(cls, data: dict) -> "Basic":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Basic":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
