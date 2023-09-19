"""
Generated class for NamingSystem. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *


@dataclass
class NamingSystem:
    """ A curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc.  Represents a "System" used within the Identifier and Coding data types.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this naming system, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the naming system (business identifier)
    :param str version: Business version of the naming system
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this naming system (computer friendly)
    :param str title: Title for this naming system (human friendly)
    :param str status: draft | active | retired | unknown
    :param str kind: codesystem | identifier | root
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str responsible: Who maintains system namespace?
    :param CodeableConcept type: e.g. driver,  provider,  patient, bank etc
    :param str description: Natural language description of the naming system
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for naming system (if applicable)
    :param str purpose: Why this naming system is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the NamingSystem was approved by publisher
    :param str lastReviewDate: When the NamingSystem was last reviewed by the publisher
    :param Period effectivePeriod: When the NamingSystem is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the CodeSystem
    :param ContactDetail editor: Who edited the NamingSystem
    :param ContactDetail reviewer: Who reviewed the NamingSystem
    :param ContactDetail endorser: Who endorsed the NamingSystem
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param str usage: How/where is it used
    :param BackboneElement uniqueId: Unique identifiers used for system
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: oid | uuid | uri | iri-stem | v2csmnemonic | other
    :param str value: The unique identifier
    :param bool preferred: Is this the id that should be used for this type
    :param str comment: Notes about identifier usage
    :param Period period: When is identifier valid?
    :param bool authoritative: Whether the identifier is authoritative
    
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
    
    kind: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    responsible: str = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
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
    
    usage: str = None
    
    uniqueId: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    value: str = None
    
    preferred: bool = None
    
    comment: str = None
    
    period: "Period" = None
    
    authoritative: bool = None
    