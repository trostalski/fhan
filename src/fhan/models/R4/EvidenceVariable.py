"""
Generated class for EvidenceVariable. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Timing import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Extension import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Characteristic(Element):
    """ A characteristic that defines the members of the evidence element. Multiple characteristics are applied with "and" semantics.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Natural language description of the characteristic
    :param Reference definitionReference: What code or expression defines members?
    :param UsageContext usageContext: What code/value pairs define members?
    :param bool exclude: Whether the characteristic includes or excludes members
    :param str participantEffectiveDateTime: What time period do participants cover
    :param Duration timeFromStart: Observation time from study start
    :param str groupMeasure: mean | median | mean-of-mean | mean-of-median | median-of-mean | median-of-median
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    description: str = None
    definitionReference: "Reference" = Reference()
    usageContext: list[UsageContext] = UsageContext() 
    
    exclude: bool = None
    
    participantEffectiveDateTime: str = None
    timeFromStart: "Duration" = Duration()
    
    groupMeasure: str = None
    

@dataclass
class EvidenceVariable(ModelBase):
    """ Explanation of what this profile contains/is for.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this evidence variable, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the evidence variable
    :param str version: Business version of the evidence variable
    :param str name: Name for this evidence variable (computer friendly)
    :param str title: Name for this evidence variable (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the EvidenceVariable
    :param str status: draft | active | retired | unknown
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the evidence variable
    :param Annotation note: Used for footnotes or explanatory notes
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for evidence variable (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the evidence variable was approved by publisher
    :param str lastReviewDate: When the evidence variable was last reviewed
    :param Period effectivePeriod: When the evidence variable is expected to be used
    :param CodeableConcept topic: The category of the EvidenceVariable, such as Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    :param str type: dichotomous | continuous | descriptive
    :param Characteristic characteristic: What defines the members of the evidence element
    """

    resourceType: str = "EvidenceVariable"
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
    
    date: str = None
    
    publisher: str = None
    
    contact: list[ContactDetail] = ContactDetail() 
    
    description: str = None
    
    note: list[Annotation] = Annotation() 
    
    useContext: list[UsageContext] = UsageContext() 
    
    jurisdiction: list[CodeableConcept] = CodeableConcept() 
    
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
    
    type: str = None
    
    characteristic: list[Characteristic] = Characteristic() 
    