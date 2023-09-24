"""
Generated class for Binary. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Binary(DomainResource):
    """ A resource that represents the data of a single raw artifact as digital content accessible in its native format.  A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param str contentType: MimeType of the binary content
    :param 'Reference' securityContext: Identifies another resource to use as proxy when enforcing access control
    :param str data: The actual content
    """
    def __init__(self, resourceType: str = "Binary",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  contentType: str = None,  securityContext: 'Reference' = None,  data: str = None, ):
        self.resourceType: str = resourceType or "Binary"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.contentType: str = contentType 
        self.securityContext: 'Reference' = securityContext 
        self.data: str = data 
        