"""
Generated class for DataType. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *


@dataclass
class DataType:
    """
    Base StructureDefinition for DataType Type: The base class for all re-useable types defined as part of the FHIR Specification.
    """
    id: str = None
    
    extension: "Extension" = None
    