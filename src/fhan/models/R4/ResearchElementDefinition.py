"""
Generated class for ResearchElementDefinition. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Period import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Characteristic(BaseModel):
    """A characteristic that defines the members of the research element. Multiple characteristics are applied with "and" semantics.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept definitionCodeableConcept: What code or expression defines members?
    :param str definitionCanonical: What code or expression defines members?
    :param Expression definitionExpression: What code or expression defines members?
    :param DataRequirement definitionDataRequirement: What code or expression defines members?
    :param UsageContext usageContext: What code/value pairs define members?
    :param bool exclude: Whether the characteristic includes or excludes members
    :param CodeableConcept unitOfMeasure: What unit is the outcome described in?
    :param str studyEffectiveDescription: What time period does the study cover
    :param str studyEffectiveDateTime: What time period does the study cover
    :param Period studyEffectivePeriod: What time period does the study cover
    :param Duration studyEffectiveDuration: What time period does the study cover
    :param Timing studyEffectiveTiming: What time period does the study cover
    :param Duration studyEffectiveTimeFromStart: Observation time from study start
    :param str studyEffectiveGroupMeasure: mean | median | mean-of-mean | mean-of-median | median-of-mean | median-of-median
    :param str participantEffectiveDescription: What time period do participants cover
    :param str participantEffectiveDateTime: What time period do participants cover
    :param Period participantEffectivePeriod: What time period do participants cover
    :param Duration participantEffectiveDuration: What time period do participants cover
    :param Timing participantEffectiveTiming: What time period do participants cover
    :param Duration participantEffectiveTimeFromStart: Observation time from study start
    :param str participantEffectiveGroupMeasure: mean | median | mean-of-mean | mean-of-median | median-of-mean | median-of-median
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "definitionCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "definitionExpression": {"class_name": "Expression", "is_contained": False},
        "definitionDataRequirement": {
            "class_name": "DataRequirement",
            "is_contained": False,
        },
        "usageContext": {"class_name": "UsageContext", "is_contained": False},
        "unitOfMeasure": {"class_name": "CodeableConcept", "is_contained": False},
        "studyEffectivePeriod": {"class_name": "Period", "is_contained": False},
        "studyEffectiveDuration": {"class_name": "Duration", "is_contained": False},
        "studyEffectiveTiming": {"class_name": "Timing", "is_contained": False},
        "studyEffectiveTimeFromStart": {
            "class_name": "Duration",
            "is_contained": False,
        },
        "participantEffectivePeriod": {"class_name": "Period", "is_contained": False},
        "participantEffectiveDuration": {
            "class_name": "Duration",
            "is_contained": False,
        },
        "participantEffectiveTiming": {"class_name": "Timing", "is_contained": False},
        "participantEffectiveTimeFromStart": {
            "class_name": "Duration",
            "is_contained": False,
        },
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        definitionCodeableConcept: "CodeableConcept" = None,
        definitionCanonical: "str" = None,
        definitionExpression: "Expression" = None,
        definitionDataRequirement: "DataRequirement" = None,
        usageContext: list["UsageContext"] = None,
        exclude: "bool" = None,
        unitOfMeasure: "CodeableConcept" = None,
        studyEffectiveDescription: "str" = None,
        studyEffectiveDateTime: "str" = None,
        studyEffectivePeriod: "Period" = None,
        studyEffectiveDuration: "Duration" = None,
        studyEffectiveTiming: "Timing" = None,
        studyEffectiveTimeFromStart: "Duration" = None,
        studyEffectiveGroupMeasure: "str" = None,
        participantEffectiveDescription: "str" = None,
        participantEffectiveDateTime: "str" = None,
        participantEffectivePeriod: "Period" = None,
        participantEffectiveDuration: "Duration" = None,
        participantEffectiveTiming: "Timing" = None,
        participantEffectiveTimeFromStart: "Duration" = None,
        participantEffectiveGroupMeasure: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.definitionCodeableConcept = definitionCodeableConcept
        self.definitionCanonical = definitionCanonical
        self.definitionExpression = definitionExpression
        self.definitionDataRequirement = definitionDataRequirement
        self.usageContext = usageContext or []
        self.exclude = exclude
        self.unitOfMeasure = unitOfMeasure
        self.studyEffectiveDescription = studyEffectiveDescription
        self.studyEffectiveDateTime = studyEffectiveDateTime
        self.studyEffectivePeriod = studyEffectivePeriod
        self.studyEffectiveDuration = studyEffectiveDuration
        self.studyEffectiveTiming = studyEffectiveTiming
        self.studyEffectiveTimeFromStart = studyEffectiveTimeFromStart
        self.studyEffectiveGroupMeasure = studyEffectiveGroupMeasure
        self.participantEffectiveDescription = participantEffectiveDescription
        self.participantEffectiveDateTime = participantEffectiveDateTime
        self.participantEffectivePeriod = participantEffectivePeriod
        self.participantEffectiveDuration = participantEffectiveDuration
        self.participantEffectiveTiming = participantEffectiveTiming
        self.participantEffectiveTimeFromStart = participantEffectiveTimeFromStart
        self.participantEffectiveGroupMeasure = participantEffectiveGroupMeasure

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ResearchElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ResearchElementDefinition(DomainResource):
    """The ResearchElementDefinition resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this research element definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the research element definition
    :param str version: Business version of the research element definition
    :param str name: Name for this research element definition (computer friendly)
    :param str title: Name for this research element definition (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the ResearchElementDefinition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param Reference subjectReference: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the research element definition
    :param str comment: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for research element definition (if applicable)
    :param str purpose: Why this research element definition is defined
    :param str usage: Describes the clinical usage of the ResearchElementDefinition
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the research element definition was approved by publisher
    :param str lastReviewDate: When the research element definition was last reviewed
    :param Period effectivePeriod: When the research element definition is expected to be used
    :param CodeableConcept topic: The category of the ResearchElementDefinition, such as Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param str library: Logic used by the ResearchElementDefinition
    :param str type: population | exposure | outcome
    :param str variableType: dichotomous | continuous | descriptive
    :param Characteristic characteristic: What defines the members of the research element
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "subjectCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "subjectReference": {"class_name": "Reference", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
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
        experimental: "bool" = None,
        subjectCodeableConcept: "CodeableConcept" = None,
        subjectReference: "Reference" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        comment: list["str"] = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        usage: "str" = None,
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
        library: list["str"] = None,
        type: "str" = None,
        variableType: "str" = None,
        characteristic: list["Characteristic"] = None,
    ):
        self.resourceType = resourceType or "ResearchElementDefinition"
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
        self.experimental = experimental
        self.subjectCodeableConcept = subjectCodeableConcept
        self.subjectReference = subjectReference
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.comment = comment or []
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.usage = usage
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
        self.library = library or []
        self.type = type
        self.variableType = variableType
        self.characteristic = characteristic or []

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchElementDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ResearchElementDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
