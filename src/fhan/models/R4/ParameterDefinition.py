"""
Generated class for ParameterDefinition. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *

@dataclass
class ParameterDefinition(Element):
    """ Base StructureDefinition for ParameterDefinition Type: The parameters to the module. This collection specifies both the input and output parameters. Input parameters are provided by the caller as part of the $evaluate operation. Output parameters are included in the GuidanceResponse.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str name: Name used to access the parameter value
    :param str use: in | out
    :param int min: Minimum cardinality
    :param str max: Maximum cardinality (a number of *)
    :param str documentation: A brief description of the parameter
    :param str type: What type of value
    :param str profile: What profile the value is expected to be
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    name: str = None
    
    use: str = None
    
    min: int = None
    
    max: str = None
    
    documentation: str = None
    
    type: str = None
    
    profile: str = None
    