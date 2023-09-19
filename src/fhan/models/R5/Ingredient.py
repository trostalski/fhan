"""
Generated class for Ingredient. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RatioRange import *
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
class Ingredient:
    """ An ingredient of a manufactured item or pharmaceutical product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: An identifier or code by which the ingredient can be referenced
    :param str status: draft | active | retired | unknown
    :param Reference for: The product which this ingredient is a constituent part of
    :param CodeableConcept role: Purpose of the ingredient within the product, e.g. active, inactive
    :param CodeableConcept function: Precise action within the drug product, e.g. antioxidant, alkalizing agent
    :param CodeableConcept group: A classification of the ingredient according to where in the physical item it tends to be used, such the outer shell of a tablet, inner body or ink
    :param bool allergenicIndicator: If the ingredient is a known or suspected allergen
    :param str comment: A place for providing any notes that are relevant to the component, e.g. removed during process, adjusted for loss on drying
    :param BackboneElement manufacturer: An organization that manufactures this ingredient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str role: allowed | possible | actual
    :param Reference manufacturer: An organization that manufactures this ingredient
    :param BackboneElement substance: The substance that comprises this ingredient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference code: A code or full resource that represents the ingredient substance
    :param BackboneElement strength: The quantity of substance, per presentation, or per volume or mass, and type of quantity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio presentationRatio: The quantity of substance in the unit of presentation
    :param RatioRange presentationRatio: The quantity of substance in the unit of presentation
    :param CodeableConcept presentationRatio: The quantity of substance in the unit of presentation
    :param Quantity presentationRatio: The quantity of substance in the unit of presentation
    :param str textPresentation: Text of either the whole presentation strength or a part of it (rest being in Strength.presentation as a ratio)
    :param Ratio concentrationRatio: The strength per unitary volume (or mass)
    :param RatioRange concentrationRatio: The strength per unitary volume (or mass)
    :param CodeableConcept concentrationRatio: The strength per unitary volume (or mass)
    :param Quantity concentrationRatio: The strength per unitary volume (or mass)
    :param str textConcentration: Text of either the whole concentration strength or a part of it (rest being in Strength.concentration as a ratio)
    :param CodeableConcept basis: A code that indicates if the strength is, for example, based on the ingredient substance as stated or on the substance base (when the ingredient is a salt)
    :param str measurementPoint: When strength is measured at a particular point or distance
    :param CodeableConcept country: Where the strength range applies
    :param BackboneElement referenceStrength: Strength expressed in terms of a reference substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference substance: Relevant reference substance
    :param Ratio strengthRatio: Strength expressed in terms of a reference substance
    :param RatioRange strengthRatio: Strength expressed in terms of a reference substance
    :param Quantity strengthRatio: Strength expressed in terms of a reference substance
    :param str measurementPoint: When strength is measured at a particular point or distance
    :param CodeableConcept country: Where the strength range applies
    
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
    
    status: str = None
    
    for: "Reference" = None
    
    role: "CodeableConcept" = None
    
    function: "CodeableConcept" = None
    
    group: "CodeableConcept" = None
    
    allergenicIndicator: bool = None
    
    comment: str = None
    
    manufacturer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: str = None
    
    manufacturer: "Reference" = None
    
    substance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableReference" = None
    
    strength: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    presentationRatio: "Ratio" = None
    
    presentationRatio: "RatioRange" = None
    
    presentationRatio: "CodeableConcept" = None
    
    presentationRatio: "Quantity" = None
    
    textPresentation: str = None
    
    concentrationRatio: "Ratio" = None
    
    concentrationRatio: "RatioRange" = None
    
    concentrationRatio: "CodeableConcept" = None
    
    concentrationRatio: "Quantity" = None
    
    textConcentration: str = None
    
    basis: "CodeableConcept" = None
    
    measurementPoint: str = None
    
    country: "CodeableConcept" = None
    
    referenceStrength: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substance: "CodeableReference" = None
    
    strengthRatio: "Ratio" = None
    
    strengthRatio: "RatioRange" = None
    
    strengthRatio: "Quantity" = None
    
    measurementPoint: str = None
    
    country: "CodeableConcept" = None
    