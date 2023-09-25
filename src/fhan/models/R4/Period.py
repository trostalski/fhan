"""
Generated class for Period. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Period(ModelBase):
    """ Base StructureDefinition for Period Type: A time period defined by a start and end date and optionally time.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str start: Starting time with inclusive boundary
    :param str end: End time with inclusive boundary, if not ongoing
    """
    def __init__(self, resourceType: str = "Period",  id: str = None,  extension: list['Extension'] = None,  start: str = None,  end: str = None, ):
        self.resourceType: str = resourceType or "Period"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.start: str = start 
        self.end: str = end 
        