"""
Generated class for Meta. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *


@dataclass
class Meta(Element):
    """ Base StructureDefinition for Meta Type: The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str versionId: Version specific identifier
    :param str lastUpdated: When the resource version last changed
    :param str source: Identifies where the resource comes from
    :param str profile: Profiles this resource claims to conform to
    :param Coding security: Security Labels applied to this resource
    :param Coding tag: Tags applied to this resource
    """

    resourceType: str = "Meta"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    versionId: str = None
    
    lastUpdated: str = None
    
    source: str = None
    
    profile: str = None
    
    security: list[Coding] = Coding() 
    
    tag: list[Coding] = Coding() 
    