"""
Generated class for RelatedArtifact. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Attachment import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class RelatedArtifact(ModelBase):
    """ Base StructureDefinition for RelatedArtifact Type: Related artifacts such as additional documentation, justification, or bibliographic references.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str type: documentation | justification | citation | predecessor | successor | derived-from | depends-on | composed-of
    :param str label: Short label
    :param str display: Brief description of the related artifact
    :param str citation: Bibliographic citation for the artifact
    :param str url: Where the artifact can be accessed
    :param 'Attachment' document: What document is being referenced
    :param str resource: What resource is being referenced
    """
    def __init__(self, resourceType: str = "RelatedArtifact",  id: str = None,  extension: list['Extension'] = None,  type: str = None,  label: str = None,  display: str = None,  citation: str = None,  url: str = None,  document: 'Attachment' = None,  resource: str = None, ):
        self.resourceType: str = resourceType or "RelatedArtifact"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: str = type 
        self.label: str = label 
        self.display: str = display 
        self.citation: str = citation 
        self.url: str = url 
        self.document: 'Attachment' = document 
        self.resource: str = resource 
        