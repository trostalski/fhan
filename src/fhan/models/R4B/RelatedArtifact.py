"""
Generated class for RelatedArtifact. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Attachment import *


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
    