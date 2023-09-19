"""
Generated class for Period. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Extension import *


@dataclass
class Period:
    """ Period Type: A time period defined by a start and end date and optionally time.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str start: Starting time with inclusive boundary
    :param str end: End time with inclusive boundary, if not ongoing
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    start: str = None
    
    end: str = None
    