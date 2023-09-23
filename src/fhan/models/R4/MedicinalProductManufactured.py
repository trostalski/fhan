"""
Generated class for MedicinalProductManufactured. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

@dataclass
class MedicinalProductManufactured(ModelBase):
    """ The manufactured item as contained in the packaged medicinal product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept manufacturedDoseForm: Dose form as manufactured and before any transformation into the pharmaceutical product
    :param CodeableConcept unitOfPresentation: The “real world” units in which the quantity of the manufactured item is described
    :param Quantity quantity: The quantity or "count number" of the manufactured item
    :param Reference manufacturer: Manufacturer of the item (Note that this should be named "manufacturer" but it currently causes technical issues)
    :param Reference ingredient: Ingredient
    :param ProdCharacteristic physicalCharacteristics: Dimensions, color etc.
    :param CodeableConcept otherCharacteristics: Other codeable characteristics
    """

    resourceType: str = "MedicinalProductManufactured"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    manufacturedDoseForm: "CodeableConcept" = CodeableConcept()
    
    unitOfPresentation: "CodeableConcept" = CodeableConcept()
    
    quantity: "Quantity" = Quantity()
    
    manufacturer: list[Reference] = Reference() 
    
    ingredient: list[Reference] = Reference() 
    
    physicalCharacteristics: "ProdCharacteristic" = ProdCharacteristic()
    
    otherCharacteristics: list[CodeableConcept] = CodeableConcept() 
    