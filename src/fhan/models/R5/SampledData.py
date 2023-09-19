"""
Generated class for SampledData. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Quantity import *
from fhan.models.R5.Extension import *


@dataclass
class SampledData:
    """ SampledData Type: A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity origin: Zero value and units
    :param float interval: Number of intervalUnits between samples
    :param str intervalUnit: The measurement unit of the interval between samples
    :param float factor: Multiply data by this before adding to origin
    :param float lowerLimit: Lower limit of detection
    :param float upperLimit: Upper limit of detection
    :param int dimensions: Number of sample points at each time point
    :param str codeMap: Defines the codes used in the data
    :param str offsets: Offsets, typically in time, at which data values were taken
    :param str data: Decimal values with spaces, or "E" | "U" | "L", or another code
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    origin: "Quantity" = None
    
    interval: float = None
    
    intervalUnit: str = None
    
    factor: float = None
    
    lowerLimit: float = None
    
    upperLimit: float = None
    
    dimensions: int = None
    
    codeMap: str = None
    
    offsets: str = None
    
    data: str = None
    