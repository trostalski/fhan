"""
Generated class for Definition. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Period import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Identifier import *


@dataclass
class Definition:
    """
    Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
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
    