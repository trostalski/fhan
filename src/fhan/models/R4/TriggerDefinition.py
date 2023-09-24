"""
Generated class for TriggerDefinition. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class TriggerDefinition(ModelBase):
    """ Base StructureDefinition for TriggerDefinition Type: A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str type: named-event | periodic | data-changed | data-added | data-modified | data-removed | data-accessed | data-access-ended
    :param str name: Name or URI that identifies the event
    :param 'Timing' timingTiming: Timing of the event
    :param list['DataRequirement'] data: Triggering data of the event (multiple = 'and')
    :param 'Expression' condition: Whether the event triggers (boolean expression)
    """
    def __init__(self, resourceType: str = "TriggerDefinition",  id: str = None,  extension: list['Extension'] = None,  type: str = None,  name: str = None,  timingTiming: 'Timing' = None,  data: list['DataRequirement'] = None,  condition: 'Expression' = None, ):
        self.resourceType: str = resourceType or "TriggerDefinition"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: str = type 
        self.name: str = name 
        self.timingTiming: 'Timing' = timingTiming 
        self.data: list['DataRequirement'] = data or []
        self.condition: 'Expression' = condition 
        