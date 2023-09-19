"""
Generated class for EvidenceReport. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.RelatedArtifact import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class EvidenceReport:
    """
    The EvidenceReport Resource is a specialized container for a collection of resources and codable concepts, adapted to support compositions of Evidence, EvidenceVariable, and Citation resources and related concepts.
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
    
    status: str = None
    
    useContext: "UsageContext" = None
    
    identifier: "Identifier" = None
    
    relatedIdentifier: "Identifier" = None
    
    citeAsReference: "Reference" = None
    
    citeAsReference: str = None
    
    type: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    subject: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    valueReference: "Reference" = None
    
    valueReference: "CodeableConcept" = None
    
    valueReference: bool = None
    
    valueReference: "Quantity" = None
    
    valueReference: "Range" = None
    
    exclude: bool = None
    
    period: "Period" = None
    
    note: "Annotation" = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    targetIdentifier: "Identifier" = None
    
    targetIdentifier: "Reference" = None
    
    section: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    focus: "CodeableConcept" = None
    
    focusReference: "Reference" = None
    
    author: "Reference" = None
    
    text: "Narrative" = None
    
    mode: str = None
    
    orderedBy: "CodeableConcept" = None
    
    entryClassifier: "CodeableConcept" = None
    
    entryReference: "Reference" = None
    
    entryQuantity: "Quantity" = None
    
    emptyReason: "CodeableConcept" = None
    
    section: "BackboneElement" = None
    