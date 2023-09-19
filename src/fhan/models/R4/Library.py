"""
Generated class for Library. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Library:
    """
    Enforces the minimum information set for the library metadata required by HL7 and other organizations that share and publish libraries
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
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
    type: "CodeableConcept" = None
    
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
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    topic: "CodeableConcept" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    parameter: "ParameterDefinition" = None
    
    dataRequirement: "DataRequirement" = None
    
    content: "Attachment" = None
    