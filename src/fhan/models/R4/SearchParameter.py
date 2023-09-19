"""
Generated class for SearchParameter. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *


@dataclass
class SearchParameter:
    """
    A search parameter that defines a named search item that can be used to search/filter on a resource.
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
    
    version: str = None
    
    name: str = None
    
    derivedFrom: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    code: str = None
    
    base: str = None
    
    type: str = None
    
    expression: str = None
    
    xpath: str = None
    
    xpathUsage: str = None
    
    target: str = None
    
    multipleOr: bool = None
    
    multipleAnd: bool = None
    
    comparator: str = None
    
    modifier: str = None
    
    chain: str = None
    
    component: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    definition: str = None
    
    expression: str = None
    