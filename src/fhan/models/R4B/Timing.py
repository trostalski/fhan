"""
Generated class for Timing. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Duration import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.Element import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *


@dataclass
class Timing:
    """
    Base StructureDefinition for Timing Type: Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    event: str = None
    
    repeat: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    boundsDuration: "Duration" = None
    
    boundsDuration: "Range" = None
    
    boundsDuration: "Period" = None
    
    count: int = None
    
    countMax: int = None
    
    duration: float = None
    
    durationMax: float = None
    
    durationUnit: str = None
    
    frequency: int = None
    
    frequencyMax: int = None
    
    period: float = None
    
    periodMax: float = None
    
    periodUnit: str = None
    
    dayOfWeek: str = None
    
    timeOfDay: str = None
    
    when: str = None
    
    offset: int = None
    
    code: "CodeableConcept" = None
    