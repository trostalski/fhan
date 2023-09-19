"""
Generated class for Definition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.UsageContext import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Identifier import *


@dataclass
class Definition:
    """ Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    :param str url: Canonical identifier for this {{title}}, represented as an absolute URI (globally unique)
    :param Identifier identifier: Business identifier for {{title}}
    :param str version: Business version of the {{title}}
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this {{title}} (computer friendly)
    :param str title: Name for this {{title}} (human friendly)
    :param str derivedFromCanonical: Based on FHIR protocol or definition
    :param str derivedFromUri: Based on external protocol or definition
    :param str partOf: Part of referenced definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableReference subject: Type of individual the defined service is for
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the {{title}}
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for {{title}} (if applicable)
    :param str purpose: Why this {{title}} is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the {{title}} was approved by publisher
    :param str lastReviewDate: When the {{title}} was last reviewed
    :param Period effectivePeriod: When the {{title}} is expected to be used
    :param CodeableConcept topic: Descriptive topics related to the content of the {{title}}. Topics provide a high-level categorization as well as keywords for the {{title}} that can be useful for filtering and searching
    :param CodeableConcept performerType: Desired kind of service performer
    :param CodeableConcept code: Service to be done
    :param CodeableReference product: Product to use/manipulate
    
    """
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    derivedFromCanonical: str = None
    
    derivedFromUri: str = None
    
    partOf: str = None
    
    status: str = None
    
    experimental: bool = None
    
    subject: "CodeableReference" = None
    
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
    
    topic: "CodeableConcept" = None
    
    performerType: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    product: "CodeableReference" = None
    