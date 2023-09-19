"""
Generated class for ManufacturedItemDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.MarketingStatus import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ManufacturedItemDefinition:
    """ The definition and characteristics of a medicinal manufactured item, such as a tablet or capsule, as contained in a packaged medicinal product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param str status: draft | active | retired | unknown
    :param str name: A descriptive name applied to this item
    :param CodeableConcept manufacturedDoseForm: Dose form as manufactured (before any necessary transformation)
    :param CodeableConcept unitOfPresentation: The “real-world” units in which the quantity of the item is described
    :param Reference manufacturer: Manufacturer of the item, one of several possible
    :param MarketingStatus marketingStatus: Allows specifying that an item is on the market for sale, or that it is not available, and the dates and locations associated
    :param CodeableConcept ingredient: The ingredients of this manufactured item. Only needed if these are not specified by incoming references from the Ingredient resource
    :param BackboneElement property: General characteristics of this item
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of characteristic
    :param CodeableConcept valueCodeableConcept: A value for the characteristic
    :param Quantity valueCodeableConcept: A value for the characteristic
    :param str valueCodeableConcept: A value for the characteristic
    :param bool valueCodeableConcept: A value for the characteristic
    :param str valueCodeableConcept: A value for the characteristic
    :param Attachment valueCodeableConcept: A value for the characteristic
    :param Reference valueCodeableConcept: A value for the characteristic
    :param BackboneElement component: Physical parts of the manufactured item, that it is intrisically made from. This is distinct from the ingredients that are part of its chemical makeup
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Defining type of the component e.g. shell, layer, ink
    :param CodeableConcept function: The function of this component within the item e.g. delivers active ingredient, masks taste
    :param Quantity amount: The measurable amount of total quantity of all substances in the component, expressable in different ways (e.g. by mass or volume)
    :param BackboneElement constituent: A reference to a constituent of the manufactured item as a whole, linked here so that its component location within the item can be indicated. This not where the item's ingredient are primarily stated (for which see Ingredient.for or ManufacturedItemDefinition.ingredient)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity amount: The measurable amount of the substance, expressable in different ways (e.g. by mass or volume)
    :param CodeableConcept location: The physical location of the constituent/ingredient within the component
    :param CodeableConcept function: The function of this constituent within the component e.g. binder
    :param CodeableReference hasIngredient: The ingredient that is the constituent of the given component
    :param BackboneElement property: General characteristics of this item
    :param BackboneElement component: Physical parts of the manufactured item, that it is intrisically made from. This is distinct from the ingredients that are part of its chemical makeup
    
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
    
    name: str = None
    
    manufacturedDoseForm: "CodeableConcept" = None
    
    unitOfPresentation: "CodeableConcept" = None
    
    manufacturer: "Reference" = None
    
    marketingStatus: "MarketingStatus" = None
    
    ingredient: "CodeableConcept" = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: "Attachment" = None
    
    valueCodeableConcept: "Reference" = None
    
    component: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    function: "CodeableConcept" = None
    
    amount: "Quantity" = None
    
    constituent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    amount: "Quantity" = None
    
    location: "CodeableConcept" = None
    
    function: "CodeableConcept" = None
    
    hasIngredient: "CodeableReference" = None
    
    property: "BackboneElement" = None
    
    component: "BackboneElement" = None
    