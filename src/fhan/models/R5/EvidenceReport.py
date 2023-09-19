"""
Generated class for EvidenceReport. 
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
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class EvidenceReport:
    """ The EvidenceReport Resource is a specialized container for a collection of resources and codeable concepts, adapted to support compositions of Evidence, EvidenceVariable, and Citation resources and related concepts.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this EvidenceReport, represented as a globally unique URI
    :param str status: draft | active | retired | unknown
    :param UsageContext useContext: The context that the content is intended to support
    :param Identifier identifier: Unique identifier for the evidence report
    :param Identifier relatedIdentifier: Identifiers for articles that may relate to more than one evidence report
    :param Reference citeAsReference: Citation for this report
    :param str citeAsReference: Citation for this report
    :param CodeableConcept type: Kind of report
    :param Annotation note: Used for footnotes and annotations
    :param RelatedArtifact relatedArtifact: Link, description or reference to artifact associated with the report
    :param BackboneElement subject: Focus of the report
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement characteristic: Characteristic
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Characteristic code
    :param Reference valueReference: Characteristic value
    :param CodeableConcept valueReference: Characteristic value
    :param bool valueReference: Characteristic value
    :param Quantity valueReference: Characteristic value
    :param Range valueReference: Characteristic value
    :param bool exclude: Is used to express not the characteristic
    :param Period period: Timeframe for the characteristic
    :param Annotation note: Footnotes and/or explanatory notes
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param BackboneElement relatesTo: Relationships to other compositions/documents
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: replaces | amends | appends | transforms | replacedWith | amendedWith | appendedWith | transformedWith
    :param BackboneElement target: Target of the relationship
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: Target of the relationship URL
    :param Identifier identifier: Target of the relationship Identifier
    :param str display: Target of the relationship Display
    :param Reference resource: Target of the relationship Resource reference
    :param BackboneElement section: Composition is broken into sections
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for section (e.g. for ToC)
    :param CodeableConcept focus: Classification of section (recommended)
    :param Reference focusReference: Classification of section by Resource
    :param Reference author: Who and/or what authored the section
    :param Narrative text: Text summary of the section, for human interpretation
    :param str mode: working | snapshot | changes
    :param CodeableConcept orderedBy: Order of section entries
    :param CodeableConcept entryClassifier: Extensible classifiers as content
    :param Reference entryReference: Reference to resources as content
    :param Quantity entryQuantity: Quantity as content
    :param CodeableConcept emptyReason: Why the section is empty
    :param BackboneElement section: Composition is broken into sections
    
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
    
    status: str = None
    
    useContext: "UsageContext" = None
    
    identifier: "Identifier" = None
    
    relatedIdentifier: "Identifier" = None
    
    citeAsReference: "Reference" = None
    
    citeAsReference: str = None
    
    type: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    subject: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    valueReference: "Reference" = None
    
    valueReference: "CodeableConcept" = None
    
    valueReference: bool = None
    
    valueReference: "Quantity" = None
    
    valueReference: "Range" = None
    
    exclude: bool = None
    
    period: "Period" = None
    
    note: "Annotation" = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    target: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    display: str = None
    
    resource: "Reference" = None
    
    section: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    focus: "CodeableConcept" = None
    
    focusReference: "Reference" = None
    
    author: "Reference" = None
    
    text: "Narrative" = None
    
    mode: str = None
    
    orderedBy: "CodeableConcept" = None
    
    entryClassifier: "CodeableConcept" = None
    
    entryReference: "Reference" = None
    
    entryQuantity: "Quantity" = None
    
    emptyReason: "CodeableConcept" = None
    
    section: "BackboneElement" = None
    