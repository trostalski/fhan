"""
Generated class for ParameterDefinition. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class ParameterDefinition(ModelBase):
    """ Base StructureDefinition for ParameterDefinition Type: The parameters to the module. This collection specifies both the input and output parameters. Input parameters are provided by the caller as part of the $evaluate operation. Output parameters are included in the GuidanceResponse.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str name: Name used to access the parameter value
    :param str use: in | out
    :param int min: Minimum cardinality
    :param str max: Maximum cardinality (a number of *)
    :param str documentation: A brief description of the parameter
    :param str type: What type of value
    :param str profile: What profile the value is expected to be
    """
    def __init__(self, resourceType: str = "ParameterDefinition",  id: str = None,  extension: list['Extension'] = None,  name: str = None,  use: str = None,  min: int = None,  max: str = None,  documentation: str = None,  type: str = None,  profile: str = None, ):
        self.resourceType: str = resourceType or "ParameterDefinition"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.name: str = name 
        self.use: str = use 
        self.min: int = min 
        self.max: str = max 
        self.documentation: str = documentation 
        self.type: str = type 
        self.profile: str = profile 
        