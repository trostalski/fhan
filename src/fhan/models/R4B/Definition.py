"""
Generated class for Definition. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


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
    