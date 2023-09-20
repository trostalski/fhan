"""
Generated class for ProductShelfLife. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.Quantity import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *




@dataclass
class ProductShelfLife(Element):
    """ Base StructureDefinition for ProductShelfLife Type: The shelf-life and storage information for a medicinal product item or container can be described using this class.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Unique identifier for the packaged Medicinal Product
    :param CodeableConcept type: This describes the shelf life, taking into account various scenarios such as shelf life of the packaged Medicinal Product itself, shelf life after transformation where necessary and shelf life after the first opening of a bottle, etc. The shelf life type shall be specified using an appropriate controlled vocabulary The controlled term and the controlled term identifier shall be specified
    :param Quantity period: The shelf life time period can be specified using a numerical value for the period of time and its unit of time measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param CodeableConcept specialPrecautionsForStorage: Special precautions for storage, if any, can be specified using an appropriate controlled vocabulary The controlled term and the controlled term identifier shall be specified
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    period: "Quantity" = None
    
    specialPrecautionsForStorage: list["CodeableConcept"] = None
    