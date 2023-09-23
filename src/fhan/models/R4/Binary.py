"""
Generated class for Binary. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

@dataclass
class Binary(ModelBase):
    """ A resource that represents the data of a single raw artifact as digital content accessible in its native format.  A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param str contentType: MimeType of the binary content
    :param Reference securityContext: Identifies another resource to use as proxy when enforcing access control
    :param str data: The actual content
    """

    resourceType: str = "Binary"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    contentType: str = None
    
    securityContext: "Reference" = Reference()
    
    data: str = None
    