"""
Generated class for Timing. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Duration import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Range import *
from fhan.models.R4.Element import *
from fhan.models.generator_models import ModelBase

    
    

class Repeat(ModelBase):
    """ A set of rules that describe when the event is scheduled.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'Duration' boundsDuration: Length/Range of lengths, or (Start and/or end) limits
    :param 'Range' boundsRange: Length/Range of lengths, or (Start and/or end) limits
    :param 'Period' boundsPeriod: Length/Range of lengths, or (Start and/or end) limits
    :param int count: Number of times to repeat
    :param int countMax: Maximum number of times to repeat
    :param float duration: How long when it happens
    :param float durationMax: How long when it happens (Max)
    :param str durationUnit: s | min | h | d | wk | mo | a - unit of time (UCUM)
    :param int frequency: Event occurs frequency times per period
    :param int frequencyMax: Event occurs up to frequencyMax times per period
    :param float period: Event occurs frequency times per period
    :param float periodMax: Upper limit of period (3-4 hours)
    :param str periodUnit: s | min | h | d | wk | mo | a - unit of time (UCUM)
    :param str dayOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param str timeOfDay: Time of day for action
    :param str when: Code for time period of occurrence
    :param int offset: Minutes from event (before or after)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  boundsDuration: 'Duration' = None,  boundsRange: 'Range' = None,  boundsPeriod: 'Period' = None,  count: int = None,  countMax: int = None,  duration: float = None,  durationMax: float = None,  durationUnit: str = None,  frequency: int = None,  frequencyMax: int = None,  period: float = None,  periodMax: float = None,  periodUnit: str = None,  dayOfWeek: str = None,  timeOfDay: str = None,  when: str = None,  offset: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.boundsDuration: 'Duration' = boundsDuration 
        self.boundsRange: 'Range' = boundsRange 
        self.boundsPeriod: 'Period' = boundsPeriod 
        self.count: int = count 
        self.countMax: int = countMax 
        self.duration: float = duration 
        self.durationMax: float = durationMax 
        self.durationUnit: str = durationUnit 
        self.frequency: int = frequency 
        self.frequencyMax: int = frequencyMax 
        self.period: float = period 
        self.periodMax: float = periodMax 
        self.periodUnit: str = periodUnit 
        self.dayOfWeek: str = dayOfWeek or []
        self.timeOfDay: str = timeOfDay or []
        self.when: str = when or []
        self.offset: int = offset 
        

class Timing(ModelBase):
    """ Base StructureDefinition for Timing Type: Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str event: When the event occurs
    :param 'Repeat' repeat: When the event is to occur
    :param 'CodeableConcept' code: BID | TID | QID | AM | PM | QD | QOD | +
    """
    def __init__(self, resourceType: str = "Timing",  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  event: str = None,  repeat: 'Repeat' = None,  code: 'CodeableConcept' = None, ):
        self.resourceType: str = resourceType or "Timing"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.event: str = event or []
        self.repeat: 'Repeat' = repeat 
        self.code: 'CodeableConcept' = code 
        