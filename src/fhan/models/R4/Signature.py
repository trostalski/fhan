"""
Generated class for Signature. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Coding import *
from fhan.models.generator_models import ModelBase

class Signature(ModelBase):
    """ Base StructureDefinition for Signature Type: A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Coding'] type: Indication of the reason the entity signed the object(s)
    :param str when: When the signature was created
    :param 'Reference' who: Who signed
    :param 'Reference' onBehalfOf: The party represented
    :param str targetFormat: The technical format of the signed resources
    :param str sigFormat: The technical format of the signature
    :param str data: The actual signature content (XML DigSig. JWS, picture, etc.)
    """
    def __init__(self, resourceType: str = "Signature",  id: str = None,  extension: list['Extension'] = None,  type: list['Coding'] = None,  when: str = None,  who: 'Reference' = None,  onBehalfOf: 'Reference' = None,  targetFormat: str = None,  sigFormat: str = None,  data: str = None, ):
        self.resourceType: str = resourceType or "Signature"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: list['Coding'] = type or []
        self.when: str = when 
        self.who: 'Reference' = who 
        self.onBehalfOf: 'Reference' = onBehalfOf 
        self.targetFormat: str = targetFormat 
        self.sigFormat: str = sigFormat 
        self.data: str = data 
        