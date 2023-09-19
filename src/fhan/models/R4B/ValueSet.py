"""
Generated class for ValueSet. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.CodeableConcept import *


@dataclass
class ValueSet:
    """
    Enforces the minimum information set for the value set metadata required by HL7 and other organizations that share and publish value sets
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
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    immutable: bool = None
    
    purpose: str = None
    
    copyright: str = None
    
    compose: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    lockedDate: str = None
    
    inactive: bool = None
    
    include: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    system: str = None
    
    version: str = None
    
    concept: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    display: str = None
    
    designation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    language: str = None
    
    use: "Coding" = None
    
    value: str = None
    
    filter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    property: str = None
    
    op: str = None
    
    value: str = None
    
    valueSet: str = None
    
    exclude: "BackboneElement" = None
    
    expansion: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: str = None
    
    timestamp: str = None
    
    total: int = None
    
    offset: int = None
    
    parameter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    valuestring: str = None
    
    valuestring: bool = None
    
    valuestring: int = None
    
    valuestring: float = None
    
    valuestring: str = None
    
    valuestring: str = None
    
    valuestring: str = None
    
    contains: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    system: str = None
    
    abstract: bool = None
    
    inactive: bool = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    
    designation: "BackboneElement" = None
    
    contains: "BackboneElement" = None
    