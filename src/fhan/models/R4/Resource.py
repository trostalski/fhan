"""
Generated class for Resource. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

class Resource(ModelBase):
    """ This is the base resource type for everything.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    """
    def __init__(self, resourceType: str = "Resource",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None, ):
        self.resourceType: str = resourceType or "Resource"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        