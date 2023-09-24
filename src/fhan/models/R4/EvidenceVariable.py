"""
Generated class for EvidenceVariable. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Period import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Timing import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Extension import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.DomainResource import *


    
    

class Characteristic(ModelBase):
    """ A characteristic that defines the members of the evidence element. Multiple characteristics are applied with "and" semantics.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Natural language description of the characteristic
    :param 'Reference' definitionReference: What code or expression defines members?
    :param list['UsageContext'] usageContext: What code/value pairs define members?
    :param bool exclude: Whether the characteristic includes or excludes members
    :param str participantEffectiveDateTime: What time period do participants cover
    :param 'Duration' timeFromStart: Observation time from study start
    :param str groupMeasure: mean | median | mean-of-mean | mean-of-median | median-of-mean | median-of-median
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  description: str = None,  definitionReference: 'Reference' = None,  usageContext: list['UsageContext'] = None,  exclude: bool = None,  participantEffectiveDateTime: str = None,  timeFromStart: 'Duration' = None,  groupMeasure: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.description: str = description 
        self.definitionReference: 'Reference' = definitionReference 
        self.usageContext: list['UsageContext'] = usageContext or []
        self.exclude: bool = exclude 
        self.participantEffectiveDateTime: str = participantEffectiveDateTime 
        self.timeFromStart: 'Duration' = timeFromStart 
        self.groupMeasure: str = groupMeasure 
        

class EvidenceVariable(DomainResource):
    """ Explanation of what this profile contains/is for.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this evidence variable, represented as a URI (globally unique)
    :param list['Identifier'] identifier: Additional identifier for the evidence variable
    :param str version: Business version of the evidence variable
    :param str name: Name for this evidence variable (computer friendly)
    :param str title: Name for this evidence variable (human friendly)
    :param str shortTitle: Title for use in informal contexts
    :param str subtitle: Subordinate title of the EvidenceVariable
    :param str status: draft | active | retired | unknown
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the evidence variable
    :param list['Annotation'] note: Used for footnotes or explanatory notes
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for evidence variable (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the evidence variable was approved by publisher
    :param str lastReviewDate: When the evidence variable was last reviewed
    :param 'Period' effectivePeriod: When the evidence variable is expected to be used
    :param list['CodeableConcept'] topic: The category of the EvidenceVariable, such as Education, Treatment, Assessment, etc.
    :param list['ContactDetail'] author: Who authored the content
    :param list['ContactDetail'] editor: Who edited the content
    :param list['ContactDetail'] reviewer: Who reviewed the content
    :param list['ContactDetail'] endorser: Who endorsed the content
    :param list['RelatedArtifact'] relatedArtifact: Additional documentation, citations, etc.
    :param str type: dichotomous | continuous | descriptive
    :param list['Characteristic'] characteristic: What defines the members of the evidence element
    """
    def __init__(self, resourceType: str = "EvidenceVariable",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  identifier: list['Identifier'] = None,  version: str = None,  name: str = None,  title: str = None,  shortTitle: str = None,  subtitle: str = None,  status: str = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  note: list['Annotation'] = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  topic: list['CodeableConcept'] = None,  author: list['ContactDetail'] = None,  editor: list['ContactDetail'] = None,  reviewer: list['ContactDetail'] = None,  endorser: list['ContactDetail'] = None,  relatedArtifact: list['RelatedArtifact'] = None,  type: str = None,  characteristic: list['Characteristic'] = None, ):
        self.resourceType: str = resourceType or "EvidenceVariable"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.url: str = url 
        self.identifier: list['Identifier'] = identifier or []
        self.version: str = version 
        self.name: str = name 
        self.title: str = title 
        self.shortTitle: str = shortTitle 
        self.subtitle: str = subtitle 
        self.status: str = status 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.note: list['Annotation'] = note or []
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.copyright: str = copyright 
        self.approvalDate: str = approvalDate 
        self.lastReviewDate: str = lastReviewDate 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.topic: list['CodeableConcept'] = topic or []
        self.author: list['ContactDetail'] = author or []
        self.editor: list['ContactDetail'] = editor or []
        self.reviewer: list['ContactDetail'] = reviewer or []
        self.endorser: list['ContactDetail'] = endorser or []
        self.relatedArtifact: list['RelatedArtifact'] = relatedArtifact or []
        self.type: str = type 
        self.characteristic: list['Characteristic'] = characteristic or []
        