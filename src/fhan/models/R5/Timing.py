"""
Generated class for Timing. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Element import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Period import *
from fhan.models.R5.Range import *
from fhan.models.R5.Duration import *


@dataclass
class Timing:
    """ Timing Type: Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str event: When the event occurs
    :param Element repeat: When the event is to occur
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Duration boundsDuration: Length/Range of lengths, or (Start and/or end) limits
    :param Range boundsDuration: Length/Range of lengths, or (Start and/or end) limits
    :param Period boundsDuration: Length/Range of lengths, or (Start and/or end) limits
    :param int count: Number of times to repeat
    :param int countMax: Maximum number of times to repeat
    :param float duration: How long when it happens
    :param float durationMax: How long when it happens (Max)
    :param str durationUnit: s | min | h | d | wk | mo | a - unit of time (UCUM)
    :param int frequency: Indicates the number of repetitions that should occur within a period. I.e. Event occurs frequency times per period
    :param int frequencyMax: Event occurs up to frequencyMax times per period
    :param float period: The duration to which the frequency applies. I.e. Event occurs frequency times per period
    :param float periodMax: Upper limit of period (3-4 hours)
    :param str periodUnit: s | min | h | d | wk | mo | a - unit of time (UCUM)
    :param str dayOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param str timeOfDay: Time of day for action
    :param str when: Code for time period of occurrence
    :param int offset: Minutes from event (before or after)
    :param CodeableConcept code: C | BID | TID | QID | AM | PM | QD | QOD | +
    
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
    