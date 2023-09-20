"""
Generated class for ProdCharacteristic. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Element import *




@dataclass
class ProdCharacteristic(Element):
    """ Base StructureDefinition for ProdCharacteristic Type: The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity height: Where applicable, the height can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity width: Where applicable, the width can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity depth: Where applicable, the depth can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity weight: Where applicable, the weight can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity nominalVolume: Where applicable, the nominal volume can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param Quantity externalDiameter: Where applicable, the external diameter can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param str shape: Where applicable, the shape can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used
    :param str color: Where applicable, the color can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used
    :param str imprint: Where applicable, the imprint can be specified as text
    :param Attachment image: Where applicable, the image can be provided The format of the image attachment shall be specified by regional implementations
    :param CodeableConcept scoring: Where applicable, the scoring can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    height: "Quantity" = None
    
    width: "Quantity" = None
    
    depth: "Quantity" = None
    
    weight: "Quantity" = None
    
    nominalVolume: "Quantity" = None
    
    externalDiameter: "Quantity" = None
    
    shape: str = None
    
    color: str = None
    
    imprint: str = None
    
    image: list["Attachment"] = None
    
    scoring: "CodeableConcept" = None
    