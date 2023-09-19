"""
Generated class for SubstanceAmount. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Element import *
from fhan.models.R4.Range import *


@dataclass
class SubstanceAmount:
    """
    Base StructureDefinition for SubstanceAmount Type: Chemical substances are a single substance type whose primary defining element is the molecular structure. Chemical substances shall be defined on the basis of their complete covalent molecular structure; the presence of a salt (counter-ion) and/or solvates (water, alcohols) is also captured. Purity, grade, physical form or particle size are not taken into account in the definition of a chemical substance or in the assignment of a Substance ID.
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    amountQuantity: "Quantity" = None
    
    amountQuantity: "Range" = None
    
    amountQuantity: str = None
    
    amountType: "CodeableConcept" = None
    
    amountText: str = None
    
    referenceRange: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    lowLimit: "Quantity" = None
    
    highLimit: "Quantity" = None
    