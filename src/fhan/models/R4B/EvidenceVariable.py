"""
Generated class for EvidenceVariable. 
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
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Expression import *
from fhan.models.R4B.Reference import *


@dataclass
class EvidenceVariable:
    """
    The EvidenceVariable resource describes an element that knowledge (Evidence) is about.
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
    
    shortTitle: str = None
    
    subtitle: str = None
    
    status: str = None
    
    date: str = None
    
    description: str = None
    
    note: "Annotation" = None
    
    useContext: "UsageContext" = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    actual: bool = None
    
    characteristicCombination: str = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    definitionReference: "Reference" = None
    
    definitionReference: str = None
    
    definitionReference: "CodeableConcept" = None
    
    definitionReference: "Expression" = None
    
    method: "CodeableConcept" = None
    
    device: "Reference" = None
    
    exclude: bool = None
    
    timeFromStart: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    quantity: "Quantity" = None
    
    range: "Range" = None
    
    note: "Annotation" = None
    
    groupMeasure: str = None
    
    handling: str = None
    
    category: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: "Range" = None
    