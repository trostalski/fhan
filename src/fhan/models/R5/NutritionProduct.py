"""
Generated class for NutritionProduct. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class NutritionProduct:
    """ A food or supplement that is consumed by patients.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept code: A code that can identify the detailed nutrients and ingredients in a specific food product
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: Broad product groups or categories used to classify the product, such as Legume and Legume Products, Beverages, or Beef Products
    :param Reference manufacturer: Manufacturer, representative or officially responsible for the product
    :param BackboneElement nutrient: The product's nutritional information expressed by the nutrients
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: The (relevant) nutrients in the product
    :param Ratio amount: The amount of nutrient expressed in one or more units: X per pack / per serving / per dose
    :param BackboneElement ingredient: Ingredients contained in this product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: The ingredient contained in the product
    :param Ratio amount: The amount of ingredient that is in the product
    :param CodeableReference knownAllergen: Known or suspected allergens that are a part of this product
    :param BackboneElement characteristic: Specifies descriptive properties of the nutrition product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code specifying the type of characteristic
    :param CodeableConcept valueCodeableConcept: The value of the characteristic
    :param str valueCodeableConcept: The value of the characteristic
    :param Quantity valueCodeableConcept: The value of the characteristic
    :param str valueCodeableConcept: The value of the characteristic
    :param Attachment valueCodeableConcept: The value of the characteristic
    :param bool valueCodeableConcept: The value of the characteristic
    :param BackboneElement instance: One or several physical instances or occurrences of the nutrition product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: The amount of items or instances
    :param Identifier identifier: The identifier for the physical instance, typically a serial number or manufacturer number
    :param str name: The name for the specific product
    :param str lotNumber: The identification of the batch or lot of the product
    :param str expiry: The expiry date or date and time for the product
    :param str useBy: The date until which the product is expected to be good for consumption
    :param Identifier biologicalSourceEvent: An identifier that supports traceability to the event during which material in this product from one or more biological entities was obtained or pooled
    :param Annotation note: Comments made about the product
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    manufacturer: "Reference" = None
    
    nutrient: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    item: "CodeableReference" = None
    
    amount: "Ratio" = None
    
    ingredient: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    item: "CodeableReference" = None
    
    amount: "Ratio" = None
    
    knownAllergen: "CodeableReference" = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: "Attachment" = None
    
    valueCodeableConcept: bool = None
    
    instance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    quantity: "Quantity" = None
    
    identifier: "Identifier" = None
    
    name: str = None
    
    lotNumber: str = None
    
    expiry: str = None
    
    useBy: str = None
    
    biologicalSourceEvent: "Identifier" = None
    
    note: "Annotation" = None
    