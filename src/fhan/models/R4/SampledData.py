"""
Generated class for SampledData. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class SampledData(ModelBase):
    """ Base StructureDefinition for SampledData Type: A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'Quantity' origin: Zero value and units
    :param float period: Number of milliseconds between samples
    :param float factor: Multiply data by this before adding to origin
    :param float lowerLimit: Lower limit of detection
    :param float upperLimit: Upper limit of detection
    :param int dimensions: Number of sample points at each time point
    :param str data: Decimal values with spaces, or "E" | "U" | "L"
    """
    def __init__(self, resourceType: str = "SampledData",  id: str = None,  extension: list['Extension'] = None,  origin: 'Quantity' = None,  period: float = None,  factor: float = None,  lowerLimit: float = None,  upperLimit: float = None,  dimensions: int = None,  data: str = None, ):
        self.resourceType: str = resourceType or "SampledData"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.origin: 'Quantity' = origin 
        self.period: float = period 
        self.factor: float = factor 
        self.lowerLimit: float = lowerLimit 
        self.upperLimit: float = upperLimit 
        self.dimensions: int = dimensions 
        self.data: str = data 
        