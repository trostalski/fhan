"""
Generated class for Count. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Count(ModelBase):
    """ Base StructureDefinition for Count Type: A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str comparator: < | <= | >= | > - how to understand the value
    :param str unit: Unit representation
    :param str system: System that defines coded unit form
    :param str code: Coded form of the unit
    """
    def __init__(self, resourceType: str = "Count",  id: str = None,  extension: list['Extension'] = None,  value: float = None,  comparator: str = None,  unit: str = None,  system: str = None,  code: str = None, ):
        self.resourceType: str = resourceType or "Count"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.value: float = value 
        self.comparator: str = comparator 
        self.unit: str = unit 
        self.system: str = system 
        self.code: str = code 
        