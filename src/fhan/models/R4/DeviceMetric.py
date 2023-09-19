"""
Generated class for DeviceMetric. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class DeviceMetric:
    """
    Describes a measurement, calculation or setting capability of a medical device.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    source: "Reference" = None
    
    parent: "Reference" = None
    
    operationalStatus: str = None
    
    color: str = None
    
    category: str = None
    
    measurementPeriod: "Timing" = None
    
    calibration: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    state: str = None
    
    time: str = None
    