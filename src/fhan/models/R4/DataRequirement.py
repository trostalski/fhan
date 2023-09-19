"""
Generated class for DataRequirement. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Coding import *


@dataclass
class DataRequirement:
    """
    Base StructureDefinition for DataRequirement Type: Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.
    """
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    profile: str = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
    mustSupport: str = None
    
    codeFilter: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    path: str = None
    
    searchParam: str = None
    
    valueSet: str = None
    
    code: "Coding" = None
    
    dateFilter: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    path: str = None
    
    searchParam: str = None
    
    valuedateTime: str = None
    
    valuedateTime: "Period" = None
    
    valuedateTime: "Duration" = None
    
    limit: int = None
    
    sort: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    path: str = None
    
    direction: str = None
    