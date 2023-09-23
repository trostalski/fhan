"""
Generated class for Count. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *


@dataclass
class Count(Element):
    """ Base StructureDefinition for Count Type: A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str comparator: < | <= | >= | > - how to understand the value
    :param str unit: Unit representation
    :param str system: System that defines coded unit form
    :param str code: Coded form of the unit
    """

    resourceType: str = "Count"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    value: float = None
    
    comparator: str = None
    
    unit: str = None
    
    system: str = None
    
    code: str = None
    