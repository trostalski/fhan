"""
Generated class for EventDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Extension import *
from fhan.models.R5.TriggerDefinition import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class EventDefinition:
    """ The EventDefinition resource provides a reusable description of when a particular event can occur.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this event definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the event definition
    :param str version: Business version of the event definition
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this event definition (computer friendly)
    :param str title: Name for this event definition (human friendly)
    :param str subtitle: Subordinate title of the event definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: Type of individual the event definition is focused on
    :param Reference subjectCodeableConcept: Type of individual the event definition is focused on
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the event definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for event definition (if applicable)
    :param str purpose: Why this event definition is defined
    :param str usage: Describes the clinical usage of the event definition
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the event definition was approved by publisher
    :param str lastReviewDate: When the event definition was last reviewed by the publisher
    :param Period effectivePeriod: When the event definition is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param TriggerDefinition trigger: "when" the event occurs (multiple = 'or')
    
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
    
    subtitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
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
    
    trigger: "TriggerDefinition" = None
    