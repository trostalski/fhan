"""
Generated class for RelatedArtifact. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Extension import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Element import *



@dataclass
class RelatedArtifact(Element):
    """ Base StructureDefinition for RelatedArtifact Type: Related artifacts such as additional documentation, justification, or bibliographic references.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: documentation | justification | citation | predecessor | successor | derived-from | depends-on | composed-of
    :param str label: Short label
    :param str display: Brief description of the related artifact
    :param str citation: Bibliographic citation for the artifact
    :param str url: Where the artifact can be accessed
    :param Attachment document: What document is being referenced
    :param str resource: What resource is being referenced
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
    