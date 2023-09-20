"""
Generated class for Evidence. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Extension import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase
@dataclass
class Evidence(ModelBase):
    """ Explanation of what this profile contains/is for.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this evidence, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the evidence
    :param str version: Business version of the evidence
    :param str name: Name for this evidence (computer friendly)
    :param str title: Name for this evidence (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the Evidence
    :param str status: draft | active | retired | unknown
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the evidence
    :param Annotation note: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for evidence (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the evidence was approved by publisher
    :param str lastReviewDate: When the evidence was last reviewed
    :param Period effectivePeriod: When the evidence is expected to be used
    :param CodeableConcept topic: The category of the Evidence, such as Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param Reference exposureBackground: What population?
    :param Reference exposureVariant: What exposure?
    :param Reference outcome: What outcome?
    """
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
    
    shortTitle: str = None
    
    subtitle: str = None
    
    status: str = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    description: str = None
    
    note: list["Annotation"] = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
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
    
    exposureBackground: "Reference" = None
    
    exposureVariant: list["Reference"] = None
    
    outcome: list["Reference"] = None
    