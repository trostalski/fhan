"""
Generated class for MarketingStatus. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *


@dataclass
class MarketingStatus:
    """
    Base StructureDefinition for MarketingStatus Type: The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    country: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    dateRange: "Period" = None
    
    restoreDate: str = None
    