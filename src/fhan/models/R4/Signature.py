"""
Generated class for Signature. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *


@dataclass
class Signature(Element):
    """ Base StructureDefinition for Signature Type: A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding type: Indication of the reason the entity signed the object(s)
    :param str when: When the signature was created
    :param Reference who: Who signed
    :param Reference onBehalfOf: The party represented
    :param str targetFormat: The technical format of the signed resources
    :param str sigFormat: The technical format of the signature
    :param str data: The actual signature content (XML DigSig. JWS, picture, etc.)
    """

    resourceType: str = "Signature"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    type: list[Coding] = Coding() 
    
    when: str = None
    
    who: "Reference" = Reference()
    
    onBehalfOf: "Reference" = Reference()
    
    targetFormat: str = None
    
    sigFormat: str = None
    
    data: str = None
    