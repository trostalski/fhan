"""
Generated class for TriggerDefinition. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Element import *


@dataclass
class TriggerDefinition(Element):
    """ Base StructureDefinition for TriggerDefinition Type: A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: named-event | periodic | data-changed | data-added | data-modified | data-removed | data-accessed | data-access-ended
    :param str name: Name or URI that identifies the event
    :param Timing timingTiming: Timing of the event
    :param DataRequirement data: Triggering data of the event (multiple = 'and')
    :param Expression condition: Whether the event triggers (boolean expression)
    """

    resourceType: str = "TriggerDefinition"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    type: str = None
    
    name: str = None
    
    timingTiming: "Timing" = Timing()
    
    data: list[DataRequirement] = DataRequirement() 
    
    condition: "Expression" = Expression()
    