"""
Generated class for Resource. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

@dataclass
class Resource(ModelBase):
    """ This is the base resource type for everything.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    """

    resourceType: str = "Resource"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    