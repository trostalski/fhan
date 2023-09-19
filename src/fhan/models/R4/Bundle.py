"""
Generated class for Bundle. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Resource import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Bundle:
    """
    A container for a collection of resources.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    identifier: "Identifier" = None
    
    type: str = None
    
    timestamp: str = None
    
    total: int = None
    
    link: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relation: str = None
    
    url: str = None
    
    entry: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    link: "BackboneElement" = None
    
    fullUrl: str = None
    
    resource: "Resource" = None
    
    search: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: str = None
    
    score: float = None
    
    request: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    method: str = None
    
    url: str = None
    
    ifNoneMatch: str = None
    
    ifModifiedSince: str = None
    
    ifMatch: str = None
    
    ifNoneExist: str = None
    
    response: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    status: str = None
    
    location: str = None
    
    etag: str = None
    
    lastModified: str = None
    
    outcome: "Resource" = None
    
    signature: "Signature" = None
    