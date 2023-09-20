"""
Generated class for Duration. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *




@dataclass
class Duration(Element):
    """ Base StructureDefinition for Duration Type: A length of time.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str comparator: < | <= | >= | > - how to understand the value
    :param str unit: Unit representation
    :param str system: System that defines coded unit form
    :param str code: Coded form of the unit
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    value: float = None
    
    comparator: str = None
    
    unit: str = None
    
    system: str = None
    
    code: str = None
    