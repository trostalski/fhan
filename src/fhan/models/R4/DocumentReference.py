"""
Generated class for DocumentReference. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class RelatesTo(BaseModel):
    """Relationships that this document has with other document references that already exist.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: replaces | transforms | signs | appends
    :param Reference target: Target of the relationship
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "target": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        target: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.target = target

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentReference":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DocumentReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Content(BaseModel):
    """The document and format referenced. There may be multiple content element repetitions, each with a different format.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment attachment: Where to access the document
    :param Coding format: Format/content rules for the document
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "attachment": {"class_name": "Attachment", "is_contained": False},
        "format": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        attachment: "Attachment" = None,
        format: "Coding" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.attachment = attachment
        self.format = format

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentReference":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DocumentReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Context(BaseModel):
    """The clinical context in which the document was prepared.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference encounter: Context of the document  content
    :param CodeableConcept event: Main clinical acts documented
    :param Period period: Time of service that is being documented
    :param CodeableConcept facilityType: Kind of facility where patient was seen
    :param CodeableConcept practiceSetting: Additional details about where the content was created (e.g. clinical specialty)
    :param Reference sourcePatientInfo: Patient demographics from source
    :param Reference related: Related identifiers or resources
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "event": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "facilityType": {"class_name": "CodeableConcept", "is_contained": False},
        "practiceSetting": {"class_name": "CodeableConcept", "is_contained": False},
        "sourcePatientInfo": {"class_name": "Reference", "is_contained": False},
        "related": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        encounter: list["Reference"] = None,
        event: list["CodeableConcept"] = None,
        period: "Period" = None,
        facilityType: "CodeableConcept" = None,
        practiceSetting: "CodeableConcept" = None,
        sourcePatientInfo: "Reference" = None,
        related: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.encounter = encounter or []
        self.event = event or []
        self.period = period
        self.facilityType = facilityType
        self.practiceSetting = practiceSetting
        self.sourcePatientInfo = sourcePatientInfo
        self.related = related or []

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentReference":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DocumentReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DocumentReference(DomainResource):
    """A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier masterIdentifier: Master Version Specific Identifier
    :param Identifier identifier: Other identifiers for the document
    :param str status: current | superseded | entered-in-error
    :param str docStatus: preliminary | final | amended | entered-in-error
    :param CodeableConcept type: Kind of document (LOINC if possible)
    :param CodeableConcept category: Categorization of document
    :param Reference subject: Who/what is the subject of the document
    :param str date: When this document reference was created
    :param Reference author: Who and/or what authored the document
    :param Reference authenticator: Who/what authenticated the document
    :param Reference custodian: Organization which maintains the document
    :param RelatesTo relatesTo: Relationships to other documents
    :param str description: Human-readable description
    :param CodeableConcept securityLabel: Document security-tags
    :param Content content: Document referenced
    :param Context context: Clinical context of document
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
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "authenticator": {"class_name": "Reference", "is_contained": False},
        "custodian": {"class_name": "Reference", "is_contained": False},
        "relatesTo": {"class_name": "RelatesTo", "is_contained": True},
        "securityLabel": {"class_name": "CodeableConcept", "is_contained": False},
        "content": {"class_name": "Content", "is_contained": True},
        "context": {"class_name": "Context", "is_contained": True},
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
        docStatus: "str" = None,
        type: "CodeableConcept" = None,
        category: list["CodeableConcept"] = None,
        subject: "Reference" = None,
        date: "str" = None,
        author: list["Reference"] = None,
        authenticator: "Reference" = None,
        custodian: "Reference" = None,
        relatesTo: list["RelatesTo"] = None,
        description: "str" = None,
        securityLabel: list["CodeableConcept"] = None,
        content: list["Content"] = None,
        context: "Context" = None,
    ):
        self.resourceType = resourceType or "DocumentReference"
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
        self.docStatus = docStatus
        self.type = type
        self.category = category or []
        self.subject = subject
        self.date = date
        self.author = author or []
        self.authenticator = authenticator
        self.custodian = custodian
        self.relatesTo = relatesTo or []
        self.description = description
        self.securityLabel = securityLabel or []
        self.content = content or []
        self.context = context

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentReference":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DocumentReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
