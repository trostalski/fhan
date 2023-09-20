"""
Generated class for Attachment. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *


@dataclass
class Attachment(Element):
    """ Base StructureDefinition for Attachment Type: For referring to data content defined in other formats.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str contentType: Mime type of the content, with charset etc.
    :param str language: Human language of the content (BCP-47)
    :param str data: Data inline, base64ed
    :param str url: Uri where the data can be found
    :param int size: Number of bytes of content (if url provided)
    :param str hash: Hash of the data (sha-1, base64ed)
    :param str title: Label to display in place of the data
    :param str creation: Date attachment was first created
    """

    resourceType: str = "Attachment"
    id: str = None
    
    extension: list["Extension"] = None
    
    contentType: str = None
    
    language: str = None
    
    data: str = None
    
    url: str = None
    
    size: int = None
    
    hash: str = None
    
    title: str = None
    
    creation: str = None
    