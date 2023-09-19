"""
Generated class for MonetaryComponent. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Money import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *


@dataclass
class MonetaryComponent:
    """ MonetaryComponent Type: Availability data for an {item}.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: base | surcharge | deduction | discount | tax | informational
    :param CodeableConcept code: Codes may be used to differentiate between kinds of taxes, surcharges, discounts etc.
    :param float factor: Factor used for calculating this component
    :param Money amount: Explicit value amount to be used
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    code: "CodeableConcept" = None
    
    factor: float = None
    
    amount: "Money" = None
    