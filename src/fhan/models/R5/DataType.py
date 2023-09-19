"""
Generated class for DataType. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Extension import *


@dataclass
class DataType:
    """ DataType Type: The base class for all re-useable types defined as part of the FHIR Specification.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    
    """
    id: str = None
    
    extension: "Extension" = None
    