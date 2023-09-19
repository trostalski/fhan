"""
Generated class for UsageContext. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class UsageContext:
    """ UsageContext Type: Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact. This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific context of care (e.g., venue, care setting, provider of care).
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding code: Type of context being specified
    :param CodeableConcept valueCodeableConcept: Value that defines the context
    :param Quantity valueCodeableConcept: Value that defines the context
    :param Range valueCodeableConcept: Value that defines the context
    :param Reference valueCodeableConcept: Value that defines the context
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    code: "Coding" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: "Range" = None
    
    valueCodeableConcept: "Reference" = None
    