"""
Generated class for Availability. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Period import *
from fhan.models.R5.Element import *
from fhan.models.R5.Extension import *


@dataclass
class Availability:
    """ Availability Type: Availability data for an {item}.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Element availableTime: Times the {item} is available
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str daysOfWeek: mon | tue | wed | thu | fri | sat | sun
    :param bool allDay: Always available? i.e. 24 hour service
    :param str availableStartTime: Opening time of day (ignored if allDay = true)
    :param str availableEndTime: Closing time of day (ignored if allDay = true)
    :param Element notAvailableTime: Not available during this time due to provided reason
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str description: Reason presented to the user explaining why time not available
    :param Period during: Service not available during this period
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    availableTime: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    daysOfWeek: str = None
    
    allDay: bool = None
    
    availableStartTime: str = None
    
    availableEndTime: str = None
    
    notAvailableTime: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    description: str = None
    
    during: "Period" = None
    