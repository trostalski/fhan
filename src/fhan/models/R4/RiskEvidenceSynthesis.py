"""
Generated class for RiskEvidenceSynthesis. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
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


class SampleSize(BaseModel):
    """A description of the size of the sample involved in the synthesis.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of sample size
    :param int numberOfStudies: How many studies?
    :param int numberOfParticipants: How many participants?
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
        description: "str" = None,
        numberOfStudies: "int" = None,
        numberOfParticipants: "int" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.numberOfStudies = numberOfStudies
        self.numberOfParticipants = numberOfParticipants

    @classmethod
    def from_dict(cls, data: dict) -> "RiskEvidenceSynthesis":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RiskEvidenceSynthesis":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PrecisionEstimate(BaseModel):
    """A description of the precision of the estimate for the effect.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of precision estimate
    :param float level: Level of confidence interval
    :param float _from: Lower bound
    :param float to: Upper bound
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        level: "float" = None,
        _from: "float" = None,
        to: "float" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.level = level
        self._from = _from
        self.to = to

    @classmethod
    def from_dict(cls, data: dict) -> "RiskEvidenceSynthesis":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RiskEvidenceSynthesis":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RiskEstimate(BaseModel):
    """The estimated risk of the outcome.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of risk estimate
    :param CodeableConcept type: Type of risk estimate
    :param float value: Point estimate
    :param CodeableConcept unitOfMeasure: What unit is the outcome described in?
    :param int denominatorCount: Sample size for group measured
    :param int numeratorCount: Number with the outcome
    :param PrecisionEstimate precisionEstimate: How precise the estimate is
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "unitOfMeasure": {"class_name": "CodeableConcept", "is_contained": False},
        "precisionEstimate": {"class_name": "PrecisionEstimate", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        description: "str" = None,
        type: "CodeableConcept" = None,
        value: "float" = None,
        unitOfMeasure: "CodeableConcept" = None,
        denominatorCount: "int" = None,
        numeratorCount: "int" = None,
        precisionEstimate: list["PrecisionEstimate"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.type = type
        self.value = value
        self.unitOfMeasure = unitOfMeasure
        self.denominatorCount = denominatorCount
        self.numeratorCount = numeratorCount
        self.precisionEstimate = precisionEstimate or []

    @classmethod
    def from_dict(cls, data: dict) -> "RiskEvidenceSynthesis":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RiskEvidenceSynthesis":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CertaintySubcomponent(BaseModel):
    """A description of a component of the overall certainty.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of subcomponent of certainty rating
    :param CodeableConcept rating: Subcomponent certainty rating
    :param Annotation note: Used for footnotes or explanatory notes
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "rating": {"class_name": "CodeableConcept", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        rating: list["CodeableConcept"] = None,
        note: list["Annotation"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.rating = rating or []
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "RiskEvidenceSynthesis":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RiskEvidenceSynthesis":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Certainty(BaseModel):
    """A description of the certainty of the risk estimate.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept rating: Certainty rating
    :param Annotation note: Used for footnotes or explanatory notes
    :param CertaintySubcomponent certaintySubcomponent: A component that contributes to the overall certainty
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "rating": {"class_name": "CodeableConcept", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "certaintySubcomponent": {
            "class_name": "CertaintySubcomponent",
            "is_contained": True,
        },
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        rating: list["CodeableConcept"] = None,
        note: list["Annotation"] = None,
        certaintySubcomponent: list["CertaintySubcomponent"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.rating = rating or []
        self.note = note or []
        self.certaintySubcomponent = certaintySubcomponent or []

    @classmethod
    def from_dict(cls, data: dict) -> "RiskEvidenceSynthesis":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RiskEvidenceSynthesis":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RiskEvidenceSynthesis(DomainResource):
    """The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state where the risk estimate is derived from a combination of research studies.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this risk evidence synthesis, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the risk evidence synthesis
    :param str version: Business version of the risk evidence synthesis
    :param str name: Name for this risk evidence synthesis (computer friendly)
    :param str title: Name for this risk evidence synthesis (human friendly)
    :param str status: draft | active | retired | unknown
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the risk evidence synthesis
    :param Annotation note: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for risk evidence synthesis (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the risk evidence synthesis was approved by publisher
    :param str lastReviewDate: When the risk evidence synthesis was last reviewed
    :param Period effectivePeriod: When the risk evidence synthesis is expected to be used
    :param CodeableConcept topic: The category of the EffectEvidenceSynthesis, such as Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param CodeableConcept synthesisType: Type of synthesis
    :param CodeableConcept studyType: Type of study
    :param Reference population: What population?
    :param Reference exposure: What exposure?
    :param Reference outcome: What outcome?
    :param SampleSize sampleSize: What sample size was involved?
    :param RiskEstimate riskEstimate: What was the estimated risk
    :param Certainty certainty: How certain is the risk
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
        "synthesisType": {"class_name": "CodeableConcept", "is_contained": False},
        "studyType": {"class_name": "CodeableConcept", "is_contained": False},
        "population": {"class_name": "Reference", "is_contained": False},
        "exposure": {"class_name": "Reference", "is_contained": False},
        "outcome": {"class_name": "Reference", "is_contained": False},
        "sampleSize": {"class_name": "SampleSize", "is_contained": True},
        "riskEstimate": {"class_name": "RiskEstimate", "is_contained": True},
        "certainty": {"class_name": "Certainty", "is_contained": True},
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
        synthesisType: "CodeableConcept" = None,
        studyType: "CodeableConcept" = None,
        population: "Reference" = None,
        exposure: "Reference" = None,
        outcome: "Reference" = None,
        sampleSize: "SampleSize" = None,
        riskEstimate: "RiskEstimate" = None,
        certainty: list["Certainty"] = None,
    ):
        self.resourceType = resourceType or "RiskEvidenceSynthesis"
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
        self.synthesisType = synthesisType
        self.studyType = studyType
        self.population = population
        self.exposure = exposure
        self.outcome = outcome
        self.sampleSize = sampleSize
        self.riskEstimate = riskEstimate
        self.certainty = certainty or []

    @classmethod
    def from_dict(cls, data: dict) -> "RiskEvidenceSynthesis":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RiskEvidenceSynthesis":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
