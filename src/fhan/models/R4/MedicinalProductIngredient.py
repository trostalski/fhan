"""
Generated class for MedicinalProductIngredient. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class MedicinalProductIngredient(ModelBase):
    """ An ingredient of a manufactured item or pharmaceutical product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier for the ingredient
    :param CodeableConcept role: Ingredient role e.g. Active ingredient, excipient
    :param bool allergenicIndicator: If the ingredient is a known or suspected allergen
    :param Reference manufacturer: Manufacturer of this Ingredient
    :param BackboneElement specifiedSubstance: A specified substance that comprises this ingredient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The specified substance
    :param CodeableConcept group: The group of specified substance, e.g. group 1 to 4
    :param CodeableConcept confidentiality: Confidentiality level of the specified substance as the ingredient
    :param BackboneElement strength: Quantity of the substance or specified substance present in the manufactured item or pharmaceutical product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio presentation: The quantity of substance in the unit of presentation, or in the volume (or mass) of the single pharmaceutical product or manufactured item
    :param Ratio presentationLowLimit: A lower limit for the quantity of substance in the unit of presentation. For use when there is a range of strengths, this is the lower limit, with the presentation attribute becoming the upper limit
    :param Ratio concentration: The strength per unitary volume (or mass)
    :param Ratio concentrationLowLimit: A lower limit for the strength per unitary volume (or mass), for when there is a range. The concentration attribute then becomes the upper limit
    :param str measurementPoint: For when strength is measured at a particular point or distance
    :param CodeableConcept country: The country or countries for which the strength range applies
    :param BackboneElement referenceStrength: Strength expressed in terms of a reference substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept substance: Relevant reference substance
    :param Ratio strength: Strength expressed in terms of a reference substance
    :param Ratio strengthLowLimit: Strength expressed in terms of a reference substance
    :param str measurementPoint: For when strength is measured at a particular point or distance
    :param CodeableConcept country: The country or countries for which the strength range applies
    :param BackboneElement substance: The ingredient substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The ingredient substance
    :param BackboneElement strength: Quantity of the substance or specified substance present in the manufactured item or pharmaceutical product
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
    
    role: "CodeableConcept" = None
    
    allergenicIndicator: bool = None
    
    manufacturer: "Reference" = None
    
    specifiedSubstance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    group: "CodeableConcept" = None
    
    confidentiality: "CodeableConcept" = None
    
    strength: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    presentation: "Ratio" = None
    
    presentationLowLimit: "Ratio" = None
    
    concentration: "Ratio" = None
    
    concentrationLowLimit: "Ratio" = None
    
    measurementPoint: str = None
    
    country: "CodeableConcept" = None
    
    referenceStrength: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substance: "CodeableConcept" = None
    
    strength: "Ratio" = None
    
    strengthLowLimit: "Ratio" = None
    
    measurementPoint: str = None
    
    country: "CodeableConcept" = None
    
    substance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    strength: "BackboneElement" = None
    