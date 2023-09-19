"""
Generated class for TriggerDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Expression import *
from fhan.models.R5.DataRequirement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Reference import *


@dataclass
class TriggerDefinition:
    """ TriggerDefinition Type: A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: named-event | periodic | data-changed | data-added | data-modified | data-removed | data-accessed | data-access-ended
    :param str name: Name or URI that identifies the event
    :param CodeableConcept code: Coded definition of the event
    :param str subscriptionTopic: What event
    :param Timing timingTiming: Timing of the event
    :param Reference timingTiming: Timing of the event
    :param str timingTiming: Timing of the event
    :param str timingTiming: Timing of the event
    :param DataRequirement data: Triggering data of the event (multiple = 'and')
    :param Expression condition: Whether the event triggers (boolean expression)
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    name: str = None
    
    code: "CodeableConcept" = None
    
    subscriptionTopic: str = None
    
    timingTiming: "Timing" = None
    
    timingTiming: "Reference" = None
    
    timingTiming: str = None
    
    timingTiming: str = None
    
    data: "DataRequirement" = None
    
    condition: "Expression" = None
    