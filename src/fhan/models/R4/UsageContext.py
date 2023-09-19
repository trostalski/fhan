"""
Generated class for UsageContext. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Coding import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Range import *
from fhan.models.R4.Element import *



@dataclass
class UsageContext(Element):
    """ Base StructureDefinition for UsageContext Type: Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact. This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific context of care (e.g., venue, care setting, provider of care).
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
    