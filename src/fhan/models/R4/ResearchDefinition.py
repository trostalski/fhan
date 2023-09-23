"""
Generated class for ResearchDefinition. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

@dataclass
class ResearchDefinition(ModelBase):
    """ The ResearchDefinition resource describes the conditional state (population and any exposures being compared within the population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is about.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this research definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the research definition
    :param str version: Business version of the research definition
    :param str name: Name for this research definition (computer friendly)
    :param str title: Name for this research definition (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the ResearchDefinition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the research definition
    :param str comment: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for research definition (if applicable)
    :param str purpose: Why this research definition is defined
    :param str usage: Describes the clinical usage of the ResearchDefinition
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the research definition was approved by publisher
    :param str lastReviewDate: When the research definition was last reviewed
    :param Period effectivePeriod: When the research definition is expected to be used
    :param CodeableConcept topic: The category of the ResearchDefinition, such as Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param str library: Logic used by the ResearchDefinition
    :param Reference population: What population?
    :param Reference exposure: What exposure?
    :param Reference exposureAlternative: What alternative exposure state?
    :param Reference outcome: What outcome?
    """

    resourceType: str = "ResearchDefinition"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    url: str = None
    
    identifier: list[Identifier] = Identifier() 
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    shortTitle: str = None
    
    subtitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectCodeableConcept: "CodeableConcept" = CodeableConcept()
    
    date: str = None
    
    publisher: str = None
    
    contact: list[ContactDetail] = ContactDetail() 
    
    description: str = None
    
    comment: str = None
    
    useContext: list[UsageContext] = UsageContext() 
    
    jurisdiction: list[CodeableConcept] = CodeableConcept() 
    
    purpose: str = None
    
    usage: str = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = Period()
    
    topic: list[CodeableConcept] = CodeableConcept() 
    
    author: list[ContactDetail] = ContactDetail() 
    
    editor: list[ContactDetail] = ContactDetail() 
    
    reviewer: list[ContactDetail] = ContactDetail() 
    
    endorser: list[ContactDetail] = ContactDetail() 
    
    relatedArtifact: list[RelatedArtifact] = RelatedArtifact() 
    
    library: str = None
    
    population: "Reference" = Reference()
    
    exposure: "Reference" = Reference()
    
    exposureAlternative: "Reference" = Reference()
    
    outcome: "Reference" = Reference()
    