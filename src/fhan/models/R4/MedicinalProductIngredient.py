"""
Generated class for MedicinalProductIngredient. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
        
    
        
    
    
@dataclass
class ReferenceStrength(Element):
    """ Strength expressed in terms of a reference substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept substance: Relevant reference substance
    :param Ratio strength: Strength expressed in terms of a reference substance
    :param Ratio strengthLowLimit: Strength expressed in terms of a reference substance
    :param str measurementPoint: For when strength is measured at a particular point or distance
    :param CodeableConcept country: The country or countries for which the strength range applies
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    substance: "CodeableConcept" = CodeableConcept()
    strength: "Ratio" = Ratio()
    strengthLowLimit: "Ratio" = Ratio()
    
    measurementPoint: str = None
    country: list[CodeableConcept] = CodeableConcept() 
    

  
    
    
@dataclass
class Strength(Element):
    """ Quantity of the substance or specified substance present in the manufactured item or pharmaceutical product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio presentation: The quantity of substance in the unit of presentation, or in the volume (or mass) of the single pharmaceutical product or manufactured item
    :param Ratio presentationLowLimit: A lower limit for the quantity of substance in the unit of presentation. For use when there is a range of strengths, this is the lower limit, with the presentation attribute becoming the upper limit
    :param Ratio concentration: The strength per unitary volume (or mass)
    :param Ratio concentrationLowLimit: A lower limit for the strength per unitary volume (or mass), for when there is a range. The concentration attribute then becomes the upper limit
    :param str measurementPoint: For when strength is measured at a particular point or distance
    :param CodeableConcept country: The country or countries for which the strength range applies
    :param ReferenceStrength referenceStrength: Strength expressed in terms of a reference substance
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    presentation: "Ratio" = Ratio()
    presentationLowLimit: "Ratio" = Ratio()
    concentration: "Ratio" = Ratio()
    concentrationLowLimit: "Ratio" = Ratio()
    
    measurementPoint: str = None
    country: list[CodeableConcept] = CodeableConcept() 
    referenceStrength: list[ReferenceStrength] = ReferenceStrength() 
    

  
    
    
@dataclass
class SpecifiedSubstance(Element):
    """ A specified substance that comprises this ingredient.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The specified substance
    :param CodeableConcept group: The group of specified substance, e.g. group 1 to 4
    :param CodeableConcept confidentiality: Confidentiality level of the specified substance as the ingredient
    :param Strength strength: Quantity of the substance or specified substance present in the manufactured item or pharmaceutical product
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    code: "CodeableConcept" = CodeableConcept()
    group: "CodeableConcept" = CodeableConcept()
    confidentiality: "CodeableConcept" = CodeableConcept()
    strength: list[Strength] = Strength() 
    

    
    
@dataclass
class Substance(Element):
    """ The ingredient substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The ingredient substance
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    code: "CodeableConcept" = CodeableConcept()
    

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
    :param SpecifiedSubstance specifiedSubstance: A specified substance that comprises this ingredient
    :param Substance substance: The ingredient substance
    """

    resourceType: str = "MedicinalProductIngredient"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: "Identifier" = Identifier()
    
    role: "CodeableConcept" = CodeableConcept()
    
    allergenicIndicator: bool = None
    
    manufacturer: list[Reference] = Reference() 
    
    specifiedSubstance: list[SpecifiedSubstance] = SpecifiedSubstance() 
    
    substance: "Substance" = Substance()
    