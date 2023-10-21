"""
Generated class for Composition. 
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


class Attester(BaseModel):
    """A participant who has attested to the accuracy of the composition/document.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: personal | professional | legal | official
    :param str time: When the composition was attested
    :param Reference party: Who attested the composition
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "party": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        mode: "str" = None,
        time: "str" = None,
        party: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.mode = mode
        self.time = time
        self.party = party

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Composition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RelatesTo(BaseModel):
    """Relationships that this composition has with other compositions or documents that already exist.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: replaces | transforms | signs | appends
    :param Identifier targetIdentifier: Target of the relationship
    :param Reference targetReference: Target of the relationship
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "targetIdentifier": {"class_name": "Identifier", "is_contained": False},
        "targetReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "str" = None,
        targetIdentifier: "Identifier" = None,
        targetReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.targetIdentifier = targetIdentifier
        self.targetReference = targetReference

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Composition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Event(BaseModel):
    """The clinical service, such as a colonoscopy or an appendectomy, being documented.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Code(s) that apply to the event being documented
    :param Period period: The period covered by the documentation
    :param Reference detail: The event(s) being documented
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "detail": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: list["CodeableConcept"] = None,
        period: "Period" = None,
        detail: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code or []
        self.period = period
        self.detail = detail or []

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Composition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Section(BaseModel):
    """The root of the sections that make up the composition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for section (e.g. for ToC)
    :param CodeableConcept code: Classification of section (recommended)
    :param Reference author: Who and/or what authored the section
    :param Reference focus: Who/what the section is about, when it is not about the subject of composition
    :param Narrative text: Text summary of the section, for human interpretation
    :param str mode: working | snapshot | changes
    :param CodeableConcept orderedBy: Order of section entries
    :param Reference entry: A reference to data that supports this section
    :param CodeableConcept emptyReason: Why the section is empty
    :param Section section: Nested Section
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "focus": {"class_name": "Reference", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "orderedBy": {"class_name": "CodeableConcept", "is_contained": False},
        "entry": {"class_name": "Reference", "is_contained": False},
        "emptyReason": {"class_name": "CodeableConcept", "is_contained": False},
        "section": {"class_name": "Section", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        title: "str" = None,
        code: "CodeableConcept" = None,
        author: list["Reference"] = None,
        focus: "Reference" = None,
        text: "Narrative" = None,
        mode: "str" = None,
        orderedBy: "CodeableConcept" = None,
        entry: list["Reference"] = None,
        emptyReason: "CodeableConcept" = None,
        section: list["Section"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title
        self.code = code
        self.author = author or []
        self.focus = focus
        self.text = text
        self.mode = mode
        self.orderedBy = orderedBy
        self.entry = entry or []
        self.emptyReason = emptyReason
        self.section = section or []

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Composition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Composition(DomainResource):
    """A set of healthcare-related information that is assembled together into a single logical package that provides a single coherent statement of meaning, establishes its own context and that has clinical attestation with regard to who is making the statement. A Composition defines the structure and narrative content necessary for a document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Version-independent identifier for the Composition
    :param str status: preliminary | final | amended | entered-in-error
    :param CodeableConcept type: Kind of composition (LOINC if possible)
    :param CodeableConcept category: Categorization of Composition
    :param Reference subject: Who and/or what the composition is about
    :param Reference encounter: Context of the Composition
    :param str date: Composition editing time
    :param Reference author: Who and/or what authored the composition
    :param str title: Human Readable name/title
    :param str confidentiality: As defined by affinity domain
    :param Attester attester: Attests to accuracy of composition
    :param Reference custodian: Organization which maintains the composition
    :param RelatesTo relatesTo: Relationships to other compositions/documents
    :param Event event: The clinical service(s) being documented
    :param Section section: Composition is broken into sections
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
        "attester": {"class_name": "Attester", "is_contained": True},
        "custodian": {"class_name": "Reference", "is_contained": False},
        "relatesTo": {"class_name": "RelatesTo", "is_contained": True},
        "event": {"class_name": "Event", "is_contained": True},
        "section": {"class_name": "Section", "is_contained": True},
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
        identifier: "Identifier" = None,
        status: "str" = None,
        type: "CodeableConcept" = None,
        category: list["CodeableConcept"] = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        date: "str" = None,
        author: list["Reference"] = None,
        title: "str" = None,
        confidentiality: "str" = None,
        attester: list["Attester"] = None,
        custodian: "Reference" = None,
        relatesTo: list["RelatesTo"] = None,
        event: list["Event"] = None,
        section: list["Section"] = None,
    ):
        self.resourceType = resourceType or "Composition"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.status = status
        self.type = type
        self.category = category or []
        self.subject = subject
        self.encounter = encounter
        self.date = date
        self.author = author or []
        self.title = title
        self.confidentiality = confidentiality
        self.attester = attester or []
        self.custodian = custodian
        self.relatesTo = relatesTo or []
        self.event = event or []
        self.section = section or []

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Composition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
