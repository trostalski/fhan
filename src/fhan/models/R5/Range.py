"""
Generated class for Range. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Quantity import *
from fhan.models.R5.Extension import *


@dataclass
class Range:
    """ Range Type: A set of ordered Quantities defined by a low and high limit.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity low: Low limit
    :param Quantity high: High limit
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    low: "Quantity" = None
    
    high: "Quantity" = None
    