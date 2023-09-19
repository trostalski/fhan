"""
Generated class for List. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class List:
    """
    A list is a curated collection of resources.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    mode: str = None
    
    title: str = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    date: str = None
    
    source: "Reference" = None
    
    orderedBy: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    entry: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    flag: "CodeableConcept" = None
    
    deleted: bool = None
    
    date: str = None
    
    item: "Reference" = None
    
    emptyReason: "CodeableConcept" = None
    