"""
Generated class for Library. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.ParameterDefinition import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.DataRequirement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Library:
    """ Supports declaration of the library metadata required by HL7 and other organizations that share and publish libraries with a focus on the aspects of that metadata that are important for post-publication activities including distribution, inclusion in repositories, consumption, and implementation.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Extension
    :param Extension extension:knowledgeCapability: shareable | computable | publishable | executable
    :param Extension extension:knowledgeRepresentationLevel: narrative | semi-structured | structured | executable
    :param Extension extension:artifactComment: Additional documentation, review, or usage guidance
    :param Extension extension:logicDefinition: A logic definition used in the artifact
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this library, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the library
    :param str version: Business version of the library
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this library (computer friendly)
    :param str title: Name for this library (human friendly)
    :param str subtitle: Subordinate title of the library
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept type: logic-library | model-definition | asset-collection | module-definition
    :param CodeableConcept subjectCodeableConcept: Type of individual the library content is focused on
    :param Reference subjectCodeableConcept: Type of individual the library content is focused on
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the library
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for library (if applicable)
    :param str purpose: Why this library is defined
    :param str usage: Describes the clinical usage of the library
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the library was approved by publisher
    :param str lastReviewDate: When the library was last reviewed by the publisher
    :param Period effectivePeriod: When the library is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: documentation | justification | citation | predecessor | successor | derived-from | depends-on | composed-of | part-of | amends | amended-with | appends | appended-with | cites | cited-by | comments-on | comment-in | contains | contained-in | corrects | correction-in | replaces | replaced-with | retracts | retracted-by | signs | similar-to | supports | supported-with | transforms | transformed-into | transformed-with | documents | specification-of | created-with | cite-as
    :param CodeableConcept classifier: Additional classifiers
    :param str label: Short label
    :param str display: Brief description of the related artifact
    :param str citation: Bibliographic citation for the artifact
    :param Attachment document: What document is being referenced
    :param str resource: What artifact is being referenced
    :param Reference resourceReference: What artifact, if not a conformance resource
    :param str publicationStatus: draft | active | retired | unknown
    :param str publicationDate: Date of publication of the artifact being referred to
    :param ParameterDefinition parameter: Parameters defined by the library
    :param DataRequirement dataRequirement: What data is referenced by this library
    :param Attachment content: Contents of the library, either embedded or referenced
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    extension:knowledgeCapability: "Extension" = None
    
    extension:knowledgeRepresentationLevel: "Extension" = None
    
    extension:artifactComment: "Extension" = None
    
    extension:logicDefinition: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
    type: "CodeableConcept" = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    usage: str = None
    
    copyright: str = None
    
    copyrightLabel: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    topic: "CodeableConcept" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    classifier: "CodeableConcept" = None
    
    label: str = None
    
    display: str = None
    
    citation: str = None
    
    document: "Attachment" = None
    
    resource: str = None
    
    resourceReference: "Reference" = None
    
    publicationStatus: str = None
    
    publicationDate: str = None
    
    parameter: "ParameterDefinition" = None
    
    dataRequirement: "DataRequirement" = None
    
    content: "Attachment" = None
    