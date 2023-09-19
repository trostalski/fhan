"""
Generated class for Meta. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Coding import *


@dataclass
class Meta:
    """
    Base StructureDefinition for Meta Type: The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
    """
    id: str = None
    
    extension: "Extension" = None
    
    versionId: str = None
    
    lastUpdated: str = None
    
    source: str = None
    
    profile: str = None
    
    security: "Coding" = None
    
    tag: "Coding" = None
    