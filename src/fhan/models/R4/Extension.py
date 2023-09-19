"""
Generated class for Extension. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *


@dataclass
class Extension:
    """
    Other resources *from the patient record* that may be relevant to the event.  The information from these resources was either used to create the instance or is provided to help with its interpretation.  This extension **should not** be used if more specific  inline elements  or extensions are available.  For example, use `Observation.hasMember`  instead of supportingInformation for  representing the members of an Observation panel.
    """
    id: str = None
    
    extension: "Extension" = None
    
    url: str = None
    
    valueReference: "Reference" = None
    