"""
Generated class for MarketingStatus. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Period import *


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
    