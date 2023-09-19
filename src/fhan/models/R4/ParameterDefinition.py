"""
Generated class for ParameterDefinition. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *


@dataclass
class ParameterDefinition:
    """
    Base StructureDefinition for ParameterDefinition Type: The parameters to the module. This collection specifies both the input and output parameters. Input parameters are provided by the caller as part of the $evaluate operation. Output parameters are included in the GuidanceResponse.
    """
    id: str = None
    
    extension: "Extension" = None
    
    name: str = None
    
    use: str = None
    
    min: int = None
    
    max: str = None
    
    documentation: str = None
    
    type: str = None
    
    profile: str = None
    