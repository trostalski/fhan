"""
Generated class for Definition. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Identifier import *
from fhan.models.generator_models import ModelBase


@dataclass
class Definition(ModelBase):
    """ Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    :param str url: Logical canonical URL to reference this {{title}} (globally unique)
    :param Identifier identifier: Business Identifier for {{title}}
    :param str version: Business version of the {{title}}
    :param str title: Name for this {{title}} (Human friendly)
    :param str derivedFromCanonical: Based on FHIR protocol or definition
    :param str derivedFromUri: Based on external protocol or definition
    :param str partOf: Part of referenced definition
    :param str replaces: Request(s) replaced by this request
    :param str status: draft | active | retired | unknown
    :param bool experimental: If for testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: Type of individual the defined service is for
    :param Reference subjectCodeableConcept: Type of individual the defined service is for
    :param str date: Date status first applied
    :param Reference publisher: The name of the individual or organization that published the {{title}}
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the {{title}}
    :param UsageContext useContext: Content intends to support these contexts
    :param CodeableConcept jurisdiction: Intended jurisdiction for {{title}} (if applicable)
    :param str purpose: Why this {{title}} is defined
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When {{title}} approved by publisher
    :param str lastReviewDate: Last review date for the {{title}}
    :param Period effectivePeriod: The effective date range for the {{title}}
    :param CodeableConcept performerType: Desired kind of service performer
    """
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    title: str = None
    
    derivedFromCanonical: str = None
    
    derivedFromUri: str = None
    
    partOf: str = None
    
    replaces: str = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    date: str = None
    
    publisher: "Reference" = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    performerType: "CodeableConcept" = None
    