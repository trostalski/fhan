"""
Generated class for RelatedArtifact. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Attachment import *
from fhan.models.R4.Extension import *


@dataclass
class RelatedArtifact:
    """
    Base StructureDefinition for RelatedArtifact Type: Related artifacts such as additional documentation, justification, or bibliographic references.
    """
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    label: str = None
    
    display: str = None
    
    citation: str = None
    
    url: str = None
    
    document: "Attachment" = None
    
    resource: str = None
    