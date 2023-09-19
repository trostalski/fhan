"""
Generated class for CodeSystem. 
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
class CodeSystem:
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
    
    purpose: str = None
    
    copyright: str = None
    
    caseSensitive: bool = None
    
    valueSet: str = None
    
    hierarchyMeaning: str = None
    
    compositional: bool = None
    
    versionNeeded: bool = None
    
    content: str = None
    
    supplements: str = None
    
    count: int = None
    
    filter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    description: str = None
    
    operator: str = None
    
    value: str = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    uri: str = None
    
    description: str = None
    
    type: str = None
    
    concept: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    display: str = None
    
    definition: str = None
    
    designation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    language: str = None
    
    use: "Coding" = None
    
    value: str = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    valuecode: str = None
    
    valuecode: "Coding" = None
    
    valuecode: str = None
    
    valuecode: int = None
    
    valuecode: bool = None
    
    valuecode: str = None
    
    valuecode: float = None
    
    concept: "BackboneElement" = None
    