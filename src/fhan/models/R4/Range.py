"""
Generated class for Range. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *


@dataclass
class Range(Element):
    """ Base StructureDefinition for Range Type: A set of ordered Quantities defined by a low and high limit.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity low: Low limit
    :param Quantity high: High limit
    """

    resourceType: str = "Range"
    id: str = None
    
    extension: list["Extension"] = None
    
    low: "Quantity" = None
    
    high: "Quantity" = None
    