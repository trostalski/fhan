"""
Generated class for Signature. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *


@dataclass
class Signature:
    """
    Base StructureDefinition for Signature Type: A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.
    """
    id: str = None
    
    extension: "Extension" = None
    
    type: "Coding" = None
    
    when: str = None
    
    who: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    targetFormat: str = None
    
    sigFormat: str = None
    
    data: str = None
    