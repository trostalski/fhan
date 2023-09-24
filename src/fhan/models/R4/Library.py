"""
Generated class for Library. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Extension import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

@dataclass
class Library(ModelBase):
    """ Enforces the minimum information set for the library metadata required by HL7 and other organizations that share and publish libraries
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this library, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the library
    :param str version: Business version of the library
    :param str name: Name for this library (computer friendly)
    :param str title: Name for this library (human friendly)
    :param str subtitle: Subordinate title of the library
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept type: logic-library | model-definition | asset-collection | module-definition
    :param CodeableConcept subjectCodeableConcept: Type of individual the library content is focused on
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the library
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for library (if applicable)
    :param str purpose: Why this library is defined
    :param str usage: Describes the clinical usage of the library
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the library was approved by publisher
    :param str lastReviewDate: When the library was last reviewed
    :param Period effectivePeriod: When the library is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param ParameterDefinition parameter: Parameters defined by the library
    :param DataRequirement dataRequirement: What data is referenced by this library
    :param Attachment content: Contents of the library, either embedded or referenced
    """

    resourceType: str = "Library"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    identifier: list["Identifier"] = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
    type: "CodeableConcept" = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    description: str = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    purpose: str = None
    
    usage: str = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    topic: list["CodeableConcept"] = None
    
    author: list["ContactDetail"] = None
    
    editor: list["ContactDetail"] = None
    
    reviewer: list["ContactDetail"] = None
    
    endorser: list["ContactDetail"] = None
    
    relatedArtifact: list["RelatedArtifact"] = None
    
    parameter: list["ParameterDefinition"] = None
    
    dataRequirement: list["DataRequirement"] = None
    
    content: list["Attachment"] = None
    