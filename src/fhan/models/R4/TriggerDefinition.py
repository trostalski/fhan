"""
Generated class for TriggerDefinition. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Expression import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Timing import *


@dataclass
class TriggerDefinition:
    """
    Base StructureDefinition for TriggerDefinition Type: A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.
    """
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    name: str = None
    
    timingTiming: "Timing" = None
    
    timingTiming: "Reference" = None
    
    timingTiming: str = None
    
    timingTiming: str = None
    
    data: "DataRequirement" = None
    
    condition: "Expression" = None
    