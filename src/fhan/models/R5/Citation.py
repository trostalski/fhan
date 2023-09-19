"""
Generated class for Citation. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
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
class Citation:
    """ The Citation Resource enables reference to any knowledge artifact for purposes of identification and attribution. The Citation Resource supports existing reference structures and developing publication practices such as versioning, expressing complex contributorship roles, and referencing computable resources.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this citation record, represented as a globally unique URI
    :param Identifier identifier: Identifier for the citation record itself
    :param str version: Business version of the citation record
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this citation record (computer friendly)
    :param str title: Name for this citation record (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: The publisher of the citation record, not the publisher of the article or artifact being cited
    :param ContactDetail contact: Contact details for the publisher of the citation record
    :param str description: Natural language description of the citation
    :param UsageContext useContext: The context that the citation record content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for citation record (if applicable)
    :param str purpose: Why this citation is defined
    :param str copyright: Use and/or publishing restrictions for the citation record, not for the cited artifact
    :param str copyrightLabel: Copyright holder and year(s) for the ciation record, not for the cited artifact
    :param str approvalDate: When the citation record was approved by publisher
    :param str lastReviewDate: When the citation record was last reviewed by the publisher
    :param Period effectivePeriod: When the citation record is expected to be used
    :param ContactDetail author: Who authored the citation record
    :param ContactDetail editor: Who edited the citation record
    :param ContactDetail reviewer: Who reviewed the citation record
    :param ContactDetail endorser: Who endorsed the citation record
    :param BackboneElement summary: A human-readable display of key concepts to represent the citation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept style: Format for display of the citation summary
    :param str text: The human-readable display of the citation summary
    :param BackboneElement classification: The assignment to an organizing scheme
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of classifier (e.g. publication type, keyword)
    :param CodeableConcept classifier: The specific classification value
    :param Annotation note: Used for general notes and annotations not coded elsewhere
    :param CodeableConcept currentState: The status of the citation record
    :param BackboneElement statusDate: An effective date or period for a status of the citation record
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept activity: Classification of the status
    :param bool actual: Either occurred or expected
    :param Period period: When the status started and/or ended
    :param RelatedArtifact relatedArtifact: Artifact related to the citation record
    :param BackboneElement citedArtifact: The article or artifact being described
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Unique identifier. May include DOI, PMID, PMCID, etc
    :param Identifier relatedIdentifier: Identifier not unique to the cited artifact. May include trial registry identifiers
    :param str dateAccessed: When the cited artifact was accessed
    :param BackboneElement version: The defined version of the cited artifact
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str value: The version number or other version identifier
    :param Reference baseCitation: Citation for the main version of the cited artifact
    :param CodeableConcept currentState: The status of the cited artifact
    :param BackboneElement statusDate: An effective date or period for a status of the cited artifact
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept activity: Classification of the status
    :param bool actual: Either occurred or expected
    :param Period period: When the status started and/or ended
    :param BackboneElement title: The title details of the article or artifact
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of title
    :param CodeableConcept language: Used to express the specific language
    :param str text: The title of the article or artifact
    :param BackboneElement abstract: Summary of the article or artifact
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of abstract
    :param CodeableConcept language: Used to express the specific language
    :param str text: Abstract content
    :param str copyright: Copyright notice for the abstract
    :param BackboneElement part: The component of the article or artifact
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of component
    :param str value: The specification of the component
    :param Reference baseCitation: The citation for the full article or artifact
    :param BackboneElement relatesTo: The artifact related to the cited artifact
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: documentation | justification | citation | predecessor | successor | derived-from | depends-on | composed-of | part-of | amends | amended-with | appends | appended-with | cites | cited-by | comments-on | comment-in | contains | contained-in | corrects | correction-in | replaces | replaced-with | retracts | retracted-by | signs | similar-to | supports | supported-with | transforms | transformed-into | transformed-with | documents | specification-of | created-with | cite-as | reprint | reprint-of
    :param CodeableConcept classifier: Additional classifiers
    :param str label: Short label
    :param str display: Brief description of the related artifact
    :param str citation: Bibliographic citation for the artifact
    :param Attachment document: What document is being referenced
    :param str resource: What artifact is being referenced
    :param Reference resourceReference: What artifact, if not a conformance resource
    :param BackboneElement publicationForm: If multiple, used to represent alternative forms of the article that are not separate citations
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement publishedIn: The collection the cited article or artifact is published in
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Kind of container (e.g. Periodical, database, or book)
    :param Identifier identifier: Journal identifiers include ISSN, ISO Abbreviation and NLMuniqueID; Book identifiers include ISBN
    :param str title: Name of the database or title of the book or journal
    :param Reference publisher: Name of or resource describing the publisher
    :param str publisherLocation: Geographic location of the publisher
    :param CodeableConcept citedMedium: Internet or Print
    :param str volume: Volume number of journal or other collection in which the article is published
    :param str issue: Issue, part or supplement of journal or other collection in which the article is published
    :param str articleDate: The date the article was added to the database, or the date the article was released
    :param str publicationDateText: Text representation of the date on which the issue of the cited artifact was published
    :param str publicationDateSeason: Season in which the cited artifact was published
    :param str lastRevisionDate: The date the article was last revised or updated in the database
    :param CodeableConcept language: Language(s) in which this form of the article is published
    :param str accessionNumber: Entry number or identifier for inclusion in a database
    :param str pageString: Used for full display of pagination
    :param str firstPage: Used for isolated representation of first page
    :param str lastPage: Used for isolated representation of last page
    :param str pageCount: Number of pages or screens
    :param str copyright: Copyright notice for the full article or artifact
    :param BackboneElement webLocation: Used for any URL for the article or artifact cited
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept classifier: Code the reason for different URLs, e.g. abstract and full-text
    :param str url: The specific URL
    :param BackboneElement classification: The assignment to an organizing scheme
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of classifier (e.g. publication type, keyword)
    :param CodeableConcept classifier: The specific classification value
    :param Reference artifactAssessment: Complex or externally created classification
    :param BackboneElement contributorship: Attribution of authors and other contributors
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool complete: Indicates if the list includes all authors and/or contributors
    :param BackboneElement entry: An individual entity named as a contributor
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference contributor: The identity of the individual contributor
    :param str forenameInitials: For citation styles that use initials
    :param Reference affiliation: Organizational affiliation
    :param CodeableConcept contributionType: The specific contribution
    :param CodeableConcept role: The role of the contributor (e.g. author, editor, reviewer, funder)
    :param BackboneElement contributionInstance: Contributions with accounting for time or number
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The specific contribution
    :param str time: The time that the contribution was made
    :param bool correspondingContact: Whether the contributor is the corresponding contributor for the role
    :param int rankingOrder: Ranked order of contribution
    :param BackboneElement summary: Used to record a display of the author/contributor list without separate data element for each list member
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Such as author list, contributorship statement, funding statement, acknowledgements statement, or conflicts of interest statement
    :param CodeableConcept style: The format for the display string
    :param CodeableConcept source: Used to code the producer or rule for creating the display string
    :param str value: The display string for the author list, contributor list, or contributorship statement
    :param Annotation note: Any additional information or content for the article or artifact
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    copyrightLabel: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    summary: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    style: "CodeableConcept" = None
    
    text: str = None
    
    classification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    classifier: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    currentState: "CodeableConcept" = None
    
    statusDate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    activity: "CodeableConcept" = None
    
    actual: bool = None
    
    period: "Period" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    citedArtifact: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    relatedIdentifier: "Identifier" = None
    
    dateAccessed: str = None
    
    version: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    value: str = None
    
    baseCitation: "Reference" = None
    
    currentState: "CodeableConcept" = None
    
    statusDate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    activity: "CodeableConcept" = None
    
    actual: bool = None
    
    period: "Period" = None
    
    title: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    language: "CodeableConcept" = None
    
    text: str = None
    
    abstract: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    language: "CodeableConcept" = None
    
    text: str = None
    
    copyright: str = None
    
    part: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    value: str = None
    
    baseCitation: "Reference" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    classifier: "CodeableConcept" = None
    
    label: str = None
    
    display: str = None
    
    citation: str = None
    
    document: "Attachment" = None
    
    resource: str = None
    
    resourceReference: "Reference" = None
    
    publicationForm: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    publishedIn: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    identifier: "Identifier" = None
    
    title: str = None
    
    publisher: "Reference" = None
    
    publisherLocation: str = None
    
    citedMedium: "CodeableConcept" = None
    
    volume: str = None
    
    issue: str = None
    
    articleDate: str = None
    
    publicationDateText: str = None
    
    publicationDateSeason: str = None
    
    lastRevisionDate: str = None
    
    language: "CodeableConcept" = None
    
    accessionNumber: str = None
    
    pageString: str = None
    
    firstPage: str = None
    
    lastPage: str = None
    
    pageCount: str = None
    
    copyright: str = None
    
    webLocation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    classifier: "CodeableConcept" = None
    
    url: str = None
    
    classification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    classifier: "CodeableConcept" = None
    
    artifactAssessment: "Reference" = None
    
    contributorship: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    complete: bool = None
    
    entry: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    contributor: "Reference" = None
    
    forenameInitials: str = None
    
    affiliation: "Reference" = None
    
    contributionType: "CodeableConcept" = None
    
    role: "CodeableConcept" = None
    
    contributionInstance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    time: str = None
    
    correspondingContact: bool = None
    
    rankingOrder: int = None
    
    summary: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    style: "CodeableConcept" = None
    
    source: "CodeableConcept" = None
    
    value: str = None
    
    note: "Annotation" = None
    