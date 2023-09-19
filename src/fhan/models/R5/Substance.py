"""
Generated class for Substance. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Substance:
    """ A homogeneous material with a definite composition.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param bool instance: Is this an instance of a substance or a kind of one
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: What class/type of substance this is
    :param CodeableReference code: What substance this is
    :param str description: Textual description of the substance, comments
    :param str expiry: When no longer valid to use
    :param Quantity quantity: Amount of substance in the package
    :param BackboneElement ingredient: Composition information about the substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio quantity: Optional amount (concentration)
    :param CodeableConcept substanceCodeableConcept: A component of the substance
    :param Reference substanceCodeableConcept: A component of the substance
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    instance: bool = None
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableReference" = None
    
    description: str = None
    
    expiry: str = None
    
    quantity: "Quantity" = None
    
    ingredient: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    quantity: "Ratio" = None
    
    substanceCodeableConcept: "CodeableConcept" = None
    
    substanceCodeableConcept: "Reference" = None
    