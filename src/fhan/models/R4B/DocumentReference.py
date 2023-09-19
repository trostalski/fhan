"""
Generated class for DocumentReference. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class DocumentReference:
    """
    A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    masterIdentifier: "Identifier" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    docStatus: str = None
    
    type: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    date: str = None
    
    author: "Reference" = None
    
    authenticator: "Reference" = None
    
    custodian: "Reference" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    target: "Reference" = None
    
    description: str = None
    
    securityLabel: "CodeableConcept" = None
    
    content: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    attachment: "Attachment" = None
    
    format: "Coding" = None
    
    context: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    encounter: "Reference" = None
    
    event: "CodeableConcept" = None
    
    period: "Period" = None
    
    facilityType: "CodeableConcept" = None
    
    practiceSetting: "CodeableConcept" = None
    
    sourcePatientInfo: "Reference" = None
    
    related: "Reference" = None
    