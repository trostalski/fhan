"""
Generated class for Publishable. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Identifier import *


@dataclass
class Publishable:
    """ Logical Model: A pattern to be followed by resources that represent a publishable knowledge artifact such as a ValueSet, Profile, Library, Decision Support Rule, or Quality Measure.
    :param Identifier identifier: Additional identifier for the {{title}}
    :param str date: Date last changed
    :param ContactDetail contact: Contact details for the publisher
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for {{title}} (if applicable)
    :param str purpose: Why this {{title}} is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the {{title}} was approved by publisher
    :param str lastReviewDate: When the {{title}} was last reviewed
    :param Period effectivePeriod: When the {{title}} is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc.
    :param ContactDetail author: Who authored the {{title}}
    :param ContactDetail editor: Who edited the {{title}}
    :param ContactDetail reviewer: Who reviewed the {{title}}
    :param ContactDetail endorser: Who endorsed the {{title}}
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc.
    
    """
    identifier: "Identifier" = None
    
    date: str = None
    
    contact: "ContactDetail" = None
    
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
    