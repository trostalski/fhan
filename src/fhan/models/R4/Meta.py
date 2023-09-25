"""
Generated class for Meta. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Meta(ModelBase):
    """ Base StructureDefinition for Meta Type: The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str versionId: Version specific identifier
    :param str lastUpdated: When the resource version last changed
    :param str source: Identifies where the resource comes from
    :param str profile: Profiles this resource claims to conform to
    :param list['Coding'] security: Security Labels applied to this resource
    :param list['Coding'] tag: Tags applied to this resource
    """
    def __init__(self, resourceType: str = "Meta",  id: str = None,  extension: list['Extension'] = None,  versionId: str = None,  lastUpdated: str = None,  source: str = None,  profile: str = None,  security: list['Coding'] = None,  tag: list['Coding'] = None, ):
        self.resourceType: str = resourceType or "Meta"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.versionId: str = versionId 
        self.lastUpdated: str = lastUpdated 
        self.source: str = source 
        self.profile: str = profile or []
        self.security: list['Coding'] = security or []
        self.tag: list['Coding'] = tag or []
        