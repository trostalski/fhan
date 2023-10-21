"""
Generated class for Evidence. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Evidence(DomainResource):
    """The Evidence resource describes the conditional state (population and any exposures being compared within the population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is about.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this evidence, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the evidence
    :param str version: Business version of the evidence
    :param str name: Name for this evidence (computer friendly)
    :param str title: Name for this evidence (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the Evidence
    :param str status: draft | active | retired | unknown
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the evidence
    :param Annotation note: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for evidence (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the evidence was approved by publisher
    :param str lastReviewDate: When the evidence was last reviewed
    :param Period effectivePeriod: When the evidence is expected to be used
    :param CodeableConcept topic: The category of the Evidence, such as Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param Reference exposureBackground: What population?
    :param Reference exposureVariant: What exposure?
    :param Reference outcome: What outcome?
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
        "note": {"class_name": "Annotation", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        "topic": {"class_name": "CodeableConcept", "is_contained": False},
        "author": {"class_name": "ContactDetail", "is_contained": False},
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        "exposureBackground": {"class_name": "Reference", "is_contained": False},
        "exposureVariant": {"class_name": "Reference", "is_contained": False},
        "outcome": {"class_name": "Reference", "is_contained": False},
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
        name: "str" = None,
        title: "str" = None,
        shortTitle: "str" = None,
        subtitle: "str" = None,
        status: "str" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        note: list["Annotation"] = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        copyright: "str" = None,
        approvalDate: "str" = None,
        lastReviewDate: "str" = None,
        effectivePeriod: "Period" = None,
        topic: list["CodeableConcept"] = None,
        author: list["ContactDetail"] = None,
        editor: list["ContactDetail"] = None,
        reviewer: list["ContactDetail"] = None,
        endorser: list["ContactDetail"] = None,
        relatedArtifact: list["RelatedArtifact"] = None,
        exposureBackground: "Reference" = None,
        exposureVariant: list["Reference"] = None,
        outcome: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "Evidence"
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
        self.name = name
        self.title = title
        self.shortTitle = shortTitle
        self.subtitle = subtitle
        self.status = status
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.note = note or []
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.copyright = copyright
        self.approvalDate = approvalDate
        self.lastReviewDate = lastReviewDate
        self.effectivePeriod = effectivePeriod
        self.topic = topic or []
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.relatedArtifact = relatedArtifact or []
        self.exposureBackground = exposureBackground
        self.exposureVariant = exposureVariant or []
        self.outcome = outcome or []

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Evidence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
