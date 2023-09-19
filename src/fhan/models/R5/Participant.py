"""
Generated class for Participant. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Identifier import *


@dataclass
class Participant:
    """ Logical Model: A pattern followed by resources that represent the participant in some activity, process, or responsible for providing information about a resource.
    :param Identifier identifier: Business Identifier for {{title}}
    :param bool active: Whether the {{title}} is currently active
    :param str name: A name for the {{title}}
    
    """
    identifier: "Identifier" = None
    
    active: bool = None
    
    name: str = None
    