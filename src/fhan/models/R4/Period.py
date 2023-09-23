"""
Generated class for Period. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *


@dataclass
class Period(Element):
    """ Base StructureDefinition for Period Type: A time period defined by a start and end date and optionally time.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str start: Starting time with inclusive boundary
    :param str end: End time with inclusive boundary, if not ongoing
    """

    resourceType: str = "Period"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    start: str = None
    
    end: str = None
    