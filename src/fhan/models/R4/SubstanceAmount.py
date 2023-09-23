"""
Generated class for SubstanceAmount. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Range import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Element import *
from fhan.models.R4.Element import *


@dataclass
class SubstanceAmount(Element):
    """ Base StructureDefinition for SubstanceAmount Type: Chemical substances are a single substance type whose primary defining element is the molecular structure. Chemical substances shall be defined on the basis of their complete covalent molecular structure; the presence of a salt (counter-ion) and/or solvates (water, alcohols) is also captured. Purity, grade, physical form or particle size are not taken into account in the definition of a chemical substance or in the assignment of a Substance ID.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity amountQuantity: Used to capture quantitative values for a variety of elements. If only limits are given, the arithmetic mean would be the average. If only a single definite value for a given element is given, it would be captured in this field
    :param CodeableConcept amountType: Most elements that require a quantitative value will also have a field called amount type. Amount type should always be specified because the actual value of the amount is often dependent on it. EXAMPLE: In capturing the actual relative amounts of substances or molecular fragments it is essential to indicate whether the amount refers to a mole ratio or weight ratio. For any given element an effort should be made to use same the amount type for all related definitional elements
    :param str amountText: A textual comment on a numeric value
    :param Element referenceRange: Reference range of possible or expected values
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity lowLimit: Lower limit possible or expected
    :param Quantity highLimit: Upper limit possible or expected
    """

    resourceType: str = "SubstanceAmount"
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    amountQuantity: "Quantity" = Quantity()
    
    amountType: "CodeableConcept" = CodeableConcept()
    
    amountText: str = None
    
    referenceRange: "Element" = Element()
    
    id: str = None
    
    extension: list[Extension] = Extension() 
    
    lowLimit: "Quantity" = Quantity()
    
    highLimit: "Quantity" = Quantity()
    