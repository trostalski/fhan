"""
Generated class for EvidenceVariable. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Expression import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Duration import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Characteristic(BaseModel):
    """A characteristic that defines the members of the evidence element. Multiple characteristics are applied with "and" semantics.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Natural language description of the characteristic
    :param Reference definitionReference: What code or expression defines members?
    :param str definitionCanonical: What code or expression defines members?
    :param CodeableConcept definitionCodeableConcept: What code or expression defines members?
    :param Expression definitionExpression: What code or expression defines members?
    :param DataRequirement definitionDataRequirement: What code or expression defines members?
    :param TriggerDefinition definitionTriggerDefinition: What code or expression defines members?
    :param UsageContext usageContext: What code/value pairs define members?
    :param bool exclude: Whether the characteristic includes or excludes members
    :param str participantEffectiveDateTime: What time period do participants cover
    :param Period participantEffectivePeriod: What time period do participants cover
    :param Duration participantEffectiveDuration: What time period do participants cover
    :param Timing participantEffectiveTiming: What time period do participants cover
    :param Duration timeFromStart: Observation time from study start
    :param str groupMeasure: mean | median | mean-of-mean | mean-of-median | median-of-mean | median-of-median
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "definitionReference": {"class_name": "Reference", "is_contained": False},
        "definitionCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "definitionExpression": {"class_name": "Expression", "is_contained": False},
        "definitionDataRequirement": {
            "class_name": "DataRequirement",
            "is_contained": False,
        },
        "definitionTriggerDefinition": {
            "class_name": "TriggerDefinition",
            "is_contained": False,
        },
        "usageContext": {"class_name": "UsageContext", "is_contained": False},
        "participantEffectivePeriod": {"class_name": "Period", "is_contained": False},
        "participantEffectiveDuration": {
            "class_name": "Duration",
            "is_contained": False,
        },
        "participantEffectiveTiming": {"class_name": "Timing", "is_contained": False},
        "timeFromStart": {"class_name": "Duration", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        description: "str" = None,
        definitionReference: "Reference" = None,
        definitionCanonical: "str" = None,
        definitionCodeableConcept: "CodeableConcept" = None,
        definitionExpression: "Expression" = None,
        definitionDataRequirement: "DataRequirement" = None,
        definitionTriggerDefinition: "TriggerDefinition" = None,
        usageContext: list["UsageContext"] = None,
        exclude: "bool" = None,
        participantEffectiveDateTime: "str" = None,
        participantEffectivePeriod: "Period" = None,
        participantEffectiveDuration: "Duration" = None,
        participantEffectiveTiming: "Timing" = None,
        timeFromStart: "Duration" = None,
        groupMeasure: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.definitionReference = definitionReference
        self.definitionCanonical = definitionCanonical
        self.definitionCodeableConcept = definitionCodeableConcept
        self.definitionExpression = definitionExpression
        self.definitionDataRequirement = definitionDataRequirement
        self.definitionTriggerDefinition = definitionTriggerDefinition
        self.usageContext = usageContext or []
        self.exclude = exclude
        self.participantEffectiveDateTime = participantEffectiveDateTime
        self.participantEffectivePeriod = participantEffectivePeriod
        self.participantEffectiveDuration = participantEffectiveDuration
        self.participantEffectiveTiming = participantEffectiveTiming
        self.timeFromStart = timeFromStart
        self.groupMeasure = groupMeasure

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceVariable":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "EvidenceVariable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class EvidenceVariable(DomainResource):
    """The EvidenceVariable resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this evidence variable, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the evidence variable
    :param str version: Business version of the evidence variable
    :param str name: Name for this evidence variable (computer friendly)
    :param str title: Name for this evidence variable (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the EvidenceVariable
    :param str status: draft | active | retired | unknown
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the evidence variable
    :param Annotation note: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for evidence variable (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the evidence variable was approved by publisher
    :param str lastReviewDate: When the evidence variable was last reviewed
    :param Period effectivePeriod: When the evidence variable is expected to be used
    :param CodeableConcept topic: The category of the EvidenceVariable, such as Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param str type: dichotomous | continuous | descriptive
    :param Characteristic characteristic: What defines the members of the evidence element
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
        "characteristic": {"class_name": "Characteristic", "is_contained": True},
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
        type: "str" = None,
        characteristic: list["Characteristic"] = None,
    ):
        self.resourceType = resourceType or "EvidenceVariable"
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
        self.type = type
        self.characteristic = characteristic or []

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceVariable":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "EvidenceVariable":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
