"""
Generated class for Distance. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Distance(ModelBase):
    """ Base StructureDefinition for Distance Type: A length - a value with a unit that is a physical distance.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str comparator: < | <= | >= | > - how to understand the value
    :param str unit: Unit representation
    :param str system: System that defines coded unit form
    :param str code: Coded form of the unit
    """
    def __init__(self, resourceType: str = "Distance",  id: str = None,  extension: list['Extension'] = None,  value: float = None,  comparator: str = None,  unit: str = None,  system: str = None,  code: str = None, ):
        self.resourceType: str = resourceType or "Distance"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.value: float = value 
        self.comparator: str = comparator 
        self.unit: str = unit 
        self.system: str = system 
        self.code: str = code 
        